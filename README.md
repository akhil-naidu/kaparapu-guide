# Kaparapu Guide

Private living document. Never reference it in the tracker, tickets, PRs or team channels.

## Layout

- `app/`: Next.js App Router pages. The site is a static export.
- `content/`: landing page, changelog, and the twelve chapters as MDX.
- `components/`: shadcn/ui components and the site shell.
- `deploy/default.conf.template`: nginx config. The image listens on `$PORT`.

## Update

1. Edit the chapter MDX in `content/chapters/`, or the landing and changelog MDX.
2. Keep interpretation marked with the Inferred badge.
3. Do not add secrets (env var names only), names in examples, time estimates, or upstream vendor names the product derives from.
4. `npm run build` writes the static export to `out/`.

## Repo

https://github.com/akhil-naidu/kaparapu-guide (private). Daily work on `dev` (default); `dev` merges into `main` quarterly.
