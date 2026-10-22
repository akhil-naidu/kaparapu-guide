import type { Metadata } from "next"
import { Geist, Geist_Mono } from "next/font/google"
import { SiteShell } from "@/components/site-shell"
import { ThemeProvider } from "@/components/theme-provider"
import { chapterLinks } from "@/lib/chapters"
import { cn } from "@/lib/utils"
import "./globals.css"

const geist = Geist({ subsets: ["latin"], variable: "--font-sans" })

const fontMono = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
})

export const metadata: Metadata = {
  title: {
    default: "Kaparapu Guide",
    template: "%s · Kaparapu Guide",
  },
  description:
    "How one organisation runs product work with a small fleet of AI assistants: chat bots with single jobs, Cursor cloud agents for code, and a human who approves every step that leaves the box. Every rule here comes from real work on a real product.",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={cn(
        "antialiased",
        fontMono.variable,
        "font-sans",
        geist.variable
      )}
    >
      <body>
        <ThemeProvider>
          <SiteShell chapters={chapterLinks}>{children}</SiteShell>
        </ThemeProvider>
      </body>
    </html>
  )
}
