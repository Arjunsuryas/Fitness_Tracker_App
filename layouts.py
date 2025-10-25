import streamlit as st

# Simulate the useFrameworkReady hook
def use_framework_ready():
    if "framework_ready" not in st.session_state:
        st.session_state.framework_ready = True
        # You can initialize other app-wide state here
        st.session_state.current_screen = "(tabs)"

# Define screens
def tabs_screen():
    st.title("Main Tabs")
    st.write("This is your main tab screen.")

def not_found_screen():
    st.title("404 - Not Found")
    st.write("The requested screen was not found.")

# Root layout
def root_layout():
    use_framework_ready()

    screen = st.session_state.get("current_screen", "(tabs)")

    if screen == "(tabs)":
        tabs_screen()
    elif screen == "+not-found":
        not_found_screen()
    else:
        not_found_screen()

    # Simulate navigation buttons for demonstration
    st.markdown("---")
    if st.button("Go to Tabs"):
        st.session_state.current_screen = "(tabs)"
    if st.button("Go to Not Found"):
        st.session_state.current_screen = "+not-found"

# Run app
if __name__ == "__main__":
    root_layout()
