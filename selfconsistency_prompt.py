import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)
prompt = """
A store has 20 apples.
It sells 7 apples and then receives 5 more.

How many apples does the store have?
"""

for i in range(3):
    response = llm.invoke(prompt)
    print(f"Attempt {i + 1}:")
    print(response.content)
    print()