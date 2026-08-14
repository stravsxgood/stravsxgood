from pathlib import Path
from html import escape

INPUT = "portrait.txt"
OUTPUT = "portrait_tspan.txt"

# --- SESUAIKAN KOORDINAT DI SINI ---
START_X = 28          # Posisi X agar pas di dalam margin kotak VISUAL.MAP
START_Y = 48          # Posisi baris pertama Y
LINE_HEIGHT = 7.55    # Jarak antar baris teks ASCII
# -----------------------------------

TRIM_LEFT = 0
TRIM_RIGHT = 0
REMOVE_EMPTY = False

lines = Path(INPUT).read_text(
    encoding="utf-8",
    errors="ignore"
).splitlines()

# Hapus trailing spaces
lines = [l.rstrip() for l in lines]

if REMOVE_EMPTY:
    lines = [l for l in lines if l.strip()]

# Trim jika diperlukan
processed = []
for line in lines:
    if TRIM_RIGHT > 0:
        line = line[:-TRIM_RIGHT]
    if TRIM_LEFT > 0:
        line = line[TRIM_LEFT:]
    processed.append(line)

y = START_Y
svg = []
for line in processed:
    svg.append(
        f'<tspan x="{START_X}" y="{y:.2f}" xml:space="preserve">{escape(line)}</tspan>'
    )
    y += LINE_HEIGHT

Path(OUTPUT).write_text(
    "\n".join(svg),
    encoding="utf-8"
)

print(f"Generated {len(svg)} tspans into {OUTPUT}!")