from fastapi import FastAPI
from supabase import create_client, Client
import os
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins =[
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
TABLE_NAME = 'indian_college_news'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def root():
    return {"message": "Indian College News API is running!"}

@app.get("/news")
def get_news():
    response = supabase.table(TABLE_NAME).select("*").execute()
    # response.data contains the rows
    return {"news": response.data}
