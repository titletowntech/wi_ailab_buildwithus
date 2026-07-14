# Prompt: Add an "Azure AI Foundry Readiness" Page to the Pre-Skilling Site

Copy everything in the fenced block below and send it to the pre-skilling website project. It only specifies **content** — the other project already has the style, layout, and navigation conventions to apply.

```text
Add a new technical readiness page to the Microsoft AI Co-Innovation Lab pre-skilling website for the Build with us: Support and Knowledge Base for Beginners event: "Azure AI Foundry Readiness."

Context:
Build with us: Support and Knowledge Base for Beginners is a hands-on event where companies build Technical Support and Knowledge Base agents in Azure AI Foundry on Day 1, then use GitHub Copilot and VS Code on Day 2 to build a small app that uses the agent. Attendees are not all senior developers — many are business/technical users, citizen builders, junior developers, or IT admins who may be new to Azure.

Why this page is needed:
The site already has an Azure Subscription readiness page, but nothing that confirms a participant can actually get into Azure AI Foundry and open a project. Having an Azure subscription is not the same as having Foundry access. This page closes that gap. Assume that if a participant can open a Foundry project, they have access to at least a minimal model — so this page does NOT need to cover model deployment permissions.

Follow the existing site conventions:
- Match the style, layout, naming, navigation pattern, and CSS of the existing readiness pages (Azure, VS Code, Python, GitHub Copilot).
- Write for non-experts in plain English. Avoid jargon unless explained simply.
- Keep the tone professional, encouraging, and clear. This is pre-event readiness, not deep technical training.
- Mirror the structure of the other readiness pages: a plain-language intro, a "what it is" section, a "why you need it" section, step-by-step checks, a "what good looks like" callout, a common issues section, a helpful links section, and a final checkbox list.

Page content to create — "Azure AI Foundry Readiness":

1. What Azure AI Foundry is, in simple terms
   - It's Microsoft's online workspace for building and testing AI agents and models.
   - You work inside "projects," which keep your agent work organized.
   - You don't need to understand how it works underneath — you just need to be able to sign in and open (or create) a project.

2. Why you need it for Build with us: Support and Knowledge Base for Beginners
   - On Day 1, the agent your team builds lives in an Azure AI Foundry project.
   - Confirming access before the event means you can start building right away instead of troubleshooting sign-in.

3. Step 1: Check if you can access Foundry
   - Go to the Foundry portal at https://ai.azure.com/ and sign in with the account you plan to use for the event (usually your work account — the same one used for your Azure subscription).
   - Confirm the portal loads without an access or permission error.
   - If the "New Foundry" toggle is shown, make sure it is on.

4. Step 2: Open or create a project
   - If you already have a project, select its name in the upper-left corner to open it.
   - If you don't have one, choose "Create new project," give it a simple name (for example, my-foundry-project), and select Create.
   - Wait for the project overview page to appear — that confirms your project is ready.

5. Important note for company laptops / accounts
   - At many companies, an administrator controls who can access Azure AI Foundry or create resources. If you hit a permission wall, contact your IT team now — not on event day — and raise it in your weekly readiness meeting so we can help you plan around the timing.

6. What good looks like (callout)
   - "I can sign in to Azure AI Foundry and open or create a project without errors."

7. Common issues
   - "I can sign into Azure but Foundry shows a permission error" — your account may not have access to Foundry yet; ask your IT/admin to grant it, or try the personal account you used for your Azure subscription.
   - "I'm not sure which account to use" — use the same account that has your Azure subscription; bring the question to your readiness meeting if unsure.
   - "I can't create a project" — you may lack permission in that subscription; contact your admin or use a subscription where you can create resources.
   - "The portal looks different from the screenshots" — make sure the New Foundry toggle is on.

8. Final checklist (checkboxes participants can use before the readiness meeting)
   - [ ] I can sign in to the Foundry portal at https://ai.azure.com/
   - [ ] I can open or create a project without errors
   - [ ] I know which account and subscription I'll use for the lab
   - [ ] I know who to contact internally if I don't have access

Official reference links to include:
- Azure AI Foundry portal: https://ai.azure.com/
- What is Microsoft Foundry: https://learn.microsoft.com/azure/foundry/what-is-foundry
- Create a project: https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects
- Quickstart — set up Foundry resources: https://learn.microsoft.com/azure/foundry/tutorials/quickstart-create-foundry-resources

Navigation and integration:
- Place this page in the readiness sequence immediately after the Azure Subscription page and before the Visual Studio Code page.
- Update the readiness overview page and any "four things to get ready" wording to account for this addition (either present it as a fifth readiness area, or nest it under the Azure area — whichever fits the existing layout best).
- Add previous/next links consistent with the other readiness pages (Previous: Azure Subscription, Next: Visual Studio Code).
```
