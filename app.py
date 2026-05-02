"""
GymGuide — Interactive Workout Planner
======================================
Entry point. This file is intentionally thin — it only handles:
  1. Page config
  2. Session state initialisation
  3. Injecting global CSS
  4. Calling the component renderers in order
"""

import streamlit as st

from styles import MAIN_CSS
from data import GOALS
from components import (
    render_hero,
    render_goal_selector,
    render_day_selector,
    render_rest_day,
    render_workout,
)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GymGuide – Your Personal Workout Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Session state defaults ────────────────────────────────────────────────────
if "goal" not in st.session_state:
    st.session_state.goal = None
if "day" not in st.session_state:
    st.session_state.day = None

# ── Step 1: Hero ──────────────────────────────────────────────────────────────
render_hero()

# ── Step 2: Goal selector ─────────────────────────────────────────────────────
render_goal_selector()

# ── Step 3: Day selector (only if a goal has been chosen) ─────────────────────
if st.session_state.goal:
    render_day_selector()

# ── Step 4: Workout / Rest day display ────────────────────────────────────────
if st.session_state.goal and st.session_state.day:
    goal_key  = st.session_state.goal
    day       = st.session_state.day
    schedule  = GOALS[goal_key]["days"]
    session   = schedule[day]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 3 — Your Workout</div>', unsafe_allow_html=True)

    if session == "Rest":
        render_rest_day()
    else:
        render_workout(session_name=session, goal_label=goal_key, day=day)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <hr class='divider'>
    <div style="text-align:center;padding:1rem 0 0.5rem;font-size:0.8rem;color:#aaa;">
        GymGuide — Built as a personal fitness companion.
        Always consult a professional before starting a new exercise programme.
    </div>
    """,
    unsafe_allow_html=True,
)
