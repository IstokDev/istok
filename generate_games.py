import os
import json
import glob

games = []
for manifest_path in glob.glob("games/*/manifest.json"):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        slug = manifest_path.split('/')[1]
        data['url'] = f"https://istok-games.github.io/games/{slug}/{data['file']}"
        data['manifest'] = f"https://istok-games.github.io/games/{slug}/manifest.json"
        games.append(data)

os.makedirs("api", exist_ok=True)
with open("api/games.json", "w", encoding="utf-8") as f:
    json.dump(games, f, ensure_ascii=False, indent=2)

print("✅ games.json обновлён!")
