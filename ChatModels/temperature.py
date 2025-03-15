from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=2)

result = model.invoke("Write a 5 line poem on Football")

print(result.content)