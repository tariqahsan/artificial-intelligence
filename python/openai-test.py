from openai import OpenAI

client = OpenAI(
  api_key=""your openai secret api key""
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "can you explain list of python?"}
  ]
)

print(completion.choices[0].message);
