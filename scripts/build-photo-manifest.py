import json
from pathlib import Path

folders = [
    "Pra",
    "Gallery",
    "Demonstrations",
    "Farmers-Visit",
    "Institutional-Visits",
    "NGO-Community"
]

extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

manifest = {}

for folder in folders:
    directory = Path(folder)

    if directory.exists():
        photos = sorted(
            str(file).replace("\\", "/")
            for file in directory.rglob("*")
            if file.is_file() and file.suffix.lower() in extensions
        )
    else:
        photos = []

    manifest[folder] = photos

Path("photo-manifest.json").write_text(
    json.dumps(manifest, indent=2),
    encoding="utf-8"
)

print("Photo manifest generated successfully!")
