import streamlit as st
from data import GOALS

DAY_ABBREVS = {
    "Monday": "MON", "Tuesday": "TUE", "Wednesday": "WED",
    "Thursday": "THU", "Friday": "FRI", "Saturday": "SAT", "Sunday": "SUN",
}


def render_week_grid(schedule: dict) -> None:
    """Render the 7-cell week overview strip."""
    cells_html = ""
    for day, session in schedule.items():
        is_rest = session == "Rest"
        cell_cls = "week-cell-rest" if is_rest else "week-cell-train"
        type_cls = "wc-type-rest" if is_rest else "wc-type-train"
        label = "REST" if is_rest else session.upper()[:8]
        cells_html += (
            f'<div class="week-cell {cell_cls}">'
            f'<div class="wc-day">{DAY_ABBREVS[day]}</div>'
            f'<div class="wc-type {type_cls}">{label}</div>'
            f"</div>"
        )
    st.markdown(
        f'<div class="week-grid">{cells_html}</div>',
        unsafe_allow_html=True,
    )


def render_day_selector() -> None:
    """Render the day selection section (Step 2)."""
    if not st.session_state.goal:
        return

    schedule = GOALS[st.session_state.goal]["days"]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 2</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">Select your training day</div>',
        unsafe_allow_html=True,
    )

    render_week_grid(schedule)

    day_cols = st.columns(len(schedule))
    for col, (day, session) in zip(day_cols, schedule.items()):
        with col:
            is_rest = session == "Rest"
            label = f"😴 {day[:3]}" if is_rest else f"🏋️ {day[:3]}"
            if st.button(label, key=f"day_{day}"):
                st.session_state.day = day
                st.rerun()
