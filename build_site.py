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

# On the published site the sample files are distributed only as a single zip.
SAMPLES_ZIP = "BWU_Sample_Files.zip"
SAMPLES_ZIP_URL = (
    "https://titletowntech.github.io/wi_ailab_buildwithus/site/BWU_Sample_Files.zip"
)

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

# The planning worksheet is rendered as an interactive tool instead of static text.
PLANNER_NAME = "Event Planning Timeline Worksheet.md"


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


def rewrite_sample_links(md_text: str) -> str:
    """Point every 05-Sample-Files link at the downloadable sample-files zip."""
    pattern = re.compile(r"\]\((?!https?://)[^)]*05-Sample-Files[^)]*\)")
    return pattern.sub(f"]({SAMPLES_ZIP_URL})", md_text)


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
    text = rewrite_sample_links(text)
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
            if name == PLANNER_NAME:
                write_planner(src, out, d)
            else:
                convert(src, out, depth=1)
            built.append(f"{d}/{name[:-3]}.html")

    # Ship the sample files as a single zip download; the site links only to this.
    samples_zip = os.path.join(ROOT, SAMPLES_ZIP)
    if os.path.isfile(samples_zip):
        shutil.copy2(samples_zip, os.path.join(OUT, SAMPLES_ZIP))
    else:
        print(f"WARNING: {SAMPLES_ZIP} not found at repo root; site links will 404.")

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

/* Interactive planner worksheet */
.planner-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  margin: 1.5rem 0 2rem;
}
.planner-field { display: flex; flex-direction: column; gap: 0.35rem; }
.planner-field label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--ms-blue-light);
}
.planner-field input,
.planner-field select,
.learn-body .planner-tbl input,
.learn-body .planner-tbl select {
  background: var(--bg-card);
  color: var(--text-primary);
  border: 1px solid var(--bg-card-border);
  border-radius: 6px;
  padding: 0.5rem 0.6rem;
  font-size: 0.95rem;
  font-family: inherit;
}
.planner-field input[type="date"] { color-scheme: dark; }
.planner-tbl input, .planner-tbl select { width: 100%; }
.planner-date { color: var(--text-accent); font-weight: 600; white-space: nowrap; }
.planner-actions { display: flex; gap: 0.8rem; flex-wrap: wrap; margin: 1.5rem 0 1rem; }
.planner-btn {
  background: linear-gradient(135deg, var(--ms-blue), var(--ms-blue-dark));
  color: #fff;
  border: none;
  border-radius: 2rem;
  padding: 0.7rem 1.4rem;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
}
.planner-btn.secondary {
  background: transparent;
  border: 1px solid rgba(80, 230, 255, 0.4);
  color: var(--ms-blue-light);
}
.planner-output textarea {
  width: 100%;
  min-height: 340px;
  background: rgba(0, 0, 0, 0.35);
  color: var(--text-primary);
  border: 1px solid var(--bg-card-border);
  border-radius: 8px;
  padding: 1rem;
  font-family: 'Consolas', 'SF Mono', 'Cascadia Code', monospace;
  font-size: 0.85rem;
  line-height: 1.5;
}
.planner-hint { font-size: 0.9rem; color: var(--text-secondary); font-style: italic; }
"""


PLANNER_BODY = r'''<p class="lead">Pick your <strong>Event Day 1</strong> date and this worksheet fills in every milestone automatically by working backward. Adjust the number of readiness weeks if your program differs, add meeting times and links, then generate a plain-text summary to paste into your notes.</p>

<div class="planner-controls">
  <div class="planner-field">
    <label for="eventDay1">Event — Day 1</label>
    <input type="date" id="eventDay1" />
  </div>
  <div class="planner-field">
    <label for="weeks">Readiness weeks</label>
    <input type="number" id="weeks" min="1" max="12" value="4" />
  </div>
</div>

<p class="planner-hint" id="anchorLine">Choose an Event Day 1 date to populate the plan.</p>

<div id="planner-tables"></div>

<div class="planner-actions">
  <button type="button" class="planner-btn" id="genBtn">Generate text summary</button>
  <button type="button" class="planner-btn secondary" id="copyBtn">Copy to clipboard</button>
  <button type="button" class="planner-btn secondary" id="dlBtn">Download .txt</button>
</div>

<div class="planner-output">
  <textarea id="output" readonly placeholder="Your populated plan will appear here after you click Generate text summary."></textarea>
</div>

<script>
(function(){
  var state = {};
  var FIXED = [
    {title: "Phase 1 \u00b7 Organizer Preparation", type: "table", rows: [
      {key: "prep_confirm", label: "Confirm event dates, venue/platform, and budget", days: 70},
      {key: "prep_materials", label: "Finalize program materials (agendas, worksheets, packages)", days: 56},
      {key: "prep_site", label: "Confirm pre-skilling site is live and current", days: 56},
      {key: "prep_day1", label: "Prepare Day 1 guided-agent kit and sample files", days: 42},
      {key: "prep_day2", label: "Confirm Day 2 template app and facilitator guide", days: 42},
      {key: "prep_teams", label: "Stand up and configure the Teams community", days: 42},
      {key: "prep_fac", label: "Confirm facilitators / coaches and their roles", days: 35}
    ]},
    {title: "Phase 2 \u00b7 Registration and Onboarding", type: "table", rows: [
      {key: "reg_open", label: "Registration opens (form live, promoted)", days: 70},
      {key: "reg_close", label: "Registration closes", days: 49},
      {key: "reg_review", label: "Applications reviewed; organizations accepted", days: 46},
      {key: "reg_onboard", label: "Acceptance / onboarding communications sent", days: 42},
      {key: "reg_added", label: "Participants added to the Teams community", days: 42}
    ]},
    {title: "Phase 3 \u00b7 Kickoff and Weekly Readiness Meetings", type: "weekly"},
    {title: "Readiness Targets (during the readiness weeks)", type: "table", rows: [
      {key: "hw_dist", label: "Homework package distributed (at Kickoff)", days: "KICKOFF"},
      {key: "pre_assign", label: "Pre-skilling assigned (at Kickoff)", days: "KICKOFF"},
      {key: "biz_ready", label: "Target: business readiness complete per org", days: 14},
      {key: "tech_ready", label: "Target: technical readiness complete per org", days: 14},
      {key: "pre_ready", label: "Target: pre-skilling complete per org", days: 14}
    ]},
    {title: "Phase 4 \u00b7 Final Readiness Review (Go / No-Go)", type: "table", rows: [
      {key: "final_review", label: "Final Readiness Review meeting (Go/No-Go)", days: 7},
      {key: "gonogo", label: "Go/No-Go decision communicated per organization", days: 7},
      {key: "lab_test", label: "Lab environment tested end-to-end", days: 7},
      {key: "attendees", label: "Final attendee list confirmed", days: 7},
      {key: "logistics", label: "Logistics confirmed (catering, room, A/V, Wi-Fi)", days: 3}
    ]},
    {title: "Phase 5 \u00b7 The Event", type: "table", rows: [
      {key: "day1", label: "Event Day 1 \u2014 build and evaluate the agent", days: 0},
      {key: "day2", label: "Event Day 2 \u2014 build the app with Copilot", days: -1},
      {key: "survey", label: "Post-event feedback survey sent", days: -1},
      {key: "followup", label: "Post-event follow-up / next steps", days: -14}
    ]}
  ];

  function pad(n){ return (n < 10 ? "0" : "") + n; }
  function isoStr(d){ return d ? d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()) : ""; }
  function friendly(d){ return d ? d.toLocaleDateString(undefined, {weekday: "short", year: "numeric", month: "short", day: "numeric"}) : "\u2014"; }
  function eventDate(){ var v = document.getElementById("eventDay1").value; if(!v) return null; var p = v.split("-"); return new Date(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10)); }
  function weeks(){ var n = parseInt(document.getElementById("weeks").value, 10); return (isNaN(n) || n < 1) ? 4 : n; }
  function addDays(base, days){ var d = new Date(base.getTime()); d.setDate(d.getDate() + days); return d; }
  function mDate(days){ var e = eventDate(); if(!e) return null; return addDays(e, -days); }
  function daysFor(spec){ return spec === "KICKOFF" ? (weeks() + 1) * 7 : spec; }
  function esc(s){ return (s || "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;"); }
  function recLabel(days){
    if(days === 0) return "Event Day 1";
    if(days < 0) return "Event +" + (-days) + ((-days) === 1 ? " day" : " days");
    if(days % 7 === 0) return "T\u2011minus " + (days / 7) + " weeks";
    return "T\u2011minus " + days + " days";
  }
  function textInp(key, ph){ return '<input type="text" data-key="' + key + '" value="' + esc(state[key]) + '" placeholder="' + ph + '" />'; }

  function render(){
    var n = weeks();
    var html = "";
    for(var i = 0; i < FIXED.length; i++){
      var ph = FIXED[i];
      html += "<h2>" + ph.title + "</h2>";
      if(ph.type === "weekly"){
        html += '<table class="planner-tbl"><thead><tr><th>Meeting</th><th>Date</th><th>Time</th><th>Link / location</th></tr></thead><tbody>';
        for(var k = 1; k <= n; k++){
          var off = ((n + 1) - (k - 1)) * 7;
          var label = (k === 1) ? "Kickoff \u2014 Week 1" : "Weekly Readiness \u2014 Week " + k;
          var d = mDate(off);
          html += "<tr><td>" + label + ' <span class="planner-hint">(' + recLabel(off) + ")</span></td>"
            + '<td class="planner-date">' + friendly(d) + "</td>"
            + "<td>" + textInp("wk_time_" + k, "e.g., 3:00 PM") + "</td>"
            + "<td>" + textInp("wk_link_" + k, "Teams link") + "</td></tr>";
        }
        html += "</tbody></table>";
      } else {
        html += '<table class="planner-tbl"><thead><tr><th>Milestone</th><th>Recommended</th><th>Date</th></tr></thead><tbody>';
        for(var r = 0; r < ph.rows.length; r++){
          var row = ph.rows[r]; var days = daysFor(row.days); var dd = mDate(days);
          html += "<tr><td>" + row.label + "</td>"
            + '<td class="planner-hint">' + recLabel(days) + "</td>"
            + '<td class="planner-date">' + friendly(dd) + "</td></tr>";
        }
        html += "</tbody></table>";
      }
    }
    document.getElementById("planner-tables").innerHTML = html;
    updateAnchor();
  }

  function updateAnchor(){
    var e = eventDate(); var el = document.getElementById("anchorLine");
    if(!e){ el.textContent = "Choose an Event Day 1 date to populate the plan."; return; }
    var d2 = addDays(e, 1);
    el.innerHTML = "<strong>Event Day 1:</strong> " + friendly(e) + " &nbsp;\u00b7&nbsp; <strong>Event Day 2:</strong> " + friendly(d2) + " &nbsp;\u00b7&nbsp; <strong>Readiness weeks:</strong> " + weeks();
  }

  function generate(){
    var e = eventDate(); var n = weeks(); var out = [];
    out.push("BUILD WITH US: SUPPORT & KNOWLEDGE BASE FOR BEGINNERS");
    out.push("Event Planning Timeline");
    out.push("==============================================");
    if(e){ out.push("Event Day 1: " + isoStr(e) + " (" + friendly(e) + ")"); out.push("Event Day 2: " + isoStr(addDays(e, 1)) + " (" + friendly(addDays(e, 1)) + ")"); }
    else { out.push("Event Day 1: (not set \u2014 pick a date above)"); }
    out.push("Readiness weeks: " + n);
    out.push("");
    for(var i = 0; i < FIXED.length; i++){
      var ph = FIXED[i]; out.push(ph.title.toUpperCase());
      if(ph.type === "weekly"){
        for(var k = 1; k <= n; k++){
          var off = ((n + 1) - (k - 1)) * 7; var d = mDate(off);
          var label = (k === 1) ? "Kickoff \u2014 Week 1" : "Weekly Readiness \u2014 Week " + k;
          var ex = []; var tm = state["wk_time_" + k]; var lk = state["wk_link_" + k];
          if(tm) ex.push("Time: " + tm); if(lk) ex.push("Link: " + lk);
          out.push("- " + (isoStr(d) || "(no date)") + "  " + label + (ex.length ? "  [" + ex.join(" | ") + "]" : ""));
        }
      } else {
        for(var r = 0; r < ph.rows.length; r++){
          var row = ph.rows[r]; var days = daysFor(row.days); var d2 = mDate(days);
          out.push("- " + (isoStr(d2) || "(no date)") + "  " + row.label);
        }
      }
      out.push("");
    }
    document.getElementById("output").value = out.join("\n");
  }

  var tablesEl = document.getElementById("planner-tables");
  tablesEl.addEventListener("input", function(ev){ var t = ev.target; if(t.dataset && t.dataset.key){ state[t.dataset.key] = t.value; } });
  tablesEl.addEventListener("change", function(ev){ var t = ev.target; if(t.dataset && t.dataset.key){ state[t.dataset.key] = t.value; } });
  document.getElementById("eventDay1").addEventListener("change", render);
  document.getElementById("weeks").addEventListener("change", render);
  document.getElementById("weeks").addEventListener("input", render);
  document.getElementById("genBtn").addEventListener("click", generate);
  document.getElementById("copyBtn").addEventListener("click", function(){
    var ta = document.getElementById("output"); if(!ta.value) generate(); ta.select();
    if(navigator.clipboard){ navigator.clipboard.writeText(ta.value); } else { try { document.execCommand("copy"); } catch(e){} }
  });
  document.getElementById("dlBtn").addEventListener("click", function(){
    var ta = document.getElementById("output"); if(!ta.value) generate();
    var blob = new Blob([ta.value], {type: "text/plain"});
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "event-plan.txt"; a.click(); URL.revokeObjectURL(a.href);
  });

  render();
})();
</script>'''


def write_planner(md_path, out_path, folder):
    with open(md_path, "r", encoding="utf-8") as f:
        title, _ = extract_title(f.read())
    category = CATEGORY.get(folder, "Overview")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html(title, category, PLANNER_BODY, depth=1))


if __name__ == "__main__":
    main()
