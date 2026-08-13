import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import load_albums, load_music, load_posts, load_projects, load_reading

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent
BASE_URL = os.getenv("BASE_URL", "https://ashwinsundar.com").rstrip("/")

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
# Hugo served static/ at the root; preserve /images and /photos URLs from old content
app.mount("/images", StaticFiles(directory=BASE_DIR / "static" / "images"), name="images")
app.mount("/photos", StaticFiles(directory=BASE_DIR / "content" / "photos"), name="photos")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(BASE_DIR / "static" / "favicon.ico")


@app.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse(BASE_DIR / "static" / "robots.txt")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

_include_drafts = os.getenv("DRAFTS", "").lower() in ("1", "true", "yes")


@app.get("/")
async def homepage(request: Request):
    posts = load_posts(include_drafts=_include_drafts)
    reading = load_reading(include_drafts=_include_drafts)
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "technical": [p for p in posts if "technical" in p.genres],
            "short_stories": [p for p in posts if "short-story" in p.genres],
            "other": [p for p in posts if "other" in p.genres],
            "reading2026": [r for r in reading if "2026" in r.genres],  # reading material has a year in the genre frontmatter
            "reading2025": [r for r in reading if "2025" in r.genres],
            "reading2024": [r for r in reading if "2024" in r.genres],
            "albums": load_albums(),
            "music": load_music(),
            "projects": load_projects(),
        },
    )


@app.get("/posts/{slug}")
async def post(request: Request, slug: str):
    posts = load_posts(include_drafts=_include_drafts)
    p = next((item for item in posts if item.slug == slug), None)
    if not p:
        raise HTTPException(404)
    return templates.TemplateResponse(request, "post.html", {"post": p})


@app.get("/posts/{slug}/{filename}")
async def post_asset(slug: str, filename: str):
    posts = load_posts(include_drafts=_include_drafts)
    p = next((item for item in posts if item.slug == slug), None)
    if not p or not p.asset_dir:
        raise HTTPException(404)
    asset = p.asset_dir / filename
    if not asset.exists() or asset.suffix.lower() == ".md":
        raise HTTPException(404)
    return FileResponse(asset)


@app.get("/index.xml", include_in_schema=False)
async def rss(request: Request):
    # Preserve the feed URL Hugo used to serve at the site root.
    posts = load_posts(include_drafts=_include_drafts)
    items = [p for p in posts if not p.draft]
    return templates.TemplateResponse(
        request,
        "rss.xml",
        {
            "posts": items,
            "base_url": BASE_URL,
            "build_date": datetime.now(timezone.utc),
        },
        media_type="application/rss+xml",
    )


@app.get("/reading/{slug}")
async def reading(request: Request, slug: str):
    notes = load_reading(include_drafts=_include_drafts)
    p = next((note for note in notes if note.slug == slug), None)
    if not p:
        raise HTTPException(404)
    return templates.TemplateResponse(request, "post.html", {"post": p})


# individual layout page for an album
@app.get("/albums/{album_name}")
async def albums(request: Request, album_name: str):
    album = next((a for a in load_albums() if a["folder"] == album_name), None)
    if not album:
        raise HTTPException(404)

    photos = []
    for p in album.get("photos", []):
        filename = p.get("filename")
        if not filename:
            logger.warning("Album %r has a photo entry with no filename, skipping", album_name)
            continue

        file_path = BASE_DIR / "content" / "photos" / album_name / filename
        if not file_path.exists():
            logger.warning("Album %r references missing file: %s", album_name, file_path)
            continue

        photo_path = quote(f"{album_name}/{filename}")
        photos.append({
            "url": request.url_for("photos", path=photo_path),
            "caption": p.get("caption", ""),
            "aspect": p.get("aspect", "")
        })

    if not photos:
        logger.warning("Album %r has no photos to display", album_name)

    return templates.TemplateResponse(request, "album.html", {"photos": photos})


# individual photo endpoint
# @app.get("/photos/{album}/{photo_name}"
