import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Check environment variables
print("MODEL_PROVIDER:", os.getenv("MODEL_PROVIDER"))
print("MODEL_NAME:", os.getenv("MODEL_NAME"))
print("OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))

# Check if API key exists
api_key = os.getenv("OPENROUTER_API_KEY")
if api_key:
    print("✅ API key found:", api_key[:20] + "..." + api_key[-4:])
else:
    print("❌ No API key found") 