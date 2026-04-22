from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

client = create_client(url, key)

def sign_up(email, password):
    return client.auth.sign_up({
        "email": email,
        "password": password
    })

def sign_in(email, password):
    return client.auth.sign_in_with_password({
        "email": email,
        "password": password
    })