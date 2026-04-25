import re

_OUTER = "group music-control cursor-pointer rounded-md px-2 shadow-lg hover:animate-pulse relative pr-4 select-none"
_ICON = "absolute flex -right-2 -top-2 opacity-0 group-hover:opacity-100 w-6 h-6 rounded-full bg-white items-center justify-center shadow-lg"

_PATTERN = re.compile(
    r'\{\{<\s*music-control\s+"([^"]+)"(?:\s+(\S+))?\s*>\}\}(.*?)\{\{</\s*music-control\s*>\}\}',
    re.DOTALL,
)


def _replace(m: re.Match) -> str:
    action, time, inner = m.group(1), m.group(2) or "", m.group(3).strip()
    if action == "resume-at":
        extra = "active:shadow-lime-500"
        icon_extra, icon = "shadow-lime-500", "&#x23F5;"
    elif action == "pause":
        extra = "active:shadow-red-500 focus:shadow-red-500"
        icon_extra, icon = "shadow-red-500", "&#x23F8;"
    else:
        extra = "active:shadow-blue-500 focus:shadow-blue-500"
        icon_extra, icon = "shadow-blue-500", "&#x23F5;"

    data_time = f' data-time="{time}"' if time else ""
    return (
        f'<span class="{_OUTER} {extra}" data-action="{action}"{data_time}>'
        f"{inner}"
        f'<span class="{_ICON} {icon_extra}">{icon}</span>'
        f"</span>"
    )


def process_mermaid(text: str) -> str:
    return re.sub(
        r"```mermaid\n(.*?)```",
        lambda m: f'<pre class="mermaid">{m.group(1)}</pre>',
        text,
        flags=re.DOTALL,
    )


def process(text: str) -> tuple[str, bool]:
    """Replace shortcodes. Returns (processed_text, has_music_controls)."""
    result, count = _PATTERN.subn(_replace, text)
    result = process_mermaid(result)
    return result, count > 0
