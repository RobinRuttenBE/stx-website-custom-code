"""Text segments of a page body, for translating with a table.

A segment is one piece of visible text between two tags (stripped), or the
value of an alt / aria-label attribute. translate() swaps every segment for
its translation from the table and keeps the markup and the whitespace
around it. Used by build-shadow-section.py; run on its own to list the
segments of a page:

  python -I code/i18n_segments.py <page.html>
"""
import html
import re
import sys

TAG = re.compile(r'(<[^>]+>)')
ATTR = re.compile(r'\b(alt|aria-label)="([^"]*)"')
SKIP = re.compile(r'^[\s\d.,:;+()%&·\-–]*$')  # numbers, punctuation: never translated


def _text_parts(body):
    """Yield (is_text, chunk) over the body, skipping <style>/<script> content."""
    inside = None
    for chunk in TAG.split(body):
        if not chunk:
            continue
        if chunk.startswith('<'):
            low = chunk.lower()
            if low.startswith('<style') or low.startswith('<script'):
                inside = 'style' if low.startswith('<style') else 'script'
            elif inside and low.startswith('</' + inside):
                inside = None
            yield False, chunk
        else:
            yield (inside is None), chunk


def segments(body):
    seen = []
    for is_text, chunk in _text_parts(body):
        if is_text:
            s = chunk.strip()
            if s and not SKIP.match(html.unescape(s)) and s not in seen:
                seen.append(s)
        else:
            for _, v in ATTR.findall(chunk):
                if v and v not in seen:
                    seen.append(v)
    return seen


def translate(body, table, lang, missing, skip=()):
    out = []
    for is_text, chunk in _text_parts(body):
        if is_text:
            s = chunk.strip()
            if s and not SKIP.match(html.unescape(s)) and s not in skip:
                t = table.get(s, {}).get(lang)
                if t is None:
                    missing.add(s)
                else:
                    lead = chunk[:len(chunk) - len(chunk.lstrip())]
                    trail = chunk[len(chunk.rstrip()):]
                    chunk = lead + t + trail
            out.append(chunk)
        else:
            def attr(m):
                v = m.group(2)
                t = table.get(v, {}).get(lang) if v else None
                if v and t is None:
                    missing.add(v)
                    return m.group(0)
                return '%s="%s"' % (m.group(1), t if v else v)
            out.append(ATTR.sub(attr, chunk))
    return ''.join(out)


if __name__ == '__main__':
    src = open(sys.argv[1], encoding='utf-8').read()
    body = re.search(r'<body[^>]*>(.*)</body>', src, re.S).group(1)
    body = re.sub(r'<script\b.*?</script>', '', body, flags=re.S)
    for s in segments(body):
        print(s)
