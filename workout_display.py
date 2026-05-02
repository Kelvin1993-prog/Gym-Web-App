import streamlit as st
from data import EXERCISES


def _render_summary_bar(exercises: list) -> None:
    """Render the dark stats bar at the top of a session."""
    total_min   = sum(e["minutes"] for e in exercises)
    working_ex  = len([e for e in exercises if "Cool Down" not in e["name"] and "Warm" not in e["name"]])
    warmup_min  = sum(e["minutes"] for e in exercises if "Warm" in e["name"])
    cooldown_min = sum(e["minutes"] for e in exercises if "Cool" in e["name"])

    st.markdown(
        f"""
        <div class="summary-bar">
            <div class="sum-item">
                <div class="sum-val">{total_min} min</div>
                <div class="sum-label">Total Duration</div>
            </div>
            <div class="sum-item">
                <div class="sum-val">{working_ex}</div>
                <div class="sum-label">Working Exercises</div>
            </div>
            <div class="sum-item">
                <div class="sum-val">{warmup_min} min</div>
                <div class="sum-label">Warm-Up</div>
            </div>
            <div class="sum-item">
                <div class="sum-val">{cooldown_min} min</div>
                <div class="sum-label">Cool Down</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_exercise_card(idx: int, ex: dict) -> None:
    """Render a single exercise card."""
    steps_html = "".join(
        f'<li data-n="{i + 1}">{step}</li>'
        for i, step in enumerate(ex["steps"])
    )

    is_cooldown = "Cool" in ex["name"]
    is_warmup   = "Warm" in ex["name"]
    num_bg = "#4caf50" if is_cooldown else ("#1565c0" if is_warmup else "#1a1a2e")

    st.markdown(
        f"""
        <div class="ex-card">
            <div class="ex-header">
                <div class="ex-num" style="background:{num_bg};">{idx + 1}</div>
                <div>
                    <div class="ex-title">{ex['name']}</div>
                    <div class="ex-muscle">{ex['muscle']}</div>
                </div>
            </div>
            <div class="ex-body">
                <div class="ex-meta-row">
                    <span class="ex-badge badge-time">⏱ {ex['minutes']} minutes</span>
                    <span class="ex-badge badge-sets">🔁 {ex['sets_reps']}</span>
                    <span class="ex-badge badge-equip">🏋️ {ex['equipment']}</span>
                    <span class="ex-badge badge-diff">⭐ {ex['difficulty']}</span>
                </div>
                <div class="steps-title">How to do it</div>
                <ul class="steps-list">{steps_html}</ul>
                <div class="tip-box">
                    <span class="tip-label">💡 Tip: </span>{ex['tip']}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_workout(session_name: str, goal_label: str, day: str) -> None:
    """Render the full workout section for a given session."""
    exercises = EXERCISES.get(session_name)

    if not exercises:
        st.info(f"Exercises for **{session_name}** are coming soon!")
        return

    # Session heading
    st.markdown(
        f"""
        <div style="margin-bottom: 1rem;">
            <h2 style="font-size:1.6rem;font-weight:800;color:#1a1a2e;margin-bottom:4px;">
                {day} — {session_name}
            </h2>
            <p style="color:#666;font-size:0.9rem;">{goal_label}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _render_summary_bar(exercises)

    for idx, ex in enumerate(exercises):
        _render_exercise_card(idx, ex)
