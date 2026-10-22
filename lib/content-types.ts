export type ChapterMeta = {
  n: number
  slug: string
  path: string
  title: string
  lede: string
}

export type Template = {
  label: string
  text: string
}

export type Example = {
  title: string
  html: string
}

export type ChapterRecord = {
  meta: ChapterMeta
  templates: Template[]
  principle: string
  why: string
  examples: Example[]
  pitfalls: string[]
}

export type Role = {
  title: string
  body: string
}

export type LandingRecord = {
  title: string
  kicker: string
  intro: string
  startHref: string
  startLabel: string
  exampleHref: string
  exampleLabel: string
  playbookTitle: string
  playbook: string
  rolesTitle: string
  rolesIntro: string
  diagram: string
  roles: Role[]
  howToTitle: string
  howTo: string
  chaptersTitle: string
}

export type ChangelogEntry = {
  version: string
  date: string
  html: string
}

export type ChangelogRecord = {
  title: string
  intro: string
  entries: ChangelogEntry[]
}
