This project collects Google search results for the keyword “smart fan” and calculates how much each brand (Atomberg, Havells, Crompton, Bajaj, etc.) is mentioned.
This helps understand which brand has the highest Share of Voice (SoV) on Google.

📌 **What This Project Does**

Searches Google using SerpAPI

Collects the top search results (title, link, snippet, position)

Checks how many times each brand appears

Calculates Share of Voice (SoV) → which brand is talked about the most

Saves results in JSON and CSV files

⚙️ **How to Set Up**
1. Install the required libraries
pip install -r requirements.txt

2. Add your SerpAPI key

Open google_search_collector.py and paste your API key:

SERP_API_KEY = "your_key_here"

▶️ **How to Run the Project**
Step 1 — Collect Google search results
python google_search_collector.py

This will create:

google_search_results.json

google_search_results.csv

Step 2 — Calculate SoV
python sov_calculator.py

This will print:

Brand mentions

Share of Voice (%)


📊 **Example Output**
Brand Mentions:
Atomberg: 1
Havells: 1
Crompton: 1
Usha: 0

Share of Voice:
Atomberg — 33.33%
Havells — 33.33%
Crompton — 33.33%
Usha — 0.00%


🛠️ **Tools Used**

Python

SerpAPI

Pandas

TextBlob (Sentiment analysis)

NLTK
