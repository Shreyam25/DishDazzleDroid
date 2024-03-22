import streamlit as st
import langchain_helper
import json,re
def display_recipe(title, ingredients, instructions):
    st.write(f"**{title}**")
    st.write("Ingredients:")
    for ingredient in ingredients:
        st.write(f"* {ingredient}")
    st.write("Instructions:")
    for i, instruction in enumerate(instructions, start=1):
        st.write(f"{i}. {instruction}")
# Set background image using custom CSS
page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://i.pinimg.com/564x/d5/08/a4/d508a4e9a881ee0bd23e09dc5d1893e4.jpg");
  background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])  # Adjust the width ratio as needed
with col1:
    st.markdown(
    f"""
    <style>
    .circular-logo {{
        width: 140px;
        height: 140px;
        border-radius: 50%;
        overflow: hidden;
    }}
    .circular-logo img {{
        object-fit: cover; /* Ensures the image covers the circular container */
        width: 100%;
        height: 100%;
    }}
    </style>
    <div class="circular-logo">
        <img src="https://i.pinimg.com/564x/52/3b/a3/523ba330168bc643f9c52f181a0f58c5.jpg">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.title("DishDazzleDroid")
    st.subheader("Dazzling dishes at your fingertips!")
    st.write("**D3 is your recipe recommendation bot. Just tell us your available ingredients, and we'll suggest delicious recipes in seconds. Say hello to effortless meal planning with DishDazzleDroid!**\n\n")
def main():
 

    # Initialize session state
    if "ingredients_list" not in st.session_state:
        st.session_state.ingredients_list = []

    # Text input for the user to enter an ingredient
    ingredient_input = st.text_input("**Enter an ingredients:**")

    # Button to add the entered ingredient to the list
    if st.button("Add") or (ingredient_input and st.session_state.last_button_clicked == "Enter"):
        if ingredient_input:
            st.session_state.ingredients_list.append(ingredient_input)
            st.session_state.last_button_clicked = "Add"  # Set the last button clicked
            ingredient_input = ""  # Reset the text input field after adding ingredient

    # Display the list of all ingredients
    st.write("**All Ingredients List:**")
    for ingredient in st.session_state.ingredients_list:
        st.write("-", ingredient)
    
    # Button to get recipe recommendations
    if st.button("Get Recipes"):
        if st.session_state.ingredients_list:
            # Call function to generate recipe recommendations
            a=  langchain_helper.get_recipe_ideas(st.session_state.ingredients_list)
            print(a)
            if a:
                st.subheader("Recommended Recipes")
                st.markdown(a,unsafe_allow_html=True)
        
            else:
                st.write("No recipes found for the provided ingredients. Try adding different ingredients.")
        else:
            st.warning("Please select some ingredients to get recipe recommendations.")

if __name__ == "__main__":
    main()
