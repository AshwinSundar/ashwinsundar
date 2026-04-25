import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import load_music, load_posts, load_projects, load_reading

BASE_DIR = Path(__file__).parent.parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
# Hugo served static/ at the root; preserve /images and /photos URLs from old content
app.mount("/images", StaticFiles(directory=BASE_DIR / "static" / "images"), name="images")
app.mount("/photos", StaticFiles(directory=BASE_DIR / "static" / "photos"), name="photos")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(BASE_DIR / "static" / "favicon.ico")


@app.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse(BASE_DIR / "static" / "robots.txt")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

_include_drafts = os.getenv("DRAFTS", "").lower() in ("1", "true", "yes")

_posts = load_posts(include_drafts=_include_drafts)
_reading = load_reading(include_drafts=_include_drafts)
_posts_by_slug = {p.slug: p for p in _posts}
_reading_by_slug = {p.slug: p for p in _reading}
_music = load_music()
_projects = load_projects()


def _by_genre(posts, genre):
    return [p for p in posts if genre in p.genres]


def _by_year(posts, year):
    return [p for p in posts if str(year) in p.genres]


@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {
            "technical": _by_genre(_posts, "technical"),
            "short_stories": _by_genre(_posts, "short-story"),
            "other": _by_genre(_posts, "other"),
            "reading2026": _by_year(_reading, 2026),
            "reading2025": _by_year(_reading, 2025),
            "reading2024": _by_year(_reading, 2024),
            "music": _music,
            "projects": _projects,
        },
    )


@app.get("/posts/{slug}")
async def post(request: Request, slug: str):
    p = _posts_by_slug.get(slug)
    if not p:
        raise HTTPException(404)
    return templates.TemplateResponse(request, "post.html", {"post": p})


@app.get("/posts/{slug}/{filename}")
async def post_asset(slug: str, filename: str):
    p = _posts_by_slug.get(slug)
    if not p or not p.asset_dir:
        raise HTTPException(404)
    asset = p.asset_dir / filename
    if not asset.exists() or asset.suffix.lower() == ".md":
        raise HTTPException(404)
    return FileResponse(asset)


@app.get("/reading/{slug}")
async def reading(request: Request, slug: str):
    p = _reading_by_slug.get(slug)
    if not p:
        raise HTTPException(404)
    return templates.TemplateResponse(request, "post.html", {"post": p})
