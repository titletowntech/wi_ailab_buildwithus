# Technical Readiness Worksheet

**Build with us: Support and Knowledge Base for Beginners**

Use this worksheet to confirm your environment is ready before the event.

---

## Day 1 Requirements: Azure AI Foundry

### Azure Subscription

- [ ] Azure subscription available
- [ ] Subscription owner identified
- [ ] Participants can successfully access Azure Portal
- [ ] No corporate restrictions preventing Azure usage
- [ ] `Microsoft.BotService` resource provider registered on the subscription (required to publish an agent to Teams / Microsoft 365)

**Subscription ID (required):**


### Azure AI Foundry Access

- [ ] Azure AI Foundry access verified
- [ ] Participants have the **Azure AI User** (Foundry User) role on the Foundry project
- [ ] Can successfully create or open a project
- [ ] Participants can access Azure AI Foundry without errors

## Knowledge Base Documents

### Documents Ready

- [ ] Technical manuals
- [ ] Troubleshooting guides
- [ ] Standard operating procedures
- [ ] Knowledge base articles
- [ ] Other supporting documentation

### Document Quality Check

- [ ] Documents are current
- [ ] Documents are accurate
- [ ] Documents can be shared during event
- [ ] Documents contain information required to answer user questions

**Approximate number of documents:**

## Day 2 Requirements: GitHub Copilot Development

### Visual Studio Code

- [ ] VS Code installed
- [ ] VS Code launches successfully

### Python

- [ ] Python installed

### Git

- [ ] Git installed
- [ ] `git --version` runs successfully in a terminal

### GitHub

- [ ] GitHub account available
- [ ] GitHub Copilot subscription active
- [ ] Copilot enabled in VS Code
- [ ] Test prompt successfully generates code

### Template App and Authentication

- [ ] Can download or clone the [Day 2 template app](https://github.com/titletowntech/wi_ailab_prototype_foundrytemplate)
- [ ] Can create a Microsoft Entra app registration, or an administrator is identified who can create it
- [ ] Can create a client secret for the app registration and store it securely
- [ ] Can assign the app registration the **Azure AI Developer** role on the Foundry project, or an Azure administrator is identified who can make the assignment
- [ ] Understand that the client secret belongs only in the local `.env` file and must not be shared or committed to source control

## Readiness Self-Assessment

Mark each area as Red, Yellow, or Green.

| Area | Status (Red / Yellow / Green) |
| --- | --- |
| Azure Access | |
| Document Readiness | |
| VS Code Setup | |
| Python Setup | |
| Git Setup | |
| GitHub Copilot | |
| Template App Access | |
| Entra App Registration / Foundry RBAC | |

---

## Technical Blockers

List any issues preventing successful participation.

| Issue | Owner | Status |
| --- | --- | --- |
| | | |
| | | |
| | | |

---

## Definition of Ready

Your organization is **Technically Ready** when:

- [ ] Azure subscription access is verified
- [ ] Knowledge base documents are prepared
- [ ] VS Code is installed and functioning
- [ ] Python is installed and functioning
- [ ] Git is installed and `git --version` runs successfully
- [ ] GitHub Copilot is active and validated
- [ ] The Day 2 template app is publicly accessible and downloads successfully
- [ ] Entra app-registration and Foundry role-assignment permissions are verified, with an administrator identified if needed
- [ ] No unresolved critical technical blockers remain
