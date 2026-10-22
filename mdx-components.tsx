import type { MDXComponents } from "mdx/types"
import { Badge } from "@/components/ui/badge"

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    Badge,
    ...components,
  }
}
