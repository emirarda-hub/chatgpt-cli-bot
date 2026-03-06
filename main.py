import requests
import json
import os

print("How can I help you?")

API_KEY = os.getenv("OPENAI_API_KEY")

def chat_gpt_bot(message):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "temperature": 1,
        "max_completion_tokens": 100,
        "messages": [
            {
                "role": "developer",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]


while True:
    message = input("> ")
    print(chat_gpt_bot(message))