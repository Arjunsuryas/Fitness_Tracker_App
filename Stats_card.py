import streamlit as st

def stats_card(title: str, value: str, unit: str, icon_html: str, colors: list[str]):
    """
    Displays a stats card with gradient background.
    :param title: The title of the stat
    :param value: The value of the stat
    :param unit: The unit of the value
    :param icon_html: HTML string for the icon
    :param colors: List of two colors for gradient
    """
    gradient = f"linear-gradient(90deg, {colors[0]}, {colors[1]})"
    card_html = f"""
    <div style="
        display: flex;
        align-items: center;
        padding: 16px;
        border-radius: 16px;
        margin: 4px;
        background: {gradient};
        color: white;
        font-family: sans-serif;
    ">
        <div style="margin-right: 16px;">{icon_html}</div>
        <div>
            <div style="font-size: 14px; opacity: 0.8;">{title}</div>
            <div style="display: flex; align-items: baseline;">
                <div style="font-size: 24px; font-weight: bold; margin-right: 4px;">{value}</div>
                <div style="font-size: 14px;">{unit}</div>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


# Example usage
stats_card(
    title="Steps",
    value="12,345",
    unit="steps",
    icon_html="👣",
    colors=["#4c669f", "#3b5998"]
)
