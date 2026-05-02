import streamlit as st

# ─── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="GymGuide – Your Personal Workout Planner",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Global CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 2rem 2rem !important; max-width: 1200px !important; }

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 20px;
    padding: 3rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(229,57,53,0.25) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-size: 2.8rem; font-weight: 800;
    color: #ffffff; margin: 0 0 0.5rem 0; line-height: 1.1;
}
.hero-title span { color: #e53935; }
.hero-sub { font-size: 1.1rem; color: rgba(255,255,255,0.7); margin: 0 0 1.5rem 0; }
.hero-chips { display: flex; gap: 10px; flex-wrap: wrap; }
.chip {
    background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
    border-radius: 99px; padding: 6px 16px;
    font-size: 0.8rem; color: rgba(255,255,255,0.85); font-weight: 500;
}

/* ── Section labels ── */
.section-label {
    font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: #e53935; margin-bottom: 0.75rem;
}
.section-title {
    font-size: 1.5rem; font-weight: 700; color: #1a1a2e; margin-bottom: 1.5rem;
}

/* ── Goal cards ── */
.goal-card {
    border-radius: 16px; padding: 1.5rem;
    border: 2px solid #e8e8e8;
    cursor: pointer; transition: all 0.2s;
    background: white; height: 100%;
    text-align: center;
}
.goal-card:hover { border-color: #e53935; transform: translateY(-3px); box-shadow: 0 8px 24px rgba(229,57,53,0.15); }
.goal-card.selected { border-color: #e53935; background: #fff5f5; box-shadow: 0 8px 24px rgba(229,57,53,0.2); }
.goal-icon { font-size: 2.5rem; margin-bottom: 0.75rem; }
.goal-name { font-size: 1rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.4rem; }
.goal-desc { font-size: 0.8rem; color: #666; line-height: 1.4; }

/* ── Day pills ── */
.day-pills { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 1.5rem; }
.day-pill {
    padding: 10px 20px; border-radius: 99px;
    font-size: 0.85rem; font-weight: 600;
    border: 2px solid; cursor: pointer; transition: all 0.2s;
}
.day-pill-train { border-color: #e53935; color: #e53935; background: #fff5f5; }
.day-pill-train:hover, .day-pill-train.active { background: #e53935; color: white; }
.day-pill-rest { border-color: #4caf50; color: #4caf50; background: #f1f8e9; }
.day-pill-rest.active { background: #4caf50; color: white; }

/* ── Exercise card ── */
.ex-card {
    background: white; border-radius: 16px;
    border: 1.5px solid #f0f0f0;
    overflow: hidden; margin-bottom: 1rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    transition: box-shadow 0.2s;
}
.ex-card:hover { box-shadow: 0 6px 24px rgba(0,0,0,0.1); }
.ex-header {
    padding: 1.2rem 1.4rem 1rem 1.4rem;
    display: flex; align-items: flex-start; gap: 1rem;
    border-bottom: 1px solid #f5f5f5;
}
.ex-num {
    width: 36px; height: 36px; border-radius: 10px;
    background: #1a1a2e; color: white;
    font-size: 0.85rem; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.ex-title { font-size: 1.05rem; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
.ex-muscle { font-size: 0.78rem; color: #e53935; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.ex-body { padding: 1rem 1.4rem 1.2rem 1.4rem; }
.ex-meta-row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 1rem; }
.ex-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 12px; border-radius: 99px; font-size: 0.78rem; font-weight: 600;
}
.badge-time { background: #e3f2fd; color: #1565c0; }
.badge-sets { background: #fce4ec; color: #c62828; }
.badge-equip { background: #f3e5f5; color: #6a1b9a; }
.badge-diff { background: #e8f5e9; color: #2e7d32; }
.steps-title { font-size: 0.78rem; font-weight: 700; color: #999; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.5rem; }
.steps-list { list-style: none; padding: 0; margin: 0 0 0.75rem 0; }
.steps-list li { font-size: 0.87rem; color: #333; padding: 4px 0 4px 24px; position: relative; line-height: 1.5; }
.steps-list li::before { content: attr(data-n); position: absolute; left: 0; color: #e53935; font-weight: 700; font-size: 0.8rem; }
.tip-box {
    background: linear-gradient(135deg, #fff8e1, #fff3e0);
    border-left: 3px solid #ff9800;
    border-radius: 0 8px 8px 0;
    padding: 8px 12px; font-size: 0.82rem; color: #5d4037;
    line-height: 1.5;
}
.tip-label { font-weight: 700; color: #e65100; }

/* ── Rest day ── */
.rest-banner {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
    border-radius: 20px; padding: 3rem 2rem;
    text-align: center; border: 2px solid #a5d6a7;
}
.rest-icon { font-size: 4rem; margin-bottom: 1rem; }
.rest-title { font-size: 1.6rem; font-weight: 800; color: #1b5e20; margin-bottom: 0.5rem; }
.rest-sub { font-size: 0.95rem; color: #2e7d32; max-width: 420px; margin: 0 auto 1.5rem; line-height: 1.6; }
.rest-tips { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 480px; margin: 0 auto; }
.rest-tip-item {
    background: white; border-radius: 12px; padding: 12px;
    border: 1px solid #a5d6a7; font-size: 0.82rem; color: #2e7d32;
    text-align: left;
}
.rest-tip-item strong { display: block; font-weight: 700; margin-bottom: 2px; color: #1b5e20; }

/* ── Summary bar ── */
.summary-bar {
    background: #1a1a2e; border-radius: 16px;
    padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;
    display: flex; gap: 2rem; flex-wrap: wrap;
}
.sum-item { text-align: center; }
.sum-val { font-size: 1.4rem; font-weight: 800; color: #e53935; }
.sum-label { font-size: 0.72rem; color: rgba(255,255,255,0.6); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 600; margin-top: 2px; }

/* ── Progress tracker ── */
.week-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-bottom: 1.5rem; }
.week-cell {
    border-radius: 10px; padding: 10px 4px;
    text-align: center; border: 1.5px solid;
}
.week-cell-train { border-color: #e53935; background: #fff5f5; }
.week-cell-rest { border-color: #e0e0e0; background: #fafafa; }
.wc-day { font-size: 0.7rem; font-weight: 700; color: #999; text-transform: uppercase; margin-bottom: 4px; }
.wc-type { font-size: 0.68rem; font-weight: 700; }
.wc-type-train { color: #e53935; }
.wc-type-rest { color: #9e9e9e; }

/* Streamlit button override */
.stButton > button {
    border-radius: 99px !important;
    font-weight: 600 !important;
    border: 2px solid #e53935 !important;
    color: #e53935 !important;
    background: white !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #e53935 !important;
    color: white !important;
}

/* Divider */
.divider { border: none; border-top: 1.5px solid #f0f0f0; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ─── Data ───────────────────────────────────────────────────────────────────

GOALS = {
    "💪 Build Muscle & Strength": {
        "icon": "💪",
        "desc": "Heavy lifting, compound movements, progressive overload",
        "color": "#e53935",
        "days": {
            "Monday": "Upper Push",
            "Tuesday": "Lower A",
            "Wednesday": "Rest",
            "Thursday": "Upper Pull",
            "Friday": "Lower B",
            "Saturday": "Rest",
            "Sunday": "Rest",
        },
    },
    "🏃 General Fitness": {
        "icon": "🏃",
        "desc": "Balanced mix of strength, cardio and flexibility",
        "color": "#1565c0",
        "days": {
            "Monday": "Full Body Strength",
            "Tuesday": "Cardio & Core",
            "Wednesday": "Rest",
            "Thursday": "Full Body Strength",
            "Friday": "Cardio & Flexibility",
            "Saturday": "Active Recovery",
            "Sunday": "Rest",
        },
    },
    "🔥 Weight Loss & Toning": {
        "icon": "🔥",
        "desc": "High-intensity circuits, fat burning & body recomposition",
        "color": "#f57c00",
        "days": {
            "Monday": "HIIT & Circuits",
            "Tuesday": "Strength & Cardio",
            "Wednesday": "Rest",
            "Thursday": "HIIT & Circuits",
            "Friday": "Strength & Cardio",
            "Saturday": "Light Cardio",
            "Sunday": "Rest",
        },
    },
    "🚴 Endurance & Cardio": {
        "icon": "🚴",
        "desc": "Aerobic capacity, stamina and cardiovascular health",
        "color": "#2e7d32",
        "days": {
            "Monday": "Steady-State Cardio",
            "Tuesday": "Interval Training",
            "Wednesday": "Cross Training",
            "Thursday": "Rest",
            "Friday": "Long Cardio Session",
            "Saturday": "Recovery Cardio",
            "Sunday": "Rest",
        },
    },
    "🧘 Flexibility & Mobility": {
        "icon": "🧘",
        "desc": "Yoga, stretching, joint health and posture improvement",
        "color": "#6a1b9a",
        "days": {
            "Monday": "Yoga Flow",
            "Tuesday": "Mobility Drills",
            "Wednesday": "Rest",
            "Thursday": "Yoga Flow",
            "Friday": "Deep Stretch",
            "Saturday": "Active Mobility",
            "Sunday": "Rest",
        },
    },
}

EXERCISES = {
    "Upper Push": [
        {
            "name": "Treadmill Warm-Up",
            "muscle": "Full Body Warm-Up",
            "minutes": 10,
            "sets_reps": "10 min continuous",
            "equipment": "Treadmill",
            "difficulty": "Beginner",
            "steps": [
                "Start at a comfortable walking pace (4–5 km/h)",
                "Gradually increase to a light jog over 5 minutes",
                "Keep arms swinging naturally, breathe steadily",
                "Last 2 minutes: return to walking to transition into lifting",
            ],
            "tip": "Never skip your warm-up. 10 minutes of light cardio raises your core temperature and primes your muscles for heavier work.",
        },
        {
            "name": "Barbell Bench Press",
            "muscle": "Chest · Shoulders · Triceps",
            "minutes": 15,
            "sets_reps": "3 sets × 8–10 reps",
            "equipment": "Barbell, Bench, Rack",
            "difficulty": "Beginner",
            "steps": [
                "Lie flat on the bench, grip bar just wider than shoulder-width",
                "Unrack the bar and hold it directly above your chest",
                "Lower bar slowly to mid-chest — elbows at about 45° angle",
                "Drive the bar back up explosively until arms are extended",
                "Keep feet flat, back slightly arched, core braced throughout",
            ],
            "tip": "Start with just the barbell (20 kg) to practise form before adding weight. A spotter is highly recommended!",
        },
        {
            "name": "Dumbbell Shoulder Press",
            "muscle": "Shoulders · Triceps",
            "minutes": 12,
            "sets_reps": "3 sets × 10–12 reps",
            "equipment": "Dumbbells, Adjustable Bench",
            "difficulty": "Beginner",
            "steps": [
                "Sit on an upright bench, dumbbells at shoulder height, palms forward",
                "Press dumbbells overhead in a controlled arc until arms are straight",
                "Don't fully lock out elbows — keep a slight bend at the top",
                "Lower dumbbells slowly back to shoulder height and repeat",
            ],
            "tip": "Keep your lower back pressed into the bench. Arching excessively puts strain on your spine.",
        },
        {
            "name": "Cable Tricep Pushdown",
            "muscle": "Triceps",
            "minutes": 10,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Cable Machine, Straight or Rope Attachment",
            "difficulty": "Beginner",
            "steps": [
                "Set the cable pulley to head height and attach a straight bar or rope",
                "Grip the attachment, tuck elbows tight to your sides",
                "Push handle straight down until arms are fully extended",
                "Slowly return to start — elbows must NOT move forward or back",
            ],
            "tip": "The key is keeping elbows stationary at your sides. If they fly forward, you're using too much weight.",
        },
        {
            "name": "Dumbbell Chest Fly",
            "muscle": "Chest (Outer)",
            "minutes": 10,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Dumbbells, Flat Bench",
            "difficulty": "Beginner",
            "steps": [
                "Lie on a flat bench, hold dumbbells above chest with slight elbow bend",
                "Open arms wide in a large arc, feeling a deep chest stretch at the bottom",
                "Squeeze your chest to bring dumbbells back together at the top",
                "Maintain the slight elbow bend throughout — never fully straighten arms",
            ],
            "tip": "Think of hugging a large tree. Avoid letting the dumbbells drop too low — shoulder height is your limit.",
        },
        {
            "name": "Cool Down & Stretching",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min — hold each stretch 30s",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Chest doorway stretch: hold 30 seconds each side",
                "Tricep overhead stretch: hold 30 seconds each arm",
                "Shoulder cross-body stretch: hold 30 seconds each",
                "Seated forward fold for back and hamstrings: 60 seconds",
            ],
            "tip": "Static stretching after training improves flexibility and reduces next-day soreness. Don't rush this!",
        },
    ],
    "Lower A": [
        {
            "name": "Dynamic Warm-Up",
            "muscle": "Legs & Hips",
            "minutes": 8,
            "sets_reps": "2 rounds of circuit",
            "equipment": "None",
            "difficulty": "Beginner",
            "steps": [
                "10 × Leg swings (front-to-back) each leg",
                "10 × Hip circles each direction",
                "10 × Bodyweight squats (slow and controlled)",
                "10 × Walking lunges across the room",
            ],
            "tip": "Dynamic warm-ups activate your hip flexors and glutes — essential before heavy leg work.",
        },
        {
            "name": "Barbell Squat",
            "muscle": "Quads · Glutes · Hamstrings",
            "minutes": 18,
            "sets_reps": "3 sets × 8–10 reps",
            "equipment": "Barbell, Squat Rack",
            "difficulty": "Intermediate",
            "steps": [
                "Set bar at shoulder height in the rack; step under and rest it on your traps",
                "Feet shoulder-width apart, toes turned out slightly",
                "Take a deep breath, brace your core, then sit down and back",
                "Squat until thighs are parallel to the floor (or below)",
                "Drive through your heels to stand back up — chest stays up throughout",
            ],
            "tip": "Beginners: start with just the bar and practise the movement for 2 weeks before adding plates.",
        },
        {
            "name": "Leg Press Machine",
            "muscle": "Quads · Glutes",
            "minutes": 14,
            "sets_reps": "3 sets × 10–12 reps",
            "equipment": "Leg Press Machine",
            "difficulty": "Beginner",
            "steps": [
                "Adjust the seat so knees bend to ~90° at the bottom",
                "Place feet shoulder-width on the platform",
                "Release safety handles and lower the plate toward you in control",
                "Push through your heels until legs are nearly (not fully) extended",
                "Re-engage the safety handles between sets",
            ],
            "tip": "Perfect for beginners — the machine guides your movement so you can focus on building quad strength safely.",
        },
        {
            "name": "Romanian Deadlift (RDL)",
            "muscle": "Hamstrings · Glutes",
            "minutes": 14,
            "sets_reps": "3 sets × 10 reps",
            "equipment": "Barbell or Dumbbells",
            "difficulty": "Intermediate",
            "steps": [
                "Stand holding a bar at hip height, feet hip-width, soft knee bend",
                "Hinge at the hips — push them BACK, not down",
                "Let the bar slide down your legs until you feel a hamstring stretch",
                "Drive hips forward to return upright — squeeze glutes at the top",
                "Keep your back flat and shoulders pulled back throughout",
            ],
            "tip": "Imagine closing a car door with your bum — that hip-hinge pattern is exactly what you need.",
        },
        {
            "name": "Leg Curl Machine",
            "muscle": "Hamstrings",
            "minutes": 10,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Lying Leg Curl Machine",
            "difficulty": "Beginner",
            "steps": [
                "Lie face down, position the pad just above your heels",
                "Curl legs upward as far as possible without lifting your hips",
                "Squeeze hamstrings hard at the top for 1 second",
                "Lower slowly over 3 seconds — the eccentric phase builds the most muscle",
            ],
            "tip": "The slow lowering phase (eccentric) is where most muscle growth happens. Don't just drop the weight!",
        },
        {
            "name": "Cool Down & Stretching",
            "muscle": "Legs & Hips",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Standing quad stretch: 30 seconds each leg",
                "Seated hamstring stretch (both legs): 60 seconds",
                "Pigeon pose for glutes: 45 seconds each side",
                "Calf stretch against wall: 30 seconds each",
            ],
            "tip": "Tight hips and hamstrings are the #1 cause of lower back pain in gym-goers. Stretch every session!",
        },
    ],
    "Upper Pull": [
        {
            "name": "Rowing Machine Warm-Up",
            "muscle": "Back, Arms & Core",
            "minutes": 8,
            "sets_reps": "8 min steady pace",
            "equipment": "Rowing Machine",
            "difficulty": "Beginner",
            "steps": [
                "Strap feet in, grip the handle with an overhand grip",
                "Push with legs first, then lean back slightly, then pull arms in",
                "Reverse the sequence to return: arms extend, lean forward, legs bend",
                "Keep a consistent rhythm — aim for 20–24 strokes per minute",
            ],
            "tip": "The rowing machine warms up your entire back and arms — perfect prep for a pull day!",
        },
        {
            "name": "Lat Pulldown",
            "muscle": "Lats · Upper Back",
            "minutes": 14,
            "sets_reps": "3 sets × 10–12 reps",
            "equipment": "Lat Pulldown Machine",
            "difficulty": "Beginner",
            "steps": [
                "Sit and adjust the knee pad to secure your legs",
                "Grip the bar wider than shoulder-width, overhand grip",
                "Lean back slightly and pull bar to your upper chest",
                "Lead with your elbows — imagine tucking them into your back pockets",
                "Let the bar rise slowly with full arm extension between reps",
            ],
            "tip": "Think 'elbows to hips' not 'hands to chest'. This engages your lats far more effectively.",
        },
        {
            "name": "Seated Cable Row",
            "muscle": "Mid-Back · Lats · Rear Delts",
            "minutes": 14,
            "sets_reps": "3 sets × 10–12 reps",
            "equipment": "Cable Row Station, V-Bar or Rope",
            "difficulty": "Beginner",
            "steps": [
                "Sit with feet on the platform, slight bend in knees, back straight",
                "Grip the handle and sit tall — don't lean back excessively",
                "Pull handle toward your lower ribcage, leading with elbows",
                "Squeeze shoulder blades together firmly at the end of the pull",
                "Extend arms back out in a slow, controlled 3-second return",
            ],
            "tip": "Your torso should barely move. If you're rocking back and forth, reduce the weight.",
        },
        {
            "name": "Dumbbell Bicep Curl",
            "muscle": "Biceps",
            "minutes": 10,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Dumbbells",
            "difficulty": "Beginner",
            "steps": [
                "Stand with dumbbells at your sides, palms facing forward",
                "Curl both dumbbells up toward your shoulders simultaneously",
                "Squeeze biceps hard at the top — hold 1 second",
                "Lower slowly over 2–3 seconds back to start",
                "Don't swing your back or use momentum — control is everything",
            ],
            "tip": "You can also alternate arms for better mind-muscle connection. Either way, NEVER swing your back!",
        },
        {
            "name": "Cable Face Pull",
            "muscle": "Rear Delts · Rotator Cuff",
            "minutes": 10,
            "sets_reps": "3 sets × 15 reps",
            "equipment": "Cable Machine, Rope Attachment",
            "difficulty": "Beginner",
            "steps": [
                "Set the pulley at face height, attach the rope",
                "Grip the rope with thumbs pointing toward you, step back",
                "Pull the rope toward your face, flaring elbows out to the sides",
                "Separate the rope at the end, squeezing rear delts and rotator cuffs",
                "Return slowly to the start position",
            ],
            "tip": "The #1 shoulder health exercise. Light weight, high reps, always. Neglecting this leads to injuries down the line.",
        },
        {
            "name": "Cool Down & Stretching",
            "muscle": "Back, Shoulders & Arms",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Child's pose — 60 seconds to open up lats",
                "Cross-body shoulder stretch: 30 seconds each arm",
                "Doorway chest/bicep stretch: 30 seconds each side",
                "Seated spinal twist: 30 seconds each direction",
            ],
            "tip": "A few minutes of cool-down stretching after a pull session massively reduces next-day muscle soreness.",
        },
    ],
    "Lower B": [
        {
            "name": "Bike Warm-Up",
            "muscle": "Legs & Cardiovascular",
            "minutes": 10,
            "sets_reps": "10 min steady",
            "equipment": "Stationary Bike",
            "difficulty": "Beginner",
            "steps": [
                "Set resistance to a comfortable level (around level 3–5)",
                "Pedal at 60–80 RPM for the first 5 minutes",
                "Increase resistance slightly for the final 5 minutes",
                "Finish with 1 minute easy to prepare for lifting",
            ],
            "tip": "The bike warms up your quads, hamstrings and hips perfectly — much better than a treadmill before leg day.",
        },
        {
            "name": "Conventional Deadlift",
            "muscle": "Hamstrings · Glutes · Back · Full Body",
            "minutes": 20,
            "sets_reps": "3 sets × 6–8 reps",
            "equipment": "Barbell, Weight Plates",
            "difficulty": "Intermediate",
            "steps": [
                "Bar over mid-foot, stand hip-width apart, grip just outside legs",
                "Hinge down to grab bar: flatten back, chest up, hips above knees",
                "Take a big breath into your belly, brace your core like you're bracing for a punch",
                "Push the floor away with your legs to lift — bar stays close to your body",
                "Lock out at the top: stand tall, hips fully extended, glutes squeezed",
                "Hinge back down with control, resetting your position each rep",
            ],
            "tip": "The king of all exercises. Ask a gym staff member to check your form on your first session — it's worth it.",
        },
        {
            "name": "Walking Lunges",
            "muscle": "Quads · Glutes · Balance",
            "minutes": 12,
            "sets_reps": "3 sets × 10 reps each leg",
            "equipment": "Bodyweight or Dumbbells",
            "difficulty": "Beginner",
            "steps": [
                "Stand tall, step forward with one leg into a wide lunge",
                "Lower your back knee toward the floor — don't let it slam down",
                "Front knee should stay directly above (not past) your toes",
                "Push off your front foot and step forward with the other leg",
                "Continue 'walking' forward for 10 steps per leg",
            ],
            "tip": "Start with bodyweight before grabbing dumbbells. A long stride is key — a short stride puts more stress on the knee.",
        },
        {
            "name": "Leg Extension Machine",
            "muscle": "Quads (Isolation)",
            "minutes": 10,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Leg Extension Machine",
            "difficulty": "Beginner",
            "steps": [
                "Sit with your back against the pad, adjust so knees align with machine pivot",
                "Position the shin pad just above your feet",
                "Extend your legs upward until almost straight",
                "Hold and squeeze your quads for 1 full second at the top",
                "Lower slowly over 3 seconds — do NOT drop the weight",
            ],
            "tip": "This is an isolation exercise — medium weight with maximum squeeze beats heavy weight with no squeeze every time.",
        },
        {
            "name": "Standing Calf Raise",
            "muscle": "Calves (Gastrocnemius)",
            "minutes": 8,
            "sets_reps": "3 sets × 15–20 reps",
            "equipment": "Calf Raise Machine or Step",
            "difficulty": "Beginner",
            "steps": [
                "Stand on the edge of a step or plate with heels hanging off",
                "Rise up on your toes as high as possible",
                "Hold at the top for 1 full second — feel the contraction",
                "Lower heels BELOW the step level for a full stretch at the bottom",
                "Don't bounce — each rep should be fully controlled",
            ],
            "tip": "Calves are slow-twitch muscles that love high reps and slow, full-range movements. Bouncing up and down does nothing!",
        },
        {
            "name": "Cool Down & Stretching",
            "muscle": "Legs, Glutes & Lower Back",
            "minutes": 10,
            "sets_reps": "10 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Standing quad stretch: 30 seconds each leg",
                "Lying glute stretch (figure-four): 45 seconds each side",
                "Downward dog calf stretch: 45 seconds each leg",
                "Child's pose for lower back: 60 seconds",
            ],
            "tip": "Your legs carry you everywhere — give them the care they deserve after a tough session.",
        },
    ],
    "Full Body Strength": [
        {
            "name": "Cardio Warm-Up",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Treadmill or Bike",
            "difficulty": "Beginner",
            "steps": [
                "5 minutes on treadmill at brisk walking or light jog",
                "10 × arm circles each direction",
                "10 × bodyweight squats",
                "10 × walking lunges",
            ],
            "tip": "A general warm-up for full body days should include both lower and upper body movements.",
        },
        {
            "name": "Goblet Squat",
            "muscle": "Quads · Glutes · Core",
            "minutes": 12,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Dumbbell or Kettlebell",
            "difficulty": "Beginner",
            "steps": [
                "Hold a dumbbell vertically at your chest with both hands",
                "Feet shoulder-width apart, toes turned slightly out",
                "Squat deep — the dumbbell keeps your chest upright naturally",
                "Drive through your heels to stand back up",
            ],
            "tip": "The goblet squat is the best teaching tool for squat mechanics. Master this before moving to a barbell.",
        },
        {
            "name": "Dumbbell Romanian Deadlift",
            "muscle": "Hamstrings · Glutes",
            "minutes": 12,
            "sets_reps": "3 sets × 10 reps",
            "equipment": "Dumbbells",
            "difficulty": "Beginner",
            "steps": [
                "Hold dumbbells in front of thighs, stand hip-width apart",
                "Hinge forward at the hips, pushing them backward",
                "Lower dumbbells along your legs until you feel a hamstring stretch",
                "Drive hips forward to return upright, squeezing glutes at the top",
            ],
            "tip": "Keep the dumbbells as close to your legs as possible throughout — they should almost brush your shins.",
        },
        {
            "name": "Dumbbell Push Press",
            "muscle": "Shoulders · Triceps · Legs",
            "minutes": 12,
            "sets_reps": "3 sets × 10 reps",
            "equipment": "Dumbbells",
            "difficulty": "Beginner",
            "steps": [
                "Hold dumbbells at shoulder height, palms facing in",
                "Dip slightly at the knees, then explosively drive dumbbells overhead",
                "Fully extend arms at the top, stand tall",
                "Lower back to shoulders in a slow, controlled manner",
            ],
            "tip": "The slight leg drive makes this easier than a strict press — great for beginners building shoulder strength.",
        },
        {
            "name": "Seated Cable Row",
            "muscle": "Back · Biceps",
            "minutes": 12,
            "sets_reps": "3 sets × 12 reps",
            "equipment": "Cable Row Station",
            "difficulty": "Beginner",
            "steps": [
                "Sit tall at the cable row station, feet on platform",
                "Grip the handle and pull toward your lower ribcage",
                "Squeeze shoulder blades together at the end of each pull",
                "Extend arms slowly back to the start position",
            ],
            "tip": "Full body days benefit from compound pulling movements — this hits your back and biceps simultaneously.",
        },
        {
            "name": "Plank Hold",
            "muscle": "Core · Full Body Stability",
            "minutes": 8,
            "sets_reps": "3 sets × 30–60 seconds",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Get into a push-up position, rest on forearms instead of hands",
                "Body should form a straight line from head to heels",
                "Engage your core, squeeze your glutes, breathe normally",
                "Hold for 30 seconds (beginner) or 60 seconds (intermediate)",
            ],
            "tip": "Quality beats duration. A solid 30-second plank is far better than a sagging 90-second one.",
        },
        {
            "name": "Cool Down",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Cat-cow spinal stretch: 60 seconds",
                "Hip flexor kneeling lunge stretch: 30 seconds each side",
                "Chest doorway stretch: 30 seconds",
                "Child's pose: 60 seconds",
            ],
            "tip": "Full body workouts are tough. Take your cool-down seriously to recover faster.",
        },
    ],
    "Cardio & Core": [
        {
            "name": "Treadmill Intervals",
            "muscle": "Cardiovascular · Legs",
            "minutes": 20,
            "sets_reps": "10 × 1 min run / 1 min walk",
            "equipment": "Treadmill",
            "difficulty": "Beginner",
            "steps": [
                "Warm up 3 minutes at brisk walking pace",
                "Increase speed to a challenging jog for 1 minute",
                "Recover at walking pace for 1 minute",
                "Repeat 10 times, then cool down walking for 2 minutes",
            ],
            "tip": "Intervals burn far more calories than steady-state cardio in the same time. Push hard during the 'on' intervals!",
        },
        {
            "name": "Plank Variations",
            "muscle": "Core",
            "minutes": 10,
            "sets_reps": "3 rounds",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Standard plank hold: 30 seconds",
                "Left side plank: 20 seconds",
                "Right side plank: 20 seconds",
                "Rest 30 seconds, then repeat for 3 total rounds",
            ],
            "tip": "Side planks target your obliques — the muscles that give you a defined waist.",
        },
        {
            "name": "Dead Bug",
            "muscle": "Deep Core Stabilisers",
            "minutes": 8,
            "sets_reps": "3 sets × 10 reps each side",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Lie on your back, arms pointing up to ceiling, knees at 90° above hips",
                "Slowly lower your right arm behind your head and left leg toward floor simultaneously",
                "Keep your lower back pressed into the mat throughout",
                "Return to start, then repeat on the opposite side",
            ],
            "tip": "This is one of the safest and most effective core exercises. It teaches your spine to stay stable during limb movement.",
        },
        {
            "name": "Mountain Climbers",
            "muscle": "Core · Cardio · Shoulders",
            "minutes": 8,
            "sets_reps": "3 sets × 30 seconds",
            "equipment": "None (Floor Space)",
            "difficulty": "Beginner",
            "steps": [
                "Get into a push-up position, wrists under shoulders",
                "Drive your right knee toward your chest, then switch legs rapidly",
                "Keep your hips level — don't let them rise or sag",
                "Move as fast as you can while maintaining good form",
            ],
            "tip": "Mountain climbers double as cardio and core work. They're harder than they look — pace yourself initially.",
        },
        {
            "name": "Stretching & Cool Down",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Lying knee-to-chest stretch: 30 seconds each side",
                "Spinal twist on floor: 30 seconds each direction",
                "Cobra pose for abs: 30 seconds",
                "Happy baby pose for hips: 60 seconds",
            ],
            "tip": "After cardio and core work, your spine needs some love. Don't skip the cool-down stretches.",
        },
    ],
    "HIIT & Circuits": [
        {
            "name": "Circuit Warm-Up",
            "muscle": "Full Body",
            "minutes": 5,
            "sets_reps": "1 round easy",
            "equipment": "None",
            "difficulty": "Beginner",
            "steps": [
                "20 × jumping jacks",
                "10 × arm circles each direction",
                "10 × bodyweight squats",
                "10 × hip hinges",
            ],
            "tip": "HIIT sessions demand a proper warm-up — your heart rate and muscles need to be ready before high-intensity work.",
        },
        {
            "name": "HIIT Circuit (x4 rounds)",
            "muscle": "Full Body — Fat Burning",
            "minutes": 25,
            "sets_reps": "4 rounds, 40s work / 20s rest",
            "equipment": "None or Dumbbells",
            "difficulty": "Intermediate",
            "steps": [
                "Burpees — 40 seconds at max effort",
                "Dumbbell squat to press — 40 seconds",
                "Jump lunges (or walking lunges) — 40 seconds",
                "Push-ups — 40 seconds",
                "Rest 90 seconds between full rounds",
            ],
            "tip": "Push as hard as you can during the 40-second work intervals — that's where the fat burning happens. The rest is there for a reason!",
        },
        {
            "name": "Core Finisher",
            "muscle": "Abs · Obliques",
            "minutes": 8,
            "sets_reps": "2 rounds",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Crunches: 20 reps",
                "Bicycle crunches: 20 reps each side",
                "Leg raises: 15 reps",
                "30-second plank to finish",
            ],
            "tip": "Always finish HIIT sessions with a core finisher — your abs are already pre-fatigued from the circuit, making this extra effective.",
        },
        {
            "name": "Cool Down",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Walk slowly around the space for 2 minutes to lower heart rate",
                "Seated forward fold: 60 seconds",
                "Pigeon pose: 45 seconds each side",
                "Child's pose: 60 seconds",
            ],
            "tip": "After intense HIIT, your heart rate needs to come down gradually. Never sit or lie down immediately — keep moving gently.",
        },
    ],
    "Strength & Cardio": [
        {
            "name": "5-Minute Cardio Warm-Up",
            "muscle": "Full Body",
            "minutes": 5,
            "sets_reps": "5 min",
            "equipment": "Treadmill or Bike",
            "difficulty": "Beginner",
            "steps": [
                "Light jog or brisk walk for 5 minutes",
                "Get heart rate up to about 50–60% of your max",
                "Breathe through your nose if possible",
                "Finish with 30 seconds faster pace",
            ],
            "tip": "A brief cardio warm-up prepares your cardiovascular system for the mixed demands of this session.",
        },
        {
            "name": "Dumbbell Full Body Circuit",
            "muscle": "Full Body",
            "minutes": 20,
            "sets_reps": "3 rounds × 12 reps each",
            "equipment": "Dumbbells",
            "difficulty": "Beginner",
            "steps": [
                "Dumbbell squat × 12 reps",
                "Dumbbell bent-over row × 12 reps",
                "Dumbbell push press × 12 reps",
                "Dumbbell Romanian deadlift × 12 reps",
                "Rest 60–90 seconds between rounds",
            ],
            "tip": "Move through each exercise back-to-back with minimal rest. This keeps your heart rate elevated for a combined strength + cardio effect.",
        },
        {
            "name": "20-Min Moderate Cardio",
            "muscle": "Cardiovascular",
            "minutes": 20,
            "sets_reps": "20 min steady state",
            "equipment": "Treadmill, Bike or Elliptical",
            "difficulty": "Beginner",
            "steps": [
                "Choose a machine and set to moderate resistance/speed",
                "Work at 60–70% of max heart rate — you should be able to talk",
                "Maintain consistent pace throughout",
                "Last 2 minutes: reduce intensity to cool down",
            ],
            "tip": "The 'fat burning zone' is 60–70% of your max heart rate. Use this formula: 220 − your age = max heart rate.",
        },
        {
            "name": "Cool Down & Stretch",
            "muscle": "Full Body",
            "minutes": 8,
            "sets_reps": "8 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Standing quad stretch: 30 seconds each leg",
                "Chest stretch against wall: 30 seconds",
                "Seated hamstring stretch: 60 seconds",
                "Deep breathing: 5 slow breaths",
            ],
            "tip": "Combining strength and cardio in one session is very demanding. Prioritise sleep and protein intake on these days.",
        },
    ],
    "Light Cardio": [
        {
            "name": "Steady-State Cardio Session",
            "muscle": "Cardiovascular",
            "minutes": 30,
            "sets_reps": "30 min continuous",
            "equipment": "Treadmill, Bike, or Elliptical",
            "difficulty": "Beginner",
            "steps": [
                "Choose your preferred cardio machine",
                "Set to a comfortable, moderate pace — you should be able to hold a conversation",
                "Maintain consistent effort for 30 minutes",
                "Focus on good posture and steady breathing throughout",
            ],
            "tip": "Light cardio on active recovery days keeps your metabolism up without stressing your muscles. Perfect for a Saturday.",
        },
        {
            "name": "Gentle Full Body Stretch",
            "muscle": "Full Body Flexibility",
            "minutes": 15,
            "sets_reps": "15 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Neck rolls: 30 seconds each direction",
                "Seated forward fold: 60 seconds",
                "Lying glute stretch (figure-four): 45 seconds each side",
                "Child's pose: 60 seconds",
                "Cobra stretch: 30 seconds × 2",
            ],
            "tip": "Saturday is your chance to improve flexibility while the week's training is still fresh in your muscles. Lean into the stretches.",
        },
    ],
    "Steady-State Cardio": [
        {
            "name": "Steady-State Cardio",
            "muscle": "Cardiovascular · Endurance",
            "minutes": 40,
            "sets_reps": "40 min at zone 2",
            "equipment": "Treadmill, Bike or Elliptical",
            "difficulty": "Beginner",
            "steps": [
                "Warm up 5 minutes at easy pace",
                "Settle into Zone 2 — 60–70% max HR, conversational pace",
                "Maintain this for 30 minutes without stopping",
                "Cool down 5 minutes at easy walking pace",
            ],
            "tip": "Zone 2 cardio builds your aerobic base — the foundation of all endurance fitness. It should feel almost too easy.",
        },
        {
            "name": "Post-Cardio Stretch",
            "muscle": "Legs & Hips",
            "minutes": 10,
            "sets_reps": "10 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Standing calf stretch: 30 seconds each",
                "Hip flexor kneeling stretch: 30 seconds each",
                "IT band stretch: 30 seconds each side",
                "Child's pose: 60 seconds",
            ],
            "tip": "After long cardio sessions, your hip flexors and calves are especially tight. Give them focused attention.",
        },
    ],
    "Interval Training": [
        {
            "name": "Speed Intervals",
            "muscle": "Cardiovascular · Legs",
            "minutes": 30,
            "sets_reps": "8 × 2 min hard / 2 min easy",
            "equipment": "Treadmill or Outdoor Track",
            "difficulty": "Intermediate",
            "steps": [
                "Warm up 5 minutes at easy jog",
                "Run at 80–85% max HR for 2 minutes (hard effort)",
                "Recover at 50% max HR for 2 minutes (easy jog or walk)",
                "Repeat 8 times, then cool down 5 minutes easy",
            ],
            "tip": "Intervals are the most time-efficient way to build cardiovascular fitness. Push hard during the effort intervals — they should be uncomfortable.",
        },
        {
            "name": "Stretching",
            "muscle": "Full Body",
            "minutes": 10,
            "sets_reps": "10 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Seated hamstring stretch: 60 seconds",
                "Quad stretch standing: 30 seconds each",
                "Hip flexor stretch kneeling: 30 seconds each",
                "Spinal twist: 30 seconds each direction",
            ],
            "tip": "Never skip stretching after intervals — your muscles have been working hard at speed and need to lengthen back out.",
        },
    ],
    "Cross Training": [
        {
            "name": "Cross-Training Circuit",
            "muscle": "Full Body — Active Recovery",
            "minutes": 35,
            "sets_reps": "3 rotations",
            "equipment": "Various",
            "difficulty": "Beginner",
            "steps": [
                "10 min swimming or aqua jogging (low-impact)",
                "10 min on the rowing machine at moderate pace",
                "10 min cycling on the stationary bike",
                "5 min cool down walking",
            ],
            "tip": "Cross training gives your primary cardio muscles a break while still working your cardiovascular system. Great mid-week session.",
        },
        {
            "name": "Gentle Stretching",
            "muscle": "Full Body",
            "minutes": 10,
            "sets_reps": "10 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Cat-cow stretch: 60 seconds",
                "Chest opener stretch: 30 seconds",
                "Seated forward fold: 60 seconds",
                "Lying spinal twist: 30 seconds each side",
            ],
            "tip": "Keep this session easy — cross training days are about active recovery, not pushing your limits.",
        },
    ],
    "Long Cardio Session": [
        {
            "name": "Long Endurance Session",
            "muscle": "Cardiovascular",
            "minutes": 60,
            "sets_reps": "60 min zone 2–3",
            "equipment": "Treadmill, Bike or Elliptical",
            "difficulty": "Intermediate",
            "steps": [
                "Warm up 10 minutes at easy pace",
                "Settle into zone 2–3 (65–75% max HR) for 40 minutes",
                "Final 5 minutes: push to zone 3 (75–80% max HR)",
                "Cool down 5 minutes easy",
            ],
            "tip": "Long sessions build the aerobic base that makes everything else easier. Fuel properly beforehand with a carb-rich meal.",
        },
        {
            "name": "Full Body Cool Down",
            "muscle": "Full Body",
            "minutes": 10,
            "sets_reps": "10 min",
            "equipment": "Exercise Mat",
            "difficulty": "Beginner",
            "steps": [
                "Walk 3 minutes to lower heart rate gradually",
                "Full body stretching circuit: legs, hips, back, shoulders",
                "Deep breathing: 5 slow, controlled breaths",
                "Foam rolling if available: 2 minutes total",
            ],
            "tip": "After an hour of cardio, a thorough cool-down is essential. Hydrate well and eat a recovery meal within 30 minutes.",
        },
    ],
    "Recovery Cardio": [
        {
            "name": "Easy Recovery Walk/Jog",
            "muscle": "Cardiovascular — Light",
            "minutes": 25,
            "sets_reps": "25 min easy",
            "equipment": "Treadmill or Outdoors",
            "difficulty": "Beginner",
            "steps": [
                "Walk or very light jog at 40–50% max HR",
                "Conversation should be completely easy at this pace",
                "Focus on good posture and relaxed breathing",
                "No pushing — this is about blood flow, not fitness gains",
            ],
            "tip": "Recovery cardio flushes lactic acid from your muscles and speeds up recovery. Resist the urge to push harder!",
        },
        {
            "name": "Mobility Work",
            "muscle": "Full Body",
            "minutes": 15,
            "sets_reps": "15 min",
            "equipment": "Exercise Mat, Foam Roller",
            "difficulty": "Beginner",
            "steps": [
                "Foam roll quads, hamstrings and calves: 60 seconds each",
                "Hip 90-90 stretch: 45 seconds each side",
                "Ankle circles: 20 each direction",
                "World's greatest stretch: 5 reps each side",
            ],
            "tip": "Recovery days and mobility work are where elite athletes separate themselves from amateurs. Don't skip them!",
        },
    ],
    "Yoga Flow": [
        {
            "name": "Sun Salutation Flow",
            "muscle": "Full Body Flexibility",
            "minutes": 20,
            "sets_reps": "5 × full sun salutation",
            "equipment": "Yoga Mat",
            "difficulty": "Beginner",
            "steps": [
                "Mountain pose → Forward fold → Halfway lift",
                "Step back to plank → Lower to cobra/upward dog",
                "Push to downward dog → Hold 5 breaths",
                "Walk feet forward → Halfway lift → Forward fold → Mountain pose",
            ],
            "tip": "Sun salutations warm up your entire spine and connect movement with breath. Move slowly and intentionally.",
        },
        {
            "name": "Standing Balance Poses",
            "muscle": "Balance · Legs · Core",
            "minutes": 15,
            "sets_reps": "30–60 seconds each pose",
            "equipment": "Yoga Mat",
            "difficulty": "Beginner",
            "steps": [
                "Tree pose: 30 seconds each leg",
                "Warrior I: 45 seconds each side",
                "Warrior II: 45 seconds each side",
                "Warrior III (advanced): 20 seconds each side",
            ],
            "tip": "Fix your gaze on a still point (drishti) to improve balance. Balance gets better quickly with consistent practice.",
        },
        {
            "name": "Floor Poses & Cool Down",
            "muscle": "Hips, Hamstrings & Lower Back",
            "minutes": 15,
            "sets_reps": "60 seconds each pose",
            "equipment": "Yoga Mat",
            "difficulty": "Beginner",
            "steps": [
                "Seated forward fold (Paschimottanasana): 60 seconds",
                "Butterfly pose: 60 seconds",
                "Supine spinal twist: 45 seconds each side",
                "Savasana (rest): 3 minutes",
            ],
            "tip": "Savasana is not optional! This is when your nervous system integrates all the benefits of the practice.",
        },
    ],
    "Mobility Drills": [
        {
            "name": "Joint Mobility Circuit",
            "muscle": "Full Body Joints",
            "minutes": 25,
            "sets_reps": "2 rounds × 10 reps each",
            "equipment": "None",
            "difficulty": "Beginner",
            "steps": [
                "Neck: slow circles 10 each direction",
                "Shoulders: arm circles 10 forward, 10 backward",
                "Hips: hip circles 10 each direction",
                "Ankles: circles 10 each direction, then flexion/extension",
            ],
            "tip": "Joint mobility training increases synovial fluid in your joints — this is what keeps them healthy long-term.",
        },
        {
            "name": "Thoracic Mobility",
            "muscle": "Upper Back & Spine",
            "minutes": 15,
            "sets_reps": "2 rounds",
            "equipment": "Foam Roller, Mat",
            "difficulty": "Beginner",
            "steps": [
                "Thoracic extension over foam roller: 2 minutes",
                "Thread-the-needle stretch: 45 seconds each side",
                "Cat-cow: 10 slow reps",
                "Open book rotation: 10 each side",
            ],
            "tip": "Most people have very poor thoracic (upper back) mobility from sitting at desks. This will transform your posture over time.",
        },
    ],
    "Deep Stretch": [
        {
            "name": "Full Body Deep Stretch",
            "muscle": "All Major Muscle Groups",
            "minutes": 45,
            "sets_reps": "Hold each 60–90 seconds",
            "equipment": "Yoga Mat, Straps (optional)",
            "difficulty": "Beginner",
            "steps": [
                "Hip flexor kneeling lunge stretch: 90 seconds each",
                "Pigeon pose (glutes): 90 seconds each side",
                "Seated hamstring stretch with strap: 90 seconds",
                "Doorway chest stretch: 60 seconds",
                "Supine spinal twist: 60 seconds each side",
                "Child's pose: 2 minutes to finish",
            ],
            "tip": "Never force deep stretches. Breathe into areas of tension and allow the muscle to relax over 60–90 seconds — rushing defeats the purpose.",
        },
    ],
    "Active Mobility": [
        {
            "name": "Active Mobility Flow",
            "muscle": "Full Body",
            "minutes": 40,
            "sets_reps": "Continuous flow",
            "equipment": "Yoga Mat",
            "difficulty": "Beginner",
            "steps": [
                "5 min foam rolling: target tight areas",
                "10 min joint circles: neck, shoulders, hips, ankles",
                "10 min yoga flow: sun salutations at slow pace",
                "10 min deep stretching: focus on areas worked this week",
                "5 min breathing: box breathing (4s in, 4s hold, 4s out, 4s hold)",
            ],
            "tip": "Saturday active mobility sessions are one of the best habits you can build. They compound over months into exceptional flexibility and joint health.",
        },
    ],
}

REST_TIPS = [
    ("💤", "Sleep 7–9 hours", "This is when muscle is built and hormones reset."),
    ("🥩", "Eat enough protein", "Aim for 1.6–2g per kg of bodyweight daily."),
    ("💧", "Stay hydrated", "Drink at least 2–3 litres of water today."),
    ("🚶", "Light walk outside", "20–30 minutes of fresh air aids recovery."),
    ("📖", "Visualise your goals", "Review your plan and track your progress."),
    ("🛁", "Contrast shower", "Alternating hot/cold water reduces muscle soreness."),
]

# ─── Session state ───────────────────────────────────────────────────────────
if "goal" not in st.session_state:
    st.session_state.goal = None
if "day" not in st.session_state:
    st.session_state.day = None

# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">💪 Gym<span>Guide</span></div>
    <div class="hero-sub">Your personalised workout planner — choose your goal, pick your day, and train with confidence.</div>
    <div class="hero-chips">
        <span class="chip">✅ Beginner friendly</span>
        <span class="chip">⏱ Time per exercise</span>
        <span class="chip">🏋️ Equipment listed</span>
        <span class="chip">📋 Step-by-step guides</span>
        <span class="chip">💡 Pro tips included</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Step 1: Goal Selection ───────────────────────────────────────────────────
st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What is your fitness goal?</div>', unsafe_allow_html=True)

goal_names = list(GOALS.keys())
cols = st.columns(len(goal_names))
for i, (col, g) in enumerate(zip(cols, goal_names)):
    with col:
        data = GOALS[g]
        selected_cls = "selected" if st.session_state.goal == g else ""
        st.markdown(f"""
        <div class="goal-card {selected_cls}">
            <div class="goal-icon">{data['icon']}</div>
            <div class="goal-name">{g.split(' ', 1)[1]}</div>
            <div class="goal-desc">{data['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Select", key=f"goal_{i}"):
            st.session_state.goal = g
            st.session_state.day = None
            st.rerun()

# ─── Step 2: Day Selection ────────────────────────────────────────────────────
if st.session_state.goal:
    goal_data = GOALS[st.session_state.goal]
    schedule = goal_data["days"]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 2</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">Select your training day</div>', unsafe_allow_html=True)

    # Week overview grid
    week_html = '<div class="week-grid">'
    day_abbrevs = {"Monday": "MON", "Tuesday": "TUE", "Wednesday": "WED",
                   "Thursday": "THU", "Friday": "FRI", "Saturday": "SAT", "Sunday": "SUN"}
    for day, session in schedule.items():
        is_rest = session == "Rest"
        cell_cls = "week-cell-rest" if is_rest else "week-cell-train"
        type_cls = "wc-type-rest" if is_rest else "wc-type-train"
        label = "REST" if is_rest else session.upper()[:8]
        week_html += f'<div class="week-cell {cell_cls}"><div class="wc-day">{day_abbrevs[day]}</div><div class="wc-type {type_cls}">{label}</div></div>'
    week_html += '</div>'
    st.markdown(week_html, unsafe_allow_html=True)

    # Day buttons
    day_cols = st.columns(len(schedule))
    for i, (day, session) in enumerate(schedule.items()):
        with day_cols[i]:
            is_rest = session == "Rest"
            label = f"😴 {day[:3]}" if is_rest else f"🏋️ {day[:3]}"
            if st.button(label, key=f"day_{i}"):
                st.session_state.day = day
                st.rerun()

# ─── Step 3: Workout Display ──────────────────────────────────────────────────
if st.session_state.goal and st.session_state.day:
    goal_data = GOALS[st.session_state.goal]
    schedule = goal_data["days"]
    selected_day = st.session_state.day
    session_name = schedule[selected_day]

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 3 — Your Workout</div>', unsafe_allow_html=True)

    if session_name == "Rest":
        # Rest day
        rest_cards = ""
        for icon, title, desc in REST_TIPS:
            rest_cards += f'<div class="rest-tip-item"><strong>{icon} {title}</strong>{desc}</div>'

        st.markdown(f"""
        <div class="rest-banner">
            <div class="rest-icon">🛌</div>
            <div class="rest-title">Rest & Recovery Day</div>
            <div class="rest-sub">
                Muscles grow during rest, not during the workout itself.
                Today is just as important as your training days — use it wisely.
            </div>
            <div class="rest-tips">{rest_cards}</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        exercises = EXERCISES.get(session_name, [])
        if not exercises:
            st.info(f"Exercises for **{session_name}** are coming soon!")
        else:
            total_min = sum(e["minutes"] for e in exercises)
            total_ex = len([e for e in exercises if "Cool Down" not in e["name"] and "Warm" not in e["name"]])

            # Header
            st.markdown(f"""
            <div style="margin-bottom: 1rem;">
                <h2 style="font-size:1.6rem;font-weight:800;color:#1a1a2e;margin-bottom:4px;">
                    {selected_day} — {session_name}
                </h2>
                <p style="color:#666;font-size:0.9rem;">{st.session_state.goal}</p>
            </div>
            """, unsafe_allow_html=True)

            # Summary bar
            st.markdown(f"""
            <div class="summary-bar">
                <div class="sum-item"><div class="sum-val">{total_min} min</div><div class="sum-label">Total Duration</div></div>
                <div class="sum-item"><div class="sum-val">{total_ex}</div><div class="sum-label">Working Exercises</div></div>
                <div class="sum-item"><div class="sum-val">{sum(e['minutes'] for e in exercises if 'Warm' in e['name'])} min</div><div class="sum-label">Warm-Up</div></div>
                <div class="sum-item"><div class="sum-val">{sum(e['minutes'] for e in exercises if 'Cool' in e['name'])} min</div><div class="sum-label">Cool Down</div></div>
            </div>
            """, unsafe_allow_html=True)

            # Exercise cards
            for idx, ex in enumerate(exercises):
                steps_html = "".join(f'<li data-n="{i+1}">{s}</li>' for i, s in enumerate(ex["steps"]))

                # Color badges based on type
                is_warmup = "Warm" in ex["name"] or "Cool" in ex["name"]
                num_bg = "#4caf50" if "Cool" in ex["name"] else ("#1565c0" if is_warmup else "#1a1a2e")

                st.markdown(f"""
                <div class="ex-card">
                    <div class="ex-header">
                        <div class="ex-num" style="background:{num_bg};">{idx+1}</div>
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
                        <div class="tip-box"><span class="tip-label">💡 Tip: </span>{ex['tip']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<hr class='divider'>
<div style="text-align:center;padding:1rem 0 0.5rem;font-size:0.8rem;color:#aaa;">
    GymGuide — Built as a personal fitness companion. Always consult a professional before starting a new exercise programme.
</div>
""", unsafe_allow_html=True)
