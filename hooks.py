import streamlit as st

def use_framework_ready():
    """
    Simulates a framework initialization hook.
    """
    if "framework_ready_called" not in st.session_state:
        st.session_state.framework_ready_called = True
        # Call the "framework ready" callback if defined
        if "framework_ready_callback" in st.session_state:
            callback = st.session_state.framework_ready_callback
            if callable(callback):
                callback()

# Example usage
def on_framework_ready():
    st.write("Framework is ready!")

st.session_state.framework_ready_callback = on_framework_ready

use_framework_ready()
