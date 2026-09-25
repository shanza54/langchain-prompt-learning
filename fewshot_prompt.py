import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

prompt = """
Here are few examples of classifying emotions in statements:

            Statement: 'I just won my first marathon!'
            Emotion: Joy

            Statement: 'I can't believe I lost my keys again.'
            Emotion: Frustration

            Statement: 'My best friend is moving to another country.'
            Emotion: Sadness

            Now, classify the emotion in the following statement:
            Statement: 'That movie was so scary I had to cover my eyes.
"""

response = llm.invoke(prompt)

print(response.content)