import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)
prompt = """
A student has 5 hours available to study.
They spend 2 hours studying Python and 1 hour studying mathematics.

Work through the calculation step by step and determine how many hours remain.

Answer:
"""

response = llm.invoke(prompt)

print(response.content)