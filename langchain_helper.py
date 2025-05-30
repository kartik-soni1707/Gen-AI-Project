from secrets_1 import OPEN_AI_KEY
import os 
os.environ['OPENAI_API_KEY']=OPEN_AI_KEY

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def generate_restaurant_name_and_items(cuisine):
    llm=OpenAI(temperature= 0.7)
    food_style_prompt=PromptTemplate(input_variables=['cuisine'],
                                    template="I want to open restaurant for {cuisine} food. Suggest one unique name for this.")
    menu_item_prompt=PromptTemplate(input_variables=['restaurant'],
                                    template="Generate 5 dish names for the {restaurant}. Return it as a comma separated list (dont list it)")
    name_chain = food_style_prompt|llm
    menu_chain = menu_item_prompt|llm
    restaurant= name_chain.invoke({"cuisine":cuisine})
    food_items= menu_chain.invoke({"restaurant":restaurant})
   
    return {"restaurant_name": restaurant, "menu_items":food_items}
