from secrets_1 import OPEN_AI_KEY
import os 
os.environ['OPENAI_API_KEY']=OPEN_AI_KEY

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
llm=OpenAI(temperature= 0.6)
food_style_prompt=PromptTemplate(input_variables=['cuisine'],
                                 template="I want to open restaurant for {cuisine} food. Suggest a unique name for this.")
chain =LLMChain( llm=llm, prompt=food_style_prompt)
chain.run("Indian")