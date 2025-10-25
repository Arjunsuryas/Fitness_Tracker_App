import streamlit as st

def not_found_screen():
    st.title("Oops!")
    st.write("This screen doesn't exist.")
    
    if st.button("Go to home screen!"):
        st.session_state.current_screen = "home"

# Example home screen for navigation
def home_screen():
    st.title("Home Screen")
    st.write("Welcome to the home screen!")

# Root layout to simulate routing
def root_layout():
    if "current_screen" not in st.session_state:
        st.session_state.current_screen = "not_found"

    screen = st.session_state.current_screen

    if screen == "home":
        home_screen()
    else:
        not_found_screen()

if __name__ == "__main__":
    root_layout()
