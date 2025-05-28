from secrets_1 import OPEN_AI_KEY
import os 
from langchain.llms import openai
llm=openai()
os.environ['OPENAI_API_KEY']=OPEN_AI_KEY
name=llm("Fast car")
print(name)