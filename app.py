import time

import requests
import streamlit as st


API_URL = "http://127.0.0.1:5000/predict"

st.set_page_config(
    page_title="Student Outcome Predictor",
    layout="wide",
    initial_sidebar_state="collapsed",
)


THEMES = {
    "light": {
        "bg": "#f6f7fb",
        "bg_alt": "#eef2ff",
        "surface": "rgba(255, 255, 255, 0.86)",
        "surface_strong": "#ffffff",
        "surface_soft": "#f8fafc",
        "border": "rgba(15, 23, 42, 0.10)",
        "ink": "#0f172a",
        "muted": "#64748b",
        "muted_strong": "#475569",
        "accent": "#111827",
        "accent_2": "#2563eb",
        "accent_3": "#7c3aed",
        "button_text": "#ffffff",
        "success": "#047857",
        "success_bg": "#ecfdf5",
        "danger": "#b42318",
        "danger_bg": "#fff1f2",
        "shadow": "0 24px 70px rgba(15, 23, 42, 0.10)",
        "shadow_soft": "0 14px 38px rgba(15, 23, 42, 0.07)",
        "nav": "rgba(255, 255, 255, 0.78)",
    },
    "dark": {
        "bg": "#080b12",
        "bg_alt": "#111827",
        "surface": "rgba(15, 23, 42, 0.76)",
        "surface_strong": "#111827",
        "surface_soft": "#0f172a",
        "border": "rgba(226, 232, 240, 0.13)",
        "ink": "#f8fafc",
        "muted": "#94a3b8",
        "muted_strong": "#cbd5e1",
        "accent": "#f8fafc",
        "accent_2": "#60a5fa",
        "accent_3": "#a78bfa",
        "button_text": "#08111f",
        "success": "#34d399",
        "success_bg": "rgba(6, 95, 70, 0.22)",
        "danger": "#fb7185",
        "danger_bg": "rgba(127, 29, 29, 0.24)",
        "shadow": "0 24px 70px rgba(0, 0, 0, 0.38)",
        "shadow_soft": "0 14px 38px rgba(0, 0, 0, 0.28)",
        "nav": "rgba(8, 11, 18, 0.78)",
    },
}


def inject_design_system(theme_name):
    theme = THEMES[theme_name]
    st.markdown(
        f"""
        <style>
            :root {{
                --bg: {theme["bg"]};
                --bg-alt: {theme["bg_alt"]};
                --surface: {theme["surface"]};
                --surface-strong: {theme["surface_strong"]};
                --surface-soft: {theme["surface_soft"]};
                --border: {theme["border"]};
                --ink: {theme["ink"]};
                --muted: {theme["muted"]};
                --muted-strong: {theme["muted_strong"]};
                --accent: {theme["accent"]};
                --accent-2: {theme["accent_2"]};
                --accent-3: {theme["accent_3"]};
                --button-text: {theme["button_text"]};
                --success: {theme["success"]};
                --success-bg: {theme["success_bg"]};
                --danger: {theme["danger"]};
                --danger-bg: {theme["danger_bg"]};
                --shadow: {theme["shadow"]};
                --shadow-soft: {theme["shadow_soft"]};
                --nav: {theme["nav"]};
                --radius-lg: 28px;
                --radius-md: 20px;
                --radius-sm: 14px;
            }}

            .stApp {{
                background:
                    radial-gradient(circle at 8% -10%, rgba(37, 99, 235, 0.16), transparent 28rem),
                    radial-gradient(circle at 92% 6%, rgba(124, 58, 237, 0.13), transparent 26rem),
                    linear-gradient(180deg, var(--bg) 0%, var(--bg-alt) 100%);
                color: var(--ink);
            }}

            .main .block-container {{
                max-width: 1180px;
                padding: 1.25rem 1.4rem 4rem;
            }}

            [data-testid="stHeader"] {{
                background: transparent;
            }}

            [data-testid="stToolbar"],
            [data-testid="stDecoration"] {{
                display: none;
            }}

            h1, h2, h3, p, label {{
                letter-spacing: 0;
            }}

            h2, h3 {{
                color: var(--ink);
            }}

            .premium-nav {{
                position: sticky;
                top: 0.75rem;
                z-index: 20;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
                margin-bottom: 2.1rem;
                padding: 0.72rem 0.82rem;
                border: 1px solid var(--border);
                border-radius: 999px;
                background: var(--nav);
                backdrop-filter: blur(20px);
                box-shadow: var(--shadow-soft);
                animation: riseIn 420ms ease both;
            }}

            .brand {{
                display: flex;
                align-items: center;
                gap: 0.7rem;
                min-width: 0;
            }}

            .brand-mark {{
                display: grid;
                place-items: center;
                width: 2.25rem;
                height: 2.25rem;
                border-radius: 999px;
                background: linear-gradient(135deg, var(--accent-2), var(--accent-3));
                color: white;
                font-size: 0.78rem;
                font-weight: 800;
                box-shadow: 0 10px 25px rgba(37, 99, 235, 0.24);
            }}

            .brand-copy {{
                display: flex;
                flex-direction: column;
                line-height: 1.1;
            }}

            .brand-title {{
                color: var(--ink);
                font-size: 0.95rem;
                font-weight: 760;
                margin: 0;
            }}

            .brand-subtitle {{
                color: var(--muted);
                font-size: 0.76rem;
                margin: 0.12rem 0 0;
            }}

            .nav-links {{
                display: flex;
                align-items: center;
                gap: 0.35rem;
            }}

            .nav-links a {{
                border-radius: 999px;
                color: var(--muted-strong);
                font-size: 0.86rem;
                font-weight: 650;
                padding: 0.58rem 0.86rem;
                text-decoration: none;
                transition: background 180ms ease, color 180ms ease, transform 180ms ease;
            }}

            .nav-links a:hover {{
                background: var(--surface-soft);
                color: var(--ink);
                transform: translateY(-1px);
            }}

            .hero {{
                display: grid;
                grid-template-columns: minmax(0, 1.1fr) minmax(300px, 0.9fr);
                gap: 1.25rem;
                align-items: stretch;
                margin-bottom: 1.25rem;
            }}

            .hero-copy,
            .hero-visual,
            .glass-card {{
                border: 1px solid var(--border);
                border-radius: var(--radius-lg);
                background: var(--surface);
                box-shadow: var(--shadow);
                backdrop-filter: blur(20px);
            }}

            .hero-copy {{
                padding: clamp(1.5rem, 4vw, 2.65rem);
                animation: riseIn 520ms ease both;
            }}

            .hero-visual {{
                position: relative;
                overflow: hidden;
                min-height: 340px;
                padding: 1.35rem;
                animation: riseIn 620ms ease both;
            }}

            .hero-visual::before {{
                content: "";
                position: absolute;
                inset: 0;
                background:
                    linear-gradient(135deg, rgba(37, 99, 235, 0.18), transparent 44%),
                    radial-gradient(circle at 78% 20%, rgba(124, 58, 237, 0.20), transparent 16rem);
                pointer-events: none;
            }}

            .eyebrow {{
                color: var(--accent-2);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                margin: 0 0 0.75rem;
                text-transform: uppercase;
            }}

            .hero-title {{
                color: var(--ink);
                font-size: clamp(2.35rem, 6vw, 4.7rem);
                font-weight: 820;
                letter-spacing: -0.04em;
                line-height: 0.98;
                margin: 0;
                max-width: 800px;
            }}

            .hero-text {{
                color: var(--muted);
                font-size: 1.04rem;
                line-height: 1.72;
                max-width: 670px;
                margin: 1.1rem 0 1.45rem;
            }}

            .hero-actions {{
                display: flex;
                flex-wrap: wrap;
                gap: 0.8rem;
                align-items: center;
            }}

            .primary-link,
            .secondary-link {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 2.8rem;
                border-radius: 999px;
                font-size: 0.92rem;
                font-weight: 760;
                padding: 0 1.12rem;
                text-decoration: none;
                transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
            }}

            .primary-link {{
                color: var(--button-text);
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                box-shadow: 0 16px 28px rgba(37, 99, 235, 0.24);
            }}

            .secondary-link {{
                color: var(--ink);
                background: var(--surface-soft);
                border: 1px solid var(--border);
            }}

            .primary-link:hover,
            .secondary-link:hover {{
                transform: translateY(-2px);
            }}

            .mini-grid {{
                position: relative;
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 0.85rem;
                height: 100%;
            }}

            .signal-card {{
                position: relative;
                border: 1px solid var(--border);
                border-radius: var(--radius-md);
                background: var(--surface);
                padding: 1rem;
                min-height: 130px;
                overflow: hidden;
            }}

            .signal-card.dark {{
                grid-column: span 2;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: white;
                min-height: 150px;
            }}

            .signal-label {{
                color: inherit;
                opacity: 0.72;
                font-size: 0.76rem;
                font-weight: 780;
                letter-spacing: 0.07em;
                margin: 0 0 0.65rem;
                text-transform: uppercase;
            }}

            .signal-value {{
                color: inherit;
                font-size: 1.85rem;
                font-weight: 820;
                line-height: 1;
                margin: 0;
            }}

            .signal-note {{
                color: inherit;
                opacity: 0.74;
                font-size: 0.82rem;
                line-height: 1.5;
                margin: 0.65rem 0 0;
            }}

            .section-shell {{
                margin-top: 1.35rem;
            }}

            .section-label {{
                color: var(--accent-2);
                font-size: 0.76rem;
                font-weight: 820;
                letter-spacing: 0.08em;
                margin: 0 0 0.45rem;
                text-transform: uppercase;
            }}

            .section-title {{
                color: var(--ink);
                font-size: clamp(1.55rem, 3vw, 2.25rem);
                font-weight: 810;
                letter-spacing: -0.03em;
                line-height: 1.08;
                margin: 0;
            }}

            .section-copy {{
                color: var(--muted);
                font-size: 0.98rem;
                line-height: 1.65;
                max-width: 640px;
                margin: 0.62rem 0 1.15rem;
            }}

            .glass-card {{
                padding: clamp(1.1rem, 3vw, 1.55rem);
                margin-bottom: 1rem;
                transition: transform 190ms ease, box-shadow 190ms ease, border-color 190ms ease;
            }}

            .glass-card:hover {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, 0.24);
                box-shadow: 0 20px 58px rgba(15, 23, 42, 0.11);
            }}

            .card-title {{
                color: var(--ink);
                font-size: 1.02rem;
                font-weight: 780;
                margin: 0 0 0.25rem;
            }}

            .card-copy {{
                color: var(--muted);
                font-size: 0.9rem;
                line-height: 1.55;
                margin: 0;
            }}

            .stat-grid {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.85rem;
                margin: 0.9rem 0 0;
            }}

            .stat-card {{
                border: 1px solid var(--border);
                border-radius: var(--radius-md);
                background: var(--surface-strong);
                padding: 1rem;
                box-shadow: var(--shadow-soft);
                transition: transform 180ms ease, border-color 180ms ease;
            }}

            .stat-card:hover {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, 0.24);
            }}

            .stat-label {{
                color: var(--muted);
                font-size: 0.76rem;
                font-weight: 760;
                letter-spacing: 0.06em;
                margin: 0 0 0.42rem;
                text-transform: uppercase;
            }}

            .stat-value {{
                color: var(--ink);
                font-size: 1.55rem;
                font-weight: 820;
                line-height: 1;
                margin: 0;
            }}

            .stat-caption {{
                color: var(--muted);
                font-size: 0.82rem;
                margin: 0.48rem 0 0;
            }}

            .result-card {{
                border: 1px solid var(--border);
                border-radius: var(--radius-lg);
                background: var(--surface-strong);
                box-shadow: var(--shadow);
                padding: 1.45rem;
                animation: riseIn 420ms ease both;
            }}

            .result-pass {{
                border-color: rgba(4, 120, 87, 0.28);
                background: linear-gradient(135deg, var(--success-bg), var(--surface-strong) 68%);
            }}

            .result-fail {{
                border-color: rgba(180, 35, 24, 0.28);
                background: linear-gradient(135deg, var(--danger-bg), var(--surface-strong) 68%);
            }}

            .result-label {{
                color: var(--muted);
                font-size: 0.76rem;
                font-weight: 820;
                letter-spacing: 0.08em;
                margin: 0 0 0.58rem;
                text-transform: uppercase;
            }}

            .result-value {{
                color: var(--ink);
                font-size: 2.7rem;
                font-weight: 840;
                letter-spacing: -0.04em;
                line-height: 1;
                margin: 0;
            }}

            .result-note {{
                color: var(--muted);
                font-size: 0.94rem;
                line-height: 1.62;
                margin: 0.82rem 0 0;
            }}

            .confidence-row {{
                display: flex;
                justify-content: space-between;
                gap: 0.8rem;
                border-top: 1px solid var(--border);
                margin-top: 1.15rem;
                padding-top: 1rem;
            }}

            .confidence-item {{
                min-width: 0;
            }}

            .confidence-kicker {{
                color: var(--muted);
                font-size: 0.74rem;
                font-weight: 760;
                margin: 0 0 0.28rem;
                text-transform: uppercase;
            }}

            .confidence-text {{
                color: var(--ink);
                font-size: 0.93rem;
                font-weight: 720;
                margin: 0;
            }}

            .stButton > button {{
                width: 100%;
                min-height: 3.15rem;
                border: 0;
                border-radius: 999px;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: var(--button-text);
                font-weight: 800;
                box-shadow: 0 18px 34px rgba(37, 99, 235, 0.23);
                transition: transform 180ms ease, box-shadow 180ms ease, filter 180ms ease;
            }}

            .stButton > button:hover {{
                color: var(--button-text);
                border: 0;
                filter: brightness(1.04);
                transform: translateY(-2px);
                box-shadow: 0 22px 40px rgba(37, 99, 235, 0.28);
            }}

            .stButton > button:active {{
                transform: translateY(0);
            }}

            [data-testid="stForm"] {{
                border: 1px solid var(--border);
                border-radius: var(--radius-lg);
                background: var(--surface);
                box-shadow: var(--shadow);
                padding: clamp(1rem, 3vw, 1.35rem);
            }}

            [data-testid="stSlider"] {{
                padding: 0.15rem 0 0.2rem;
            }}

            [data-testid="stSlider"] label,
            [data-testid="stSelectbox"] label,
            [data-testid="stCheckbox"] label {{
                color: var(--muted-strong);
                font-weight: 680;
            }}

            [data-testid="stMetric"] {{
                border: 1px solid var(--border);
                border-radius: var(--radius-md);
                background: var(--surface-strong);
                padding: 1rem;
                box-shadow: var(--shadow-soft);
            }}

            [data-testid="stMetricLabel"] {{
                color: var(--muted);
            }}

            [data-testid="stMetricValue"] {{
                color: var(--ink);
            }}

            .empty-state {{
                border: 1px dashed var(--border);
                border-radius: var(--radius-lg);
                background: var(--surface);
                padding: 1.4rem;
                text-align: left;
            }}

            .empty-state p {{
                color: var(--muted);
                line-height: 1.6;
                margin: 0;
            }}

            .footer-note {{
                color: var(--muted);
                font-size: 0.82rem;
                line-height: 1.55;
                margin-top: 0.7rem;
            }}

            @keyframes riseIn {{
                from {{
                    opacity: 0;
                    transform: translateY(10px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @media (max-width: 920px) {{
                .main .block-container {{
                    padding: 1rem 1rem 3rem;
                }}

                .premium-nav {{
                    align-items: flex-start;
                    border-radius: 24px;
                    flex-direction: column;
                    position: relative;
                    top: 0;
                }}

                .nav-links {{
                    flex-wrap: wrap;
                    width: 100%;
                }}

                .hero {{
                    grid-template-columns: 1fr;
                }}

                .hero-visual {{
                    min-height: 280px;
                }}

                .stat-grid {{
                    grid-template-columns: 1fr;
                }}
            }}

            @media (max-width: 620px) {{
                .hero-copy,
                .hero-visual,
                .glass-card,
                .result-card,
                [data-testid="stForm"] {{
                    border-radius: 22px;
                }}

                .hero-actions {{
                    align-items: stretch;
                    flex-direction: column;
                }}

                .primary-link,
                .secondary-link {{
                    width: 100%;
                }}

                .mini-grid {{
                    grid-template-columns: 1fr;
                }}

                .signal-card.dark {{
                    grid-column: span 1;
                }}

                .confidence-row {{
                    flex-direction: column;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def nav():
    st.markdown(
        """
        <nav class="premium-nav">
            <div class="brand">
                <div class="brand-mark">ST</div>
                <div class="brand-copy">
                    <p class="brand-title">Student Outcome</p>
                    <p class="brand-subtitle">Prediction dashboard</p>
                </div>
            </div>
            <div class="nav-links">
                <a href="#overview">Overview</a>
                <a href="#profile">Profile</a>
                <a href="#prediction">Prediction</a>
            </div>
        </nav>
        """,
        unsafe_allow_html=True,
    )


def hero():
    st.markdown(
        """
        <section class="hero" id="overview">
            <div class="hero-copy">
                <p class="eyebrow">Student analytics platform</p>
                <h1 class="hero-title">Predict student outcomes with clarity.</h1>
                <p class="hero-text">
                    A polished decision support interface for estimating pass or fail outcomes from
                    academic performance, attendance, health, and study behavior.
                </p>
                <div class="hero-actions">
                    <a class="primary-link" href="#profile">Start prediction</a>
                    <a class="secondary-link" href="#prediction">View result panel</a>
                </div>
            </div>
            <div class="hero-visual" aria-label="Prediction dashboard summary">
                <div class="mini-grid">
                    <div class="signal-card dark">
                        <p class="signal-label">Model accuracy</p>
                        <p class="signal-value">87.34%</p>
                        <p class="signal-note">Decision tree trained on the student performance dataset.</p>
                    </div>
                    <div class="signal-card">
                        <p class="signal-label">Inputs</p>
                        <p class="signal-value">6</p>
                        <p class="signal-note">Study, attendance, health, and grade signals.</p>
                    </div>
                    <div class="signal-card">
                        <p class="signal-label">Output</p>
                        <p class="signal-value">Pass/Fail</p>
                        <p class="signal-note">Simple outcome language for fast review.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def section_header(anchor, label, title, copy):
    st.markdown(
        f"""
        <section class="section-shell" id="{anchor}">
            <p class="section-label">{label}</p>
            <h2 class="section-title">{title}</h2>
            <p class="section-copy">{copy}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def stat_card(label, value, caption):
    st.markdown(
        f"""
        <div class="stat-card">
            <p class="stat-label">{label}</p>
            <p class="stat-value">{value}</p>
            <p class="stat-caption">{caption}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def result_card(prediction, average_grade, absence_band, risk_level):
    is_pass = prediction == "Pass"
    result_class = "result-pass" if is_pass else "result-fail"
    tone = "On track" if is_pass else "Needs attention"
    note = (
        "The profile currently looks positive. Keep reinforcing consistent study time and attendance."
        if is_pass
        else "The profile shows risk. Prioritize attendance, recovery support, and near-term grade improvement."
    )
    st.markdown(
        f"""
        <div class="result-card {result_class}">
            <p class="result-label">Predicted outcome</p>
            <p class="result-value">{prediction}</p>
            <p class="result-note">{note}</p>
            <div class="confidence-row">
                <div class="confidence-item">
                    <p class="confidence-kicker">Status</p>
                    <p class="confidence-text">{tone}</p>
                </div>
                <div class="confidence-item">
                    <p class="confidence-kicker">Grade average</p>
                    <p class="confidence-text">{average_grade:.1f}/20</p>
                </div>
                <div class="confidence-item">
                    <p class="confidence-kicker">Risk level</p>
                    <p class="confidence-text">{risk_level}</p>
                </div>
                <div class="confidence-item">
                    <p class="confidence-kicker">Absences</p>
                    <p class="confidence-text">{absence_band}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_result_state():
    st.markdown(
        """
        <div class="empty-state">
            <p>
                Complete the student profile and run the model. The prediction summary,
                status, grade average, absence band, and risk signal will appear here.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def get_prediction(payload):
    response = requests.post(API_URL, json=payload, timeout=8)
    response.raise_for_status()
    return response.json()["prediction"]


def absence_level(absences):
    if absences <= 10:
        return "Low"
    if absences <= 30:
        return "Moderate"
    return "High"


def risk_level(average_grade, failures, absences):
    risk_points = 0
    risk_points += 1 if average_grade < 12 else 0
    risk_points += 1 if failures > 0 else 0
    risk_points += 1 if absences > 20 else 0

    if risk_points == 0:
        return "Low"
    if risk_points == 1:
        return "Medium"
    return "High"


if "prediction" not in st.session_state:
    st.session_state.prediction = None
    st.session_state.last_payload = None

with st.sidebar:
    st.markdown("### Appearance")
    dark_mode = st.toggle("Dark mode", value=False)
    st.caption("Switch between a bright Apple-inspired UI and a premium dark dashboard.")

theme_name = "dark" if dark_mode else "light"
inject_design_system(theme_name)
nav()
hero()

section_header(
    "profile",
    "Prediction workflow",
    "Build the student profile",
    "Use the sliders to describe the student's academic performance and learning context.",
)

left_col, right_col = st.columns([1.18, 0.82], gap="large")

with left_col:
    with st.form("prediction_form"):
        st.markdown(
            """
            <div class="glass-card">
                <p class="card-title">Student signals</p>
                <p class="card-copy">Adjust each indicator, then submit the profile for prediction.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        academic_col, context_col = st.columns(2, gap="large")

        with academic_col:
            st.subheader("Academic")
            studytime = st.slider(
                "Weekly study time level",
                min_value=1,
                max_value=4,
                value=2,
                help="1 is lowest study time, 4 is highest study time.",
            )
            failures = st.slider(
                "Past class failures",
                min_value=0,
                max_value=4,
                value=0,
                help="Number of previous class failures.",
            )
            g1 = st.slider("First period grade", min_value=0, max_value=20, value=10)
            g2 = st.slider("Second period grade", min_value=0, max_value=20, value=10)

        with context_col:
            st.subheader("Context")
            absences = st.slider(
                "School absences",
                min_value=0,
                max_value=100,
                value=5,
                help="Total recorded absences.",
            )
            health = st.slider(
                "Health rating",
                min_value=1,
                max_value=5,
                value=3,
                help="1 is very poor health, 5 is very good health.",
            )

            average_grade = (g1 + g2) / 2
            absence_band = absence_level(absences)
            current_risk = risk_level(average_grade, failures, absences)

            st.markdown("### Live snapshot")
            st.metric("Average prior grade", f"{average_grade:.1f}/20")
            st.metric("Absence level", absence_band)
            st.metric("Risk signal", current_risk)

        submitted = st.form_submit_button("Run prediction", type="primary")

with right_col:
    section_header(
        "prediction",
        "Model output",
        "Prediction summary",
        "A clear outcome card keeps the result readable and easy to act on.",
    )

    st.markdown(
        """
        <div class="glass-card">
            <p class="card-title">Result panel</p>
            <p class="card-copy">Powered by the Flask API and the trained decision tree model.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if submitted:
        payload = {
            "studytime": studytime,
            "failures": failures,
            "absences": absences,
            "health": health,
            "G1": g1,
            "G2": g2,
        }

        try:
            with st.spinner("Analyzing student profile..."):
                time.sleep(0.35)
                prediction = get_prediction(payload)

            st.session_state.prediction = prediction
            st.session_state.last_payload = payload
            st.session_state.last_average_grade = average_grade
            st.session_state.last_absence_band = absence_band
            st.session_state.last_risk = current_risk
        except requests.exceptions.RequestException:
            st.session_state.prediction = None
            st.error("The prediction API is not reachable. Start the Flask API, then run the prediction again.")
        except (KeyError, ValueError):
            st.session_state.prediction = None
            st.error("The API returned an unexpected response. Check that the Flask service is using the latest code.")

    if st.session_state.prediction:
        result_card(
            st.session_state.prediction,
            st.session_state.last_average_grade,
            st.session_state.last_absence_band,
            st.session_state.last_risk,
        )
    else:
        empty_result_state()

    st.markdown(
        '<p class="footer-note">Inputs used by the model: studytime, failures, absences, health, G1, and G2.</p>',
        unsafe_allow_html=True,
    )
