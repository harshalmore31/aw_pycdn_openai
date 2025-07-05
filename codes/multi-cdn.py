import os
from dotenv import load_dotenv
import pycdn

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY", "demo-key-for-testing")

# Initialize PyCDN (enables both classic and natural syntax)
cdn = pycdn.pkg("https://685e19a20010ac4f850e.fra.appwrite.run/")
print("✅ PyCDN connected")

from cdn.openai import OpenAI
client = OpenAI(api_key=api_key)

print("💬 Chat with the model (type 'exit' or 'quit' to stop):")
while True:
    user = input("You: ")
    if user.strip().lower() in ("exit", "quit"):
        print("👋 Bye!")
        break
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user}]
    )
    print("🤖 Model:", response.choices[0].message.content.strip())