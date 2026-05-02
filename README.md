# 💪 GymGuide — Interactive Workout Planner

A personalised, interactive gym guide built with Streamlit.

## Features
- 5 fitness goals: Muscle & Strength, General Fitness, Weight Loss, Endurance, Flexibility
- 7-day weekly schedule per goal
- Every exercise includes: duration (minutes), sets/reps, equipment needed, step-by-step guide & tips
- Rest day guidance with recovery tips
- Beautiful, mobile-friendly UI

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How to Deploy on Streamlit Community Cloud (Free)

1. Push this folder to a GitHub repository
2. Go to https://share.streamlit.io
3. Sign in with GitHub
4. Click "New app" → select your repo → set `app.py` as the main file
5. Click "Deploy" — your app will be live in ~2 minutes!

## File Structure
```
gym_guide/
├── app.py            ← Main Streamlit application
├── requirements.txt  ← Python dependencies
└── README.md         ← This file
```
