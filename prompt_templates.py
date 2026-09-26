import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5 
)
topic=input("enter the topic which you want to understand ")
prompt=PromptTemplate.from_template(
    "Explain {topic} in simple words"
)
formatted_prompt=prompt.format(topic=topic)
response=llm.invoke(formatted_prompt)
print(response.content)