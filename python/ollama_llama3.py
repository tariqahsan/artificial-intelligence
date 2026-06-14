import requests

url = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3",
    "messages": [
        {"role": "user", "content": "Hello, how are you?"}
    ]
}
response = requests.post(url, json=payload)

data = response.json()
just_content = data['message']['content']
print(just_content)
