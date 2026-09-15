#!/usr/bin/env python3
"""Regenerates src/content/offers/*.md and src/content/pages/*.md from
docs/northstar/mvp/distinctiveness.md, docs/bible/game_bible.md, and the
epic purpose/"obviously working" sections in the ouroboros-manifold repo,
read at one pinned commit so the site cannot drift silently from the bible.

Idempotent: running twice with the same pinned commit produces byte-identical
output. Copy is hand-edited for tone after regeneration; re-running this
script overwrites that hand-editing, so check the diff before committing.

Usage:
    scripts/pull_content.py [--commit SHA]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
SOURCE_REPO = SITE_ROOT.parent / "ouroboros-manifold"
DEFAULT_COMMIT = "e10649a13c6681968dec563f525ea71160a8d606"

OFFERS_OUT = SITE_ROOT / "src" / "content" / "offers"
PAGES_OUT = SITE_ROOT / "src" / "content" / "pages"

TABLE_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*(\d)\s*\|\s*([\d.]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$"
)
SECTION_RE = re.compile(r"^## (.+)$")


def git_show(commit: str, path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(SOURCE_REPO), "show", f"{commit}:{path}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git show {commit}:{path} failed: {result.stderr.strip()}")
    return result.stdout


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s


def yaml_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def parse_offers(distinctiveness_text: str) -> list[dict]:
    offers = []
    for line in distinctiveness_text.splitlines():
        m = TABLE_ROW_RE.match(line)
        if not m:
            continue
        num, offer, epics, dist, risk, cost, priority, hypothesis, round_ = m.groups()
        epic_ids = re.findall(r"E-\d+", epics)
        offers.append(
            {
                "num": int(num),
                "offer": offer,
                "epics": epic_ids,
                "dist": int(dist),
                "risk": int(risk),
                "cost": int(cost),
                "priority": float(priority),
                "hypothesis": hypothesis,
                "round": round_,
            }
        )
    return offers


def split_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        m = SECTION_RE.match(line)
        if m:
            current = m.group(1).strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items()}


def epic_file_path(commit: str, epic_id: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(SOURCE_REPO), "ls-tree", "-r", "--name-only", commit, "docs/bible/epics/"],
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if Path(line).name.startswith(f"{epic_id}-"):
            return line
    return None


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--commit", default=DEFAULT_COMMIT)
    args = ap.parse_args(argv)
    commit = args.commit

    distinctiveness = git_show(commit, "docs/northstar/mvp/distinctiveness.md")
    offers = parse_offers(distinctiveness)
    if not offers:
        print("no offer rows parsed from distinctiveness.md", file=sys.stderr)
        return 1

    OFFERS_OUT.mkdir(parents=True, exist_ok=True)
    for offer in offers:
        primary_epic = offer["epics"][0]
        epic_path = epic_file_path(commit, primary_epic)
        purpose, obvious = "", ""
        if epic_path:
            epic_text = git_show(commit, epic_path)
            sections = split_sections(epic_text)
            purpose = sections.get("Purpose", "")
            obvious = sections.get("Obviously working in 60 seconds", "")

        slug = slugify(offer["offer"])
        fname = f"{offer['num']:02d}-{slug}.md"
        frontmatter = "\n".join(
            [
                "---",
                f'title: "{yaml_escape(offer["offer"])}"',
                f"order: {offer['num']}",
                f"epics: [{', '.join(offer['epics'])}]",
                f"distinctiveness: {offer['dist']}",
                f"risk: {offer['risk']}",
                f"cost: {offer['cost']}",
                f"priority: {offer['priority']}",
                f'hypothesis: "{yaml_escape(offer["hypothesis"])}"',
                f'round: "{yaml_escape(offer["round"])}"',
                f"source_commit: {commit}",
                "---",
            ]
        )
        body_parts = []
        if purpose:
            body_parts.append(f"## Why this is here\n\n{purpose}")
        if obvious:
            body_parts.append(f"## What it feels like in a 60-second session\n\n{obvious}")
        body = "\n\n".join(body_parts) if body_parts else "_(no epic purpose text found for this offer's epics)_"
        (OFFERS_OUT / fname).write_text(frontmatter + "\n\n" + body + "\n", encoding="utf-8")

    hub = git_show(commit, "docs/bible/game_bible.md")
    hub_sections = split_sections(hub)
    what_this_is = hub_sections.get("Vision and Identity", "")

    mvp_readme = git_show(commit, "docs/northstar/mvp/README.md")
    rounds_match = re.search(r"## Rounds\n\n(\|.+?\n)\n", mvp_readme, re.DOTALL)
    rounds_table = rounds_match.group(1) if rounds_match else ""

    PAGES_OUT.mkdir(parents=True, exist_ok=True)
    home_fm = "\n".join(["---", "title: Home", f"source_commit: {commit}", "---"])
    (PAGES_OUT / "home.md").write_text(
        home_fm + "\n\n" + what_this_is + "\n", encoding="utf-8"
    )
    roadmap_fm = "\n".join(["---", "title: Roadmap", f"source_commit: {commit}", "---"])
    (PAGES_OUT / "roadmap.md").write_text(
        roadmap_fm + "\n\n" + rounds_table + "\n", encoding="utf-8"
    )

    print(f"wrote {len(offers)} offer page(s) to {OFFERS_OUT.relative_to(SITE_ROOT)}")
    print(f"wrote 2 page(s) to {PAGES_OUT.relative_to(SITE_ROOT)}")
    print(f"pinned commit: {commit}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
