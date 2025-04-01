import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.environ.get("API_KEY"),
)
prompt = input("Enter your quary: ")
text = f'you are a finaancial expert ai assestant. you task is to provide and insightful to the folling user query related to finance: {prompt} for any other topic , respond with I,Don\'t Know'
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": text,
        }
    ],
    model="deepseek-r1-distill-llama-70b",
)

print(chat_completion.choices[0].message.content)