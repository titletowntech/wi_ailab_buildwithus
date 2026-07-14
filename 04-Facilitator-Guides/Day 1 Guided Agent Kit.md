# Build with us: Support and Knowledge Base for Beginners — Day 1 Guided Agent Kit

Everything the facilitator needs to run the **guided agent** in Step 4 of the [Day 1 Facilitator Guide](Day%201%20Facilitator%20Guide.md): the agent prompt, the test questions (should-work and should-not-work), and the good-vs-bad-data demo.

The guided agent is an **Adventure Works** bicycle technical-support assistant, grounded in the troubleshooting articles in [Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/) (documents TS-001 through TS-020).

> Facilitator note: paste the prompt below into the agent's **instructions**, upload the **[Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/)** set as the agent's knowledge/files, then work through the questions with the room.

---

## 1. Guided Agent Prompt

Copy everything in the fenced block into the agent's instructions field.

```text
You are the Adventure Works Technical Support Assistant. You help riders and shop
staff troubleshoot and repair Adventure Works bicycles — including the Trailblazer MTB,
Summit Trail, City Cruiser, Velocity Road, PowerRide e-Bike, and City Cruiser-E.

YOUR KNOWLEDGE
- Answer only from the Adventure Works technical support documents provided to you
  (the TS-001 through TS-020 troubleshooting guides).
- These documents cover symptoms, likely causes, step-by-step customer fixes,
  technician references, and torque specifications for common bicycle issues.
- If the answer is not in the provided documents, say so plainly. Do not guess,
  invent steps, or use general knowledge to fill gaps.

HOW TO ANSWER
- Start with the most likely cause, then give clear, numbered steps a home mechanic
  can follow. Use plain, friendly language and avoid unnecessary jargon.
- When a document lists a specific value (torque spec, tire pressure, clearance,
  pad thickness), quote it exactly. Do not round or estimate.
- Reference the source document number when helpful (for example, "see TS-001").
- If a question could relate to several issues, ask a short clarifying question
  before giving a long answer.

SAFETY
- Brakes, e-bike batteries, and chargers are safety-critical. Always include the
  relevant safety warnings from the documents.
- Never advise mixing brake fluids, using a non-manufacturer charger, or riding a
  bike with unreliable brakes.
- When the documents say to visit a service center, tell the rider to do so and
  explain why.

STAYING IN SCOPE
- You only help with Adventure Works bicycle troubleshooting and repair.
- If asked about pricing, warranty, purchasing, store hours, appointments, order
  status, non-Adventure Works products, other vehicles, or anything unrelated,
  politely explain that you can only help with Adventure Works bicycle
  troubleshooting from the support guides, and suggest they contact the shop for
  those questions.
- You cannot take actions such as booking service, placing orders, or looking up
  accounts. You provide troubleshooting guidance only.
```

---

## 2. Test Questions — Should Work

These are all answerable from [Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/). Use them to show the agent giving accurate, grounded answers. The document each draws from is noted for the facilitator.

1. My brake lever pulls almost to the handlebar before the bike slows down. What should I check first? *(TS-001)*
2. What's the correct torque for the disc brake caliper mount bolts? *(TS-001 — 6–8 N·m)*
3. Which Adventure Works models does the spongy-brakes guide apply to? *(TS-001)*
4. My disc brakes squeal and rub. How do I fix it? *(TS-002)*
5. My gears won't shift onto the largest cog. What's likely wrong? *(TS-004 — limit screws)*
6. How much should I turn the barrel adjuster when indexing gears? *(TS-004 — a quarter turn at a time)*
7. How do I fix a flat tire and replace the tube? *(TS-005)*
8. What tire pressure should I run for a 2.3-inch mountain bike tire? *(TS-005 — 22–30 psi)*
9. My chain keeps dropping off the chainring. How do I stop that? *(TS-008)*
10. My e-bike won't power on. What are the first steps? *(TS-019)*
11. How should I store my e-bike battery for the winter? *(TS-019 — ~40–60% charge, cool and dry)*
12. Why does my e-bike lose range in cold weather? *(TS-019)*

---

## 3. Test Questions — Should NOT Work

These are outside the knowledge base. Use them to show the agent correctly declining and staying in scope — this is the *right* behavior, not a failure.

1. How much does a new brake caliper cost? *(pricing — not in the documents)*
2. What's the warranty on my Trailblazer MTB? *(warranty — not in the documents)*
3. Can you book a service appointment for me next Tuesday? *(action the agent can't take)*
4. Which bike should I buy for commuting to work? *(sales recommendation, not troubleshooting)*
5. What are your store hours and location? *(not in the knowledge base)*
6. How do I change the brake pads on my motorcycle? *(different vehicle)*
7. How do I fix the brakes on my car? *(different vehicle)*
8. What's the weather like for a ride today? *(unrelated)*
9. Write me a short poem about mountain biking. *(off-task)*
10. What's the status of my online order? *(account/order lookup, not supported)*

---

## 4. Good Data vs. Bad Data Demo

Show the same question against two knowledge sets to prove the point: **the agent is only as good as the documents behind it.**

**Setup:** Keep the prompt the same. First run the agent with [Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/), then swap in [Sample Files - Bad](../05-Sample-Files/Sample%20Files%20-%20Bad/) and ask the identical question.

**Recommended demo question:**

> "My brakes feel soft and the lever pulls to the bar. What should I do, and what torque should I use on the caliper bolts?"

**With the good data ([Sample Files - Good](../05-Sample-Files/Sample%20Files%20-%20Good/)):** the agent gives clear, ordered steps (inspect pads, check pad-to-rim gap, clean the rotor, take up cable slack, re-test at walking pace), the exact spec (**disc caliper mount bolts 6–8 N·m**), and the correct safety warnings — because [TS-001](../05-Sample-Files/Sample%20Files%20-%20Good/) is complete, structured, and specific.

**With the bad data ([Sample Files - Bad](../05-Sample-Files/Sample%20Files%20-%20Bad/)):** the answer falls apart. The matching source files are unusable —
- `BAD-001` is vague, uncertain notes ("bleed it or dont… idk it depends"),
- `BAD-002` is an old forum thread with **no accepted answer**,
- `BAD-005` is a **DRAFT with "TODO" placeholders** and no steps.

The agent can't provide torque specs or reliable steps, hedges, or has to say it doesn't know.

**The takeaway to land with the room:**

> Same model, same prompt — only the knowledge changed. Clean, complete, well-structured documents produce a trustworthy agent. Vague notes, forum threads, and unfinished drafts produce an untrustworthy one. This is why your Day 2 (and real-world) success starts with good source material.
