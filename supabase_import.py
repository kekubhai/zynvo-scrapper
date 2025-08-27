import json
from supabase import create_client, Client
import os

# Load JSON data from file
with open('indian_college_news.json', 'r', encoding='utf-8') as f:
    news_data = json.load(f)

# Supabase credentials (set these in your environment or replace directly)
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception('Supabase credentials not set. Please set SUPABASE_URL and SUPABASE_KEY environment variables.')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Table name
TABLE_NAME = 'indian_college_news'

# Insert data
if isinstance(news_data, list):
    for item in news_data:
        response = supabase.table(TABLE_NAME).insert(item).execute()
        print(response)
else:
    response = supabase.table(TABLE_NAME).insert(news_data).execute()
    print(response)

print('Data imported to Supabase Postgres table:', TABLE_NAME)
