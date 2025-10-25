import streamlit as st

def progress_bar(title: str, current: float, target: float, unit: str, colors: list[str]):
    """
    Displays a progress bar with gradient fill.
    """
    percentage = min((current / target) * 100, 100)
    gradient = f"linear-gradient(to right, {colors[0]}, {colors[1]})"

    bar_html = f"""
    <div style="margin-bottom: 12px;">
        <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 4px;">
            <div>{title}</div>
            <div>{current} / {target} {unit}</div>
        </div>
        <div style="
            position: relative;
            height: 24px;
            background-color: #e0e0e0;
            border-radius: 12px;
            overflow: hidden;
        ">
            <div style="
                width: {percentage}%;
                height: 100%;
                background: {gradient};
                border-radius: 12px 0 0 12px;
            "></div>
            <div style="
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                color: black;
            ">
                {round(percentage)}%
            </div>
        </div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

# Example usage
progress_bar(
    title="Calories Burned",
    current=450,
    target=600,
    unit="kcal",
    colors=["#4c669f", "#3b5998"]
)
