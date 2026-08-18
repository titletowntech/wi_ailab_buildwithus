# Build with us: Support and Knowledge Base for Beginners — Day 2 Facilitator Guide

A detailed, step-by-step plan for the facilitator to run Day 2. Work through it in order, but let the day breathe: the schedule is a guide, not a stopwatch. When a good question or discovery opens a useful tangent, follow it — then bring the room back to the current step.

**Day 2 focus:** Each company uses **GitHub Copilot and VS Code** to build a small app around the agent they created on Day 1 — first a guided build together using the provided template, then a version customized for their own use case. The theme: *building software with AI assistance.*

Companion documents: [Day 2 Agenda.md](../03-Event-Agendas/Day%202%20Agenda.md) · [Day 1 Facilitator Guide.md](Day%201%20Facilitator%20Guide.md) · [Day 2 Guided Agent Kit.md](Day%202%20Guided%20Agent%20Kit.md)

Template app: [titletowntech/wi_ailab_prototype_foundrytemplate](https://github.com/titletowntech/wi_ailab_prototype_foundrytemplate) — the source participants use to connect their Day 1 Foundry agent to an app.

---

## How to Use This Guide

- **Move step by step.** Each section below is a stop on the path. Finish one before moving to the next.
- **Not time-bound.** The agenda has suggested times, but the day progresses at whatever pace it goes. Don't rush a step that's landing well; don't linger on one that's done.
- **Allow tangents.** Real questions from the room are where the learning happens. Follow a worthwhile tangent, capture anything off-topic in a "parking lot," and return to the step you left.
- **Protect the group.** Never stall the whole room for one blocked team. Hand blockers to the escalation facilitator and keep the group moving.
- **Keep Copilot in the driver's seat — with a human at the wheel.** The goal today is for participants to *build with AI assistance*: describe what they want, let Copilot draft it, then read, test, and iterate. Reinforce that they stay in control — accept, reject, and adjust.

---

## Facilitator Roles

If you have a team, split these roles. If you're running it solo, keep the order the same and lean on the group to help each other.

- **Lead facilitator** — Owns pacing and transitions, opens and closes each step, leads the guided build and demos, decides when to follow a tangent and when to move on.
- **Technical facilitators** — Circulate during hands-on steps; help with VS Code, Copilot, Python, Git, running the app, and connecting the agent; surface repeated issues so the lead can address the whole room.
- **Escalation facilitator** — Owns environment and connection blockers (Copilot sign-in, Python, Git, `.env`, Foundry agent auth) so they don't slow the room; pulls blocked participants aside; tracks unresolved issues in Teams.
- **Room / ops support** — Wi-Fi, check-in, Teams and file sharing, breaks, and logistics.

---

## Before the Day Starts

- [ ] Room, Wi-Fi, and power confirmed; Teams channel open for file sharing.
- [ ] Your own copy of the template app running locally — you will demo the finished experience.
- [ ] The **finished app** ready to show as the "destination" before anyone builds.
- [ ] The template repository is public, or the source is published at another publicly downloadable location and every link in these materials is updated.
- [ ] The template repo is confirmed downloadable without authentication on the event network.
- [ ] A known-good **`.env`** recipe is ready — the exact Azure AI Foundry values participants need (`AZURE_FOUNDRY_ENDPOINT`, `AZURE_FOUNDRY_API_KEY`, `AZURE_AI_PROJECT_ENDPOINT`, `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET`).
- [ ] A participant walkthrough is ready for creating an Entra app registration and client secret, then assigning **Azure AI Developer** on the team's Foundry project.
- [ ] Teams without app-registration or Azure role-assignment permission have identified administrators available to complete those steps.
- [ ] A short list of **guided-build Copilot prompts** ready to share (branding change, add a page, add a feature) — see the [Copilot 101 handout](Copilot%20101%20-%20Sample%20Markdown%20and%20Prompts.md).
- [ ] A shared blocker tracker open (Teams or a simple list) with columns for issue, owner, and status.

> **Connecting to the Day 1 agent — read this first.** The template chats with a Foundry **model** out of the box. To route chat to the **agent** each team built on Day 1, the app's **Settings** page has a **Backend** dropdown ("Azure Foundry Agent"). Microsoft Agent Framework requires Microsoft Entra authentication for this connection; the Foundry API key alone is not sufficient. Each team creates a dedicated app registration and client secret, then grants that service principal the **Azure AI Developer** role on its Foundry project. Keep the secret only in the local `.env` file: never post it in Teams, place it in participant materials, or commit it to source control. See the template's README section *"Connect to an Azure Foundry agent."*

---

## Step 1 · Tech Setup

**Goal:** Everyone's development environment is ready before any content begins.

Do this:
1. Welcome people and point them to Wi-Fi and the Teams channel.
2. Confirm each participant can **open VS Code** and that **GitHub Copilot is signed in and working** (Copilot Chat responds).
3. Confirm each participant has the **template app downloaded** and open in VS Code.
4. Confirm each team can create an **Entra app registration** and assign Azure roles, or has the appropriate administrators available.
5. Confirm Python is available and they can create/activate a virtual environment.
6. Open a terminal and confirm `git --version` runs successfully.
7. Technical and escalation facilitators circulate to clear setup issues immediately.

Watch for:
- Copilot not suggesting or Chat unavailable → check sign-in and the correct GitHub account with an active Copilot plan.
- `python` not recognized, or `pip install` blocked → work as an escalation blocker.
- `git` not recognized → install Git, restart the terminal, and run `git --version` again.
- Template not downloaded → get them the repo before content starts.
- App registration or role assignment is blocked → involve the team's Entra or Azure administrator.

Move on when: most of the room has VS Code, Python, Git, and Copilot working and the template open. Hand stragglers to escalation and begin.

---

## Step 2 · Day 2 Overview

**Goal:** Everyone understands what they're building today and how AI helps them build it.

Do this:
1. State the goal plainly: *today we wrap your Day 1 agent in a simple app, using GitHub Copilot to help us write the code.*
2. **Show the finished app.** Type a question, show it answering through the agent. Seeing the destination first makes the build make sense.
3. Give a quick tour of how the day flows: Copilot 101 → guided build together → build your own → share.
4. Set expectations: you don't need to be a developer today; you need to describe what you want and work with Copilot to get there.

Tangent to allow: "how much coding do I actually have to know?" — address it head-on. The reassuring answer sets the tone for the whole day.

Move on when: the room can describe, in a sentence, what they're building and the role Copilot plays.

---

## Step 3 · GitHub Copilot 101

**Goal:** Everyone can use Copilot effectively before the build starts. Keep it practical and hands-on — this short segment is what makes the guided build go smoothly.

Handout: [Copilot 101 — Sample Markdown & Prompt Examples](Copilot%20101%20-%20Sample%20Markdown%20and%20Prompts.md). Open it in VS Code and use it live — it doubles as the sample Markdown file (below) and the prompt reference.

### 3a. Show what Copilot does in VS Code
1. **Inline suggestions** — start typing or write a comment describing what you want; Copilot suggests code you accept with **Tab**.
2. **Copilot Chat** — ask questions or request changes in plain language in the chat panel.
3. **Edits across files** — Copilot can propose changes spanning multiple files; you review and apply them.
4. Point out that you can always **undo** (Ctrl+Z) if a suggestion isn't right.

### 3b. Explain Markdown (and show a real `.md` file)
1. Open the handout [Copilot 101 — Sample Markdown & Prompt Examples](Copilot%20101%20-%20Sample%20Markdown%20and%20Prompts.md) and press **Ctrl+Shift+V** to show the rendered preview next to the raw text.
2. Point out the handful of symbols that do everything: `#` headings, `**bold**`, `-` lists, `` `code` ``, links, and code blocks.
3. Explain *why we care*: our notes, docs, and many prompts are Markdown — and it's the plain, readable format Copilot works well with.

### 3c. Teach a good-prompt pattern
Walk through the five parts of a strong prompt (full version and more examples are in the handout):

1. **Goal** — what you want to happen.
2. **Context** — which file or part of the app.
3. **Specifics** — names, values, colors, wording.
4. **Example or format** — show a sample or say how it should look.
5. **Constraints** — what *not* to change.

A pattern that works: *"In `<file>`, `<do this specific thing>` so that `<this happens>`. Keep `<this>` unchanged."*

Show a weak-vs-strong pair so the difference lands:

- Weak: *"Make it look better."*
- Strong: *"In `project_config.py`, change the app name to **Acme Support** and the primary color to a dark blue (#1B3A6B)."*

### 3d. Show the accept / reject / iterate loop
1. Accept a suggestion, then refine it with a follow-up (*"good, now also…"*).
2. Reject one and rewrite the prompt more specifically.
3. Show how to **undo** when Copilot goes the wrong way, and re-approach with a clearer prompt.

### 3e. Quick hands-on together
Do one small exercise as a group so everyone succeeds once — for example, open the handout and have everyone ask Copilot Chat: *"Explain what a `project_config.py` file is likely used for in a small web app, in plain language."* Confirm everyone gets a response.

Watch for: participants accepting code they don't understand. Model the habit out loud — *read it, run it, then keep or revert.*

Move on when: everyone has generated and accepted (or rejected) at least one Copilot suggestion.

---

## Step 4 · Guided Build — Connect the Agent (Template App)

**Goal:** Everyone builds the *same* app together using the template, connects it to a Day 1 agent, and sees it respond. This is the anchor of the day — go slow enough that everyone succeeds.

Use the [Day 2 Guided Agent Kit](Day%202%20Guided%20Agent%20Kit.md) for the exact build script, connection recipe, and step-by-step Copilot prompts.

### 4a. Tour the template
1. Walk the room through the template's structure: each prototype lives in its own folder under `projects/`, and a developer only edits a few files.
2. Point out the **files you edit** — `project_config.py` (name, UI, agent config), `core/tools/example_tools.py` (the FAQ/example data), `custom_tools.py` (optional custom tools), and `app.py` (routes) — and the **framework you don't** (`core/` and `ui/`).
3. Emphasize: copy the template folder first, then work only in those few files.

### 4b. Create the project and set credentials
1. Have each team **copy** `projects/_template` to a new folder (e.g., `projects/my-company`).
2. Have each team create a dedicated **Microsoft Entra app registration** and a client secret. Copy the secret value immediately and store it securely; it is shown only once.
3. In the Azure portal, open the team's Foundry project access control (**IAM**) and assign the app registration the **Azure AI Developer** role.
4. Copy `.env.example` to `.env` and fill in the Azure AI Foundry values plus `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET`. Confirm `.env` is excluded from source control.
5. Install dependencies and confirm the app **runs** before changing anything: activate the virtual environment, `pip install -r requirements.txt`, `python app.py`, then open `http://localhost:5000`.
6. Get a working, unmodified app on every screen before customizing — a shared "it works" moment.

### 4c. Connect the Day 1 agent
1. Confirm the team's app registration, client secret, and Foundry role assignment are complete.
2. In the running app, open the **Settings** page and set the **Backend** to **Azure Foundry Agent** so chat routes to the team's Day 1 agent.
3. Confirm the app answers using the agent, not a generic model.

### 4d. Customize with Copilot
1. Use Copilot Chat to make guided changes step by step — share your prepared prompts. Good first changes:
   - **Branding / UI** — change the app name, colors, and sample prompts in `project_config.py`.
   - **Content** — update the example FAQ data.
   - **Behavior** — adjust a sample prompt or add a small feature.
2. After each change: **read it, run it, test it.** Reinforce the accept/reject/iterate loop.
3. Do frequent check-ins: "Thumbs up when your app restarts cleanly." Wait for the room before advancing.

### 4e. Test
1. Ask questions that **should** work and confirm the app responds through the agent.
2. Note that good app behavior depends on the Day 1 agent behind it — a callback to yesterday's *good data* lesson.

Watch for:
- App won't start → almost always a `.env` value or a Python/venv issue; check those first.
- Port `5000` already in use → stop the other process or run on a different port.
- Agent errors / auth failures → verify tenant/client IDs, secret value and expiration, and the Foundry role assignment; never ask a participant to post the secret in chat or Teams.
- Copilot edit breaks the app → use it as a teaching moment: undo, describe the goal more precisely, try again.

Tangent to allow: "could Copilot add *X*?" is a great live demo — try it together briefly, then return.

Move on when: every team has the template app running, connected to their Day 1 agent, with at least one Copilot-made change and a successful test.

---

## Step 5 · Lunch / Working Break

Use this as a buffer. Technical and escalation facilitators stay available to unblock any team that's behind so everyone starts the afternoon on even footing.

---

## Step 6 · Build Your Own

**Goal:** Each company customizes the app for their own use case, with one-on-one coaching. This is where it becomes their app.

Do this:
1. Have teams point the app at **their own** Day 1 agent (their company's use case).
2. Use Copilot to **customize** the app — branding, sample prompts, the example FAQ/tools, and any small features that fit their scenario.
3. Encourage progressive changes, each tested before the next:
   - Branding / UI change
   - Add or change a page or screen
   - Add a small piece of functionality
   - Tune the experience for their users
4. Have them **test** deliberately:
   - Which questions **should** work?
   - Which questions **should not** work?

Facilitators: coach one-on-one. Circulate constantly. Encourage teams to describe intent to Copilot in plain language, then read and test what it produces.

Watch for:
- Scope creep → help them pick one or two changes they can finish and demo.
- A team stuck on setup → escalate so their build time isn't lost.
- Copilot rabbit holes → coach them to revert to the last working version and re-approach with a clearer prompt.

Move on when: each team has a working app of their own (even a modest one) and something they're proud to show.

---

## Step 7 · Demos

**Goal:** Teams share what they built and learn from each other. Demos are optional but strongly encouraged.

Do this:
1. Invite companies to give a short demo, each covering:
   - **Problem** — what they set out to solve
   - **Solution** — the app they built
   - **Lessons** — what they learned building with AI assistance
2. Keep them short so several teams can share.
3. Call out patterns — especially clever uses of Copilot and moments where describing intent clearly produced better results.

Move on when: a good cross-section of teams has shared.

---

## Step 8 · Wrap-Up & Next Steps

**Goal:** Close the event and point participants toward what's next.

Do this:
1. **Recap the two days** — from a knowledge-grounded agent on Day 1 to a working app around it on Day 2.
2. **Discuss future deployment** — what it would take to move from prototype to something their team could use.
3. Have each company name a concrete next step:
   - What they built and the problem it solves
   - What a version 2 should include
   - Who owns next steps, and what help they need
4. **Share resources** for continued learning (Copilot, the template, Azure AI Foundry).
5. Q&A and closing.

---

## Blocker Model (Green / Yellow / Red)

Use this all day to keep the room moving:

- **Green** — Team is progressing normally.
- **Yellow** — Minor issue, but they can continue. A technical facilitator helps in the flow.
- **Red** — Team is blocked and cannot progress. Escalation facilitator takes it aside; capture it in the tracker; rejoin the team to the main flow when ready.

Rules: don't stop the whole room for one red blocker; keep every blocker visible with an owner.

Common issues and responses:

| Issue | Response |
|---|---|
| Copilot not suggesting / Chat unavailable | Check sign-in and the correct GitHub account with an active Copilot plan |
| `python` not recognized / venv won't activate | Escalation support; confirm Python install and activation command |
| `pip install` fails or is blocked | Check network/proxy; escalation support for company restrictions |
| App won't start | Check `.env` values and that the virtual environment is active |
| Port 5000 already in use | Stop the other process or run the app on a different port |
| Agent auth / Foundry connection error | Verify the team's app registration, secret, tenant/client IDs, and Foundry role assignment; hand to escalation without sharing the secret |
| App runs but the agent errors | Verify endpoint and keys in `.env` and the Settings backend selection |
| Copilot edit broke the app | Undo to the last working version; restate the goal and retry |
| Team is behind | Keep them on the guided build; skip optional customizations |

---

## End-of-Day Facilitator Checklist

Before closing, confirm:

- [ ] Every team ran the template app locally.
- [ ] Every team connected the app to a Day 1 agent and saw it respond.
- [ ] Every team made at least one change with Copilot and tested it.
- [ ] Every team customized the app for **their own** use case (even modestly).
- [ ] Teams shared or prepared a short demo.
- [ ] Each company named a concrete next step and who owns it.
- [ ] Open blockers are captured with an owner for follow-up.

---

## Closing Through-Line

Use or adapt this to close the event:

> Over two days you went from an idea to something real: on Day 1 you built a knowledge-grounded agent from trusted documents, and today you wrapped it in a working app — with GitHub Copilot helping you write the code. That's what building with AI assistance looks like. You described what you wanted, AI drafted it, and you read, tested, and refined it. You don't have to be a career developer to build something useful — you have to know your problem, bring good knowledge, and work with your tools. Take that back to your team, and keep building.
