# Copilot 101 — Sample Markdown & Prompt Examples

A companion handout for the **GitHub Copilot 101** segment of Day 2 (see the [Day 2 Facilitator Guide](Day%202%20Facilitator%20Guide.md), Step 3). It has two jobs:

1. **Be a real Markdown file** you can open and preview so the room can see what Markdown looks like.
2. **Give ready-to-use prompt examples** participants can adapt during the build.

> Tip: In VS Code, open this file and press **Ctrl+Shift+V** (Cmd+Shift+V on Mac) to see the rendered preview side by side with the raw text.

---

## Part 1 · This Is a Markdown File

Markdown is just plain text with a few simple symbols that turn into formatting. You write it in any editor, and tools like VS Code and GitHub render it nicely. We use it for notes, documentation, and prompts.

Here is the same content shown as raw symbols (left) and what it becomes (rendered):

### Headings
Put `#` symbols before a line. More `#` means a smaller heading.

```markdown
# Big heading
## Medium heading
### Small heading
```

### Emphasis
```markdown
**bold text**   *italic text*   `inline code`
```
Renders as: **bold text**, *italic text*, `inline code`.

### Lists
```markdown
- First item
- Second item
  - Indented sub-item

1. Step one
2. Step two
```
- First item
- Second item
  - Indented sub-item

1. Step one
2. Step two

### Checkboxes
```markdown
- [ ] Not done yet
- [x] Done
```
- [ ] Not done yet
- [x] Done

### Links
```markdown
[Link text](https://example.com)
```
Renders as: [Link text](https://example.com)

### Code blocks
Wrap code in triple backticks. Add the language name for color:

````markdown
```python
def hello():
    print("Hello, world!")
```
````

```python
def hello():
    print("Hello, world!")
```

### Quotes and tables
```markdown
> This is a quote — good for callouts.

| Column A | Column B |
|----------|----------|
| Row 1    | Value    |
```

> This is a quote — good for callouts.

| Column A | Column B |
|----------|----------|
| Row 1    | Value    |

That's most of what you'll ever need. Everything in this file — and every `.md` file in this repo — uses only these symbols.

---

## Part 2 · How to Write a Good Prompt

A good prompt gives Copilot enough to get it right the first time. Aim for these five parts (you won't always need all of them):

1. **Goal** — what you want to happen.
2. **Context** — which file, function, or part of the app it applies to.
3. **Specifics** — names, values, colors, wording, behavior.
4. **Example or format** — show a sample, or say how the result should look.
5. **Constraints** — what *not* to change, or rules to follow.

A simple pattern that works:

> "In `<file>`, <do this specific thing> so that <this happens>. Keep <this> unchanged."

Then **iterate**: run it, see the result, and refine with a follow-up like *"good, now also…"* or *"that broke X — fix it and keep the rest."*

---

## Part 3 · Weak vs. Strong Prompts

Same intent — the strong version gets a better result.

| Weak (vague) | Strong (specific) |
|---|---|
| "Make it look better." | "In `project_config.py`, change the app name to **Acme Support** and the primary color to a dark blue (#1B3A6B)." |
| "Add a page." | "In `app.py`, add a new route `/about` that renders a simple page with a heading 'About Acme Support' and one paragraph describing the company." |
| "Fix the error." | "Running `python app.py` gives this error: *[paste the error]*. What's causing it and how do I fix it?" |
| "Add a tool." | "In `custom_tools.py`, add an async function `get_store_hours` that returns our hours (Mon–Fri 9–5). Give it a clear docstring so the agent can call it." |
| "Change the questions." | "In `project_config.py`, replace the sample prompts with three questions a customer would ask our support agent about bike brakes." |
| "Explain this." | "Explain what `project_config.py` does, section by section, in plain language for a non-developer." |

---

## Part 4 · Ready-to-Use Prompts for Today's Build

Adapt these during the guided build and your own build. They match the template app's files.

### Understand the code
- "Give me a plain-language tour of this project's folder structure. Which files am I meant to edit?"
- "Explain `project_config.py` section by section. What does each setting control?"
- "What does the `agent_config` section do, and how does the app decide which agent to talk to?"

### Branding and UI
- "In `project_config.py`, set the app `name` to **[Company] Support Assistant** and update the description to one sentence about what it helps with."
- "Change the sample prompts shown on the chat screen to three realistic questions our users would ask."
- "Change the app's primary color to **[hex or color name]** and make the header show our company name."

### Content and behavior
- "In `core/tools/example_tools.py`, replace the `_FAQ_DATA` entries with five questions and answers about [our topic]."
- "In `custom_tools.py`, add an async function `[name]` that [does X]. Include a clear docstring, then show me how to register it in `project_config.py`."
- "Add a friendly welcome message that appears when the chat first loads."

### Add a feature or page
- "In `app.py`, add a route `/help` that renders a page listing three example questions users can ask."
- "Add a button labeled 'Clear conversation' that resets the chat."

### Test and fix
- "Running the app shows this error: *[paste error]*. Explain the cause and give me the fix."
- "The app starts but the agent doesn't respond. Walk me through what to check in my `.env` and the Settings page."
- "This change broke the page. Undo the layout change but keep the new text."

### Golden rule
> After every prompt: **read it, run it, test it.** If it's wrong, undo and try a clearer prompt. You are always in control — Copilot drafts, you decide.
