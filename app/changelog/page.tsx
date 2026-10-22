import type { Metadata } from "next"
import { ChangelogDocument } from "@/components/changelog-parts"
import { changelog } from "@/content/changelog.mdx"

export const metadata: Metadata = {
  title: "Changelog",
}

export default function ChangelogPage() {
  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-8">
      <ChangelogDocument changelog={changelog} />
    </div>
  )
}
