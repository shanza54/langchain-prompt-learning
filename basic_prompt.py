import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)
prompts=["The wind is",
         "Once upon a time in a distant galaxy",
         "The benefits of sustainable energy include"]
for prompt in prompts:
    response=llm.invoke(prompt)
    print(response.content)