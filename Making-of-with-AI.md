# Making This Guide with AI — A Beginner's Playbook

This is the behind-the-scenes story of how the entire **Build with us** event guide was created: starting from an **empty folder** in VS Code and building every document by *chatting* with an AI assistant (GitHub Copilot). No document was written from a blank page by hand — each one grew out of a conversation.

This playbook explains, in plain language, how that worked and how **you** can do the same for your own guide, handbook, playbook, or knowledge base. You don't need to be a developer. If you can describe what you want in a sentence, you can do this.

---

## What You're Really Doing

Think of the AI as a **fast, tireless writing partner**. You bring the ideas, the judgment, and the "that's not quite right." The AI brings the drafting, the structure, and the willingness to redo things instantly.

The whole method comes down to a simple loop:

1. **Describe** what you want.
2. **Read** what the AI drafts.
3. **React** — keep it, fix it, or redirect it.
4. **Repeat** for the next piece.

You are the editor and director. The AI is the writer. The magic isn't one perfect prompt — it's the back-and-forth.

---

## What You Need

- **VS Code** — a free editor from Microsoft.
- **GitHub Copilot** — the AI assistant that chats with you inside VS Code.
- **An empty folder** — your project's home.
- **An idea** — even a rough one. You'll refine it by talking it through.

Everything you create will be a **Markdown file** (a `.md` file) — plain text with light formatting. More on why that matters below.

---

## Start From Empty

Open your empty folder in VS Code, open the chat, and just say what you're trying to make. You don't need the perfect words.

Example opening prompts:

```text
I want to plan a two-day hands-on event. Help me create a README that
summarizes the whole program so people can get started.
```

```text
This folder will hold everything for a customer onboarding handbook.
Let's start by outlining what documents we'll need.
```

The AI will draft a first file. It won't be perfect — that's the point. You now have something to react to, which is far easier than facing a blank page.

---

## Build One Piece at a Time

The biggest lesson: **don't ask for everything at once.** Build the guide the way you'd build with blocks — one document, one section at a time. Each request is small enough to review well.

That's how this project came together, in order, over many small conversations:

- A program summary (the README)
- A high-level timeline
- Day-by-day agendas
- Homework and pre-skilling packages
- Fill-in worksheets
- Facilitator guides
- A community setup guide
- A planning worksheet

Each one started with a single, plain request like:

```text
Create a Day 1 agenda for the event. It's a hands-on lab from 9 to 3,
focused on building a support agent.
```

Then it was refined through follow-ups. You're never "done" in one shot — you shape it.

---

## Steer With Plain Feedback

You don't need technical language to correct the AI. Talk to it like a colleague. Real examples from building this guide:

**Redirecting when it misunderstood:**

```text
I meant the Day 2 template app, not Day 1.
```

**Correcting a wrong assumption:**

```text
There is no Day 1 template app. But we do need a facilitator guide.
```

**Changing your mind about naming:**

```text
This isn't the "AI as a Teammate" event. Let's rename it to
"Support and Knowledge Base for Beginners."
```

**Removing something you no longer want:**

```text
Remove all references to a lab assistant agent. We don't want that at
this time.
```

Notice these are just normal sentences. The AI adjusts every affected file, not just the one in front of you. Short, honest feedback is the most powerful tool you have.

---

## Let the AI Do the Heavy Lifting

Once you have one good document, use it as a springboard. The AI can build new material *from* what already exists, keeping everything consistent.

**Generate one document from another:**

```text
Create a detailed facilitator guide based on the Day 1 agenda, so a
facilitator can move step by step through the day.
```

**Work backward from a goal:**

```text
We don't have an event date yet. Build a worksheet that plans all the
dates leading up to the event, working backward from the event date.
```

**Ground the content in your real material:**

```text
Use the files in this folder as the examples. Base the questions on
what's actually in those documents.
```

**Ask it to make big, sweeping changes:**

```text
Rename the event everywhere to "Build with us: Support and Knowledge
Base for Beginners."
```

This is where working with AI shines: changes that would take an hour of find-and-replace happen in seconds, across every file at once.

---

## Keep It Organized as It Grows

Small projects become big ones. When you have a pile of files, ask the AI to help you tidy up.

```text
Group these files into folders by purpose, and update the README so
everything still links correctly.
```

```text
I still see two copies of the checklist. Remove the duplicate.
```

A good habit: keep **one "front door" file** (a README) that summarizes the project and links to everything else. Ask the AI to update it whenever you add something new, so the map never goes stale.

```text
Add the new planning worksheet to the README so people can find it.
```

---

## Ask the AI to Think With You

The AI isn't only a writer — it's a second set of eyes. Invite it to spot problems and suggest ideas.

```text
Look over all the files and tell me if anything is inconsistent or
missing.
```

```text
Think of some interesting ways we could make this event a
world-class experience.
```

And let it **ask you** questions when your request is fuzzy. A great prompt to keep handy:

```text
Before you start, ask me anything you need to get this right.
```

Answering a few short questions up front usually beats redoing a whole document later.

---

## When It Gets Something Wrong

It will, sometimes. That's normal and easy to handle:

- **It guessed wrong?** Tell it plainly what you actually meant. It'll redo it.
- **Content drifted apart across files?** Ask it to reconcile them: *"Make sure these two documents agree."*
- **It went too far?** Ask it to undo or scale back: *"Keep the wording but remove the last section."*
- **You're not sure it's right?** Ask it to explain its choices before you accept them.

You never have to accept a draft you don't like. "Try again, but…" is always available.

---

## Why Markdown

Every file in this project is Markdown — plain text with a few simple symbols for headings, **bold**, and lists. Why it's the perfect format for this:

- **Anyone can read it**, even with no special software.
- **It travels anywhere** — paste it into a doc, a website, an email, or another tool.
- **AI works beautifully with it**, because it's clean and structured.
- **It's future-proof** — plain text never goes out of date.

You focus on the words and ideas; the formatting stays simple and tidy.

---

## Try It Yourself

Here's a starter sequence to build your own guide from an empty folder:

1. **Open an empty folder in VS Code** and start a chat.
2. **Describe your project** and ask for a README to anchor it:
   ```text
   I'm creating a [handbook / playbook / guide] about [topic] for
   [audience]. Create a README that gives an overview and outlines the
   documents we'll build.
   ```
3. **Build the first real document:**
   ```text
   Now create the [first document]. Keep it plain-language for
   beginners.
   ```
4. **Refine it** with plain feedback until it's right.
5. **Repeat** for each new document, and ask the AI to keep the README updated.
6. **Tidy up** into folders as it grows, and ask the AI to check for gaps.

That's it. Start small, react honestly, and let the conversation build your guide one piece at a time.

---

## The Takeaways

- **You direct; the AI drafts.** Your judgment is the most important ingredient.
- **Work in small steps.** One document, one change at a time.
- **Talk plainly.** Normal sentences and honest feedback steer it best.
- **Reuse what you have.** Generate new material from existing files to stay consistent.
- **Keep a map.** A README as the front door keeps everything findable.
- **Let it help you think.** Ask for gaps, ideas, and clarifying questions.

Starting from an empty folder, a handful of conversations turned into a complete, organized event guide. The same simple loop can turn your idea into your own.
