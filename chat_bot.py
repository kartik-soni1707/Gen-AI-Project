from secrets_1 import OPEN_AI_KEY
import os 
os.environ['OPENAI_API_KEY']=OPEN_AI_KEY

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
llm=OpenAI(temperature= 0.7)
food_style_prompt=PromptTemplate(input_variables=['cuisine'],
                                 template="I want to open restaurant for {cuisine} food. Suggest one unique name for this.")
chain = food_style_prompt|llm
response= chain.invoke({"cuisine":"INdian"})
print(response)