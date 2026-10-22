import { Html } from "@/components/html"
import { Prose } from "@/components/prose"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { ChangelogRecord } from "@/lib/content-types"

export function ChangelogDocument({
  changelog,
}: {
  changelog: ChangelogRecord
}) {
  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-col gap-2">
        <h1 className="font-heading text-3xl font-semibold tracking-tight">
          {changelog.title}
        </h1>
        <p className="text-muted-foreground">{changelog.intro}</p>
      </div>
      <div className="flex flex-col gap-4">
        {changelog.entries.map((entry) => (
          <Card key={entry.version}>
            <CardHeader>
              <CardTitle>
                <span className="flex flex-wrap items-center gap-2">
                  <Badge>{entry.version}</Badge>
                  <time
                    dateTime={entry.date}
                    className="text-sm font-normal text-muted-foreground"
                  >
                    {entry.date}
                  </time>
                </span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <Prose>
                <Html html={entry.html} />
              </Prose>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}
