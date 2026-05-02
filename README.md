#  GymGuide — Interactive Workout Planner

A modular, interactive gym guide built with Streamlit.

## Project Structure

```
gymguide/
├── app.py                      ← Entry point (thin orchestration only)
├── requirements.txt
├── README.md
│
├── data/                       ← Pure data — no UI code
│   ├── __init__.py
│   ├── goals.py                ← 5 fitness goals + weekly schedules
│   ├── exercises.py            ← All exercise definitions (name, time, steps, tips)
│   └── rest_tips.py            ← Rest day recovery tips
│
├── components/                 ← UI building blocks (one concern per file)
│   ├── __init__.py
│   ├── hero.py                 ← Top banner
│   ├── goal_selector.py        ← Step 1: goal cards
│   ├── day_selector.py         ← Step 2: week grid + day buttons
│   ├── rest_day.py             ← Rest day banner + tips
│   └── workout_display.py      ← Step 3: summary bar + exercise cards
│
└── styles/                     ← All CSS in one place
    ├── __init__.py
    └── css.py                  ← MAIN_CSS string injected via st.markdown
```

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to Deploy on Streamlit Community Cloud (Free)

1. Push this folder to a **GitHub repository**
2. Go to **https://share.streamlit.io**
3. Sign in with GitHub
4. Click **"New app"** → select your repo → set `app.py` as the main file
5. Click **"Deploy"** — live in ~2 minutes at `https://yourname-gymguide.streamlit.app`

## Adding New Exercises

Edit `data/exercises.py` and add a new session key with a list of exercise dicts:

```python
"My New Session": [
    {
        "name": "Exercise Name",
        "muscle": "Target Muscles",
        "minutes": 12,
        "sets_reps": "3 sets × 10 reps",
        "equipment": "Dumbbells",
        "difficulty": "Beginner",
        "steps": ["Step 1", "Step 2", "Step 3"],
        "tip": "Your coaching tip here.",
    },
]
```

## Adding a New Goal

Edit `data/goals.py` to add a new goal key, then map each day to a session name
that exists in `data/exercises.py`.
