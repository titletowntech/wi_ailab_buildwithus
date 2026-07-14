# Build with us: Support and Knowledge Base for Beginners — Day 2 Guided Agent Kit

Everything the facilitator needs to run the **guided build** in Step 4 of the [Day 2 Facilitator Guide](Day%202%20Facilitator%20Guide.md): the shared scenario, the connection recipe, an ordered build script with the exact Copilot prompts to use at each step, and test questions.

The guided build continues yesterday's story: everyone wraps the **Adventure Works** bicycle support agent from Day 1 in a simple app using the [prototype template](https://github.com/titletowntech/wi_ailab_prototype_template), with GitHub Copilot doing the typing.

Companion handout: [Copilot 101 — Sample Markdown & Prompt Examples](Copilot%20101%20-%20Sample%20Markdown%20and%20Prompts.md).

> Facilitator note: participants only ever edit a few files — `project_config.py`, `core/tools/example_tools.py`, `custom_tools.py`, and `app.py`. The `core/` and `ui/` folders are the shared framework and stay untouched.

---

## 0. Connection Recipe (facilitator provides)

Have these ready so teams don't lose time on setup or authentication:

- **Template** downloaded, VS Code open, GitHub Copilot signed in and working.
- **`.env` values** for the Foundry project:
  - `AZURE_FOUNDRY_ENDPOINT`
  - `AZURE_FOUNDRY_API_KEY`
  - `AZURE_AI_PROJECT_ENDPOINT`
- **To connect the Day 1 agent** (the Foundry agent runtime needs a real sign-in — the API key alone is **not** accepted), pre-stage a **service principal** and give teams:
  - `AZURE_TENANT_ID`
  - `AZURE_CLIENT_ID`
  - `AZURE_CLIENT_SECRET`
  - (The app registration needs the **Azure AI Developer** role on the Foundry project.)
- **The Day 1 agent name** — the Adventure Works support agent each team deployed (set on the app's Settings page).

---

## 1. Copy the Template and Run the Baseline

Get an unmodified app running on every screen first — a shared "it works" moment before any changes.

1. Copy `projects/_template` to a new folder, e.g. `projects/adventure-works`.
2. Copy `.env.example` to `.env` and fill in the values from the recipe above.
3. Activate the virtual environment, then install and run:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python app.py
   ```
4. Open `http://localhost:5000` and confirm the app loads and the chat responds.

> Checkpoint: everyone sees a running app before moving on.

---

## 2. Connect the Day 1 Agent

Route the app's chat to the team's Day 1 Adventure Works agent.

1. In the running app, open the **Settings** page.
2. Set the **Backend** to **Azure Foundry Agent**.
3. Choose the **agent by name** (the Adventure Works support agent from Day 1).
4. Ask a bike question and confirm the answer comes from the agent (grounded, specific), not a generic model.

> Under the hood this sets `agent_config.provider` to `"foundry_agent"` and uses the service-principal values in `.env`. If a team prefers, they can set those in `project_config.py` directly — but the Settings page is the easy path.

---

## 3. Customize with Copilot

Work through these in order. For each step, give participants the **prompt**, then have them **read it, run it, and test it**. Restart the app after each change.

### 3a. Brand the app
> **Copilot prompt:** "In `project_config.py`, set `name` to **Adventure Works Bike Support** and `description` to *'Helps riders troubleshoot and repair their Adventure Works bikes.'* In the `ui` section, set `title` to **Adventure Works Bike Support**, `subtitle` to *'Ask a question about your bike'*, and `theme_color` to a deep blue (#1B3A6B). Don't change anything else."

Expected result: the header, title, and color update when the app restarts.

### 3b. Set helpful sample prompts
> **Copilot prompt:** "In `project_config.py`, replace the `ui.sample_inputs` list with three realistic questions a rider would ask — one about spongy brakes, one about fixing a flat tire, and one about an e-bike that won't turn on."

Expected result: three new clickable starter buttons appear on the chat screen.

### 3c. (Optional) Update the example FAQ content
> **Copilot prompt:** "In `core/tools/example_tools.py`, replace the entries in `_FAQ_DATA` with three bike-support question-and-answer pairs: brake pad wear, correct tire pressure, and e-bike battery storage. Keep the same dictionary format."

Expected result: the built-in FAQ tool now returns bike answers.

### 3d. (Stretch) Add a simple Help page
> **Copilot prompt:** "In `app.py`, add a new route `/help` that returns a simple HTML page (as a string) titled 'How to use Adventure Works Bike Support' with a short paragraph and a bulleted list of three example questions. Keep all existing routes unchanged and don't edit anything in `ui/`."

Expected result: visiting `http://localhost:5000/help` shows the new page.

---

## 4. Test the App

Confirm the app answers through the agent. These should work (they're grounded in the Day 1 knowledge base):

1. My brake lever pulls almost to the handlebar before the bike slows. What should I check first?
2. How do I fix a flat tire and replace the tube?
3. My e-bike won't power on — what are the first steps?
4. What tire pressure should I run for a 2.3-inch mountain bike tire?

And these should be politely declined (out of scope), showing the agent stays in its lane:

1. How much does a new brake caliper cost?
2. Can you book a service appointment for me?
3. What's the weather like for a ride today?

> If answers look generic or wrong, check the Settings backend (should be **Azure Foundry Agent**) and the `.env` values before touching anything else.

---

## 5. Facilitator Notes

- Keep the whole room on the **same app** through Section 3 so no one falls behind; save personal creativity for the afternoon "Build Your Own" block.
- The biggest time-sink is **agent authentication** (Section 2). Pre-stage the service principal and hand out the values.
- When a Copilot change breaks the app, coach the **undo → clearer prompt → retry** loop rather than debugging line by line.
- More prompt patterns and weak-vs-strong examples are in the [Copilot 101 handout](Copilot%20101%20-%20Sample%20Markdown%20and%20Prompts.md).
- Full step-by-step facilitation lives in the [Day 2 Facilitator Guide](Day%202%20Facilitator%20Guide.md).
