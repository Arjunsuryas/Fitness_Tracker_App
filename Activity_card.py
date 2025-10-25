import streamlit as st
from dataclasses import dataclass

# Define the Activity type
@dataclass
class Activity:
    id: str
    type: str
    name: str
    duration_minutes: int
    distance_km: float

# Function to get activity icon
def get_activity_icon(activity_type: str) -> str:
    icons = {
        "run": "🏃‍♂️",
        "walk": "🚶‍♂️",
        "cycle": "🚴‍♂️",
        "swim": "🏊‍♂️",
        "yoga": "🧘‍♀️",
        "workout": "💪",
    }
    return icons.get(activity_type, "❓")

# Function to render Activity Card
def activity_card(activity: Activity, on_click=None):
    icon = get_activity_icon(activity.type)
    card_html = f"""
    <div style="
        display: flex;
        align-items: center;
        padding: 12px;
        margin: 6px 0;
        border-radius: 12px;
        background-color: #f0f0f0;
        cursor: pointer;
    ">
        <div style="font-size: 24px; margin-right: 12px;">{icon}</div>
        <div>
            <div style="font-weight: bold;">{activity.name}</div>
            <div style="font-size: 12px; color: #555;">
                Duration: {activity.duration_minutes} min | Distance: {activity.distance_km} km
            </div>
        </div>
    </div>
    """
    if on_click:
        if st.button(f"{activity.name} Details", key=activity.id):
            on_click()
    else:
        st.markdown(card_html, unsafe_allow_html=True)

# Example usage
example_activity = Activity(
    id="1",
    type="run",
    name="Morning Run",
    duration_minutes=30,
    distance_km=5.0
)

def show_activity_details():
    st.write("Showing detailed activity info...")

activity_card(example_activity, on_click=show_activity_details)
