#!/usr/bin/env python3
"""
Build a static, shareable HTML site from the repository's Markdown files,
styled to match the Microsoft AI Co-Innovation Lab pre-skilling website.

Output goes to ./site/ (ready to publish to GitHub Pages).
Re-run this script whenever the Markdown changes:  python build_site.py
"""

import os
import re
import shutil
import html as htmllib

try:
    import markdown
except ImportError:
    raise SystemExit(
        "The 'markdown' package is required. Install it with:\n"
        "    python -m pip install markdown"
    )

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")

# Absolute URL to the live pre-skilling stylesheet (guarantees an exact match).
BASE_CSS = "https://titletowntech.github.io/wi_ailab_labwebsite/styles.css"

# Folders whose Markdown we publish, plus the root README.
CONTENT_DIRS = [
    "01-Program-Overview",
    "02-Participant-Materials",
    "03-Event-Agendas",
    "04-Facilitator-Guides",
]

CATEGORY = {
    "": "Overview",
    "01-Program-Overview": "Program Overview",
    "02-Participant-Materials": "Participant Materials",
    "03-Event-Agendas": "Event Agendas",
    "04-Facilitator-Guides": "Facilitator Guides",
}

MD_EXT = ["extra", "sane_lists", "toc"]


def rewrite_links(md_text: str) -> str:
    """Rewrite intra-repo .md links to .html (README.md -> index.html)."""
    pattern = re.compile(r"\]\((?!https?://)([^)]*?)\.md(#[^)]*)?\)")

    def repl(m):
        path, anchor = m.group(1), m.group(2) or ""
        directory, name = os.path.split(path)
        if name == "README":
            name = "index"
        newpath = f"{directory}/{name}" if directory else name
        return f"]({newpath}.html{anchor})"

    return pattern.sub(repl, md_text)


def task_checkboxes(md_text: str) -> str:
    lines = []
    for line in md_text.split("\n"):
        line = re.sub(r"^(\s*)-\s\[ \]\s", lambda m: m.group(1) + "- \u2610 ", line)
        line = re.sub(r"^(\s*)-\s\[[xX]\]\s", lambda m: m.group(1) + "- \u2611 ", line)
        lines.append(line)
    return "\n".join(lines)


def extract_title(md_text: str):
    for line in md_text.split("\n"):
        if line.startswith("# "):
            title = line[2:].strip()
            body = md_text.replace(line, "", 1)
            return title, body
    return "Document", md_text


def page_html(title, category, body_html, depth):
    up = "../" * depth
    extras = f"{up}site-extras.css"
    back = "" if depth == 0 else (
        f'<a class="back-link" href="{up}index.html">&larr; All documents</a>'
    )
    safe_title = htmllib.escape(title)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{safe_title}</title>
  <link rel="stylesheet" href="{BASE_CSS}" />
  <link rel="stylesheet" href="{extras}" />
</head>
<body>

  <header>
    <div class="header-inner">
      <div class="ms-logo"><span class="sq1"></span><span class="sq2"></span><span class="sq3"></span><span class="sq4"></span></div>
      <div class="header-title">AI Co-Innovation Lab - Wisconsin</div>
    </div>
  </header>

  <section class="learn-hero">
    <div class="learn-hero-inner">
      {back}
      <div class="term-name">{htmllib.escape(category)}</div>
      <h1>{safe_title}</h1>
      <div class="learn-meta">
        <span>Build with us: Support &amp; Knowledge Base for Beginners</span>
      </div>
    </div>
  </section>

  <article class="learn-body">
{body_html}
  </article>

  <footer>
    <p>Microsoft AI Co-Innovation Lab — Wisconsin &nbsp;·&nbsp; Build with us: Support and Knowledge Base for Beginners</p>
  </footer>

</body>
</html>
"""


def convert(md_path, out_path, depth):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    text = rewrite_links(text)
    text = task_checkboxes(text)
    title, body = extract_title(text)
    category = CATEGORY.get(os.path.basename(os.path.dirname(md_path)), "Overview")
    body_html = markdown.markdown(body, extensions=MD_EXT)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html(title, category, body_html, depth))
    return title


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    built = []

    # Root README -> index.html
    readme = os.path.join(ROOT, "README.md")
    if os.path.exists(readme):
        convert(readme, os.path.join(OUT, "index.html"), depth=0)
        built.append("index.html")

    # Content folders
    for d in CONTENT_DIRS:
        src_dir = os.path.join(ROOT, d)
        if not os.path.isdir(src_dir):
            continue
        for name in sorted(os.listdir(src_dir)):
            if not name.endswith(".md"):
                continue
            src = os.path.join(src_dir, name)
            out = os.path.join(OUT, d, name[:-3] + ".html")
            convert(src, out, depth=1)
            built.append(f"{d}/{name[:-3]}.html")

    # Copy the sample-file folders so their assets travel with the site.
    samples = os.path.join(ROOT, "05-Sample-Files")
    if os.path.isdir(samples):
        shutil.copytree(samples, os.path.join(OUT, "05-Sample-Files"))

    # Write the extras stylesheet.
    with open(os.path.join(OUT, "site-extras.css"), "w", encoding="utf-8") as f:
        f.write(EXTRAS_CSS)

    print(f"Built {len(built)} pages into {OUT}")
    for b in built:
        print("  -", b)


EXTRAS_CSS = """/* Extras for generated pages: elements the base stylesheet doesn't cover.
   Uses the same CSS variables as the base stylesheet so it blends in. */

/* Tables */
.learn-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.2rem 0 1.6rem;
  font-size: 0.97rem;
}
.learn-body th,
.learn-body td {
  border: 1px solid var(--bg-card-border);
  padding: 0.6rem 0.8rem;
  text-align: left;
  vertical-align: top;
}
.learn-body th {
  background: rgba(0, 120, 212, 0.15);
  color: var(--text-primary);
  font-weight: 700;
}
.learn-body td { color: var(--text-secondary); }
.learn-body tr:nth-child(even) td { background: rgba(255, 255, 255, 0.02); }
.learn-body table code { white-space: nowrap; }

/* Fenced code blocks */
.learn-body pre {
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid var(--bg-card-border);
  border-left: 3px solid var(--ms-blue);
  border-radius: 6px;
  padding: 0.9rem 1.1rem;
  margin: 1rem 0 1.4rem;
  overflow-x: auto;
}
.learn-body pre code {
  display: block;
  font-family: 'Consolas', 'SF Mono', 'Cascadia Code', monospace;
  font-size: 0.9rem;
  line-height: 1.6;
  white-space: pre;
  background: none;
  border: none;
  padding: 0;
  color: var(--text-primary);
}

/* Blockquotes / callouts */
.learn-body blockquote {
  border-left: 4px solid var(--ms-blue);
  background: linear-gradient(135deg, rgba(0, 120, 212, 0.10), rgba(0, 180, 216, 0.05));
  border-radius: 8px;
  padding: 1rem 1.4rem;
  margin: 1.4rem 0;
}
.learn-body blockquote p { color: var(--text-primary); margin-bottom: 0.5rem; }
.learn-body blockquote p:last-child { margin-bottom: 0; }

/* Nested lists */
.learn-body ul ul,
.learn-body ul ol,
.learn-body ol ul,
.learn-body ol ol { margin: 0.5rem 0 0.5rem 0; }
.learn-body ol { padding-left: 1.4rem; color: var(--text-secondary); }
.learn-body ol li { font-size: 1.02rem; margin-bottom: 0.3rem; }

/* Horizontal rule */
.learn-body hr {
  border: none;
  border-top: 1px solid var(--bg-card-border);
  margin: 2.2rem 0;
}

/* Microsoft 2x2 logo (no image dependency) */
.ms-logo { display: grid; grid-template-columns: 11px 11px; gap: 3px; }
.ms-logo span { display: block; width: 11px; height: 11px; }
.ms-logo .sq1 { background: #F25022; }
.ms-logo .sq2 { background: #7FBA00; }
.ms-logo .sq3 { background: #00A4EF; }
.ms-logo .sq4 { background: #FFB900; }
"""


if __name__ == "__main__":
    main()
