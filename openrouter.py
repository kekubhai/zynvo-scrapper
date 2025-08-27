import requests
import json
import os
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
    "Content-Type": "application/json",
#    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "perplexity/sonar",
    "messages": [
      {
        "role": "user",
        "content": 
            "You are an expert news researcher who tracks everything happening in Indian colleges. "
            "Your task is to provide the **latest Indian college news** that is:\n"
            "1. General updates – official news, events, fests, academic changes, policy updates.\n"
            "2. Fun updates – quirky incidents, student festivals, viral campus trends, unique activities.\n"
            "3. Controversial updates – protests, political clashes, student union elections, college demands, strikes.\n"
            "4. Insider or less-reported updates – rumors, gossip, hidden talks from campus forums, "
            "student confessions, underground movements, issues not covered by mainstream media.\n\n"
            "Instructions:\n"
            "- Make the results **timely, relevant, and categorized** (General, Fun, Controversial, Insider).\n"
            "- Include both **mainstream reports (from DU Beat, Campus Varta, Campus Reporter, EdexLive, Telegraph Edugraph, etc.)** "
            "and **hidden/viral chatter (from anonymous forums, Reddit, or student confessions)**.\n"
            "- Summarize each story clearly with: { 'title': '...', 'category': '...', 'summary': '...', 'source': '...', 'date': '...' }\n"
            "- Ensure the focus is **Indian colleges only**.\n"
            "- If exact sources are unavailable, infer possible campus trends and controversies based on ongoing social/political/academic contexts.\n\n"
            "Output in structured JSON format."
      }
    ],
    
  })
)
data=response.json()
if(data==None):
  print('Response is None')
  exit(1)
  with open('response_data.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
      print('Response saved to response_data.json')