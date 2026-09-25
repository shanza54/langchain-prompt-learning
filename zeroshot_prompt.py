import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)
prompt="""Classify the following movie review as positive or negative.

Review:
"The movie was amazing. The acting was excellent and the story was interesting."

Answer:"""
response=llm.invoke(prompt)
print(response.content)
