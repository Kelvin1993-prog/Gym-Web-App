import streamlit as st
from data import REST_TIPS


def render_rest_day() -> None:
    """Render the rest day banner with recovery tips."""
    tip_cards_html = "".join(
        f'<div class="rest-tip-item"><strong>{icon} {title}</strong>{desc}</div>'
        for icon, title, desc in REST_TIPS
    )
    st.markdown(
        f"""
        <div class="rest-banner">
            <div class="rest-icon">🛌</div>
            <div class="rest-title">Rest & Recovery Day</div>
            <div class="rest-sub">
                Muscles grow during rest, not during the workout itself.
                Today is just as important as your training days — use it wisely.
            </div>
            <div class="rest-tips">{tip_cards_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
