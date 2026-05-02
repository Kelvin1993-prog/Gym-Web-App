import streamlit as st
from data import GOALS


def render_goal_selector() -> None:
    """Render the goal selection cards (Step 1)."""
    st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">What is your fitness goal?</div>',
        unsafe_allow_html=True,
    )

    goal_names = list(GOALS.keys())
    cols = st.columns(len(goal_names))

    for col, goal_key in zip(cols, goal_names):
        data = GOALS[goal_key]
        selected_cls = "selected" if st.session_state.goal == goal_key else ""

        with col:
            st.markdown(
                f"""
                <div class="goal-card {selected_cls}">
                    <div class="goal-icon">{data['icon']}</div>
                    <div class="goal-name">{goal_key.split(' ', 1)[1]}</div>
                    <div class="goal-desc">{data['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Select", key=f"goal_{goal_key}"):
                st.session_state.goal = goal_key
                st.session_state.day = None
                st.rerun()
