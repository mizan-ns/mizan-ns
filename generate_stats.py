#!/usr/bin/env python3
"""
Generates a full-width SVG Programming Activity stats card for GitHub README.
Edit the LANGUAGES list below to update your stats.
"""

import os

# ──────────────────────────────────────────────
# Edit your stats here
# ──────────────────────────────────────────────
TITLE = "💻 Programming Activity"

LANGUAGES = [
    {"name": "Python",     "time": "5 hrs 54 mins", "percent": 76.5,  "icon": "python"},
    {"name": "Go",         "time": "3 hrs 5 mins",  "percent": 55.5,  "icon": "go"},
    {"name": "JavaScript", "time": "2 hrs 47 mins", "percent": 36.4,  "icon": "javascript"},
]

# Bar colors
BAR_COLORS = {
    "python":     "#3572A5",
    "go":         "#00ADD8",
    "javascript": "#F7DF1E",
}
BAR_BG    = "#333"
BG_COLOR  = "#0d1117"   # dark GitHub background
TEXT_COLOR = "#c9d1d9"
DIM_COLOR  = "#8b949e"

# ──────────────────────────────────────────────
# Layout constants
# ──────────────────────────────────────────────
WIDTH       = 860
PAD_X       = 32
ROW_H       = 42
HEADER_H    = 60
FOOTER_H    = 16
BAR_H       = 14
BAR_RADIUS  = 7

COL_NAME_W  = 160   # Language name column
COL_TIME_W  = 160   # Time spent column
BAR_START   = PAD_X + COL_NAME_W + COL_TIME_W
BAR_END     = WIDTH - PAD_X
BAR_W       = BAR_END - BAR_START

HEIGHT = HEADER_H + ROW_H * len(LANGUAGES) + FOOTER_H


def bar(x, y, w, h, r, fill, bg):
    """Rounded progress bar (background + fill)."""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}"/>'
        f'<rect x="{x}" y="{y}" width="{w * fill / 100:.1f}" height="{h}" rx="{r}" fill="#4894ca"/>'
    )


def icon_url(name: str) -> str:
    return f"https://cdn.simpleicons.org/{name}?viewbox=auto&size=16"


def generate() -> str:
    rows = []
    for i, lang in enumerate(LANGUAGES):
        y_center = HEADER_H + i * ROW_H + ROW_H // 2
        y_bar    = y_center - BAR_H // 2
        y_img    = y_center - 10
        y_txt    = y_center + 5

        filled_w = BAR_W * lang["percent"] / 100
        color    = BAR_COLORS.get(lang["icon"], "#4894ca")

        rows.append(f"""
  <!-- Row {i}: {lang['name']} -->
  <image href="{icon_url(lang['icon'])}" x="{PAD_X}" y="{y_img}" width="20" height="20"/>
  <text x="{PAD_X + 26}" y="{y_txt}" fill="{TEXT_COLOR}" font-family="monospace" font-size="13">{lang['name']}</text>
  <text x="{PAD_X + COL_NAME_W}" y="{y_txt}" fill="{DIM_COLOR}" font-family="monospace" font-size="12">{lang['time']}</text>
  <rect x="{BAR_START}" y="{y_bar}" width="{BAR_W}" height="{BAR_H}" rx="{BAR_RADIUS}" fill="{BAR_BG}"/>
  <rect x="{BAR_START}" y="{y_bar}" width="{filled_w:.1f}" height="{BAR_H}" rx="{BAR_RADIUS}" fill="{color}"/>
  <text x="{BAR_END + 8}" y="{y_txt}" text-anchor="start" fill="{DIM_COLOR}" font-family="monospace" font-size="11" display="none">{lang['percent']:.1f}%</text>""")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <rect width="{WIDTH}" height="{HEIGHT}" rx="12" fill="{BG_COLOR}" stroke="#30363d" stroke-width="1"/>
  <!-- Title -->
  <text x="{PAD_X}" y="38" fill="{TEXT_COLOR}" font-family="monospace" font-size="15" font-weight="bold">{TITLE}</text>
{''.join(rows)}
</svg>"""
    return svg


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "stats.svg")
    svg_content = generate()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Generated: {out_path}")
