# Build with us: Support and Knowledge Base for Beginners — Teams Community Setup Guide

A step-by-step guide for the **event organizer** to stand up and configure the Microsoft Teams community that runs the program — plus ideas for weaving in AI so the community runs smoothly.

> **The big idea:** Make the community the calmest part of the program — one predictable place where every question gets answered and every blocker is tracked, so teams arrive on event day ready to build.

Related: this supports the **Registration** and **Event Operations** items in the [Preparation Checklist](Preparation%20Checklist.md).

---

## 1. What This Community Is For

One place where participating organizations (who come from **different companies**) can:

- Get announcements and program updates
- Ask readiness questions and get help clearing blockers
- Share files, discoveries, and lessons learned
- Collaborate as a community — not as isolated teams
- Reach the facilitators between sessions

---

## 2. Assumptions & Prerequisites

This guide assumes:

- You have a **Microsoft 365 tenant** with Microsoft Teams.
- You (or a partner admin) have **Teams admin** rights to enable guest access.
- Participants are **external** to your organization (different companies) and will join as **guests**.
- *Optional, for the AI layer:* **Microsoft 365 Copilot** licenses for the organizers who run meetings (for meeting recaps and channel summaries).

> **What would change the approach below:** If participants turn out to be *inside your tenant*, skip guest access entirely. If your security policy **forbids adding guests**, use **shared channels** instead (see the decision in Section 3) and drop the Planner/moderation features. If Copilot isn't available, the community still works fully — the AI layer in Section 9 is additive, not required.

---

## 3. Key Design Decision — How External People Join

Because participants come from other companies, you must choose how they collaborate. The choice affects which features you get.

| Approach | External people join as… | Apps & flows in channel | Planner (Tasks) | Channel moderation | Best when |
|---|---|---|---|---|---|
| **One team + guest access** *(recommended)* | Guests (a B2B account in your directory) | ✅ Yes | ✅ Yes | ✅ Yes | You want a full community with a blocker board, in-channel forms/automations, and moderated announcements |
| **Shared channels (Teams Connect)** | External participants (no guest account needed) | ❌ No | ❌ No | ❌ No | Guests aren't allowed, or people must stay in their own Teams without switching profiles |
| **Multiple teams (one per cohort/company)** | Guests | ✅ | ✅ | ✅ | Very large cohorts needing isolation — more overhead to manage |

**Recommendation: one team with guest access and standard channels.** It's the only option that supports all three community features we want — the **shared blocker board (Planner)**, **in-channel forms and automations**, and **moderated announcements** — in one place.

> **What would change this recommendation:** If your org can't or won't add guests, switch to **shared channels** (you'll lose Planner, moderation, and some app support). If cohorts are large and need strict separation, split into multiple teams and replicate the channel structure below in each.

---

## 4. Step 1 — Enable Guest Access (Teams Admin)

Guest access is what lets people from other companies into your team. It's controlled at the tenant level and may take a short time to take effect.

1. In the **Teams admin center**, turn on **guest access**. See [Turn on or turn off guest access](https://learn.microsoft.com/microsoftteams/set-up-guests).
2. Walk the dependent settings (Microsoft Entra B2B, Microsoft 365 Groups, SharePoint/OneDrive) using the [Guest access checklist](https://learn.microsoft.com/microsoftteams/guest-access-checklist).
3. Review what guests can and can't do: [Guest access in Microsoft Teams](https://learn.microsoft.com/microsoftteams/guest-access).

> Guests sign in with their existing work or personal email; those without a Microsoft account use a one-time passcode. A guest must be **added to the team** before guest features light up.

---

## 5. Step 2 — Create the Team

1. In Teams, choose **+ Join or create a team → Create team → From scratch**.
2. Set privacy to **Private** (people join by invitation/approval).
3. Name it clearly, e.g. **Build with us: Support & Knowledge Base for Beginners**.
4. Add a short description and a recognizable team picture/logo.
5. Add **at least two owners** (you plus a co-organizer) so ownership is never single-threaded.

References: [Create and manage teams and channels](https://learn.microsoft.com/training/modules/create-manage-teams-channels-microsoft-teams/) · [Teams and channels overview](https://learn.microsoft.com/microsoftteams/teams-channels-overview) · [Manage teams in the admin center](https://learn.microsoft.com/microsoftteams/manage-teams-in-modern-portal).

---

## 6. Step 3 — Channel Architecture

Keep it simple and predictable. Use **standard** channels (visible to all members) unless noted. Recommended set:

| Channel | Purpose | Notes |
|---|---|---|
| **📣 Announcements** | Program updates, dates, reminders | Turn on **moderation** so only owners post (see Step 4) |
| **👋 Start Here** | Onboarding, introductions, how the community works | Pin the welcome post and key links |
| **✅ Readiness Help** | Business + technical readiness questions and blockers | The busiest channel; questions and blockers land here |
| **🧠 Pre-Skilling & Resources** | Curriculum links, worksheets, readiness pages, recordings | Pin docs as tabs (Step 5) |
| **🛠️ Tech Support & Blockers** | Environment/setup issues (Azure, VS Code, Python, Copilot) | Feeds the blocker board |
| **💡 Show & Tell** | Discoveries, tips, "prompt of the day," demos | Celebrate wins; encourage peer learning |
| **🎉 Event Days** | Live Day 1 / Day 2 coordination and Q&A | Active only during the event |
| **☕ Community / Social** | Introductions and informal chat | Keeps the community human |

> Prefer **fewer, well-named channels**. You can always add more; too many splinters the conversation. Reserve **private channels** for the facilitator team's internal coordination (only team members can be added; up to 30 per team).

---

## 7. Step 4 — Configure Channels

- **Lock down Announcements:** turn on **channel moderation** so only owners/moderators start posts and (optionally) control replies. See [Set up and manage channel moderation](https://learn.microsoft.com/microsoftteams/manage-channel-moderation-in-teams).
- **Post announcements as Announcements** (the formatted headline style) for scannability.
- **Pin a welcome post** in *Start Here* summarizing the channels and how to get help.
- **Name consistently** and add a one-line description to each channel so newcomers self-orient.

---

## 8. Step 5 — Add Apps, Tabs & Shared Tools

Turn each channel into a workspace by pinning the right tabs:

- **Files / worksheets** — Upload the [Homework Package](../02-Participant-Materials/Homework%20Package.md), [Pre-Skilling Package](../02-Participant-Materials/Pre-Skilling%20Package.md), and the [Business](../02-Participant-Materials/Business%20Readiness%20Worksheet.md) and [Technical](../02-Participant-Materials/Technical%20Readiness%20Worksheet.md) worksheets, and pin them as tabs in *Pre-Skilling & Resources*.
- **Blocker board (Planner / Tasks in Teams)** — Add a **Tasks by Planner** tab in *Tech Support & Blockers* with buckets **New → In Progress → Resolved**, assign an owner and due date to each blocker, and label by area (Azure, VS Code, Python, Copilot). See [Use the Tasks app in Teams](https://learn.microsoft.com/training/modules/create-manage-teams-channels-microsoft-teams/6-use-tasks-app-teams).
- **Shared knowledge base (OneNote or a Wiki-style page)** — Capture recurring answers and fixes so the same question is answered once.
- **Website tabs** — Pin the [pre-skilling site](https://titletowntech.github.io/wi_ailab_labwebsite/index.html) and its readiness pages directly in *Pre-Skilling & Resources*.
- **Forms** — A short weekly **readiness pulse** and a **post-event feedback** form (see Section 9 for AI summarization).

---

## 9. The AI Layer — Make It World-Class

This is where the community becomes a showcase. Add these on top of the basics above.

### 9a. Intelligent meeting recaps (weekly readiness meetings)
With **Microsoft 365 Copilot**, record/transcribe the weekly readiness meetings to get an **automatic recap, notes, and action items** — then paste the actions into the blocker board. Saves the facilitator from manual note-taking and keeps absent teams in the loop. *(Requires Microsoft 365 Copilot licensing for the meeting organizer.)*

### 9b. "Catch me up" and drafting with Copilot in Teams
Encourage facilitators to use Copilot in Teams to **summarize a busy channel**, **catch up** after time away, and **draft announcements** in a consistent, friendly tone. *(Requires Microsoft 365 Copilot.)*

### 9c. Pulse + feedback, summarized by AI
Collect a weekly **Forms** readiness pulse ("green/yellow/red, and your biggest blocker") and use Copilot to **summarize themes** for the facilitator team, so the next meeting targets the real blockers. Reuse the same pattern for **post-event feedback**.

### 9d. "Prompt of the day"
In *Show & Tell*, post a daily Copilot prompt participants can try (great warm-up for Day 2). Builds prompt fluency before the build day.

---

## 10. Step 6 — Automations (Power Automate)

Light automation keeps the community responsive without manual effort:

- **Welcome flow** — when a new member joins, auto-post a friendly welcome in *Start Here* with the key links.
- **Blocker intake** — when someone posts in *Tech Support & Blockers* with a keyword/tag, **create a Planner task** and **notify the escalation facilitator**.
- **Weekly reminders** — auto-post the readiness-meeting reminder and agenda each week.
- **Digest** — a weekly summary of open blockers and their owners.

---

## 11. Step 7 — Invite Participants

1. Add each participant as a **guest** by email (People picker → type their email → **Add**). They must be added to the team before guest features work.
2. Send a short welcome note explaining how to accept the invite and switch to the **guest profile** in Teams.
3. Point them to **Start Here** first.

Reference: [Collaborate with guests in a team](https://learn.microsoft.com/microsoft-365/solutions/collaborate-as-team).

---

## 12. Governance & Care

- **Two+ owners** at all times; document who owns what.
- **Code of conduct** pinned in *Start Here* (be kind, share openly, no confidential company data).
- **No secrets or private data** — remind participants not to paste credentials, keys, or sensitive documents into chat.
- **Moderation** on Announcements; keep other channels open for conversation.
- **Accessibility** — use the Announcement style, descriptive link text, and alt text on images.
- **Lifecycle** — decide what happens to the team after the event (archive vs. keep as an alumni community).

---

## 13. Cadence — How the Community Is Used

- **Pre-event (Weeks 1–4):** readiness Q&A, weekly pulse, blocker board, meeting recaps.
- **During the event (Day 1 & 2):** the *Event Days* channel for live coordination, file sharing, and quick help.
- **Post-event:** share recordings and resources, capture feedback, and decide whether to keep the community running for alumni.

---

## 14. Organizer Setup Checklist

- [ ] Guest access enabled in the Teams admin center
- [ ] Team created (Private), described, with a logo and **2+ owners**
- [ ] Channels created and named per Section 6
- [ ] Announcements channel moderated
- [ ] Worksheets, packages, and readiness links pinned as tabs
- [ ] Planner blocker board set up (New / In Progress / Resolved)
- [ ] Shared knowledge base (OneNote) started
- [ ] Weekly pulse and post-event feedback Forms created
- [ ] Power Automate welcome + blocker-intake flows configured *(automation)*
- [ ] Code of conduct and "no secrets" reminder pinned in Start Here
- [ ] Participants invited as guests and welcomed

---

## 15. References (Microsoft Learn)

- Guest access: [overview](https://learn.microsoft.com/microsoftteams/guest-access) · [turn on/off](https://learn.microsoft.com/microsoftteams/set-up-guests) · [checklist](https://learn.microsoft.com/microsoftteams/guest-access-checklist) · [collaborate with guests in a team](https://learn.microsoft.com/microsoft-365/solutions/collaborate-as-team)
- Teams & channels: [overview](https://learn.microsoft.com/microsoftteams/teams-channels-overview) · [create & manage (training)](https://learn.microsoft.com/training/modules/create-manage-teams-channels-microsoft-teams/) · [shared channels](https://learn.microsoft.com/microsoftteams/shared-channels) · [private channels](https://learn.microsoft.com/microsoftteams/private-channels)
- Operations: [channel moderation](https://learn.microsoft.com/microsoftteams/manage-channel-moderation-in-teams) · [Tasks app in Teams](https://learn.microsoft.com/training/modules/create-manage-teams-channels-microsoft-teams/6-use-tasks-app-teams) · [manage teams in admin center](https://learn.microsoft.com/microsoftteams/manage-teams-in-modern-portal)
