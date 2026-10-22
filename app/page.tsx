import { LandingDocument } from "@/components/landing-parts"
import { ChapterGrid } from "@/components/chapter-grid"
import { Separator } from "@/components/ui/separator"
import { landing } from "@/content/landing.mdx"
import { chapters } from "@/lib/chapters"

export default function HomePage() {
  return (
    <div className="mx-auto flex w-full max-w-5xl flex-col gap-10">
      <LandingDocument landing={landing} />
      <Separator />
      <section className="flex flex-col gap-4">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          {landing.chaptersTitle}
        </h2>
        <ChapterGrid chapters={chapters} />
      </section>
    </div>
  )
}
