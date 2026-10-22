import type { Metadata } from "next"
import Link from "next/link"
import { notFound } from "next/navigation"
import { ChapterDocument } from "@/components/chapter-parts"
import { Button } from "@/components/ui/button"
import { chapters, getChapter } from "@/lib/chapters"

type ChapterPageProps = {
  params: Promise<{ slug: string }>
}

export function generateStaticParams() {
  return chapters.map((chapter) => ({ slug: chapter.meta.path }))
}

export const dynamicParams = false

export async function generateMetadata({
  params,
}: ChapterPageProps): Promise<Metadata> {
  const { slug } = await params
  const chapter = getChapter(slug)
  if (!chapter) {
    return { title: "Kaparapu Guide" }
  }
  const number = String(chapter.meta.n).padStart(2, "0")
  return { title: `${number} ${chapter.meta.title}` }
}

export default async function ChapterPage({ params }: ChapterPageProps) {
  const { slug } = await params
  const chapter = getChapter(slug)
  if (!chapter) {
    notFound()
  }

  const index = chapters.findIndex((item) => item.meta.path === slug)
  const previous = index > 0 ? chapters[index - 1] : null
  const next = index + 1 < chapters.length ? chapters[index + 1] : null
  const number = String(chapter.meta.n).padStart(2, "0")

  return (
    <article className="mx-auto flex w-full max-w-3xl flex-col gap-8">
      <div className="flex flex-col gap-3">
        <p className="text-sm text-muted-foreground">
          Chapter {number} of {String(chapters.length).padStart(2, "0")}
        </p>
        <h1 className="font-heading text-3xl font-semibold tracking-tight">
          {chapter.meta.title}
        </h1>
        <p className="text-lg text-muted-foreground">{chapter.meta.lede}</p>
      </div>
      <ChapterDocument chapter={chapter} />
      <nav
        aria-label="Previous and next"
        className="grid gap-4 sm:grid-cols-2"
      >
        <Button
          variant="outline"
          nativeButton={false}
          className="h-auto justify-start px-3 py-3 whitespace-normal"
          render={<Link href={previous ? previous.href : "/"} />}
        >
          <span className="flex flex-col items-start gap-1 text-left">
            <span className="text-xs text-muted-foreground">
              {previous ? "Previous" : "Back"}
            </span>
            <span>{previous ? previous.meta.title : "Overview"}</span>
          </span>
        </Button>
        <Button
          variant="outline"
          nativeButton={false}
          className="h-auto px-3 py-3 whitespace-normal sm:justify-end"
          render={<Link href={next ? next.href : "/changelog"} />}
        >
          <span className="flex flex-col items-start gap-1 text-left sm:items-end sm:text-right">
            <span className="text-xs text-muted-foreground">Next</span>
            <span>{next ? next.meta.title : "Changelog"}</span>
          </span>
        </Button>
      </nav>
    </article>
  )
}
