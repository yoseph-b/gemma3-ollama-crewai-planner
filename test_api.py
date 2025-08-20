import requests
import json

# Test the API key directly
api_key = "sk-or-v1-e2fc52d6c1e5b363f0ea88762146001dcab8c970a236f358888f942c6ca29f8"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Test with a simple completion request
data = {
    "model": "openrouter/deepseek/deepseek-r1",
    "messages": [
        {"role": "user", "content": "Hello, this is a test."}
    ],
    "max_tokens": 50
}

try:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        print("✅ API key is working!")
    else:
        print("❌ API key is not working")
        
except Exception as e:
    print(f"Error: {e}") 