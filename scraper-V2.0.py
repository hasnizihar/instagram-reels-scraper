import requests
import pandas as pd
import datetime
from pathlib import Path

# Config
task = 3
INPUT_FILE = f"byusername/input/input{task}.txt"
OUTPUT_DIR = Path(f"byusername/output/output{task}/excel")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://instagram-scraper-api2.p.rapidapi.com/v1/reels"
HEADERS = {
"x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
"x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
}

def fetch_reels(username: str):
    """Fetch reels data for a given username."""
    try:
        response = requests.get(API_URL, headers=HEADERS, params={"username_or_id_or_url": username}, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"[ERROR] Failed for {username}: {e}")
        return []

    reels_list = data.get("data", {}).get("items", [])
    reels_data = []
    for item in reels_list:
        posted_time = (
            datetime.datetime.fromtimestamp(item.get("taken_at")).strftime('%Y-%m-%d %H:%M:%S')
            if item.get("taken_at") else None
        )
        reels_data.append({
            "Username": username,
            "Posted Time": posted_time,
            "Views": item.get("play_count"),
            "Reel URL": f"https://www.instagram.com/reel/{item.get('code', '')}/"
        })
    return reels_data

def main():
    with open(INPUT_FILE, "r") as f:
        usernames = [u.strip() for u in f if u.strip()]

    for username in usernames:
        print(f"Fetching reels for: {username}")
        reels_data = fetch_reels(username)

        if not reels_data:
            print(f"No reels found for {username}")
            continue

        df = pd.DataFrame(reels_data)
        output_file = OUTPUT_DIR / f"instagram_reels_{username}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"✅ Saved {len(df)} reels → {output_file}")

    print("\n🎉 All data processed and saved successfully.")

if __name__ == "__main__":
    main()
