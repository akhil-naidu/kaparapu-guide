#!/usr/bin/env python3
"""Generates the playbook HTML from chapters.py. Run: python3 _src/build.py"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from chapters import CHAPTERS, CHANGELOG
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITLE = "Working with AI: an organisation playbook"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config={{darkMode:'class',theme:{{extend:{{fontFamily:{{sans:['Inter','ui-sans-serif','system-ui','sans-serif']}},
colors:{{background:'hsl(var(--background))',foreground:'hsl(var(--foreground))',muted:{{DEFAULT:'hsl(var(--muted))',foreground:'hsl(var(--muted-foreground))'}},
border:'hsl(var(--border))',card:{{DEFAULT:'hsl(var(--card))',foreground:'hsl(var(--card-foreground))'}},primary:{{DEFAULT:'hsl(var(--primary))',foreground:'hsl(var(--primary-foreground))'}},
accent:{{DEFAULT:'hsl(var(--accent))',foreground:'hsl(var(--accent-foreground))'}},destructive:'hsl(var(--destructive))'}},
borderRadius:{{lg:'var(--radius)',md:'calc(var(--radius) - 2px)',sm:'calc(var(--radius) - 4px)'}}}}}}}};
if(localStorage.theme==='dark'||(!localStorage.theme&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.classList.add('dark');
</script>
<link rel="preconnect" href="https://rsms.me/"><link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body class="bg-background text-foreground font-sans antialiased">
<header class="sticky top-0 z-10 border-b border-border bg-background/90 backdrop-blur">
 <div class="mx-auto flex h-14 max-w-6xl items-center justify-between px-4">
  <a href="index.html" class="font-semibold tracking-tight">Working with AI <span class="text-muted-foreground font-normal">· organisation playbook</span></a>
  <nav class="flex items-center gap-1 text-sm">
   <a class="tab" href="index.html">Overview</a><a class="tab" href="01-roles-and-anti-jobs.html">Chapters</a><a class="tab" href="changelog.html">Changelog</a>
   <button id="theme" class="tab" aria-label="Toggle dark mode" onclick="document.documentElement.classList.toggle('dark');localStorage.theme=document.documentElement.classList.contains('dark')?'dark':'light'">◐</button>
  </nav>
 </div>
</header>
"""
FOOT = """<footer class="border-t border-border mt-16"><div class="mx-auto max-w-6xl px-4 py-6 text-sm text-muted-foreground">Private living document. Last built from <code>_src/chapters.py</code>. See <a class="underline" href="changelog.html">changelog</a>.</div></footer>
<script>
document.querySelectorAll('pre.tpl').forEach(p=>{const b=document.createElement('button');b.textContent='Copy';b.className='copy';b.onclick=()=>{navigator.clipboard.writeText(p.innerText.replace(/^Copy\\n?/,''));b.textContent='Copied';setTimeout(()=>b.textContent='Copy',1200)};p.prepend(b)});
</script>
</body></html>"""

def fname(c): return f"{c['n']:02d}-{c['slug']}.html"
def esc(s): return html.escape(s)

def sidebar(cur):
    items = "".join(
        f'<li><a class="side{" active" if c is cur else ""}" href="{fname(c)}"><span class="num">{c["n"]:02d}</span>{esc(c["title"])}</a></li>'
        for c in CHAPTERS)
    return f'<aside class="hidden lg:block w-64 shrink-0"><nav class="sticky top-20" aria-label="Chapters"><p class="mb-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">Chapters</p><ol class="space-y-1">{items}</ol></nav></aside>'

def section(h, body): return f'<section class="mt-10"><h2 class="text-xl font-semibold tracking-tight">{h}</h2><div class="prose-body mt-3">{body}</div></section>'

def chapter_page(i, c):
    ex = "".join(f'<div class="card"><div class="flex items-center gap-2"><span class="badge">Example</span><h3 class="font-medium">{esc(e[0])}</h3></div><div class="prose-body mt-2">{e[1]}</div></div>' for e in c["examples"])
    tp = "".join(f'<div class="mt-4"><p class="text-sm font-medium">{esc(t[0])}</p><pre class="tpl">{esc(t[1])}</pre></div>' for t in c["templates"])
    pf = "".join(f"<li>{p}</li>" for p in c["pitfalls"])
    prev = CHAPTERS[i-1] if i > 0 else None
    nxt = CHAPTERS[i+1] if i+1 < len(CHAPTERS) else None
    pn = '<nav class="mt-12 grid gap-4 sm:grid-cols-2" aria-label="Previous and next">'
    pn += f'<a class="card hover:bg-muted" href="{fname(prev)}"><span class="text-xs text-muted-foreground">← Previous</span><div class="font-medium">{esc(prev["title"])}</div></a>' if prev else '<a class="card hover:bg-muted" href="index.html"><span class="text-xs text-muted-foreground">← Back</span><div class="font-medium">Overview</div></a>'
    pn += f'<a class="card hover:bg-muted text-right" href="{fname(nxt)}"><span class="text-xs text-muted-foreground">Next →</span><div class="font-medium">{esc(nxt["title"])}</div></a>' if nxt else '<a class="card hover:bg-muted text-right" href="changelog.html"><span class="text-xs text-muted-foreground">Next →</span><div class="font-medium">Changelog</div></a>'
    pn += "</nav>"
    body = f"""<div class="mx-auto flex max-w-6xl gap-10 px-4 py-10">{sidebar(c)}
<main class="min-w-0 flex-1"><p class="text-sm text-muted-foreground">Chapter {c['n']:02d} of {len(CHAPTERS)}</p>
<h1 class="mt-1 text-3xl font-bold tracking-tight">{esc(c['title'])}</h1><p class="mt-3 text-lg text-muted-foreground">{esc(c['lede'])}</p>
<div class="card mt-8 border-l-4 border-l-primary"><span class="badge">Principle</span><div class="prose-body mt-2">{c['principle']}</div></div>
{section('Why it matters', c['why'])}
{section('Worked examples', '<div class="grid gap-4">'+ex+'</div>')}
{section('Templates', tp) if c['templates'] else ''}
{section('Pitfalls', '<ul>'+pf+'</ul>')}
{pn}</main></div>"""
    return HEAD.format(t=f"{c['n']:02d} {esc(c['title'])} · {TITLE}") + body + FOOT

def index_page():
    cards = "".join(f'<a href="{fname(c)}" class="card hover:bg-muted block"><span class="badge">{c["n"]:02d}</span><h3 class="mt-2 font-semibold">{esc(c["title"])}</h3><p class="mt-1 text-sm text-muted-foreground">{esc(c["lede"])}</p></a>' for c in CHAPTERS)
    roles = [("Human owner","Decides, approves, corrects context. The only source of approval."),
             ("PM / research bot","Research, spikes, PRDs, epics, ticket reviews. Never edits the tracker, never writes code."),
             ("Ticket-keeper bot","The only bot that writes to the tracker. One per organisation."),
             ("Coding bot","Code, PRs and releases, only through the organisation's Cursor Project cloud agents."),
             ("Email triage bot","Reads and sorts mail, drafts replies. Never sends without approval."),
             ("Personal advisor bot","Digests, priorities, cross-cutting advice. No org writes."),
             ("Fleet-admin bot","Designs and tunes the bots and their instructions. No product work.")]
    rcards = "".join(f'<div class="card"><h3 class="font-medium">{a}</h3><p class="mt-1 text-sm text-muted-foreground">{b}</p></div>' for a,b in roles)
    body = f"""<main class="mx-auto max-w-6xl px-4">
<section class="py-16 sm:py-24"><span class="badge">Private · living document</span>
<h1 class="mt-4 text-4xl font-bold tracking-tight sm:text-5xl">{TITLE}</h1>
<p class="mt-4 max-w-2xl text-lg text-muted-foreground">How one organisation runs product work with a small fleet of AI assistants: chat bots with single jobs, Cursor cloud agents for code, and a human who approves every step that leaves the box. Every rule here comes from real work on a real product.</p>
<div class="mt-8 flex gap-3"><a class="btn-primary" href="01-roles-and-anti-jobs.html">Start reading</a><a class="btn-outline" href="{{RUN}}">Jump to the worked example</a></div></section>

{section('What this playbook is', '<p>A guide to working with AI inside <em>one</em> organisation. It merges the habits of an owner who runs several bots day to day into a single set of practices: who does what, how approval flows, how research turns into tickets, how tickets turn into PRs, and how the process remembers what it learned.</p><p>The running example is a real internal-platform project (a Kubernetes-based PaaS, called <code>kube-poc</code> here) taken from a first question about one ticket all the way to an approved, phased epic.</p>')}

<section class="mt-10"><h2 class="text-xl font-semibold tracking-tight">Bot roles</h2>
<p class="mt-2 text-muted-foreground">One job each, plus explicit anti-jobs. Arrows show handoffs; only the keeper touches the tracker and only the coding bot touches code.</p>
<pre class="diagram mt-4" aria-label="Bot roles diagram">
                 ┌──────────────────────┐
                 │     Human owner      │  approves · corrects context
                 └──────────┬───────────┘
        asks / approves     │      digests / alerts
   ┌──────────────┬─────────┼───────────┬──────────────┐
   ▼              ▼         ▼           ▼              ▼
┌────────┐  ┌──────────┐ ┌────────┐ ┌──────────┐ ┌───────────┐
│ PM bot │  │  Email   │ │Advisor │ │Fleet-    │ │ (one set  │
│research│  │  triage  │ │  bot   │ │admin bot │ │  per org) │
└───┬────┘  └────┬─────┘ └────────┘ └──────────┘ └───────────┘
    │ handoff (exact approval words + time)
    ├──────────────────────┐
    ▼                      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐
│ Ticket-keeper│     │  Coding bot  │────▶│ Cursor cloud agents  │
│ (only tracker│     │ (only code)  │     │ in the org's Project │
│   writer)    │◀────│  PR events   │     └──────────┬───────────┘
└──────────────┘     └──────────────┘                ▼
        ▲                                    draft PR → review → merge
        └──── status moves only on PR events ────────┘
</pre>
<div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{rcards}</div></section>

{section('How to read it', '<ol><li>Read chapters 01 to 10 in order. Each builds on the previous one: roles, clean requests, approvals, research, documents, the tracker, tools, communication, memory and finally the execution loop.</li><li>Chapter 11 replays the whole kube-poc story step by step, linking back to the rule each step illustrates.</li><li>Chapter 12 describes the owner&#39;s working style: the habits that make the rest work.</li><li>Copy templates straight from the grey boxes. Text marked <span class="badge-muted">Inferred</span> is interpretation, not a recorded rule.</li></ol>')}

<section class="mt-10"><h2 class="text-xl font-semibold tracking-tight">Chapters</h2><div class="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{cards}</div></section>
</main>"""
    return HEAD.format(t=TITLE) + body.replace("{RUN}", fname(next(c for c in CHAPTERS if c["slug"]=="running-example"))) + FOOT

def changelog_page():
    rows = "".join(f'<li class="card"><div class="flex items-center gap-2"><span class="badge">{esc(v)}</span><time class="text-sm text-muted-foreground">{esc(d)}</time></div><div class="prose-body mt-2">{b}</div></li>' for v,d,b in CHANGELOG)
    body = f'<main class="mx-auto max-w-3xl px-4 py-12"><h1 class="text-3xl font-bold tracking-tight">Changelog</h1><p class="mt-2 text-muted-foreground">Newest first. Add an entry every time a chapter changes or the process learns something.</p><ol class="mt-8 space-y-4">{rows}</ol></main>'
    return HEAD.format(t="Changelog · "+TITLE) + body + FOOT

def main():
    w = lambda n, s: open(os.path.join(OUT, n), "w").write(s)
    w("index.html", index_page()); w("changelog.html", changelog_page())
    for i, c in enumerate(CHAPTERS): w(fname(c), chapter_page(i, c))
    print("built", 2 + len(CHAPTERS), "pages")
if __name__ == "__main__": main()
