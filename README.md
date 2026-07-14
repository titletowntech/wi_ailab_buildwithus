
# Build With Us Program Context

This file captures the working context, decisions, artifacts, and next steps for the **Build With Us: AI as a Teammate** event planning effort so a coding agent in VS Code can pick up the work without needing the prior chat history.

## 1. Program Summary

**Program name:** Build With Us: AI as a Teammate  
**Initial audience:** Developers, technical business users, citizen builders, IT admins, and company participants who may not be senior developers.  
**Format:** Hands-on lab, not a workshop or lecture.  
**Duration:** 2 days, 9:00 AM to 3:00 PM each day.  
**Primary focus for this round:** Technical Support and Knowledge Base agent use cases only.  
**Core idea:** Participants learn to build with AI as a teammate by creating a useful knowledge-based agent on Day 1, then using GitHub Copilot and VS Code on Day 2 to build or modify an application that uses the agent.

## 2. Important Scope Decisions

### In Scope

The Build With Us agent and event should focus on:

- Technical Support Agents
- Knowledge Base Agents
- Troubleshooting Agents
- Internal knowledge discovery
- Support documentation search
- Agent answers grounded in company-provided documents
- Simple application experience using the agent
- AI-assisted coding with GitHub Copilot and VS Code

### Out of Scope for This Round

Avoid expanding the event into broader AI solution categories such as:

- General AI strategy sessions
- Broad custom enterprise AI systems
- Complex production deployment architecture
- Large-scale app modernization
- Unconstrained AI brainstorming
- Non-knowledge-base use cases
- Advanced custom agent orchestration
- Full production security/compliance review

### Important simplification

Do **not** require SME names, developer names, technical lead names, or executive sponsor names in the Business Readiness Worksheet. For this event readiness model, keep the business worksheet centered on:

- Problem
- Desired outcome
- Success criteria
- Example questions
- Available documents/data

## 3. Overall Program Flow

The readiness and event flow should be:

1. Registration
2. Kickoff Meeting
   - Homework assigned
   - Pre-skilling assigned
3. Weekly readiness check-in meetings for 4 weeks
   - Check homework progress
   - Address technical readiness issues
   - Help participants complete requirements
   - Encourage collaboration among participant companies
   - Share knowledge across the community
4. Final readiness meeting
   - Go / No-Go reminder
   - Confirm readiness requirements
   - Identify unresolved blockers
5. Event
   - Day 1: Build and evaluate knowledge/technical support agent
   - Day 2: Build software with AI as a teammate using GitHub Copilot

## 4. Pre-Event Readiness Overview

### Registration

Organizations submit:

- Primary point of contact
- Use case description
- Desired business outcome
- Expected attendee list

Approved organizations:

- Are accepted into the program
- Receive onboarding communications
- Are added to the Build With Us Teams community

The Teams community should be the central location for:

- Announcements
- Readiness support
- Technical questions
- File sharing
- Peer collaboration
- Knowledge sharing
- Blocker tracking

### Kickoff Meeting, Week 1

The Kickoff Meeting is combined with the first readiness meeting.

Purpose:

- Establish expectations
- Introduce participants
- Launch readiness activities
- Explain how the program works
- Clarify what participants are expected to complete before the event

Topics include:

- Program overview
- Event agenda and milestones
- Expectations and participation requirements
- Introductions
- Community collaboration model
- Readiness process and success criteria
- Homework package
- Pre-skilling package

### Homework Assigned

Organizations begin preparing the readiness artifacts that will be reviewed during weekly meetings.

Business readiness work includes:

- One-paragraph use case statement
- Desired business outcome
- Success criteria
- Sample user questions
- Sample documents and data

Technical readiness work includes:

- Azure subscription access
- Azure AI Foundry access
- VS Code installation
- Python installation
- GitHub account readiness
- GitHub Copilot Pro or higher subscription

### Pre-Skilling Assigned

Participants complete the Microsoft AI Co-Innovation Lab Getting Started curriculum prior to the event.

Existing pre-skilling website:

- [Microsoft AI Co-Innovation Lab Getting Started](https://titletowntech.github.io/wi_ailab_labwebsite/index.html)

The website should be expanded with technical readiness pages for:

1. Azure subscription readiness
2. VS Code readiness
3. Python readiness
4. GitHub Copilot readiness
5. Final readiness checklist

### Weekly Readiness Meetings, Weeks 1 to 4

Primary objective:

> Eliminate business and technical barriers before event week.

Standard agenda:

1. Pre-skilling review
2. Technical readiness review
3. Business readiness review
4. Collective learning and knowledge sharing

Participants should share:

- Technical discoveries
- Lessons learned
- Emerging use cases
- Open questions and challenges

The objective is to create a collaborative community, not a collection of independent teams.

### Final Readiness Review, Go / No-Go

Conducted one week before the event.

Ensure these are complete:

- Pre-skilling requirements
- Business readiness requirements
- Technical readiness requirements
- Participation requirements

Participation requirements:

- Attended kickoff session
- Participated in readiness meetings
- Completed pre-skilling activities
- Completed business readiness requirements
- Completed technical requirements
- Confirmed event attendees

Go / No-Go principle:

> Organizations with unresolved technical blockers may be deferred to a future program so event time stays focused on building, not environment setup.

### Success Principle

Every readiness interaction should focus on one question:

> Could this team begin building within 30 minutes if the event started tomorrow?

If not, the identified gap becomes the highest-priority action item for the following week.

## 5. Business Readiness Worksheet

Purpose: Help participating organizations define a suitable Technical Support or Knowledge Base use case before the event.

### Company Information

- Company Name:
- Primary Contact:
- Email:

### Problem Statement

What technical support or knowledge problem are you trying to solve?

Examples:

- Technicians spend too much time searching manuals.
- Employees struggle to find internal procedures.
- Customer support teams cannot quickly answer common support questions.
- Engineering teams search across too many documents.

Prompt:

> Describe the support or knowledge problem users face today.

### Desired Outcome

What should users be able to do after this solution is built?

Examples:

- Quickly find troubleshooting steps.
- Ask questions in natural language.
- Locate relevant documentation.
- Reduce time spent searching for information.

### Success Criteria

How will you know the solution was successful?

Examples:

- Answers common support questions correctly.
- Reduces search time.
- Locates relevant documentation.
- Returns accurate troubleshooting guidance.

Suggested fields:

1. Success Criterion 1:
2. Success Criterion 2:
3. Success Criterion 3:

### Users

Who will use this solution?

Options:

- Internal employees
- Customer support staff
- Field technicians
- Service engineers
- Manufacturing operators
- Other

Estimated number of users:

### Example Questions

Provide examples of questions the agent should answer.

#### Questions that SHOULD work

1.
2.
3.
4.
5.

#### Questions that SHOULD NOT work

Examples:

- Questions unrelated to the provided documents
- Questions requiring data not included in the knowledge base

1.
2.
3.

### Knowledge Base Readiness

What documents will be used?

Options:

- PDF manuals
- Troubleshooting guides
- Standard operating procedures
- Knowledge base articles
- Word documents
- PowerPoint presentations
- Excel documentation
- Other

Approximately how many documents will be provided?

Are the documents available today?

- Yes
- Partially
- No

Are the documents current and accurate?

- Yes
- No
- Unsure

Known document issues:

Examples:

- Outdated procedures
- Duplicate documents
- Missing troubleshooting steps
- Conflicting information

### Event Goals

Rank from 1 to 5:

- Working Technical Support Agent
- Working Knowledge Base Agent
- Better understanding of Azure AI Foundry
- Better understanding of AI Agents
- Plan for future deployment

### Readiness Self-Assessment

Use Red / Yellow / Green:

- Problem clearly defined
- Desired outcome defined
- Success criteria defined
- Example questions ready
- Documents identified
- Documents available
- Documents current

### Definition of Business Ready

An organization is Business Ready when:

- Technical support or knowledge problem is clearly defined
- Desired outcome is documented
- Success criteria are established
- Example questions are identified
- Knowledge base documents are available
- Documents are reasonably accurate and current
- Team can explain what the agent should do

Goal:

> If the event started tomorrow, the team could immediately begin building a Technical Support or Knowledge Base Agent using its own documents.

## 6. Technical Readiness Checklist

Purpose: Ensure participants are technically prepared before the event.

### Required items participants need to know

1. How to create or verify they have an Azure subscription
2. Whether VS Code is installed
3. Whether Python is installed
4. Whether they have GitHub Copilot Pro or higher

Important audience note:

> Attendees are not all senior developers. Readiness content should be written for non-experts using clear, plain language.

### Technical Readiness Requirements

#### Azure Subscription

Participants should confirm:

- They can sign in to the Azure portal.
- They can see an Azure subscription.
- They know which subscription they will use for the lab.
- If company approval is required, they have started that process before event week.

Common blocker categories:

- Can sign in but see no subscription
- Company blocks Azure access
- Unsure whether to use personal or company account
- Need IT/admin approval

#### VS Code

Participants should confirm:

- VS Code is installed.
- VS Code opens successfully.
- They can open a folder.
- They can open the terminal inside VS Code.
- Extensions can be installed or are not blocked.

Common blocker categories:

- Cannot install software on work laptop
- VS Code installed through company software center only
- Extensions blocked by company policy

#### Python

Participants should confirm one of these commands works:

```bash
python --version
python3 --version
py --version
```

Participants should also confirm pip works:

```bash
python -m pip --version
```

Common blocker categories:

- Python command not recognized
- Multiple Python versions installed
- Permission to install Python is blocked
- pip missing or blocked

#### GitHub Copilot

Participants should confirm:

- They have a GitHub account.
- They have GitHub Copilot Pro or higher.
- Copilot is available in VS Code.
- They are signed into the correct GitHub account.

Acceptable Copilot access:

- GitHub Copilot Pro
- GitHub Copilot Pro+
- GitHub Copilot Max
- GitHub Copilot Business
- GitHub Copilot Enterprise

Important clarification:

> A free GitHub account alone is not enough for this lab if Pro or higher is required.

Common blocker categories:

- Signed into the wrong GitHub account
- GitHub account exists but Copilot subscription is missing
- Copilot works in browser but not VS Code
- Copilot extension or sign-in is blocked
- Company-managed GitHub access requires admin support

### Definition of Technically Ready

An organization is Technically Ready when:

- Azure subscription access is verified
- Azure AI Foundry access is verified
- Required AI models are available
- Knowledge base documents are prepared
- VS Code is installed and functional
- Python is installed and functional
- GitHub access works
- GitHub Copilot Pro or higher is active and validated
- Template application can run successfully
- No unresolved critical blockers remain

Final readiness question:

> If the event started tomorrow, could the team begin building within 30 minutes?

## 7. Prompt for VS Code + Claude Opus to Create Technical Readiness Webpages

Use this prompt when working in the AI Lab pre-skilling website repo.

```text
Update the Microsoft AI Co-Innovation Lab pre-skilling website for the Build With Us event.

Context:
This is a hands-on AI lab where companies build Technical Support and Knowledge Base agents, then use GitHub Copilot and VS Code to work with a simple application experience. Attendees are not all senior developers. Some are business/technical users, citizen builders, junior developers, IT admins, or developers who may be new to Azure, VS Code, Python, or GitHub Copilot.

Goal:
Create simple, friendly, step-by-step technical readiness webpages that participants can use before the event to verify they are ready.

Technical readiness requirements participants need help with:
1. Create or verify they have an Azure subscription.
2. Verify Visual Studio Code is installed.
3. Verify Python is installed.
4. Verify they have GitHub Copilot Pro or higher.

Audience guidance:
- Write for non-experts.
- Do not assume the reader is a senior developer.
- Avoid jargon unless explained simply.
- Use plain English.
- Make each page actionable.
- Include how to check if they already have the requirement.
- Include how to install, sign up, or request help if they do not.
- Include a "Good looks like" section at the end of each page.
- Include a simple troubleshooting section.
- Include a final checkbox section participants can use before the readiness meeting.
- Keep the tone professional, encouraging, and clear.
- This is pre-event readiness, not deep technical training.

Existing site:
This is a static pre-skilling website. Inspect the current project structure first. Follow the existing style, layout, naming conventions, navigation pattern, and CSS conventions. Do not introduce a new framework unless the site already uses one. If the site uses a static generator, create pages in the correct content format.

Official reference links to include:
- Azure account / subscription: https://azure.microsoft.com/pricing/purchase-options/azure-account
- VS Code overview: https://code.visualstudio.com/docs/getstarted/overview
- VS Code download: https://code.visualstudio.com/download
- Python setup and usage: https://docs.python.org/3/using/index.html
- Python installing modules and pip: https://docs.python.org/3/installing/index.html
- GitHub Copilot plans and pricing: https://github.com/features/copilot/plans
- GitHub Copilot plan docs: https://docs.github.com/copilot/about-github-copilot/plans-for-github-copilot

Create or update these pages:

Page 1: Technical Readiness Overview
- Title: Technical Readiness for Build With Us
- Explain why technical readiness matters.
- Explain that the goal is to arrive ready to build, not spend event time setting up accounts or software.
- Cover the four readiness areas:
  1. Azure subscription
  2. VS Code
  3. Python
  4. GitHub Copilot Pro or higher
- Explain that weekly readiness meetings are used to resolve blockers.
- Add a simple readiness checklist.

Page 2: Azure Subscription Readiness
- Explain Azure subscription in simple terms.
- Explain why it is needed for Build With Us.
- Include how to check if they already have one:
  - Go to Azure portal.
  - Sign in with the account they plan to use.
  - Look for Subscriptions.
  - Confirm they can see at least one subscription.
- Include what to do if they do not have one.
- Link to the Azure account page.
- Explain that company laptops or company accounts may require IT/admin approval.
- Good looks like:
  - Can sign into Azure.
  - Can see a subscription.
  - Knows which subscription to use for the lab.
- Common issues:
  - Can sign in but see no subscription.
  - Company blocks Azure access.
  - Unsure whether to use personal or company account.
  - Need admin approval.
- Add final checkbox list.

Page 3: Visual Studio Code Readiness
- Explain VS Code in simple terms.
- Explain why it is needed for Day 2.
- Include how to check if VS Code is installed:
  - Windows Start menu.
  - macOS Applications.
  - Launch VS Code.
- Include install link to official VS Code download page.
- Recommend standard installer unless company requires software center.
- Include simple checks:
  - VS Code opens.
  - Can open a folder.
  - Can open terminal.
  - Extensions can be installed.
- Common issues:
  - Cannot install software on work laptop.
  - Extensions blocked.
  - Company requires software center or IT approval.
- Add final checkbox list.

Page 4: Python Readiness
- Explain Python in simple terms.
- Explain why it is needed for the template app.
- Include how to verify Python is installed.
- Tell users to open VS Code terminal or system terminal and try:
  python --version
  python3 --version
  py --version
- Explain that one working command is enough.
- Include how to check pip:
  python -m pip --version
- Explain pip simply as the tool Python uses to install packages.
- Link to official Python setup documentation.
- Explain company laptop installations may require IT approval.
- Good looks like:
  - One Python version command works.
  - pip command works.
- Common issues:
  - Python installed but command not recognized.
  - Multiple Python versions installed.
  - Permission to install Python blocked.
  - pip missing or blocked.
- Add final checkbox list.

Page 5: GitHub Copilot Readiness
- Explain GitHub Copilot simply.
- Explain why it is needed for Day 2.
- Clarify requirement:
  Participants need GitHub Copilot Pro or higher.
  A free GitHub account alone is not enough if the lab requires Pro or higher.
- Explain acceptable access:
  - Copilot Pro
  - Copilot Pro+
  - Copilot Max
  - Copilot Business
  - Copilot Enterprise
- Include how to check subscription status in GitHub account settings.
- Link to GitHub Copilot plans page and GitHub Copilot plan docs.
- Explain company-managed accounts may require admin help.
- Explain how to verify Copilot works in VS Code:
  - Open VS Code.
  - Sign into GitHub.
  - Confirm Copilot Chat or Copilot suggestions are available.
  - Try a simple prompt such as: "Explain this project structure" or "Create a simple hello world function."
- Common issues:
  - GitHub account exists but Copilot subscription is missing.
  - Signed into wrong GitHub account.
  - Copilot works in browser but not VS Code.
  - VS Code extension or sign-in blocked.
- Add final checkbox list.

Page 6: Readiness Summary Checklist
- Give participants a single page to use before weekly readiness meetings and final Go / No-Go.
- Include a readiness table/checklist for:
  Azure:
  - Can sign into Azure.
  - Can see subscription.
  - Know which subscription to use.
  - Know if company approval/admin help is needed.
  VS Code:
  - Installed.
  - Opens successfully.
  - Can open folder.
  - Can open terminal.
  Python:
  - Python version command works.
  - pip version command works.
  GitHub Copilot:
  - Have Copilot Pro or higher.
  - Sign into GitHub works.
  - Copilot works in VS Code.
- Add final question:
  If the event started tomorrow, could you begin building within 30 minutes?
- Add blocker section:
  - Azure access
  - VS Code installation
  - Python installation
  - GitHub Copilot subscription
  - Company laptop restrictions
  - Unsure which account to use

Implementation requirements:
- Follow existing website design.
- Update navigation so new readiness pages are easy to find.
- Add short landing section from the existing pre-skilling home page pointing to Technical Readiness.
- Use consistent headings, cards, callouts, and checklists.
- Make pages mobile friendly.
- Use accessible HTML.
- Use descriptive link text, not bare URLs.
- Avoid heavy animations or complex UI.
- Prefer simple static pages.
- Reuse existing styles and CSS.

Deliverables:
1. Add readiness pages.
2. Update navigation.
3. Add a link from the pre-skilling home page.
4. Add final readiness checklist page.
5. Ensure official reference links use descriptive text.
6. Keep tone consistent with Microsoft AI Co-Innovation Lab.

After making changes:
- Summarize files created or updated.
- Explain how to preview the site locally.
- List anything that should be manually reviewed.
```

## 8. Day 1 Event Agenda

Day 1 focuses on creating a Technical Support or Knowledge Base Agent.

Recommended flow:

1. Tech Setup
   - Connect to Wi-Fi
   - Connect to Teams for file sharing
   - Load Azure and Azure AI Foundry
2. Event Overview
   - Explain Technical Support and Knowledge Base agent focus
   - Show what participants are building today
3. Introductions
   - Companies share use case
4. Show final result
   - Show finished agent experience before building
5. Create first guided agent
   - Use provided prompt
   - Use provided documents/files
   - Test agent
   - Deploy or prepare deployment
6. Show best practices
   - Show good data vs bad data
   - Use two prepared file sets
   - Demonstrate how document quality affects answer quality
7. Create second company agent
   - Upload/use company files
   - Use company-specific prompt
   - Test questions that should work
   - Test questions that should not work
   - Deploy or prepare deployment
8. Demo
   - Companies demo what they built
   - Share problem, solution, and lessons learned
9. Prep for Day 2
   - Confirm VS Code installed
   - Confirm GitHub Copilot installed and active
   - Confirm Python installed
   - Download or prepare template app

## 9. Day 2 Event Agenda

Day 2 focuses on building software with AI as a teammate.

Current planned flow:

1. Verify VS Code and GitHub Copilot installed for each user
2. Verify template app is downloaded
3. Load app and verify it opens
4. Configure app to use first agent built on Day 1
5. Simple intro to vibe coding / AI-assisted development
6. Modify template app using guided GitHub Copilot prompts
7. Create a new copy of the template app using second agent from Day 1 and modify as needed

Suggested Day 2 enhancements:

- Show finished application before coding
- Explain AI as a Teammate rules
- Include good vs bad prompt examples
- Use progressive exercises:
  1. Branding/UI change
  2. Add new screen/page
  3. Add functionality
  4. Integrate custom company agent
  5. Free-form customization
- End with a Next Steps session where each company states:
  - What they built
  - What problem it solves
  - What version 2 should include
  - Who owns next steps
  - What help they need after the event

## 10. Day 1 Facilitator Guide

### Day 1 Purpose

Day 1 helps each company build and deploy an AI-powered Technical Support or Knowledge Base agent using its own documents and example questions.

Goal is not only to create an agent. Participants should understand how document quality, question design, testing, and iteration affect the usefulness of an AI solution.

### Day 1 Success Outcomes

By the end of Day 1, each company should have:

- Connected to event tools and collaboration space
- Understood what they are building and why
- Built a guided example agent
- Tested the guided agent using expected and unexpected questions
- Seen how good data and bad data affect results
- Built a second agent using company knowledge base documents
- Deployed or prepared to deploy the agent
- Shared what they built, what worked, and what they learned

### Facilitator Roles

#### Lead Facilitator

Responsibilities:

- Own room pacing and transitions
- Open and close the day
- Explain purpose of each activity
- Keep the group on schedule
- Lead demos and discussion
- Move the room forward
- Protect the larger group from being stalled by one blocked team

#### Technical Facilitators

Responsibilities:

- Help teams during hands-on activities
- Troubleshoot Azure AI Foundry and access issues
- Help participants upload or connect data
- Validate agent behavior
- Track repeated issues that need group clarification

#### Escalation Facilitator

Responsibilities:

- Handle blockers that should not slow down the room
- Own access and environment setup problems
- Pull blocked participants aside when needed
- Coordinate support through Teams
- Keep unresolved blockers visible

#### Room Operations Support

Responsibilities:

- Wi-Fi support
- Check-in support
- Teams and file sharing support
- Materials distribution
- Break timing
- Room logistics

### Required Materials

Facilitator materials:

- Day 1 slide deck
- Demo script
- Guided Agent instructions
- Good data / bad data demo files
- Agent evaluation worksheet
- Troubleshooting guide
- Teams channel support process
- Final sharing prompts

Participant materials:

- Day 1 workbook
- Business Readiness Worksheet
- Technical Readiness Checklist
- Sample agent prompt
- Guided Agent documents
- Agent evaluation worksheet
- Links to files and resources
- Pre-skilling site

Technical materials:

- Azure access instructions
- Azure AI Foundry access instructions
- Sample document set for Guided Agent
- Good data set
- Bad data set
- Participant upload instructions
- Deployment instructions
- Teams channel for questions and blockers

### Recommended Day 1 Agenda

| Time | Section | Purpose |
|---|---|---|
| 9:00 - 9:30 | Arrival and Tech Setup | Confirm Wi-Fi, Teams, Azure, Foundry |
| 9:30 - 9:50 | Event Overview | Explain what participants are building and why |
| 9:50 - 10:10 | Introductions | Each company shares use case |
| 10:10 - 10:25 | Show Finished Result | Demonstrate target experience before building |
| 10:25 - 11:20 | Build Guided Agent | Everyone builds the same first agent |
| 11:20 - 11:45 | Test Guided Agent | Evaluate which questions work and do not work |
| 11:45 - 12:15 | Data Quality Demo | Show good data vs bad data impact |
| 12:15 - 12:45 | Lunch / Working Break | Support blocked teams |
| 12:45 - 1:45 | Build Company Agent | Companies build with their own documents |
| 1:45 - 2:15 | Test and Improve Company Agent | Improve behavior based on test results |
| 2:15 - 2:40 | Company Demos | Share problem, solution, and lessons learned |
| 2:40 - 3:00 | Prep for Day 2 | Explain agent-to-app experience and setup |

### Troubleshooting Model

Use Green / Yellow / Red:

- Green: Team is progressing normally.
- Yellow: Team has a minor issue but can continue.
- Red: Team is blocked and cannot progress.

Rules:

- Do not stop the full room for one blocked team.
- Escalation facilitator owns red blockers.
- Capture blockers in Teams or a shared tracker.
- Rejoin teams to main flow when ready.

Common issues and responses:

| Issue | Facilitator Response |
|---|---|
| Cannot access Azure | Move to escalation support, validate account/tenant/subscription |
| Cannot open Azure AI Foundry | Validate access, browser, account, tenant, permissions |
| Cannot upload files | Check file type, location, browser permissions |
| Agent answers vaguely | Review document quality and prompt instructions |
| Agent answers unsupported questions | Improve instructions and test unsupported examples |
| Team has poor data | Encourage sample files or narrower scenario |
| Team is behind | Keep them on guided agent and skip optional refinements |

### Facilitator Principles

- Keep the day moving.
- Make the destination visible before participants build.
- Teach evaluation, not just agent creation.
- Reinforce that better knowledge produces better agent behavior.
- Encourage peer learning across companies.
- Keep scope narrow: Technical Support and Knowledge Base agents only.
- Make next steps concrete.

### End-of-Day Facilitator Checklist

Before closing Day 1, confirm:

- Each company created or interacted with the Guided Agent.
- Each company tested questions that should work and should not work.
- Each company saw the good data vs bad data demo.
- Each company started or completed its own agent.
- Each company identified one improvement area.
- Companies shared or prepared short demos.
- Day 2 setup requirements were reviewed.
- Blockers were captured for follow-up.
- Participants know where to find Day 2 materials.

### Day 1 Closing Script

Use or adapt this:

> Today we built the foundation: a knowledge-driven agent that helps users find answers from trusted information. Successful AI solutions are not just about the model. They depend on clear use cases, good source material, thoughtful instructions, and structured testing. Tomorrow we build on this by using GitHub Copilot and VS Code to connect the agent experience into an application. That is where the idea of AI as a teammate becomes concrete: using AI to help build software around the intelligence you created today.

## 11. Remaining Work Checklist

### Readiness Process

- [ ] Create Business Readiness Worksheet
- [ ] Create Technical Readiness Checklist
- [ ] Create Go / No-Go Scorecard
- [ ] Create Participant Homework Package
- [ ] Create Kickoff Deck
- [ ] Define Green / Yellow / Red readiness status model

### Pre-Skilling

- [ ] Finalize Microsoft AI Co-Innovation Lab Getting Started site content
- [ ] Add technical readiness pages to the pre-skilling website
- [ ] Validate all links and learning modules
- [ ] Define required vs optional learning
- [ ] Define completion verification process

### Day 1 Preparation: Guided Agent

- [ ] Create Adventure Works or equivalent sample dataset
- [ ] Build troubleshooting knowledge base files
- [ ] Create Agent #1 prompt
- [ ] Define Agent #1 success criteria
- [ ] Create evaluation/test questions
- [ ] Create deployment instructions

### Day 1 Preparation: Data Quality Demo

- [ ] Create Good Data sample files
- [ ] Create Bad Data sample files
- [ ] Build side-by-side comparison demo
- [ ] Create discussion guide explaining results

### Day 1 Preparation: Evaluation

- [ ] Create Agent Evaluation Worksheet
- [ ] Define questions that should work
- [ ] Define questions that should not work
- [ ] Create pass/fail testing process

### Day 1 Participant Materials

- [ ] Day 1 workbook
- [ ] Day 1 facilitator guide
- [ ] Day 1 demo script
- [ ] Day 1 troubleshooting guide

### Day 2 Preparation: Template Application

- [ ] Finalize application concept
- [ ] Build starter Flask application
- [ ] Connect application to Foundry Agent
- [ ] Create setup instructions
- [ ] Publish source repository

### Day 2 Preparation: GitHub Copilot Content

- [ ] Create AI as a Teammate introduction
- [ ] Create Vibe Coding overview
- [ ] Create prompt engineering guide
- [ ] Create sample Copilot prompts

### Day 2 Hands-On Exercises

- [ ] Exercise 1: Branding/UI changes
- [ ] Exercise 2: Add new page/screen
- [ ] Exercise 3: Add functionality
- [ ] Exercise 4: Integrate custom company agent
- [ ] Exercise 5: Free-form customization

### Day 2 Participant Materials

- [ ] Day 2 workbook
- [ ] Day 2 facilitator guide
- [ ] Copilot cheat sheet
- [ ] Day 2 demo script

### Event Operations

- [ ] Create Teams Team
- [ ] Create Announcements channel
- [ ] Create Readiness Support channel
- [ ] Create Technical Questions channel
- [ ] Create Resources channel
- [ ] Upload readiness materials
- [ ] Define troubleshooting workflow
- [ ] Define escalation process
- [ ] Create status tracking process
- [ ] Create participant support checklist

### Event Logistics

- [ ] Wi-Fi instructions
- [ ] Room setup plan
- [ ] Power/network requirements
- [ ] Check-in process
- [ ] Food/break schedule
- [ ] Signage

### Technical Validation

Day 1 readiness:

- [ ] Validate Azure access
- [ ] Validate Foundry access
- [ ] Validate Teams access
- [ ] Validate file-sharing process

Day 2 readiness:

- [ ] Validate VS Code installation
- [ ] Validate Python installation
- [ ] Validate GitHub Copilot access
- [ ] Validate template app download
- [ ] Validate application startup process

### Program Enhancements

- [ ] Show finished troubleshooting agent before building
- [ ] Add Agent Evaluation Worksheet
- [ ] Add Lessons Learned discussion after Agent #1
- [ ] Add Agent Success Checklist before Agent #2
- [ ] Show finished application before coding
- [ ] Create Vibe Coding Rules slide
- [ ] Create progressive learning exercises
- [ ] Create Good vs Bad Prompt examples
- [ ] Create Next Steps session
- [ ] Create company action plan worksheet
- [ ] Define ownership and follow-up plan

### Measurement and Follow-Up

- [ ] Event feedback survey
- [ ] Agent #1 completion metric
- [ ] Agent #2 completion metric
- [ ] Template application completion metric
- [ ] 30-day follow-up process
- [ ] 90-day impact assessment process

## 12. Top Priorities

If prioritizing, do these first:

1. Business Readiness Worksheet
2. Technical Readiness Checklist
3. Go / No-Go Scorecard
4. Participant Homework Package
5. Adventure Works or equivalent dataset plus Agent #1
6. Agent Evaluation Worksheet
7. Day 2 Template Application
8. Teams Community Setup
9. Day 1 Workbook and Facilitator Guide
10. Day 2 Workbook and Facilitator Guide

## 13. Tone and Style Guidance

Use this style across all participant-facing content:

- Practical
- Clear
- Friendly
- Professional
- Hands-on
- Non-intimidating
- Not overly formal
- Not overly technical
- Written for non-experts
- Focused on action and readiness

Avoid:

- Overly broad AI language
- Heavy jargon
- Abstract strategy talk
- Long theoretical explanations
- Promising production-ready outcomes
- Framing as a lecture or workshop

Preferred language:

- “Build with us”
- “AI as a teammate”
- “Arrive ready to build”
- “Technical Support Agent”
- “Knowledge Base Agent”
- “Use your own documents”
- “Test what should work and what should not work”
- “Better knowledge produces better results”

## 14. Core Teaching Arc

The event should tell this story:

1. Start with a real support or knowledge problem.
2. Prepare useful documents.
3. Build a grounded knowledge agent.
4. Test what the agent should and should not answer.
5. Learn how good data and bad data change outcomes.
6. Build a company-specific agent.
7. Connect the agent to an application experience.
8. Use GitHub Copilot as an AI teammate to improve the application.
9. Leave with a working artifact and a concrete next step.

## 15. Key Principle for the Agent Continuing This Work

When creating new artifacts, keep the program constrained and practical:

> This is a two-day hands-on lab for Technical Support and Knowledge Base agents, built around readiness, guided construction, evaluation, and AI-assisted application development.

If the agent is unsure whether to add something, use this rule:

> Does this help participants arrive ready, build successfully, evaluate what they made, or continue after the event?

If yes, include it. If not, keep it out.
