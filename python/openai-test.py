from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "can you explain list of python?"}
  ]
)

print(completion.choices[0].message);
