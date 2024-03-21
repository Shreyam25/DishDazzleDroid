import streamlit.web.cli as stcli

from langchain.llms import GooglePalm
# Access the secret key from the environment
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("API")

llm= GooglePalm(temperature=0.23,google_api_key=api)

def get_recipe_ideas(ingredients):
    prompt = (
        "Based on the provided ingredients, suggest 3 delicious recipe ideas in the following format:"
        "Ingredients provided:"
    )
    
    for ingredient in ingredients:
        prompt += f"  {ingredient},\n"
        
    completion = llm(
        prompt=prompt,
        temperature=0.33,
        google_api_key=api
    )
    
 

    return completion
print(api)
if __name__ == "__main__":
    ingredients = ["eggs", "flour", "milk", "chocolate chips"]
    recipe_ideas = get_recipe_ideas(ingredients)
    print(recipe_ideas)