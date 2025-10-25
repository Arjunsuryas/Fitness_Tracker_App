import streamlit as st
from dataclasses import dataclass

# Food dataclass
@dataclass
class Food:
    name: str
    calories: float
    protein: float
    carbs: float
    fat: float
    quantity: float
    unit: str
    mealType: str  # breakfast, lunch, dinner, snack

# Helper functions
def get_meal_icon(meal_type: str) -> str:
    icons = {
        "breakfast": "🥞",
        "lunch": "🍽️",
        "dinner": "🍽️",
        "snack": "🍎"
    }
    return icons.get(meal_type, "🍽️")

def format_meal_type(meal_type: str) -> str:
    return meal_type.capitalize()

# Render FoodCard
def food_card(food: Food, on_click=None):
    icon = get_meal_icon(food.mealType)
    card_html = f"""
    <div style="
        display: flex;
        align-items: center;
        padding: 12px;
        margin: 6px 0;
        border-radius: 12px;
        background-color: #f9f9f9;
        cursor: pointer;
    ">
        <div style="font-size: 24px; margin-right: 12px;">{icon}</div>
        <div>
            <div style="font-weight: bold;">{food.name}</div>
            <div style="font-size: 12px; color: #555;">
                {format_meal_type(food.mealType)} | {food.calories} kcal | {food.quantity} {food.unit}
            </div>
        </div>
    </div>
    """
    if on_click:
        if st.button(f"{food.name} Details"):
            on_click()
    else:
        st.markdown(card_html, unsafe_allow_html=True)

# Example usage
example_food = Food(
    name="Oatmeal",
    calories=150,
    protein=5,
    carbs=27,
    fat=3,
    quantity=1,
    unit="bowl",
    mealType="breakfast"
)

def show_food_details():
    st.write("Showing detailed food info...")

food_card(example_food, on_click=show_food_details)
