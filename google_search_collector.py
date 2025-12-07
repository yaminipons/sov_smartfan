import json
import csv
from serpapi import GoogleSearch
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
# ---------------------------------------------
# CONFIG
# ---------------------------------------------
SERP_API_KEY = os.getenv("SERP_API_KEY")
  # Put your key here
QUERY = "smart fan"
RESULTS_LIMIT = 20


def google_search_collector():
    print(f"\n🔍 Searching Google for: '{QUERY}' ...\n")

    params = {
        "engine": "google",
        "q": QUERY,
        "api_key": SERP_API_KEY,
        "google_domain": "google.com",
        "gl": "in",               # Change region if needed
        "hl": "en",
        "num": 10,
        "start": 0
    }


    # Send search request
    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract organic results
    organic = results.get("organic_results", [])

    print(f"📌 Found {len(organic)} results.\n")

    data = []

    for r in organic:
        entry = {
            "title": r.get("title"),
            "snippet": r.get("snippet"),
            "link": r.get("link"),
            "position": r.get("position"),
            "date_collected": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(entry)

        print(f"{r.get('position')}. {r.get('title')}")
        print(f"   🔗 {r.get('link')}")
        print()

    # ---------------------------------------------
    # SAVE TO JSON
    # ---------------------------------------------
    json_filename = "google_search_results.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # ---------------------------------------------
    # SAVE TO CSV
    # ---------------------------------------------
    csv_filename = "google_search_results.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Results saved to:\n   📄 {json_filename}\n   📄 {csv_filename}")


if __name__ == "__main__":
    google_search_collector()
