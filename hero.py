import streamlit as st


def render_hero() -> None:
    """Render the top hero banner."""
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">💪 Gym<span>Guide</span></div>
            <div class="hero-sub">
                Your personalised workout planner — choose your goal, pick your day,
                and train with confidence.
            </div>
            <div class="hero-chips">
                <span class="chip">✅ Beginner friendly</span>
                <span class="chip">⏱ Time per exercise</span>
                <span class="chip">🏋️ Equipment listed</span>
                <span class="chip">📋 Step-by-step guides</span>
                <span class="chip">💡 Pro tips included</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
