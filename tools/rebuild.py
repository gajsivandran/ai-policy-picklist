#!/usr/bin/env python3
"""
Regenerate the app's content from the Word pick-list.

Edit AI_Policy_Pick-List_CEnv.docx, then run:

    pip install python-docx
    python tools/rebuild.py AI_Policy_Pick-List_CEnv.docx

This rewrites only the data line inside index.html. The design and
behaviour of the page are untouched.

The parser relies on the Word styles used in the source document:
  Heading 2  "AIAS Level 1: No AI"        -> a course-level statement
  Block Text                               -> statement / policy paragraphs
  "When to choose this level: ..."         -> the guidance line
  Heading 2  "A. Written and analytical work"  -> a section
  Heading 3  "A1. Written essay or argument"   -> a task
  "Goal: <name> Bloom's: <levels>"             -> a cognitive goal
Keep those conventions and new entries appear in the app automatically.
"""
import json
import re
import sys
from pathlib import Path

try:
    import docx
except ImportError:
    sys.exit("Run: pip install python-docx")


def parse(path):
    d = docx.Document(path)
    paras = [(p.style.name, p.text.strip()) for p in d.paragraphs if p.text.strip()]

    aias, sections = [], []
    mode = level = section = task = goal = None

    for style, t in paras:
        if t.startswith("Section 1:"):
            mode = "aias"
            continue
        if t.startswith("Choosing the right level"):
            mode = None
            continue
        if t.startswith("Section 2:"):
            mode = "picklist"
            continue

        if mode == "aias":
            if style == "Heading 2" and t.startswith("AIAS Level"):
                level = {"label": t, "body": [], "when": ""}
                aias.append(level)
            elif level is not None:
                if t.startswith("When to choose this level:"):
                    level["when"] = t.split(":", 1)[1].strip()
                elif style == "Block Text":
                    level["body"].append(t)

        elif mode == "picklist":
            if style == "Heading 2" and re.match(r"^[A-Z]\.\s", t):
                section = {"id": t[0], "title": t[3:].strip(), "tasks": []}
                sections.append(section)
                task = None
            elif style == "Heading 3" and re.match(r"^[A-Z]\d+\.", t) and section:
                code, name = t.split(".", 1)
                task = {"code": code.strip(), "title": name.strip(), "goals": []}
                section["tasks"].append(task)
                goal = None
            elif t.startswith("Goal:") and task is not None:
                rest, bloom = t[5:].strip(), ""
                parts = re.split(r"Bloom[\u2019']s:", rest)
                if len(parts) == 2:
                    rest, bloom = parts[0].strip(), parts[1].strip()
                goal = {"goal": rest, "bloom": bloom, "text": ""}
                task["goals"].append(goal)
            elif style == "Block Text" and goal is not None and not goal["text"]:
                goal["text"] = t

    return {"aias": aias, "sections": sections}


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python tools/rebuild.py <picklist.docx>")

    root = Path(__file__).resolve().parent.parent
    page = root / "index.html"
    data = parse(sys.argv[1])

    goals = sum(len(t["goals"]) for s in data["sections"] for t in s["tasks"])
    missing = [
        f'{t["code"]}: {g["goal"]}'
        for s in data["sections"] for t in s["tasks"] for g in t["goals"]
        if not g["text"]
    ]
    print(f'{len(data["aias"])} course levels, '
          f'{len(data["sections"])} sections, {goals} goals')
    for m in missing:
        print(f"  no policy text (shown as a cross-reference): {m}")

    if not data["aias"] or not goals:
        sys.exit("Parsed nothing. Check the heading styles in the document.")

    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    html = page.read_text(encoding="utf-8")
    new, n = re.subn(r"const DATA = .*?;\n", f"const DATA = {blob};\n", html, count=1, flags=re.S)
    if n != 1:
        sys.exit("Could not find the data line in index.html.")
    page.write_text(new, encoding="utf-8")
    print(f"Updated {page}")


if __name__ == "__main__":
    main()
