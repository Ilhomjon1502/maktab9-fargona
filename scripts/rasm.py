"""Tadbir rasmini sayt uchun tayyorlaydi: 1200px gacha kichraytiradi, WebP qiladi, metadata'ni olib tashlaydi.

Ishlatish (loyiha papkasidan):
    python -I scripts/rasm.py <manba-rasm> <img/tadbir/nom.webp> [x0,y0,x1,y1]

Oxirgi (ixtiyoriy) argument — kesish chegarasi, asl rasm pikselida.
"""
import sys
from pathlib import Path
from PIL import Image

if len(sys.argv) < 3:
    sys.exit(__doc__)

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
im = Image.open(src).convert("RGB")  # RGB — EXIF/GPS ma'lumotlari saqlanmaydi
if len(sys.argv) > 3:
    im = im.crop(tuple(int(v) for v in sys.argv[3].split(",")))
im.thumbnail((1200, 1200), Image.LANCZOS)
dst.parent.mkdir(parents=True, exist_ok=True)
im.save(dst, "WEBP", quality=78, method=6)
print(f"{dst}  {im.width}x{im.height}  {dst.stat().st_size // 1024} KB")
