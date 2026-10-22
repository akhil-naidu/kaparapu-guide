import { CopyButton } from "@/components/copy-button"
import { Html } from "@/components/html"
import { Prose } from "@/components/prose"
import { Badge } from "@/components/ui/badge"
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import type { ChapterRecord } from "@/lib/content-types"

export function ChapterDocument({ chapter }: { chapter: ChapterRecord }) {
  return (
    <>
      <Card>
        <CardHeader>
          <CardTitle>Principle</CardTitle>
        </CardHeader>
        <CardContent>
          <Prose>
            <Html html={chapter.principle} />
          </Prose>
        </CardContent>
      </Card>
      <Separator />
      <section className="flex flex-col gap-3">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          Why it matters
        </h2>
        <Prose>
          <Html html={chapter.why} />
        </Prose>
      </section>
      <Separator />
      <section className="flex flex-col gap-4">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          Worked examples
        </h2>
        {chapter.examples.map((example) => (
          <Card key={example.title}>
            <CardHeader>
              <Badge variant="secondary">Example</Badge>
              <CardTitle>
                <Html html={example.title} />
              </CardTitle>
            </CardHeader>
            <CardContent>
              <Prose>
                <Html html={example.html} />
              </Prose>
            </CardContent>
          </Card>
        ))}
      </section>
      {chapter.templates.length > 0 ? (
        <>
          <Separator />
          <section className="flex flex-col gap-4">
            <h2 className="font-heading text-xl font-semibold tracking-tight">
              Templates
            </h2>
            {chapter.templates.map((item) => (
              <Card key={item.label}>
                <CardHeader>
                  <CardTitle>{item.label}</CardTitle>
                </CardHeader>
                <CardContent>
                  <pre className="overflow-x-auto font-mono text-sm whitespace-pre-wrap">
                    {item.text}
                  </pre>
                </CardContent>
                <CardFooter>
                  <CopyButton text={item.text} />
                </CardFooter>
              </Card>
            ))}
          </section>
        </>
      ) : null}
      <Separator />
      <section className="flex flex-col gap-3">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          Pitfalls
        </h2>
        <ul className="list-disc pl-5 leading-7 [&>li+li]:mt-2">
          {chapter.pitfalls.map((pitfall) => (
            <li key={pitfall}>
              <Html html={pitfall} />
            </li>
          ))}
        </ul>
      </section>
    </>
  )
}
