from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


def insert_data(df, user_email):
    data = df.to_dict(orient="records")

    # adiciona usuário em cada linha
    for row in data:
        row["user_email"] = user_email

    response = supabase.table("sales_raw").insert(data).execute()

    return response