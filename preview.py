"""
📌 YouTube Scraper – Project Preview (Python + Selenium)

🔍 DESCRIPTION:
This tool scrapes both YouTube videos and channels using **Selenium** without an API key.
It can:
    ✅ Search YouTube by keyword and extract multiple video details
    ✅ Scrape direct video URLs for full metadata
    ✅ Scrape channel pages (via /about) for name, handle, subscriber count, etc.
    ✅ Export everything into clean CSV files

🎬 Demo Video: https://youtu.be/u4PV3uRqpR0

💼 Custom Scraping Services or Full Source Code:
📩 Email: isubhanali3@gmail.com
💬 Discord: s.a3
💻 Upwork: https://www.upwork.com/freelancers/~01b6c1b6819be875f2?mp_source=share
"""

# ▶️ VIDEO SCRAPER MODULE
# -----------------------
# Inputs: search term or direct video URL
# Output: For each video, saves:
#     - Title
#     - Views
#     - Likes
#     - Comments count
#     - Upload date
#     - Duration (converted from PT1M30S → 1m 30s)
#     - Full description
#     - URL

# ▶️ CHANNEL SCRAPER MODULE
# --------------------------
# Inputs: YouTube channel URL or auto-extracted from video page
# Output: For each channel, saves:
#     - Channel Name
#     - Handle (@username)
#     - Subscribers
#     - Join Date
#     - Total Videos
#     - URL

# 📂 CSV OUTPUT FILES:
# - `output/video_data.csv`
# - `output/channel_data.csv`

# ⚙️ CLI USAGE EXAMPLES (after buying full version):
# python main.py --mode video --search "ai video editing" --limit 3
# python main.py --mode video --url https://youtube.com/watch?v=XYZ
# python main.py --mode channel --url https://youtube.com/@example/about

# 🧠 Built with:
# - Python 3.10+
# - Selenium (headless Chrome)
# - CSV module
# - Argparse for command-line support

# 👀 For a working preview, check the demo:
# https://youtu.be/u4PV3uRqpR0

print("👋 This file is just a preview of what the YouTube Scraper project does.")
print("▶️ To see it in action, watch the demo video: https://youtu.be/u4PV3uRqpR0")
print("📩 For full code or custom scrapers, email: isubhanali3@gmail.com")
