"""Make external and PDF links open in a new tab across all generated pages."""

import re
from pathlib import Path

from pelican import signals

LINK_TAG = re.compile(r"<a\s[^>]*>", re.IGNORECASE)
HREF = re.compile(r'href\s*=\s*"([^"]*)"', re.IGNORECASE)


def _add_target(match, siteurl):
    tag = match.group(0)
    href = HREF.search(tag)
    if not href or "target=" in tag.lower():
        return tag
    url = href.group(1)
    if siteurl and url.startswith(siteurl):
        return tag
    if not (url.startswith(("http://", "https://")) or url.lower().endswith(".pdf")):
        return tag
    return tag[:-1] + ' target="_blank" rel="noopener">'


def rewrite_links(path, context):
    if not path.endswith(".html"):
        return
    file = Path(path)
    html = file.read_text(encoding="utf-8")
    siteurl = context.get("SITEURL", "")
    updated = LINK_TAG.sub(lambda m: _add_target(m, siteurl), html)
    if updated != html:
        file.write_text(updated, encoding="utf-8")


def register():
    signals.content_written.connect(rewrite_links)
