import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
# =======================
# Configurations
# =======================
load_dotenv()
API_KEY = os.getenv("PERPLEXITY_API_KEY")  # set in your environment
if not API_KEY:
    raise ValueError("Please set the PERPLEXITY_API_KEY environment variable.")

API_URL = "https://api.perplexity.ai/chat/completions"

PROMPT = """
You are a specialist news aggregator monitoring happenings in Indian colleges. 
Provide the **latest Indian college news**, inclusive of:
1. General updates – events, fests, academic changes, announcements.
2. Fun news – quirky incidents, viral student trends.
3. Controversial events – protests, strikes, student politics, campus demands.
4. Insider or less reported news – rumors, underground movements, hidden campus chatter.

Categorize each item under:
- General, Fun, Controversial, Insider

Present each item in JSON format as:
{{
  "title": "...",
  "category": "...",
  "summary": "...",
  "source": "...",
  "date": "YYYY-MM-DD"
}}

Deliver the output as a JSON array. If exact sources are limited, infer possible college topics based on recent social or academic context.
"""

# =======================
# API Request
# =======================
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": PROMPT}
    ],
    "stream": False,
    "enable_search_classifier": True   # triggers web search when needed :contentReference[oaicite:1]{index=1}
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {API_KEY}"
}

response = requests.post(API_URL, json=payload, headers=headers)
response.raise_for_status()
data = response.json()

# =======================
# Parse Response
# =======================
# Assuming the API returns a standard GPT-like response
# with 'choices' → first choice → 'message' → 'content'
content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
if not content:
    raise ValueError("Empty content returned from API.")

# Attempt to parse JSON array from content
try:
    parsed = json.loads(content)
    if not isinstance(parsed, list):
        raise ValueError("Expected JSON array.")
except json.JSONDecodeError as e:
    print("Failed to parse API response as JSON:")
    print(content)
    raise e

# =======================
# Save to file
# =======================
OUTPUT_FILE = "indian_college_news.json"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

print(f"Success: Saved {len(parsed)} items to '{OUTPUT_FILE}' at {datetime.now().isoformat()}.")
