import Link from "next/link"
import { Button } from "@/components/ui/button"

export default function NotFound() {
  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-4">
      <h1 className="font-heading text-3xl font-semibold tracking-tight">
        Page not found
      </h1>
      <Button nativeButton={false} render={<Link href="/" />}>
        Back to Kaparapu Guide
      </Button>
    </div>
  )
}
