<h1 align="center">📸 Instagram Reels Scraper</h1>
<p align="center">
  A simple Python tool to fetch <b>Instagram Reels metadata</b> (views, time, URLs) and export to Excel 📊
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
  <img src="https://img.shields.io/badge/Output-Excel%20(.xlsx)-orange.svg">
  <img src="https://img.shields.io/github/stars/hasnizihar/instagram-reels-scraper?style=social">
</p>

A simple **Python script** to scrape **Instagram Reels metadata** (posted time, views, username, reel URL) for one or more accounts using the **RapidAPI Instagram Scraper API**.  

The script reads usernames or hashtags from a text file, fetches reels data, and saves the results to **Excel files**.
## 🎯 Purpose
<p align="justify">
This project is designed to help developers, researchers, and social media analysts quickly fetch and organize <b>Instagram Reels metadata</b> (posted time, views, and URLs) into Excel files for easier analysis and reporting.  
It saves time, automates repetitive tasks, and provides structured data for insights or research purposes.
</p>

---
## 🚀 Features
- 🔍 Fetches Instagram Reels metadata (username, views, time, URL)  
- 📂 Handles multiple usernames from one file  
- 📊 Saves results in clean **Excel (.xlsx)** format  
- 🛠️ Auto-creates input/output folders  
- ⚡ Fast, modular, and error-handled code  

---
## 📂 Project Structure


```

instagram-reels-scraper/
├── byhashtag/
│   ├── input/
│   │   └── input1.txt
│   └── output/
│       └── output1/
│           └── excel/
│
├── byusername/
│   ├── input/
│   │   └── input1.txt
│   └── output/
│       └── output1/
│           └── excel/
│
├── LICENSE
├── README.md
├── scraper-V1.0.py
├── scraper-V2.0.py
└── scraper-V3.0.py

```
---
## 🛠️ Requirements
- Python **3.8+**
- [Requests](https://pypi.org/project/requests/)  
- [Pandas](https://pypi.org/project/pandas/)  
- [OpenPyXL](https://pypi.org/project/openpyxl/) (Excel support)

## 🔌 API Details
This project uses the **Instagram Scraper API** from [RapidAPI](https://rapidapi.com/).  
It fetches Instagram Reels metadata such as posted time, views, and reel URLs.

---
##  Install dependencies:
```bash
pip install requests pandas openpyxl
````

---

## 📖 Usage Guide

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/instagram-reels-scraper.git
   cd instagram-reels-scraper
   ```

2. Add Instagram usernames/hashtag to an input file (e.g., `input/input1.txt`):

   ```
   username1
   username2
   username3
   ```

3. Run the script:

   ```bash
   scraper-V2.0.py
   ```

4. Find results in:

   ```
   output/output1/excel/
   ```

Each username gets its own Excel file:

```
instagram_reels_username1.xlsx
instagram_reels_username2.xlsx
...
```

---

## ⚙️ Configuration

At the top of the script, you can change the task input/output:

```python
task = 1   # change input/output set
INPUT_FILE = f"input/input{task}.txt"
OUTPUT_DIR = Path(f"output/output{task}/excel")
```

* `task = 1` → uses `input/input1.txt` and saves results in `output/output1/excel/`.
* Change the task number for different batches of usernames.

---

## 🔑 API Key

This project uses the [Instagram Scraper API](https://rapidapi.com/) from **RapidAPI**.
Replace the placeholder key in the script with your own:

```python
HEADERS = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
}
```

---

## 📊 Sample Output

Example row in the Excel file:

| Username | Posted Time      | Views  | Reel URL                                                                         |
| -------- | ---------------- | ------ | -------------------------------------------------------------------------------- |
| testuser | 2025-08-16 14:23 | 12,345 | [https://www.instagram.com/reel/ABC123/](https://www.instagram.com/reel/ABC123/) |

---
## 📝 Roadmap
- [ ] 📦 Save all usernames into a single Excel file  
- [ ] 🖥️ Add CLI arguments for input/output  
- [ ] 📷 Extend support for posts & stories  
- [ ] 🐳 Add Docker support for deployment  


## ⚠️ Disclaimer

This tool is built for **educational and research purposes**.
Use responsibly and comply with Instagram’s **Terms of Service**.
The author is **not responsible** for misuse.

---

## 👨‍💻 Author
 **Hasni Zihar**

 https://www.hasnizihar.com

---

⭐ If you find this useful, **give it a star** on GitHub!

Do you want me to also **add usage examples with screenshots of Excel output** for better GitHub presentation?
#
