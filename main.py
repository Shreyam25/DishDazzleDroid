import streamlit as st
import  langchain_helper
def main():
    st.title("DishDazzleDroid")
    st.subtitle("Dazzling dishes at your fingertips!")



    # Initialize session state
    if "ingredients_list" not in st.session_state:
        st.session_state.ingredients_list = []

    # Text input for the user to enter an ingredient
    ingredient_input = st.text_input("Enter an ingredient:")

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
    if st.button("Get Recipes"):
        if st.session_state.ingredients_list:
            # Call function to generate recipe recommendations
            recommendations =  langchain_helper.get_recipe_ideas(st.session_state.ingredients_list)
            
            # Display recommendations
            if recommendations:
                st.subheader("Recommended Recipes")
                st.write(recommendations)
            else:
                st.write("No recipes found for the provided ingredients. Try adding different ingredients.")
        else:
            st.warning("Please select some ingredients to get recipe recommendations.")
if __name__ == "__main__":
    main()
