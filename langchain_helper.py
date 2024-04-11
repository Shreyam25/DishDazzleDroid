import streamlit.web.cli as stcli
import streamlit as st

from langchain.llms import GooglePalm
# Access the secret key from the environment
from dotenv import load_dotenv
import os

load_dotenv()

api = st.secrets["API"]

llm= GooglePalm(temperature=0.01,google_api_key=api)

def get_recipe_ideas(ingredients):
    prompt = (
        "[INST] <<SYS>> You are a helpful assistant who is expert at providing recipes given available ingredients only. Tom is a person who has only {ingrdiants} available at home and he is very hungry and he cant go to market to buy more ingrediants <</SYS>>.Your task is to generate some recipe ideas using only the {ingredients} so that Tom will make some food.The input will consist of a list of available ingredients provided by the user.</SYS>. Ensure that the suggested recipes do not include any ingredients other than those mentioned by the user. "
         "The format for presenting the recipe ideas should include the name of the dish and a brief description of the recipe. Your recommendations should be presented in the following format:\n"        "<h4 style='font-size: larger; font-weight: bold; text-decoration: underline;'>Recipe: {title}</h4>\n"
        "<h5 style='font-weight: bold; '>Ingredients:</h5> {ingredients}\n"
        "<h5 style='font-weight: bold; '>Instructions:</h5> {instructions}\n"
        "\n\n\n [/INST]"
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
