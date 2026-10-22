# Working with AI: an organisation playbook (private)

Private living document. Never reference it in the tracker, tickets, PRs or team channels.

## Layout
- `index.html`, `01-…12-*.html`, `changelog.html`: generated pages (don't hand-edit).
- `assets/theme.css`: shadcn/ui tokens (light + dark) and small component classes (card, badge, tab, side). Copy into `globals.css` when porting to Next.js + shadcn.
- `_src/chapters.py`: all content (chapters + changelog). `_src/build.py`: layout and generator.

## Update
1. Edit `_src/chapters.py` (add a chapter dict, or edit one; `n` sets order and the file name `NN-slug.html`).
2. Add a CHANGELOG entry at the top (version, date, what changed).
3. `python3 _src/build.py`
4. Mark interpretation with `INF`; never add secrets (env var names only), bot names in examples, time estimates, or upstream vendor names the product derives from.

Port note: each chapter maps to a route; `card`/`badge`/sidebar map to shadcn Card, Badge and a Sidebar/Tabs nav.

## Repo
https://github.com/akhil-naidu/ai-workflow-guide (private). Daily work on `dev` (default); `dev` merges into `main` quarterly.
