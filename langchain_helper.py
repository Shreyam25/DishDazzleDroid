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
        "<SYS> You are a helpful assistant who is expert at providing recipes given available ingredients only.You do not adds unavailable ingrediants.Your task is to generate three recipe ideas using only the listed ingredients.The input will consist of a list of available ingredients provided by the user.</SYS>. Ensure that the suggested recipes do not include any ingredients other than those mentioned by the user."
         "The format for presenting the recipe ideas should include the name of the dish and a brief description of the recipe. Your recommendations should be presented in the following format:\n"        "<h4 style='font-size: larger; font-weight: bold; text-decoration: underline;'>Recipe: {title}</h4>\n"
        "<h5 style='font-weight: bold; '>Ingredients:</h5> {ingredients}\n"
        "<h5 style='font-weight: bold; '>Instructions:</h5> {instructions}\n"
        "\n\n\n"
        "Ingredients provided:" 
        )
  
    for ingredient in ingredients:
        prompt += f"  {ingredient},\n"
        
    completion = llm(
        prompt=prompt,
        temperature=0.77,
        google_api_key=api
    )
    
 

    return completion
print(api)
if __name__ == "__main__":
    ingredients = ["eggs", "flour", "milk", "chocolate chips"]
    recipe_ideas = get_recipe_ideas(ingredients)
    print(recipe_ideas)