#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

root_dir = Path(__file__).resolve().parent.parent
data_path = root_dir / "_data" / "foinse.yaml"
tags_dir = root_dir / "tags"
dialects_dir = root_dir / "dialects"

if not data_path.exists():
    print(f"Missing {data_path}", file=sys.stderr)
    sys.exit(1)

text = data_path.read_text().splitlines()

def collect_list(key: str) -> list[str]:
    items: list[str] = []
    in_list = False
    indent = None
    for line in text:
        scalar_match = re.match(rf"^(\s*){re.escape(key)}:\s+(.+?)\s*$", line)
        if scalar_match:
            items.append(scalar_match.group(2).strip())
            in_list = False
            indent = None
            continue

        if not in_list:
            m = re.match(rf"^(\s*){re.escape(key)}:\s*$", line)
            if m:
                in_list = True
                indent = len(m.group(1)) + 2
            continue

        if re.match(r"^\s*$", line):
            in_list = False
            indent = None
            continue

        if indent is not None and line.startswith(" " * indent + "- "):
            items.append(line[indent + 2 :].strip())
        else:
            in_list = False
            indent = None
    return items


unique_tags = sorted(set(collect_list("tags")), key=lambda s: s.lower())
unique_dialects = sorted(set(collect_list("dialect")), key=lambda s: (s.lower() == "historical", s.lower()))


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "tag"


tags_dir.mkdir(parents=True, exist_ok=True)
dialects_dir.mkdir(parents=True, exist_ok=True)

for idx, tag in enumerate(unique_tags, start=1):
    slug = slugify(tag)
    title = tag.replace("-", " ")
    content = (
        "---\n"
        "layout: default\n"
        f"title: {title}\n"
        "parent: Browse by tags\n"
        f"nav_order: {idx}\n"
        "---\n\n"
        "{% include resource-styles.html %}\n\n"
        f"{{% assign items = site.data.foinse | where_exp: \"item\", \"item.tags contains '{tag}'\" | sort: \"name\" %}}\n"
        "<div class=\"resource-list\">\n"
        "{% for item in items %}\n"
        "  {% include resource-entry.html item=item %}\n"
        "{% endfor %}\n"
        "</div>\n"
    )
    (tags_dir / f"{slug}.md").write_text(content, encoding="utf-8")

for idx, dialect in enumerate(unique_dialects, start=1):
    slug = slugify(dialect)
    title = dialect.replace("-", " ")
    content = (
        "---\n"
        "layout: default\n"
        f"title: {title}\n"
        "parent: Browse by dialect\n"
        f"nav_order: {idx}\n"
        "---\n\n"
        "{% include resource-styles.html %}\n\n"
        f"{{% assign items = site.data.foinse | where_exp: \"item\", \"item.dialect contains '{dialect}'\" | sort: \"name\" %}}\n"
        "<div class=\"resource-list\">\n"
        "{% for item in items %}\n"
        "  {% include resource-entry.html item=item %}\n"
        "{% endfor %}\n"
        "</div>\n"
    )
    (dialects_dir / f"{slug}.md").write_text(content, encoding="utf-8")

print(f"Generated {len(unique_tags)} tag pages in {tags_dir}/")
print(f"Generated {len(unique_dialects)} dialect pages in {dialects_dir}/")
