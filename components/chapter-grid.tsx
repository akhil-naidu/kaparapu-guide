import Link from "next/link"
import { Badge } from "@/components/ui/badge"
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import type { Chapter } from "@/lib/chapters"

export function ChapterGrid({ chapters }: { chapters: Chapter[] }) {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {chapters.map((chapter) => {
        const number = String(chapter.meta.n).padStart(2, "0")
        return (
          <Link key={chapter.href} href={chapter.href} className="block h-full">
            <Card className="h-full">
              <CardHeader>
                <Badge>{number}</Badge>
                <CardTitle>{chapter.meta.title}</CardTitle>
                <CardDescription>{chapter.meta.lede}</CardDescription>
              </CardHeader>
            </Card>
          </Link>
        )
      })}
    </div>
  )
}
