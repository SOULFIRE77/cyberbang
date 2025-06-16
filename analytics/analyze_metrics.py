import os
import pandas as pd
from supabase import create_client

# Скрипт для базовой аналитики
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_activity():
    resp = supabase.table("users").select("*").execute()
    users = pd.DataFrame(resp.data)
    # Пример: retention, distribution баланса
    print(users.head())

if __name__ == "__main__":
    get_user_activity()
