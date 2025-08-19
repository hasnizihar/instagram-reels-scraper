import requests
import pandas as pd
import datetime
import json

# Instagram Scraper for Reels

inputdata=open("byusername/input/input1.txt", "r").read()
for username in inputdata.split():
    print(username)

    # API request details
    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/reels"
    querystring = {"username_or_id_or_url": username}  # change to target username

    headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=querystring)

    # Print raw response for debugging
    print("Raw API Response:")
    print(json.dumps(response.json(), indent=2))

    data = response.json()

    # Adjust based on actual JSON structure
    reels_list = data.get("data", {}).get("items", [])  # many APIs put reels in data -> items

    reels_data = []
    for item in reels_list:
        posted_time = datetime.datetime.fromtimestamp(item.get("taken_at")).strftime('%Y-%m-%d %H:%M:%S') if item.get("taken_at") else None
        reels_data.append({
            "Posted Time": posted_time,
            "Views": item.get("play_count"),
            "username": username,
            "Reel URL": f"https://www.instagram.com/reel/{item.get('code', '')}/"
        })

    df = pd.DataFrame(reels_data)
    df.to_excel(f"byusername/output/output1/excel/instagram_reels_{username}.xlsx", index=False)

    print(f"Saved {len(df)} reels to byusername/output/output1/excel/instagram_reels_{username}.xlsx")


print("All data processed and saved successfully.")