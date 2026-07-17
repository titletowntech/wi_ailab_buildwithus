# Build with us: Support and Knowledge Base for Beginners — Day 1 Facilitator Guide

A detailed, step-by-step plan for the facilitator to run Day 1. Work through it in order, but let the day breathe: the schedule is a guide, not a stopwatch. When a good question or discovery opens a useful tangent, follow it — then bring the room back to the current step.

**Day 1 focus:** Each company builds and evaluates a Technical Support / Knowledge Base agent in Azure AI Foundry — first a guided agent together, then one using their own documents.

Companion documents: [Day 1 Agenda.md](../03-Event-Agendas/Day%201%20Agenda.md) · [Business Readiness Worksheet](../02-Participant-Materials/Business%20Readiness%20Worksheet.md) · [Technical Readiness Worksheet](../02-Participant-Materials/Technical%20Readiness%20Worksheet.md)

Sample materials: [Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/) (a clean, well-structured bike-troubleshooting knowledge base) and [Sample Files - Bad](../05-Sample-Files/Sample%20Files%20-%20Bad/) (the same topics as messy drafts, duplicates, and off-format documents) — used for the guided agent and the good-vs-bad-data demo.

Guided agent materials: the agent prompt, test questions, and the good-vs-bad-data demo are in the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md).

---

## How to Use This Guide

- **Move step by step.** Each section below is a stop on the path. Finish one before moving to the next.
- **Not time-bound.** The agenda has suggested times, but the day progresses at whatever pace it goes. Don't rush a step that's landing well; don't linger on one that's done.
- **Allow tangents.** Real questions from the room are where the learning happens. Follow a worthwhile tangent, capture anything off-topic in a "parking lot," and return to the step you left.
- **Protect the group.** Never stall the whole room for one blocked team. Hand blockers to the escalation facilitator and keep the group moving.
- **Watch for the through-line.** Everything today reinforces one idea: *better knowledge and clearer instructions produce a better agent.*

---

## Facilitator Roles

If you have a team, split these roles. If you're running it solo, keep the order the same and lean on the group to help each other.

- **Lead facilitator** — Owns pacing and transitions, opens and closes each step, leads demos and discussion, decides when to follow a tangent and when to move on.
- **Technical facilitators** — Circulate during hands-on steps, help with Foundry, uploads, prompts, and testing; surface repeated issues so the lead can address the whole room.
- **Escalation facilitator** — Owns access and environment blockers so they don't slow the room; pulls blocked participants aside; tracks unresolved issues in Teams.
- **Room / ops support** — Wi-Fi, check-in, Teams and file sharing, breaks, and logistics.

---

## Before the Day Starts

- [ ] Room, Wi-Fi, and power confirmed; Teams channel open and ready for file sharing.
- [ ] Your own Foundry project open and working — you will demo from it.
- [ ] The **finished guided agent** ready to show as the "destination" before anyone builds.
- [ ] The **guided agent materials** ready to share — prompt, test questions, and demo in the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md); sample file set in [Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/).
- [ ] The **good data** and **bad data** file sets ready for the data-quality demo ([Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/) and [Sample Files - Bad](../05-Sample-Files/Sample%20Files%20-%20Bad/)).
- [ ] Predefined test questions ready — ones that *should* work and ones that *should not* (see the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md)).
- [ ] A shared blocker tracker open (Teams or a simple list) with columns for issue, owner, and status.

---

## Step 1 · Tech Setup

**Goal:** Everyone is connected and can open a Foundry project before any content begins.

Do this:
1. Welcome people as they arrive and point them to Wi-Fi and the Teams channel.
2. Ask each participant to sign in to Azure and open Azure AI Foundry.
3. Confirm each person can **open (or create) a Foundry project** — this is the real readiness check.
4. Technical and escalation facilitators circulate to clear access issues immediately.

Watch for:
- "I can sign in but see no subscription" → escalation facilitator validates account / tenant / subscription.
- Wrong account or tenant → get them into the account they'll use for the lab.
- Can't open a project → work it as a red blocker so it doesn't surface later.

Move on when: most of the room can open a Foundry project. Don't hold the whole group for one or two stragglers — hand those to escalation and begin.

---

## Step 2 · Event Overview

**Goal:** Everyone understands what they're building today and why it matters.

Do this:
1. State the goal plainly: *today we each build a Technical Support / Knowledge Base agent grounded in real documents.*
2. **Show the finished guided agent.** Ask it a question it answers well, and one it correctly declines. Seeing the destination first makes the build make sense.
3. Give a quick tour of how the day flows: build a guided agent together → see how data quality changes results → build your own agent → share.
4. Set the tone: this is hands-on and collaborative; questions are welcome; we help each other.

Tangent to allow: if people ask "what can and can't an agent like this do?" — lean in briefly. It sets expectations and pays off all day. Park deep architecture or production questions for later.

Move on when: the room can describe, in a sentence, what they're building and what "good" looks like.

---

## Step 3 · Introductions

**Goal:** Everyone learns from one another's use cases and the room warms up.

Do this:
1. Go around the room. Each company shares, briefly:
   - Who they are
   - The support or knowledge problem they want to solve
   - One example question they'd love their agent to answer
2. Keep it moving — a couple of sentences each. Note interesting overlaps out loud so teams see shared challenges.

Watch for: a team whose use case is too broad or not a support/knowledge fit. Note it gently now; you'll help them narrow it in Step 6.

Move on when: everyone has shared and the room feels connected.

---

## Step 4 · Create the 1st Foundry Agent (Guided)

**Goal:** Everyone builds the *same* agent together, using materials you provide, and sees how to test and deploy it. This is the anchor of the day — go slow enough that everyone succeeds.

### 4a. Build the guided agent together
1. Share the **provided prompt** (from the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md)) and walk through what each part of it does and why.
2. Have participants upload **your** sample file set ([Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/)).
3. Build the agent step by step. Narrate what you're doing and pause so the room can catch up.
4. Do frequent check-ins: "Thumbs up when your agent is created." Wait for the room before advancing.

### 4b. Test the agent
1. Run the predefined questions that **should** work (see the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md)). Point out *why* the answers are good — they're grounded in the documents.
2. Run the predefined questions that **should not** work. Show the agent declining or staying within its knowledge, and explain why that's the *correct* behavior.
3. Emphasize the habit: *always test both what should and should not work.*

### 4c. Deploy the agent
1. Walk the room through deploying (or preparing to deploy) the agent.
2. Confirm each team has a working, deployed guided agent before moving on.

> **Publishing to Teams / Microsoft 365 requires one-time subscription setup.** The first time an agent is published, Foundry creates an **Azure Bot** resource, which needs the **`Microsoft.BotService`** resource provider registered on the subscription. If it isn't, publishing fails with *"The subscription is not registered to use namespace 'Microsoft.BotService'... [Code: MissingSubscriptionRegistration]"*. Confirm this was handled during readiness (see the [Technical Readiness Worksheet](../02-Participant-Materials/Technical%20Readiness%20Worksheet.md) and the [Day 1 Guided Agent Kit](Day%201%20Guided%20Agent%20Kit.md#5-publishing-to-teams--microsoft-365)). If a team hits this in the room, have someone with **Owner/Contributor** register the provider (Azure Portal → Subscription → **Resource providers** → **Microsoft.BotService** → **Register**, or `az provider register --namespace Microsoft.BotService`) — registration takes 1–2 minutes, after which they can retry publishing.

### 4d. Best practices — good data vs. bad data
1. Start with the **good data** set ([Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/)) and ask a question; note the quality of the answer.
2. Switch to the **bad data** set ([Sample Files - Bad](../05-Sample-Files/Sample%20Files%20-%20Bad/)) and ask the *same* question; show how the answer degrades.
3. Draw the lesson explicitly: *the agent is only as good as the knowledge and instructions you give it.* This is the single most important takeaway of the day.

Watch for:
- Vague answers → usually a document-quality or prompt-instruction issue; use it as a teaching moment.
- A team answering unsupported questions → tighten the instructions and re-test the "should not" examples.
- Teams falling behind → keep them on the guided agent; it's fine to skip optional refinements.

Tangent to allow: "how would I make it say X instead?" is a great prompt-and-grounding discussion. Follow it briefly, then return.

Move on when: every team has built, tested, deployed the guided agent, and has seen the good-vs-bad data demo.

---

## Step 5 · Lunch / Working Break

Use this as a buffer. Technical and escalation facilitators stay available to unblock any team that's behind so everyone starts the afternoon on even footing.

---

## Step 6 · Create the 2nd Agent (Their Own)

**Goal:** Each company applies what they learned to their own use case, with one-on-one coaching. This is where the value becomes real for them.

Do this:
1. Point teams back to their [Business Readiness Worksheet](../02-Participant-Materials/Business%20Readiness%20Worksheet.md) — problem, outcome, example questions, documents.
2. Have them upload **their own** files.
3. Have them write **their own** prompt. Encourage reusing the structure of the guided prompt as a starting point.
4. Have them **test** deliberately:
   - Which questions **should** work?
   - Which questions **should not** work?
5. Have them iterate — adjust documents or instructions based on what the tests reveal.
6. Have them **deploy** (or prepare to deploy) their agent.

Facilitators: coach one-on-one. Circulate constantly. Reinforce the good-vs-bad-data lesson when you see it play out in their own results.

Watch for:
- Poor or missing data → suggest a narrower scenario or a smaller, cleaner document set so they still get a win.
- Scope too broad → help them focus on one clear support/knowledge question they can nail.
- A team stuck on setup → escalate so their build time isn't lost.

Move on when: each team has a working agent of their own (even a modest one) and has identified at least one thing they'd improve.

---

## Step 7 · Demos

**Goal:** Teams share what they built and learn from each other. Demos are optional but strongly encouraged.

Do this:
1. Invite companies to give a short demo, each covering:
   - **Problem** — what they set out to solve
   - **Solution** — what they built
   - **Lessons** — what they learned
2. Keep them short so several teams can share.
3. Call out patterns across demos — especially where better documents or clearer instructions produced better results.

Move on when: a good cross-section of teams has shared and the room has heard varied approaches.

---

## Step 8 · Prep for Day 2 & Wrap-Up

**Goal:** Everyone is set up and motivated for Day 2, where they'll build a small app around their agent using GitHub Copilot.

Do this:
1. **Preview Day 2.** Show briefly what's possible with code — connecting the agent into a simple application using GitHub Copilot and VS Code.
2. **Confirm Day 2 setup.** Remind participants to have **VS Code** and **GitHub Copilot** installed and working, and to have the **template app** downloaded ([titletowntech/wi_ailab_prototype_template](https://github.com/titletowntech/wi_ailab_prototype_template)).
3. Flag any setup gaps now so they can be resolved before Day 2 — hand these to the escalation facilitator.
4. **Recap the day** and take questions.
5. Close with the through-line below.

---

## Blocker Model (Green / Yellow / Red)

Use this all day to keep the room moving:

- **Green** — Team is progressing normally.
- **Yellow** — Minor issue, but they can continue. A technical facilitator helps in the flow.
- **Red** — Team is blocked and cannot progress. Escalation facilitator takes it aside; capture it in the tracker; rejoin the team to the main flow when ready.

Rules: don't stop the whole room for one red blocker; keep every blocker visible with an owner; follow up on anything unresolved before Day 2.

Common issues and responses:

| Issue | Response |
|---|---|
| Can't access Azure | Escalation support; validate account / tenant / subscription |
| Can't open Foundry | Validate access, browser, account, tenant, permissions |
| Can't upload files | Check file type, location, browser permissions |
| Agent answers vaguely | Review document quality and prompt instructions |
| Agent answers unsupported questions | Tighten instructions and re-test the "should not" examples |
| Team has weak data | Suggest sample files or a narrower scenario |
| Team is behind | Keep them on the guided agent; skip optional refinements |

---

## End-of-Day Facilitator Checklist

Before closing, confirm:

- [ ] Every team built, tested, and deployed the **guided** agent.
- [ ] Every team saw the **good data vs. bad data** demo.
- [ ] Every team started or completed **their own** agent.
- [ ] Every team tested questions that **should** and **should not** work.
- [ ] Every team identified at least one improvement area.
- [ ] Teams shared or prepared a short demo.
- [ ] Day 2 setup requirements were reviewed (VS Code, GitHub Copilot, template app).
- [ ] Open blockers are captured with an owner for follow-up before Day 2.

---

## Closing Through-Line

Use or adapt this to close the day:

> Today we built the foundation: a knowledge-driven agent that helps people find answers from trusted information. A good agent isn't just about the model — it depends on a clear use case, good source material, thoughtful instructions, and honest testing of what should and should not work. Tomorrow we build on this: we'll use GitHub Copilot and VS Code to wrap your agent in a simple app. That's where building with AI assistance becomes concrete — using AI to help you build software around the intelligence you created today.
