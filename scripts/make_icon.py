"""Draw .claude-plugin/icon.png: a stylised chip with a price tag. Run once; output is committed."""
from pathlib import Path

from PIL import Image, ImageDraw

S = 1024
OUT = Path(__file__).resolve().parent.parent / ".claude-plugin" / "icon.png"
img = Image.new("RGBA", (S, S), (24, 32, 48, 255))
d = ImageDraw.Draw(img)

# Chip body and pins.
c0, c1 = 262, 762
for i in range(5):
    p = c0 + 50 + i * 90
    for box in ((p, c0 - 90, p + 40, c0), (p, c1, p + 40, c1 + 90), (c0 - 90, p, c0, p + 40), (c1, p, c1 + 90, p + 40)):
        d.rounded_rectangle(box, 10, fill=(160, 174, 192, 255))
d.rounded_rectangle((c0, c0, c1, c1), 48, fill=(56, 189, 148, 255))
d.rounded_rectangle((c0 + 70, c0 + 70, c1 - 70, c1 - 70), 28, outline=(24, 32, 48, 255), width=22)

# Price tag in the corner.
d.polygon([(600, 600), (860, 600), (940, 700), (860, 800), (600, 800)], fill=(251, 191, 36, 255))
d.ellipse((835, 680, 875, 720), fill=(24, 32, 48, 255))

img.resize((512, 512), Image.LANCZOS).save(OUT)
assert Image.open(OUT).size == (512, 512)
print(OUT)
