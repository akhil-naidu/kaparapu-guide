"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import type { ComponentProps, ComponentType, ReactNode } from "react"
import type { ChapterLink } from "@/lib/chapters"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInset,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarRail,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { TooltipProvider } from "@/components/ui/tooltip"

function MenuLink({
  href,
  isActive,
  children,
}: {
  href: string
  isActive: boolean
  children: ReactNode
}) {
  const Button = SidebarMenuButton as ComponentType<
    ComponentProps<typeof SidebarMenuButton> & { nativeButton?: boolean }
  >
  return (
    <Button
      isActive={isActive}
      nativeButton={false}
      render={<Link href={href} />}
    >
      {children}
    </Button>
  )
}

function Crumbs({ chapters }: { chapters: ChapterLink[] }) {
  const pathname = usePathname()
  const chapter = chapters.find((item) => item.href === pathname)
  const firstChapter = chapters[0]

  return (
    <Breadcrumb>
      <BreadcrumbList>
        {pathname === "/" ? (
          <BreadcrumbItem>
            <BreadcrumbPage>Kaparapu Guide</BreadcrumbPage>
          </BreadcrumbItem>
        ) : (
          <BreadcrumbItem>
            <BreadcrumbLink render={<Link href="/" />}>
              Kaparapu Guide
            </BreadcrumbLink>
          </BreadcrumbItem>
        )}
        {pathname === "/changelog" ? (
          <>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Changelog</BreadcrumbPage>
            </BreadcrumbItem>
          </>
        ) : null}
        {chapter && firstChapter ? (
          <>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbLink render={<Link href={firstChapter.href} />}>
                Chapters
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>{chapter.title}</BreadcrumbPage>
            </BreadcrumbItem>
          </>
        ) : null}
      </BreadcrumbList>
    </Breadcrumb>
  )
}

function AppSidebar({ chapters }: { chapters: ChapterLink[] }) {
  const pathname = usePathname()

  return (
    <Sidebar>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <MenuLink href="/" isActive={pathname === "/"}>
              <span>Kaparapu Guide</span>
            </MenuLink>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Guide</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem>
                <MenuLink href="/" isActive={pathname === "/"}>
                  <span>Overview</span>
                </MenuLink>
              </SidebarMenuItem>
              <SidebarMenuItem>
                <MenuLink href="/changelog" isActive={pathname === "/changelog"}>
                  <span>Changelog</span>
                </MenuLink>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
        <SidebarGroup>
          <SidebarGroupLabel>Chapters</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {chapters.map((chapter) => {
                const number = String(chapter.n).padStart(2, "0")
                return (
                  <SidebarMenuItem key={chapter.href}>
                    <MenuLink
                      href={chapter.href}
                      isActive={pathname === chapter.href}
                    >
                      <span>{number}</span>
                      <span>{chapter.title}</span>
                    </MenuLink>
                  </SidebarMenuItem>
                )
              })}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <p className="px-2 text-xs text-muted-foreground">Kaparapu Guide</p>
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}

export function SiteShell({
  chapters,
  children,
}: {
  chapters: ChapterLink[]
  children: ReactNode
}) {
  return (
    <TooltipProvider>
      <SidebarProvider>
        <AppSidebar chapters={chapters} />
        <SidebarInset>
          <header className="flex h-14 shrink-0 items-center gap-2 border-b px-4">
            <SidebarTrigger />
            <Separator orientation="vertical" className="h-4" />
            <Crumbs chapters={chapters} />
          </header>
          <div className="flex flex-1 flex-col gap-8 p-4 md:p-8">
            {children}
            <Separator />
            <footer className="text-sm text-muted-foreground">
              Private living document. See{" "}
              <Link href="/changelog" className="underline">
                changelog
              </Link>
              .
            </footer>
          </div>
        </SidebarInset>
      </SidebarProvider>
    </TooltipProvider>
  )
}
