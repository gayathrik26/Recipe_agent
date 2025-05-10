import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client(api key)  # Replace with your actual key

# Function to generate recipes
def get_recipe(ingredients):
    response = co.generate(
        model='command-r-plus',
        prompt=f'Give me a recipe using {ingredients}.',
        max_tokens=500
    )
    return response.generations[0].text.strip()

# Streamlit UI
st.title("AI Recipe Generator 🍽️")

ingredients = st.text_input("Enter the ingredients (comma-separated):")

if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Cooking up your recipe..."):
            recipe = get_recipe(ingredients)
        st.subheader("Here's a recipe suggestion:")
        st.text_area("Recipe", recipe, height=300)
    else:
        st.warning("Please enter some ingredients first.")
