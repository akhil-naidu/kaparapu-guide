import { chapter as chapter01 } from "@/content/chapters/01-roles-and-anti-jobs.mdx"
import { chapter as chapter02 } from "@/content/chapters/02-clean-requests.mdx"
import { chapter as chapter03 } from "@/content/chapters/03-approvals-and-handoffs.mdx"
import { chapter as chapter04 } from "@/content/chapters/04-research-before-proposing.mdx"
import { chapter as chapter05 } from "@/content/chapters/05-spikes-prds-epics.mdx"
import { chapter as chapter06 } from "@/content/chapters/06-tracker-hygiene.mdx"
import { chapter as chapter07 } from "@/content/chapters/07-tools-tokens-verification.mdx"
import { chapter as chapter08 } from "@/content/chapters/08-communication.mdx"
import { chapter as chapter09 } from "@/content/chapters/09-shared-memory.mdx"
import { chapter as chapter10 } from "@/content/chapters/10-execution-loop.mdx"
import { chapter as chapter11 } from "@/content/chapters/11-running-example.mdx"
import { chapter as chapter12 } from "@/content/chapters/12-working-style.mdx"
import type { ChapterRecord } from "@/lib/content-types"

export type Chapter = ChapterRecord & {
  href: string
}

export type ChapterLink = {
  n: number
  title: string
  href: string
}

const records = [
  chapter01,
  chapter02,
  chapter03,
  chapter04,
  chapter05,
  chapter06,
  chapter07,
  chapter08,
  chapter09,
  chapter10,
  chapter11,
  chapter12,
]

export const chapters: Chapter[] = records
  .map((record) => ({
    ...record,
    href: `/${record.meta.path}`,
  }))
  .sort((left, right) => left.meta.n - right.meta.n)

export const chapterLinks: ChapterLink[] = chapters.map((chapter) => ({
  n: chapter.meta.n,
  title: chapter.meta.title,
  href: chapter.href,
}))

export function getChapter(slug: string) {
  return chapters.find((chapter) => chapter.meta.path === slug)
}
