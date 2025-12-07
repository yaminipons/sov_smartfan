import json
from collections import Counter

BRANDS = ["Atomberg", "Crompton", "Havells", "Usha"]

def calculate_sov():
    try:
        with open("google_search_results.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("❌ google_search_results.json not found or unreadable.")
        return

    if not data:
        print("❌ JSON is empty. Run google_search_collector.py first.")
        return

    brand_counts = Counter()

    for entry in data:
        text = (entry.get("title", "") + " " + entry.get("snippet", "")).lower()

        for brand in BRANDS:
            if brand.lower() in text:
                brand_counts[brand] += 1

    # Print raw counts
    print("\n📊 Brand Mentions Count:")
    for brand in BRANDS:
        print(f"   {brand}: {brand_counts.get(brand, 0)}")

    total_mentions = sum(brand_counts.values())

    if total_mentions == 0:
        print("\n⚠️ No brand mentions found.")
        return

    print("\n📈 Share of Voice (SoV):")
    for brand in BRANDS:
        count = brand_counts.get(brand, 0)
        sov = (count / total_mentions) * 100 if total_mentions else 0
        print(f"   {brand}: {sov:.2f}%")

    print("\n✅ SoV calculation completed.")

if __name__ == "__main__":
    calculate_sov()
