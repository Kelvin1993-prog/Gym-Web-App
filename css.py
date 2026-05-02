MAIN_CSS = """
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

/* ── Week overview grid ── */
.week-grid { display: grid; grid-template-columns: repeat(7,1fr); gap: 6px; margin-bottom: 1.5rem; }
.week-cell { border-radius: 10px; padding: 10px 4px; text-align: center; border: 1.5px solid; }
.week-cell-train { border-color: #e53935; background: #fff5f5; }
.week-cell-rest  { border-color: #e0e0e0; background: #fafafa; }
.wc-day  { font-size: 0.7rem; font-weight: 700; color: #999; text-transform: uppercase; margin-bottom: 4px; }
.wc-type { font-size: 0.68rem; font-weight: 700; }
.wc-type-train { color: #e53935; }
.wc-type-rest  { color: #9e9e9e; }

/* ── Summary bar ── */
.summary-bar {
    background: #1a1a2e; border-radius: 16px;
    padding: 1.2rem 1.5rem; margin-bottom: 1.5rem;
    display: flex; gap: 2rem; flex-wrap: wrap;
}
.sum-item  { text-align: center; }
.sum-val   { font-size: 1.4rem; font-weight: 800; color: #e53935; }
.sum-label { font-size: 0.72rem; color: rgba(255,255,255,0.6); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 600; margin-top: 2px; }

/* ── Exercise card ── */
.ex-card {
    background: white; border-radius: 16px;
    border: 1.5px solid #f0f0f0;
    overflow: hidden; margin-bottom: 1rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    transition: box-shadow 0.2s;
}
.ex-card:hover { box-shadow: 0 6px 24px rgba(0,0,0,0.10); }
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
.ex-title  { font-size: 1.05rem; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
.ex-muscle { font-size: 0.78rem; color: #e53935; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.ex-body   { padding: 1rem 1.4rem 1.2rem 1.4rem; }

/* ── Exercise meta badges ── */
.ex-meta-row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 1rem; }
.ex-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 12px; border-radius: 99px; font-size: 0.78rem; font-weight: 600;
}
.badge-time  { background: #e3f2fd; color: #1565c0; }
.badge-sets  { background: #fce4ec; color: #c62828; }
.badge-equip { background: #f3e5f5; color: #6a1b9a; }
.badge-diff  { background: #e8f5e9; color: #2e7d32; }

/* ── Steps ── */
.steps-title { font-size: 0.78rem; font-weight: 700; color: #999; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.5rem; }
.steps-list  { list-style: none; padding: 0; margin: 0 0 0.75rem 0; }
.steps-list li { font-size: 0.87rem; color: #333; padding: 4px 0 4px 24px; position: relative; line-height: 1.5; }
.steps-list li::before { content: attr(data-n); position: absolute; left: 0; color: #e53935; font-weight: 700; font-size: 0.8rem; }

/* ── Tip box ── */
.tip-box {
    background: linear-gradient(135deg, #fff8e1, #fff3e0);
    border-left: 3px solid #ff9800;
    border-radius: 0 8px 8px 0;
    padding: 8px 12px; font-size: 0.82rem; color: #5d4037; line-height: 1.5;
}
.tip-label { font-weight: 700; color: #e65100; }

/* ── Rest day ── */
.rest-banner {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
    border-radius: 20px; padding: 3rem 2rem;
    text-align: center; border: 2px solid #a5d6a7;
}
.rest-icon  { font-size: 4rem; margin-bottom: 1rem; }
.rest-title { font-size: 1.6rem; font-weight: 800; color: #1b5e20; margin-bottom: 0.5rem; }
.rest-sub   { font-size: 0.95rem; color: #2e7d32; max-width: 420px; margin: 0 auto 1.5rem; line-height: 1.6; }
.rest-tips  { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 480px; margin: 0 auto; }
.rest-tip-item {
    background: white; border-radius: 12px; padding: 12px;
    border: 1px solid #a5d6a7; font-size: 0.82rem; color: #2e7d32; text-align: left;
}
.rest-tip-item strong { display: block; font-weight: 700; margin-bottom: 2px; color: #1b5e20; }

/* ── Streamlit button overrides ── */
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

/* ── Divider ── */
.divider { border: none; border-top: 1.5px solid #f0f0f0; margin: 1.5rem 0; }
</style>
"""
