
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

try:
    response = supabase.table("seeds").select("*").limit(10).execute()

    print("Successfully connected to seeds table!")
    print("Number of records:", len(response.data))
    print("Seed data:", response.data)

except Exception as e:
    print("Database error:", e)
