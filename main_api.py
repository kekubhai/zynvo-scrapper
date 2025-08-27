from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
TABLE_NAME = 'indian_college_news'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/news")
def get_news():
    response = supabase.table(TABLE_NAME).select("*").execute()
    # response.data contains the rows
    return {"news": response.data}
