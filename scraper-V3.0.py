import requests
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

# ------------------- Helper Functions -------------------

def fetch_hashtag_data(hashtag, api_key):
    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/hashtag"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }
    params = {"hashtag": hashtag}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        print(f"✅ Data fetched successfully for #{hashtag}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed for #{hashtag}: {e}")
        return None

def _normalize_time(raw):
    if raw is None:
        return None
    try:
        if isinstance(raw, (int, float)) or (isinstance(raw, str) and raw.isdigit()):
            return datetime.fromtimestamp(int(raw), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(raw, str):
            s = raw.replace("Z", "+00:00")
            try:
                return datetime.fromisoformat(s).astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                return raw
    except Exception:
        return raw
    return raw

def _collect_candidate_posts(d):
    if not isinstance(d, dict):
        return []
    dd = d.get("data", d)
    keys = ["top_posts", "recent_posts", "items", "posts", "medias", "results", "edges"]
    posts = []
    for k in keys:
        val = dd.get(k)
        if isinstance(val, list):
            posts.extend(val)
    flat = []
    for p in posts:
        if isinstance(p, dict):
            if "node" in p and isinstance(p["node"], dict):
                p = p["node"]
            if "media" in p and isinstance(p["media"], dict):
                p = p["media"]
            flat.append(p)
    return flat

def extract_posts(data, hashtag):
    rows = []
    for post in _collect_candidate_posts(data):
        user = post.get("user") or post.get("owner") or {}
        username = user.get("username") or post.get("username")
        shortcode = post.get("code") or post.get("shortcode") or post.get("short_code")
        reel_url = f"https://www.instagram.com/reel/{shortcode}/" if shortcode else None
        view_count = post.get("play_count") or post.get("view_count") or post.get("video_view_count") or 0
        raw_time = post.get("taken_at") or post.get("created_at") or post.get("created_time") or post.get("timestamp") or post.get("posted_at")
        time_str = _normalize_time(raw_time)
        rows.append({
            "hashtag": hashtag,
            "username": username,
            "reel_url": reel_url,
            "view_count": view_count,
            "time": time_str,
        })
    print(f"✅ Extracted {len(rows)} posts for #{hashtag}")
    return rows

# ------------------- Main -------------------

if __name__ == "__main__":
    API_KEY = "ef3af7d866mshce861f3459cfd84p1b1569jsn52569df60d9f"

    # Config
    task = 1
    INPUT_FILE = f"byhashtag/input/input{task}.txt"
    OUTPUT_DIR = Path(f"byhashtag/output/output{task}/excel")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Read hashtags from input.txt (one per line)
    with open(INPUT_FILE, "r") as f:
        hashtags = [line.strip() for line in f if line.strip()]

    all_rows = []

    for tag in hashtags:
        print(f"Fetching #{tag} ...")
        data = fetch_hashtag_data(tag, API_KEY)
        if data:
            posts = extract_posts(data, tag)
            all_rows.extend(posts)

    if all_rows:
        df = pd.DataFrame(all_rows, columns=["hashtag", "username", "reel_url", "view_count", "time"])
        output_file = OUTPUT_DIR / f"all_hashtags_reels{task}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"✅ Data saved to {output_file} with {len(all_rows)} rows")
    else:
        print("⚠ No posts found for any hashtags.")
