import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import frontmatter
from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin

from .shortcodes import process

BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / "content"
DATA_DIR = BASE_DIR / "data"

_md = MarkdownIt(options_update={"html": True})
footnote_plugin(_md)


@dataclass
class Post:
    slug: str
    title: str
    date: date
    genres: list[str]
    draft: bool
    html: str
    audio_file: str | None = None
    audio_title: str | None = None
    has_music_controls: bool = False
    asset_dir: Path | None = None


def _parse_date(val) -> date:
    if isinstance(val, datetime):
        return val.date()
    if isinstance(val, date):
        return val
    if isinstance(val, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(val[: len(fmt)], fmt).date()
            except ValueError:
                continue
    return date(2000, 1, 1)


def _abs_img_srcs(html: str, slug: str, section: str) -> str:
    """Rewrite relative src= values to absolute paths so they resolve correctly
    regardless of whether the post URL has a trailing slash."""
    def repl(m):
        src = m.group(1)
        if src.startswith(("http", "/", "data:")):
            return m.group(0)
        return f'src="/{section}/{slug}/{src.lstrip("./")}"'
    return re.sub(r'src="([^"]*)"', repl, html)


def _is_draft(meta: dict) -> bool:
    v = meta.get("draft", False)
    return v is True or str(v).lower() == "true"


def _load(path: Path, slug: str, section: str, asset_dir: Path | None = None) -> Post | None:
    try:
        post = frontmatter.load(path)
    except Exception:
        return None

    meta = post.metadata
    text, has_music_controls = process(post.content)
    html = _abs_img_srcs(_md.render(text), slug, section)

    return Post(
        slug=slug,
        title=meta.get("title", slug),
        date=_parse_date(meta.get("date")),
        genres=meta.get("genres", []),
        draft=_is_draft(meta),
        html=html,
        audio_file=meta.get("audioFile"),
        audio_title=meta.get("audioTitle"),
        has_music_controls=has_music_controls,
        asset_dir=asset_dir,
    )


def _scan_dir(directory: Path, section: str, include_drafts: bool) -> list[Post]:
    posts = []
    for entry in directory.iterdir():
        if entry.is_dir():
            index = entry / "index.md"
            if index.exists():
                post = _load(index, entry.name, section, asset_dir=entry)
                if post and (include_drafts or not post.draft):
                    posts.append(post)
        elif entry.suffix == ".md" and entry.name not in ("_index.md",):
            post = _load(entry, entry.stem, section)
            if post and (include_drafts or not post.draft):
                posts.append(post)
    return posts


def load_posts(include_drafts: bool = False) -> list[Post]:
    posts = _scan_dir(CONTENT_DIR / "posts", "posts", include_drafts)
    return sorted(posts, key=lambda p: p.date, reverse=True)


def load_reading(include_drafts: bool = False) -> list[Post]:
    notes = _scan_dir(CONTENT_DIR / "reading", "reading", include_drafts)
    return sorted(notes, key=lambda p: p.date, reverse=True)


def load_music() -> list[dict]:
    return json.loads((DATA_DIR / "music.json").read_text())


def load_projects() -> list[dict]:
    return json.loads((DATA_DIR / "projects.json").read_text())
