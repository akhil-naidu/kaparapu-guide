"""Playbook content. Edit here, then run: python3 _src/build.py
Each chapter: n, slug, title, lede, principle, why (HTML), examples [(title, HTML)],
templates [(label, text)], pitfalls [HTML]. Mark interpretation with INF."""
INF = '<span class="badge-muted">Inferred</span>'

CHAPTERS = [
dict(n=1, slug="roles-and-anti-jobs", title="One bot, one job",
 lede="Give every assistant a single job and an explicit list of things it must never do.",
 principle="<p>Each bot owns exactly one job and has written <strong>anti-jobs</strong>. Roles are mirrored per organisation (one keeper, one coding bot, one content bot each); general bots serve the owner across everything.</p>",
 why="<p>When one assistant researches, edits the tracker and writes code, nobody can tell which change came from where, and approvals get blurred. Single jobs make every action traceable to one role, keep instructions short, and let you tune or replace one bot without touching the rest.</p><p>A single writer per system is the key idea: only the keeper writes to the tracker; only the coding bot touches repositories.</p>",
 examples=[
  ("The roster", "<ul><li><b>PM / research bot</b>: research, spikes, PRDs, epics, ticket reviews. Anti-jobs: never edits the tracker, never writes code or PRs.</li><li><b>Ticket-keeper bot</b>: the only tracker writer; sweeps PRs against tickets, keeps the action list. Anti-jobs: no code, no ticket creation without approval.</li><li><b>Coding bot</b>: code, PRs, releases, only through cloud agents in the organisation's Cursor Project; logs every agent it launches. Anti-jobs: no tracker writes, no merges without the owner.</li><li><b>Email triage bot</b>: reads and sorts mail, drafts. Anti-job: never sends without approval.</li><li><b>Personal advisor bot</b>: digests and priorities across everything. Anti-job: no org writes.</li><li><b>Fleet-admin bot</b>: designs bots and pushes approved process fixes to them. Anti-job: no product work.</li></ul>"),
  ("A handoff instead of a shortcut", "<p>In the kube-poc work the owner said \"update the ticket then\". The PM bot had the API token and could have edited the ticket itself. Instead it sent the rewritten PRD to the keeper bot, which updated the ticket and replied with the link. The PM bot then confirmed to the owner only after the keeper reported back.</p>"),
  ("Naming by role, not by bot", "<p>Bots get a fitting character name for the owner's convenience (a navigator for the keeper, a strategist for the PM). That name never leaves the owner's chat: see chapter 06.</p>"),
 ],
 templates=[("Role card (paste into a bot's instructions)", """ROLE: <PM / research bot> for <organisation>.
JOB: research, spikes, PRDs, epics, ticket reviews for <products/repos>.
ANTI-JOBS:
- Never edit the tracker. Hand tracker changes to the keeper bot.
- Never write code or open PRs. Hand code work to the coding bot.
- Never send email or post to team channels; drafts only.
HANDOFFS: carry the owner's exact words and the time (see chapter 03).
READ FIRST: /persistence/INDEX.md and <org>/context.md.""")],
 pitfalls=["Letting a bot \"just quickly\" do another bot's job because it has the access. Access is not permission.",
  "Two bots writing to the same system: you will get duplicate tickets and conflicting statuses.",
  "Mixing organisations in one bot. Mirrored bots share <em>process</em>, never org data."]),

dict(n=2, slug="clean-requests", title="Write a clean request before you send it",
 lede="Dictate or type the ask, run it through a polish and a prompt-engineer pass, read it back, then send.",
 principle="<p>Every request to a bot or any AI is cleaned before it is sent. The owner's practice (in his words, 2026-10-22): dictate with <b>Wispr Flow</b>, or type when he needs to think; when done, run Wispr Flow's transformers <b>Option+1 (Polish)</b> and <b>Option+2 (Prompt engineer)</b>. Reading the polished or prompt-engineered version also confirms his own understanding of the ask and lets him check it's what he actually wants.</p>",
 why="<ul><li><b>It is a verification loop.</b> The rewrite is a second reading of your own intent. If the cleaned text says something you did not mean, you caught a misunderstanding before any bot acted on it.</li><li><b>Fewer correction rounds.</b> A vague ask produces a plausible but wrong answer, then a correction, then a redo. A clean ask removes most of those loops. " + INF + " the effect is largest on long research or ticket requests.</li><li><b>Better downstream text.</b> Bots often quote the owner's words in handoffs (chapter 03). Clean words make clean approvals.</li></ul>",
 examples=[
  ("The steps", "<ol><li>Dictate the request in Wispr Flow, or type it when you need to think it through.</li><li>Select it and press <b>Option+1</b> (Polish) for grammar and clarity.</li><li>For anything non-trivial, press <b>Option+2</b> (Prompt engineer) to structure it: goal, context, constraints, expected output.</li><li>Read the result. Ask: is this what I actually want? Fix anything that drifted.</li><li>Send.</li></ol>"),
  ("Before and after <span class=\"badge-muted\">Illustrative</span>", "<p>This pair is written for the guide; it is not a recorded message.</p><p><b>Raw dictation:</b></p><pre class=\"tpl\">ok so the api info thing shows wrong version i think and the builder too, we had open spec for this right so why, if its a bug put it in the old ticket</pre><p><b>After Polish + Prompt engineer:</b></p><pre class=\"tpl\">Check https://k8s.dflow.sh/api/v1/info. The version and the default builder image look wrong.\n1. Confirm whether each value is wrong, and why.\n2. Explain why our OpenAPI/OpenSpec contract did not catch it.\n3. If it is a bug, add it to the existing version-mismatch bug ticket (don't create a new one).</pre><p>Reading the second version, the owner can see he is asking for three things, including a root-cause question he only implied.</p>"),
 ],
 templates=[("Self-check before sending", """Before I send:
[ ] Goal in one sentence?
[ ] Context the bot can't know (product, environment, constraints)?
[ ] Exactly which action I approve (create / update / draft only)?
[ ] What I want back (link, list, decision, draft)?
[ ] Does the cleaned version say what I actually mean?""")],
 pitfalls=["Sending the prompt-engineered text without reading it. The read-back is the point.",
  "Letting the rewrite add scope you didn't ask for (extra deliverables, invented constraints). Delete them.",
  "Over-engineering one-line asks. Polish alone is enough for \"link to the ticket\"."]),

dict(n=3, slug="approvals-and-handoffs", title="Approvals travel with the work",
 lede="Only the human approves. Every handoff carries the exact approval words and a timestamp.",
 principle="<p>Anything irreversible or visible to others (sending, posting, creating or updating tickets, merging, spending) needs the owner's explicit approval. When a bot hands work to another bot, it quotes the owner's <b>exact words</b> and the <b>time</b> so the receiver can verify the approval instead of trusting a paraphrase.</p><p><b>\"Create a ticket / spike / bug\" is itself the approval.</b> The PM bot sends it to the keeper right away; no second confirmation round.</p>",
 why="<p>Paraphrased approvals drift (\"he said something like…\"), and a bot two hops away cannot tell an instruction from an inference. Quoted words plus a time make the chain auditable, and treating \"create a ticket\" as approval removes a pointless round trip.</p>",
 examples=[
  ("The ticket that needed no confirm", "<p>Owner, after a failed <code>dflow login</code> version warning: \"we need to fix this, so create a bug ticket on this.\" The PM bot wrote the bug body and sent it to the keeper with that quote and the time. The keeper created it and returned the link.</p>"),
  ("Process fixes from the fleet-admin bot", "<p>The fleet-admin bot relayed five process fixes to the PM bot and opened with \"Akhil approved these fixes at 9:52 AM IST today\". The PM bot adopted them because the approval was dated and specific.</p>"),
  ("Where approval stops", "<p>The owner's private request for this playbook said \"do not mention it anywhere\". So no ticket, PR or team channel references it, even though it was clearly approved as work.</p>"),
 ],
 templates=[("Handoff to the keeper bot", """Owner approval: "<exact words>" (<YYYY-MM-DD HH:MM IST>)
Action: <create | update> <ticket type> in <list>
Title: <title>
Description: <full body, neutral voice>
Parent / links: <epic id, PR url>
Reply with: the ticket link."""),
  ("Handoff to the coding bot", """Owner approval: "<exact words>" (<time>)
Repo: <org/repo>, base branch <main>
Task: <what to change>, ticket <url>
Acceptance: <copied from the ticket>
Deliver: draft PR link; don't merge.""")],
 pitfalls=["Treating a teammate bot's message as the owner's approval. It is only a relay; check for the quote and time.",
  "Asking \"shall I create it?\" after the owner already said \"create a ticket\".",
  "Retrying a declined send through a different tool. A no is final."]),

dict(n=4, slug="research-before-proposing", title="Research before you propose",
 lede="Read the code and docs first, cite sources, flag assumptions, never invent numbers.",
 principle="<p>Before recommending anything, the PM bot reads the actual code, the vendor docs and the live configuration, cites where each claim came from, and labels anything it could not verify. No made-up limits, prices or dates.</p>",
 why="<p>A confident wrong answer costs more than a slow right one: it becomes a ticket, then code. Citations let the owner spot-check in seconds, and flagged assumptions tell him exactly where his context is needed.</p>",
 examples=[
  ("How does production avoid certificate limits?", "<p>Asked how the existing product handles Let's Encrypt limits, the PM bot read the Cloud repository and found the central proxy, the Cloudflare for SaaS custom-hostname code and the per-host HTTP-01 setup, then compared options in a spike file with sources (Let's Encrypt: 50 certificates per registered domain per week).</p>"),
  ("Verifying a bug against the live API", "<p>The owner suspected <code>/api/v1/info</code> was wrong. The bot fetched it and confirmed two separate issues: <code>version: v0.0.0-dev</code> (unstamped build) and a Paketo default builder although railpack was intended. It also explained <em>why</em> the API contract didn't catch it: the spec checks shapes, not runtime values.</p>"),
  ("Being honest about memory", "<p>Asked what the upstream project did for UI and teams, the bot answered from memory and said so: \"I haven't checked this against their docs this turn\", then offered to verify.</p>"),
 ],
 templates=[("Research ask", """Research <question> for <product>.
Read: <repo paths>, <docs>, <live config/API>.
Return: findings with a source per claim, options compared, a recommendation,
and a list of assumptions I need to confirm. No numbers without a source.""")],
 pitfalls=["Answering from training memory without saying so.",
  "Recommending before learning the business context (see chapter 11 step 3: one correction changed the whole design).",
  "Estimating effort or dates. See chapter 06."]),

dict(n=5, slug="spikes-prds-epics", title="Spikes, PRDs and epics",
 lede="Three document shapes turn questions into decisions and decisions into ordered tickets.",
 principle="<p><b>Spike</b> answers a question. <b>PRD</b> specifies what to build once the answer is known. <b>Epic</b> orders the resulting tickets with acceptance criteria and dependencies. Files live in the persistence folder; tickets link to them.</p>",
 why="<p>Mixing the question with the spec produces tickets that are half research, half build, which can't be accepted cleanly. Separate shapes give each ticket a clear \"done\".</p>",
 examples=[
  ("Spike → PRD", "<p>The TLS research spike ended with a decision section linking to the rewritten Spike 01 PRD (wildcard Origin CA certificate as the proxy default, no per-app Let's Encrypt, Cloudflare for SaaS custom domains ported from existing code).</p>"),
  ("A standalone spike", "<p>The owner asked for <code>dflow upgrade</code> as \"a new, separate one\", not a continuation. The spike compared self-update libraries, found that versions weren't stamped into builds, and ended with a ticket breakdown.</p>"),
  ("The epic", "<p>Seven phases, 19 sub-tickets (two non-kube-poc tickets were removed after review, and every kube-poc ticket now carries a <code>kube-poc</code> tag), ordered so every feature hangs off a stable foundation: release pipeline, platform foundations, resource model and tenancy, app runtime, data services, templates, console.</p>"),
 ],
 templates=[("Spike", """# Spike: <question>
1. Question (one sentence)
2. Context and current state (with file paths)
3. Options considered
4. Findings, each with a source
5. Recommendation
6. Risks and open questions
7. Proposed tickets (title + acceptance criteria)"""),
  ("PRD", """# PRD: <title>
1 Problem  2 Decision summary  3 Context / current state
4 Users  5 Goals and non-goals  6 Detailed requirements
7 UX flow (CLI and UI contract)  8 Security  9 Observability
10 Success metrics (qualitative)  11 Rollout  12 Test plan
13 Acceptance criteria  14 Open questions  15 Risks  16 References"""),
  ("Epic", """# Epic: <outcome>
Execution: phase by phase, one ticket at a time.
Phase 1 – <name>
  - <ticket>: AC: <...>  Depends on: <...>
Phase 2 – ...
Parallel: <which phases may overlap>
Rules: no time estimates; status moves only on PR events.""")],
 pitfalls=["Success metrics with invented numbers; keep them qualitative unless sourced.",
  "PRDs that silently keep an option the owner removed (the rewrite dropped tunnel mode entirely).",
  "Epics without dependencies; the order is the value."]),

dict(n=6, slug="tracker-hygiene", title="A clean tracker and neutral text",
 lede="No time estimates, correct types and statuses, and team-visible text that never names a bot or vendor upstream.",
 principle="<ul><li>No time estimates, timeboxes or day counts in tickets, PRDs or outlines.</li><li>Every ticket gets a real task type (Bug, Spike, Task…) and the list's proper status.</li><li>Team-visible text is neutral: no bot names, no \"Created by…\" attribution lines, no upstream project names the product is derived from.</li><li>Descriptions contain the actual information, with source links at the bottom.</li></ul>",
 why="<p>The tracker is the team's shared truth. Estimates written by an assistant are guesses that harden into commitments; bot names and attribution make the work about the tool instead of the outcome; and upstream names leak internals the owner doesn't want public.</p>",
 examples=[
  ("Status colours shared across organisations", "<p>Both keepers agreed one colour scheme (grey to do, blue in progress, purple review, yellow QA, red blocked, green done) while each workspace keeps its own status names.</p>"),
  ("Linking PRs", "<p>The team links PRs by posting the PR URL as a ticket comment. The keeper only comments when the match is certain (by title or branch).</p>"),
 ],
 templates=[("Neutral ticket body", """## Context
<what and why, plain language>
## Acceptance criteria
- [ ] <observable outcome>
## Links
Spec: <file/PR>   Source: <thread/email>""")],
 pitfalls=["\"Should take 2 days\" in a description.","\"Generated by <bot>\" footers.","Moving a status because work feels done instead of on a PR event."]),

dict(n=7, slug="tools-tokens-verification", title="Tools, tokens and verification",
 lede="Read-only tokens per organisation, REST over rate-limited connectors, commands checked against the code, releases with a smoke test.",
 principle="<ul><li>One read-only API token per organisation, stored as an env var (for example <code>CLICKUP_API_TOKEN</code> and <code>CLICKUP_TALLEFLOW_API_TOKEN</code>); never printed.</li><li>Prefer the REST API over shared connectors that hit daily limits.</li><li>Verify CLI flags and install steps in the code or with <code>--help</code> before giving commands; give one tested version.</li><li>Every release gets a version smoke test.</li></ul>",
 why="<p>A command that fails on the owner's laptop costs a round trip and trust. A shared connector that runs out of quota stops every bot at once. And an unstamped build makes every test result ambiguous.</p>",
 examples=[
  ("An honest correction", "<p>After adopting the verify-first rule, the PM bot admitted it had never checked the <code>--instances</code> flag in earlier scaling advice and offered to verify it.</p>"),
  ("The smoke test that was missing", "<p>Releases v0.0.2 and v0.0.3 went out, but the installer built the server from the checkout, so <code>/api/v1/info</code> reported <code>v0.0.0-dev</code>. The bug ticket gained acceptance criteria for a release smoke test that fails on a dev version or the wrong builder; PR #6 fixes version stamping.</p>"),
 ],
 templates=[("Release smoke check (shell)", """VER=$(curl -fsS https://<api-host>/api/v1/info | jq -r .version)
[ "$VER" = "$EXPECTED" ] || { echo "version $VER != $EXPECTED"; exit 1; }
dflow version   # CLI must match too""")],
 pitfalls=["Giving three alternative install methods instead of one tested one.","Pasting a token into a ticket or log.","Trusting the spec to catch runtime values."]),

dict(n=8, slug="communication", title="Concise messages, at the right time",
 lede="At most one short \"on it\", then one result message. Respect working hours.",
 principle="<p>Fleet rule (approved 2026-10-21): every bot sends at most one short \"on it\" message, then one result message. Non-urgent items outside working hours go to a shared overnight queue that feeds a morning digest instead of pinging the owner.</p>",
 why="<p>Status chatter buries results. One result message is easy to scan from a phone. " + INF + " the overnight queue exists to protect the owner's off hours; the exact hours aren't written in the source files.</p>",
 examples=[
  ("Good", "<p>\"The bug ticket now includes the /info findings, both the dev version and the Paketo builder, plus the three new acceptance criteria.\" One line, a link, done.</p>"),
  ("Silence is fine", "<p>When the keeper confirmed a ticket update, the PM bot relayed it once and sent nothing back to the keeper: no acknowledgement needed.</p>"),
 ],
 templates=[("Result message", """<Outcome in one sentence> — <link>.
<1–3 bullets only if needed>
<One question, only if a decision is needed>""")],
 pitfalls=["Three progress updates for one task.","Replying to teammate bots just to say thanks.","Ending every message with an offer instead of a result."]),

dict(n=9, slug="shared-memory", title="Shared memory and living docs",
 lede="Persist decisions in one indexed folder; let paired bots share process learnings, never org data.",
 principle="<ul><li>One persistence folder with an <code>INDEX.md</code>: look there first, add a row for anything that must last, never delete without the owner's OK, no secrets.</li><li>A context note per product (e.g. <code>kube-poc-context.md</code>) captures the corrections the owner has made.</li><li>Paired bots in mirrored roles share a learnings file: process only.</li><li>Living documents (action lists, this playbook) carry a changelog.</li></ul>",
 why="<p>Chat history is lost between sessions; files are not. The context note means the owner corrects \"it's an internal PaaS\" once, not every week.</p>",
 examples=[
  ("Learnings row", "<p>\"No time on tickets\" was learned by the dFlow keeper on 2026-10-21 and adopted by the other organisation's keeper the next day, marked \"adopted\" with a reason.</p>"),
 ],
 templates=[("Learnings row", "| <date> | <from role> | <process learning, no org data> | adopted by <role> <date> (<why it fits>) |"),
  ("Context note", """# <product> context (<date>)
- What it is / who uses it:
- Constraints already paid for or decided:
- Rules for tickets about it:
- Which token / tool to use:""")],
 pitfalls=["Putting ticket contents or customer names in a shared learnings file.","Saving into a bot-private scratch folder.","Rewriting someone else's persisted file without approval."]),

dict(n=10, slug="execution-loop", title="The phase-by-phase execution loop",
 lede="One ticket at a time: spike, approve, track, implement in a cloud agent, PR, test, retro.",
 principle="<ol><li>Pick the next ticket in the epic order.</li><li>PM bot writes or refreshes the spike / PRD.</li><li>Owner approves (his words, quoted).</li><li>Keeper updates the ticket and status.</li><li>Coding bot launches a Cursor cloud agent in the organisation's Project; draft PR.</li><li>Owner tests on real infrastructure.</li><li>Status moves only on PR events (opened → review, merged → QA/done).</li><li>Retro note: a learnings row and a changelog entry.</li></ol>",
 why="<p>One ticket in flight keeps statuses truthful and comments clean, and makes every failure easy to trace to one change.</p>",
 examples=[("Where kube-poc enters the loop", "<p>Phase 1 starts with the version-mismatch bug (merge PR #6), because until it lands every test runs on a <code>v0.0.0-dev</code> build.</p>")],
 templates=[("Loop kick-off", """Next ticket: <url> (phase <n>).
1) PM: refresh spike/PRD, list open questions.
2) After my OK: keeper -> in progress; coding bot -> cloud agent, draft PR.
3) I test on <server>. Status moves on PR events only.
4) Retro: one learnings row.""")],
 pitfalls=["Starting ticket two while ticket one waits for review.","Commenting progress on the ticket instead of in chat.","Skipping the retro note."]),

dict(n=11, slug="running-example", title="Worked example: kube-poc end to end",
 lede="Nine steps from one question about a ticket to an approved, phased epic.",
 principle="<p>Read each step with the chapter it illustrates in mind.</p>",
 why="<p>Rules are easier to remember when you have seen them prevent a mistake.</p>",
 examples=[
  ("1. A question about a ticket (ch. 02)", "<p>The owner asks the PM bot to explain Spike 01 (production domains and TLS).</p>"),
  ("2. Research (ch. 04)", "<p>The PM bot reads the kube-poc code, the existing product's code, Let's Encrypt limits and Cloudflare's options, and the live Cloudflare zone.</p>"),
  ("3. Context correction → PRD (ch. 05, 12)", "<p>The owner corrects the framing: \"this application … is not for distributing to multiple users, we use it internally … as our paas\", ACM is already paid for, and \"tunnel mode is not required, create a PRD … very detailed\". The spike becomes a detailed PRD without tunnel mode.</p>"),
  ("4. Keeper updates the tracker (ch. 01, 03)", "<p>\"update the ticket then\" → handoff to the keeper, which updates the ticket and returns the link.</p>"),
  ("5. Coding bot releases (ch. 07)", "<p>The coding bot cuts v0.0.2 and v0.0.3 and opens PR #6 to stamp versions into builds.</p>"),
  ("6. Real-server test finds a bug (ch. 04, 07)", "<p>The owner reinstalls a server, sees a version-mismatch warning and asks for a bug ticket. Later he spots <code>/api/v1/info</code>; the bot verifies two issues and the keeper extends the same bug with smoke-test criteria.</p>"),
  ("7. Architecture decision (ch. 05)", "<p>API and user-model questions establish that the platform has users and namespace roles but no teams or user API. Decision: Cloud owns orgs, billing and auth; kube-poc trusts tokens Cloud signs, scoped to an org's namespaces.</p>"),
  ("8. Phased order (ch. 05)", "<p>The PM bot proposes 7 phases. The owner catches two tickets that belong to other work, so they're removed and a <code>kube-poc</code> tag is added to prevent mix-ups. That leaves 19 tickets.</p>"),
  ("9. Approved as an epic (ch. 10)", "<p>The owner makes it a top-level epic with sub-tickets, executed phase by phase, one ticket at a time, with clean statuses and comments.</p>"),
 ],
 templates=[],
 pitfalls=["Reading this as a script: the value is in the corrections at steps 3 and 6."]),

dict(n=12, slug="working-style", title="The owner's working style",
 lede="Habits worth emulating when you lead a team of assistants.",
 principle="<p>These are observations from the kube-poc work and the bot rules, written as practices to copy. " + INF + " where noted, they are interpretation.</p>",
 why="<p>The fleet works because of how it is directed, not only how it is configured.</p>",
 examples=[
  ("Clean requests first", "<p>Every request is dictated or typed in Wispr Flow, then run through Polish (Option+1) and Prompt engineer (Option+2) and read back to confirm it says what he wants (chapter 02).</p>"),
  ("Decisive context corrections", "<p>One message (\"internal PaaS, ACM already paid, no tunnel mode\") reset a whole design. Correct early and plainly; the bot should then record it in the context note.</p>"),
  ("Pushes for detail", "<p>\"very detailed\" PRDs; acceptance criteria and test plans, not summaries.</p>"),
  ("Testable on real infrastructure", "<p>Releases are proven by reinstalling a real server and logging in, which is how the version bug surfaced.</p>"),
  ("Terse messages", "<p>Short asks (\"link to the ticket\", \"update the ticket then\") and an expectation of short answers.</p>"),
  ("One source of truth per tool", "<p>One tracker writer, one coding route, one persistence folder, one token per organisation.</p>"),
  ("A private team-visible surface", "<p>No bot names, attribution, estimates or upstream names where the team can see; private work (like this playbook) stays untracked there.</p>"),
  ("Delegating by role", "<p>He asks the role, not the tool: tracker work goes to the keeper, code to the coding bot, and he expects bots to route among themselves.</p>"),
 ],
 templates=[],
 pitfalls=["Copying the terseness without the clean-request habit: short only works when it is precise."]),
]

CHANGELOG = [
 ("v1.1", "2026-10-22", "<p><b>Scope tag for products.</b> While reviewing the execution epic, the owner spotted two tickets from other work (an app UI rework and uptime monitoring). Fix: they were removed from the epic, the phases were renumbered (19 sub-tickets), and a <code>kube-poc</code> tag now goes on every related ticket. All relevant bots were told. Lesson: tag product scope from day one, so an AI-built roadmap can't pull in tickets that only look related. Tracker limitation: the ClickUp API can't clear a parent, so moving those two tickets out of the epic is a manual step in the app.</p><p><b>Living-guide cadence.</b> Every significant process change the bots report gets a changelog entry. The guide goes public one week after v1.0 and is refreshed every three months. It also works as a rulebook: when a new ask conflicts with an earlier rule, the bots point to the chapter and ask before acting.</p>"),
 ("v1.0", "2026-10-22", "<p>Initial version: landing page with bot-roles diagram, 12 chapters (including <b>Write a clean request before you send it</b>, added the same day from the owner's Wispr Flow Polish / Prompt-engineer practice, and mentioned in the working-style chapter), worked kube-poc example, templates, README.</p>"),
]
