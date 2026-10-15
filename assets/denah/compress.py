from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None

SRC = "light.jpeg"
DST = "Denah-web.jpeg"
TMP = "Denah-web.tmp.jpeg"

MAX_SIZE = 2 * 1024 * 1024  # 2 MB

# Target resolusi awal
MAX_WIDTH = 7000
MAX_HEIGHT = 3500

print("=== COMPRESS JPG -> JPEG ===")

img = Image.open(SRC).convert("RGB")

print(f"Input      : {SRC}")
print(f"Original   : {img.width}x{img.height}")
print(f"Size awal  : {os.path.getsize(SRC) / 1024 / 1024:.2f} MB")

# Resize
img.thumbnail(
    (MAX_WIDTH, MAX_HEIGHT),
    Image.LANCZOS
)

print(f"Resized    : {img.width}x{img.height}")

# Coba quality
qualities = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40]

for quality in qualities:

    print(f"Quality {quality}...")

    img.save(
        TMP,
        format="JPEG",
        quality=quality,
        optimize=True,
        progressive=True
    )

    size = os.path.getsize(TMP)

    print(f"  -> {size / 1024 / 1024:.2f} MB")

    if size <= MAX_SIZE:

        os.replace(TMP, DST)

        print()
        print("=== SELESAI ===")
        print(f"Output     : {DST}")
        print(f"Format     : JPEG")
        print(f"Resolution : {img.width}x{img.height}")
        print(f"Quality    : {quality}")
        print(f"Size       : {size / 1024 / 1024:.2f} MB")
        print()
        break

else:

    if os.path.exists(TMP):
        os.remove(TMP)

    print()
    print("Masih > 2 MB.")
    print("Coba turunkan MAX_WIDTH menjadi 6000.")
