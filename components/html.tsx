import parse, {
  Element,
  domToReact,
  type DOMNode,
} from "html-react-parser"
import type { ReactNode } from "react"
import { Badge } from "@/components/ui/badge"

const KNOWN_TAG =
  /<\/?(?:p|ul|ol|li|b|strong|em|code|pre|table|thead|tbody|tr|th|td|span|a|br|div)\b[^>]*>/gi

function escapeUnknownTags(source: string) {
  const kept: string[] = []
  const shielded = source.replace(KNOWN_TAG, (tag) => {
    const token = `\u0000${kept.length}\u0000`
    kept.push(tag)
    return token
  })
  const escaped = shielded.replace(/</g, "&lt;").replace(/>/g, "&gt;")
  return escaped.replace(/\u0000(\d+)\u0000/g, (_match, index: string) => {
    return kept[Number(index)] ?? ""
  })
}

function isElement(node: DOMNode): node is Element {
  return node instanceof Element
}

export function Html({ html }: { html: string }) {
  const nodes = parse(escapeUnknownTags(html), {
    replace(node) {
      if (!isElement(node) || node.attribs.class !== "badge-muted") {
        return undefined
      }
      return (
        <Badge variant="secondary">
          {domToReact(node.children as DOMNode[])}
        </Badge>
      )
    },
  })
  return nodes as ReactNode
}
