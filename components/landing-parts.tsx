import Link from "next/link"
import { Html } from "@/components/html"
import { Prose } from "@/components/prose"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import type { LandingRecord } from "@/lib/content-types"

export function LandingDocument({ landing }: { landing: LandingRecord }) {
  return (
    <>
      <section className="flex flex-col gap-4 py-8">
        <Badge variant="secondary">{landing.kicker}</Badge>
        <h1 className="font-heading text-4xl font-semibold tracking-tight">
          {landing.title}
        </h1>
        <p className="max-w-2xl text-lg text-muted-foreground">{landing.intro}</p>
        <div className="flex flex-wrap gap-3">
          <Button
            nativeButton={false}
            render={<Link href={landing.startHref} />}
          >
            {landing.startLabel}
          </Button>
          <Button
            variant="outline"
            nativeButton={false}
            render={<Link href={landing.exampleHref} />}
          >
            {landing.exampleLabel}
          </Button>
        </div>
      </section>
      <Separator />
      <section className="flex flex-col gap-3">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          {landing.playbookTitle}
        </h2>
        <Prose>
          <Html html={landing.playbook} />
        </Prose>
      </section>
      <Separator />
      <section className="flex flex-col gap-4">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          {landing.rolesTitle}
        </h2>
        <p className="text-muted-foreground">{landing.rolesIntro}</p>
        <pre
          className="overflow-x-auto font-mono text-xs leading-5"
          aria-label="Bot roles diagram"
        >
          {landing.diagram}
        </pre>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {landing.roles.map((role) => (
            <Card key={role.title}>
              <CardHeader>
                <CardTitle>{role.title}</CardTitle>
                <CardDescription>{role.body}</CardDescription>
              </CardHeader>
            </Card>
          ))}
        </div>
      </section>
      <Separator />
      <section className="flex flex-col gap-3">
        <h2 className="font-heading text-xl font-semibold tracking-tight">
          {landing.howToTitle}
        </h2>
        <Prose>
          <Html html={landing.howTo} />
        </Prose>
      </section>
    </>
  )
}
