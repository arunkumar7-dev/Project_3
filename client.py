from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)

