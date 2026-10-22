declare module "*.mdx" {
  export const chapter: {
    meta: {
      n: number
      slug: string
      path: string
      title: string
      lede: string
    }
    templates: { label: string; text: string }[]
    principle: string
    why: string
    examples: { title: string; html: string }[]
    pitfalls: string[]
  }

  export const landing: {
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
    roles: { title: string; body: string }[]
    howToTitle: string
    howTo: string
    chaptersTitle: string
  }

  export const changelog: {
    title: string
    intro: string
    entries: { version: string; date: string; html: string }[]
  }
}
