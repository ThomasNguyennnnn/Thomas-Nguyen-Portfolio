
import streamlit as st
from pathlib import Path
import base64
from textwrap import dedent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About Me | Thomas Nguyen",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROFILE_IMAGE = PROJECT_ROOT / "assets" / "profile_photo.jpg"
RESUME_FILE = PROJECT_ROOT / "assets" / "resume.pdf"

GITHUB_URL = "https://github.com/ThomasNguyennnnn"
LINKEDIN_URL = "https://www.linkedin.com/in/thomas-tuan-nguyen/"
EMAIL = "thomas.nttn.au@gmail.com"


# ============================================================
# HTML HELPERS
# ============================================================

def compact_html(source):
    return " ".join(
        line.strip()
        for line in dedent(source).splitlines()
        if line.strip()
    )


def render_html(source):
    st.markdown(
        compact_html(source),
        unsafe_allow_html=True
    )


def render_grid(css_class, cards):
    render_html(
        f'<div class="{css_class}">'
        + "".join(cards)
        + "</div>"
    )


def section_heading(title, subtitle):
    render_html(f"""
        <div class="section-title">{title}</div>
        <div class="section-subtitle">{subtitle}</div>
    """)


def image_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(
            file.read()
        ).decode("utf-8")


def get_image_mime(path):
    return (
        "image/png"
        if path.suffix.lower() == ".png"
        else "image/jpeg"
    )


# ============================================================
# CARD HELPERS
# ============================================================

def metric_card(value, label, note):
    return compact_html(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-note">{note}</div>
        </div>
    """)


def info_card(label, title, text):
    return compact_html(f"""
        <div class="info-card">
            <div class="card-label">{label}</div>
            <div class="card-title">{title}</div>
            <div class="card-text">{text}</div>
        </div>
    """)


def timeline_card(title, meta, text):
    return compact_html(f"""
        <div class="timeline-card">
            <div class="timeline-title">{title}</div>
            <div class="timeline-meta">{meta}</div>
            <div class="timeline-text">{text}</div>
        </div>
    """)


def capability_card(label, title, tools, text):
    return compact_html(f"""
        <div class="capability-card">
            <div class="card-label">{label}</div>
            <div class="capability-title">{title}</div>
            <div class="capability-tools">{tools}</div>
            <div class="capability-text">{text}</div>
        </div>
    """)


def research_card(
    label,
    status,
    title,
    description,
    methods,
    outcome
):
    return compact_html(f"""
        <div class="research-card">

            <div class="research-topline">
                <span class="card-label">{label}</span>
                <span class="research-status">{status}</span>
            </div>

            <div class="research-title">{title}</div>

            <div class="research-description">
                {description}
            </div>

            <div class="research-methods">
                {methods}
            </div>

            <div class="research-outcome">
                {outcome}
            </div>

        </div>
    """)


# ============================================================
# CSS — CONSISTENT WITH HOME PAGE
# ============================================================

st.markdown(
    """
<style>

:root {
    --text-900: #0f172a;
    --text-700: #334155;
    --text-500: #64748b;

    --blue: #2563eb;
    --violet: #7c3aed;
    --cyan: #06b6d4;

    --card-border: rgba(129,140,248,0.28);
}

/* ========================================================
   GLOBAL
======================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(79,70,229,0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(6,182,212,0.22),
            transparent 26%
        ),
        radial-gradient(
            circle at 50% 92%,
            rgba(37,99,235,0.14),
            transparent 34%
        ),
        linear-gradient(
            135deg,
            #edf4ff 0%,
            #f7f1ff 46%,
            #e9feff 100%
        );
}

/* FIX: EXTRA TOP SPACING FOR STREAMLIT HEADER */

.block-container {
    padding-top: 5.5rem;
    padding-bottom: 4rem;
    max-width: 1280px;
}

footer {
    visibility: hidden;
}

/* ========================================================
   SIDEBAR
======================================================== */

section[data-testid="stSidebar"] {
    background:
        radial-gradient(
            circle at top left,
            rgba(37,99,235,0.35),
            transparent 30%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(124,58,237,0.25),
            transparent 34%
        ),
        linear-gradient(
            180deg,
            #020617 0%,
            #0f172a 55%,
            #1e1b4b 100%
        );
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

/* ========================================================
   HERO
======================================================== */

.hero-card {
    padding: 2.6rem 2.7rem;
    border-radius: 36px;

    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(37,99,235,0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 100% 0%,
            rgba(6,182,212,0.20),
            transparent 24%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(124,58,237,0.16),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            rgba(255,255,255,0.94),
            rgba(239,246,255,0.89)
        );

    border: 1px solid rgba(129,140,248,0.36);

    box-shadow:
        0 30px 80px rgba(30,41,59,0.13),
        0 0 0 1px rgba(255,255,255,0.35) inset;

    backdrop-filter: blur(14px);
}

.hero-grid {
    display: grid;
    grid-template-columns:
        minmax(0,1.75fr)
        minmax(270px,0.9fr);

    gap: 2rem;
    align-items: center;
}

.eyebrow {
    display: inline-block;

    padding: 0.45rem 0.9rem;
    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #dbeafe,
            #ede9fe,
            #ccfbf1
        );

    border: 1px solid rgba(37,99,235,0.28);

    color: #0f172a;
    font-size: 0.83rem;
    font-weight: 850;

    margin-bottom: 1rem;
}

.page-title {
    font-size: 3.45rem;
    font-weight: 950;
    letter-spacing: -1.8px;
    line-height: 1.1;

    color: #0f172a;
    margin-bottom: 0.75rem;
}

.gradient-text {
    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );

    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 1.18rem;
    font-weight: 850;
    line-height: 1.5;

    color: #1e293b;
    margin-bottom: 1.15rem;
}

.body-text {
    color: #334155;
    font-size: 1rem;
    line-height: 1.79;
}

.body-text p {
    margin: 0 0 1rem;
}

.body-text b {
    color: #1e293b;
}

.hero-tags {
    margin-top: 1rem;
}

.hero-tag {
    display: inline-block;

    padding: 0.4rem 0.7rem;
    margin: 0.2rem 0.2rem 0.1rem 0;

    border-radius: 999px;
    background: rgba(255,255,255,0.75);
    border: 1px solid rgba(167,139,250,0.3);

    color: #334155;
    font-size: 0.8rem;
    font-weight: 850;
}

/* ========================================================
   PROFILE PHOTO
======================================================== */

.profile-area {
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-image-box {
    width: 305px;
    height: 305px;
    padding: 10px;

    border-radius: 40px;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );

    box-shadow:
        0 28px 72px rgba(37,99,235,0.25),
        0 0 44px rgba(6,182,212,0.18);

    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-image-box img {
    width: 285px;
    height: 285px;

    object-fit: cover;
    object-position: center;

    border-radius: 33px;
}

/* ========================================================
   HEADINGS
======================================================== */

.section-title {
    font-size: 1.93rem;
    font-weight: 950;
    letter-spacing: -0.5px;

    color: #0f172a;

    margin-top: 2.7rem;
    margin-bottom: 0.35rem;
}

.section-subtitle {
    font-size: 1rem;
    color: #64748b;
    line-height: 1.65;
    margin-bottom: 1.35rem;
}

/* ========================================================
   GRIDS
======================================================== */

.grid-2 {
    display: grid;

    grid-template-columns:
        repeat(2,minmax(0,1fr));

    gap: 1.25rem;
    align-items: stretch;
}

.grid-3 {
    display: grid;

    grid-template-columns:
        repeat(3,minmax(0,1fr));

    gap: 1.25rem;
    align-items: stretch;
}

.grid-4 {
    display: grid;

    grid-template-columns:
        repeat(4,minmax(0,1fr));

    gap: 1.2rem;
    align-items: stretch;
}

/* ========================================================
   SHARED CARDS
======================================================== */

.metric-card,
.info-card,
.timeline-card,
.capability-card,
.research-card,
.resume-panel {
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(
            circle at top right,
            rgba(124,58,237,0.07),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            rgba(255,255,255,0.96),
            rgba(248,250,252,0.92)
        );

    border: 1px solid var(--card-border);

    box-shadow:
        0 16px 38px rgba(59,130,246,0.08),
        0 0 0 1px rgba(255,255,255,0.25) inset;

    backdrop-filter: blur(10px);
}

.metric-card::before,
.info-card::before,
.capability-card::before,
.research-card::before {
    content: "";

    position: absolute;
    top: 0;
    left: 0;

    width: 100%;
    height: 6px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );
}

/* ========================================================
   METRIC CARDS
======================================================== */

.metric-card {
    padding: 1.35rem;
    border-radius: 26px;

    min-height: 170px;
    height: 100%;
}

.metric-value {
    color: #0f172a;

    font-size: 1.9rem;
    font-weight: 950;
    line-height: 1.25;

    margin-bottom: 0.4rem;
}

.metric-label {
    color: #4f46e5;

    font-size: 0.9rem;
    font-weight: 900;

    margin-bottom: 0.4rem;
}

.metric-note {
    color: #64748b;

    font-size: 0.82rem;
    line-height: 1.5;
}

/* ========================================================
   INFO CARDS
======================================================== */

.info-card {
    padding: 1.5rem 1.55rem;
    border-radius: 28px;

    min-height: 240px;
    height: 100%;
}

.card-label {
    display: inline-block;
    width: fit-content;

    padding: 0.32rem 0.7rem;
    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #dbeafe,
            #ede9fe,
            #ccfbf1
        );

    border: 1px solid rgba(167,139,250,0.42);

    color: #0f172a;

    font-size: 0.76rem;
    font-weight: 900;

    margin-bottom: 0.8rem;
}

.card-title {
    color: #0f172a;

    font-size: 1.17rem;
    font-weight: 950;
    line-height: 1.4;

    margin-bottom: 0.6rem;
}

.card-text {
    color: #475569;

    font-size: 0.94rem;
    line-height: 1.73;
}

/* ========================================================
   TIMELINE CARDS
======================================================== */

.timeline-card {
    padding: 1.5rem 1.6rem;
    border-radius: 26px;

    min-height: 225px;
    height: 100%;
}

.timeline-title {
    color: #0f172a;

    font-size: 1.15rem;
    font-weight: 950;

    margin-bottom: 0.45rem;
}

.timeline-meta {
    color: #4f46e5;

    font-size: 0.87rem;
    font-weight: 850;
    line-height: 1.6;

    margin-bottom: 0.65rem;
}

.timeline-text {
    color: #475569;

    font-size: 0.94rem;
    line-height: 1.7;
}

/* ========================================================
   RESEARCH CARDS
======================================================== */

.research-card {
    padding: 1.7rem;
    border-radius: 30px;

    min-height: 380px;
    height: 100%;

    display: flex;
    flex-direction: column;
}

.research-topline {
    display: flex;
    flex-wrap: wrap;

    justify-content: space-between;
    align-items: center;

    gap: 0.65rem;
    margin-bottom: 0.65rem;
}

.research-topline .card-label {
    margin-bottom: 0;
}

.research-status {
    display: inline-block;

    padding: 0.32rem 0.7rem;
    border-radius: 999px;

    background: #dcfce7;
    border: 1px solid #86efac;

    color: #166534;

    font-size: 0.75rem;
    font-weight: 900;
}

.research-title {
    color: #0f172a;

    font-size: 1.2rem;
    font-weight: 950;
    line-height: 1.4;

    margin-bottom: 0.8rem;
}

.research-description {
    color: #475569;

    font-size: 0.94rem;
    line-height: 1.72;

    margin-bottom: 0.85rem;
}

.research-methods {
    color: #3730a3;

    font-size: 0.87rem;
    font-weight: 850;
    line-height: 1.6;

    margin-bottom: 1rem;
}

.research-outcome {
    margin-top: auto;

    padding: 0.9rem 1rem;
    border-radius: 18px;

    background:
        linear-gradient(
            90deg,
            rgba(219,234,254,0.84),
            rgba(237,233,254,0.78)
        );

    border: 1px solid rgba(167,139,250,0.25);

    color: #334155;
    font-size: 0.88rem;
    line-height: 1.6;
}

/* ========================================================
   CAPABILITY CARDS
======================================================== */

.capability-card {
    padding: 1.45rem 1.5rem;
    border-radius: 27px;

    min-height: 235px;
    height: 100%;
}

.capability-title {
    color: #0f172a;

    font-size: 1.1rem;
    font-weight: 950;
    line-height: 1.4;

    margin-bottom: 0.55rem;
}

.capability-tools {
    color: #3730a3;

    font-size: 0.87rem;
    font-weight: 850;
    line-height: 1.55;

    margin-bottom: 0.7rem;
}

.capability-text {
    color: #475569;

    font-size: 0.89rem;
    line-height: 1.65;
}

/* ========================================================
   RESUME PANEL
======================================================== */

.resume-panel {
    border-radius: 29px;

    padding: 1.7rem 1.8rem;
    margin-top: 2.5rem;
    margin-bottom: 1.2rem;
}

.resume-title {
    color: #0f172a;

    font-size: 1.25rem;
    font-weight: 950;

    margin-bottom: 0.55rem;
}

.resume-text {
    color: #475569;

    font-size: 0.95rem;
    line-height: 1.75;
}

/* ========================================================
   BUTTONS
======================================================== */

div.stDownloadButton > button,
div.stLinkButton > a {
    border-radius: 999px !important;

    font-weight: 850 !important;
    height: 2.9rem !important;

    border:
        1px solid rgba(37,99,235,0.35) !important;

    background:
        rgba(255,255,255,0.84) !important;

    color: #0f172a !important;

    box-shadow:
        0 8px 20px rgba(59,130,246,0.10) !important;
}

div.stDownloadButton > button *,
div.stLinkButton > a * {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

/* ========================================================
   RESPONSIVE
======================================================== */

@media (max-width: 1050px) {

    .hero-grid {
        grid-template-columns: 1fr;
    }

    .grid-4 {
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }

    .profile-image-box {
        margin: 1rem auto 0;
    }
}

@media (max-width: 760px) {

    .block-container {
        padding-top: 4.5rem;
    }

    .hero-card {
        padding: 1.7rem 1.4rem;
    }

    .page-title {
        font-size: 2.5rem;
    }

    .grid-2,
    .grid-3,
    .grid-4 {
        grid-template-columns: 1fr;
    }

    .info-card,
    .timeline-card,
    .capability-card,
    .research-card {
        min-height: auto;
    }

    .section-title {
        font-size: 1.65rem;
    }

    .profile-image-box {
        width: 260px;
        height: 260px;
    }

    .profile-image-box img {
        width: 240px;
        height: 240px;
    }
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

if PROFILE_IMAGE.exists():

    encoded_image = image_to_base64(PROFILE_IMAGE)
    image_mime = get_image_mime(PROFILE_IMAGE)

    photo_html = f"""
        <div class="profile-area">
            <div class="profile-image-box">
                <img
                    src="data:{image_mime};base64,{encoded_image}"
                    alt="Thomas Nguyen profile photo"
                >
            </div>
        </div>
    """

else:

    photo_html = """
        <div class="profile-area">
            <div class="profile-image-box"
                 style="background:rgba(219,234,254,0.8);">

                <div style="color:#334155;text-align:center;">
                    Profile image:
                    assets/profile_photo.jpg
                </div>

            </div>
        </div>
    """


render_html(f"""
    <div class="hero-card">

        <div class="hero-grid">

            <div>

                <div class="eyebrow">
                    About Me · Data Science Graduate · Research &amp; Analytics
                </div>

                <div class="page-title">
                    I connect
                    <span class="gradient-text">data science</span>
                    with business decisions.
                </div>

                <div class="subtitle">
                    Data Scientist · Data Analyst · Business Analyst
                </div>

                <div class="body-text">

                    <p>
                        I am <b>Thomas Nguyen</b>, a
                        <b>Master of Data Science and Innovation graduate
                        from the University of Technology Sydney</b>,
                        with a foundation in business analytics,
                        machine learning, statistical reasoning,
                        and data visualisation.
                    </p>

                    <p>
                        My background combines
                        <b>academic research, industry analytics,
                        and applied data science</b>.
                        I have contributed to cyber-risk research
                        resulting in two accepted papers and completed
                        industry analytics work in sports sponsorship
                        and media reporting.
                    </p>

                    <p>
                        I enjoy working across the analytical process:
                        understanding the problem, preparing reliable
                        data, selecting suitable methods, evaluating
                        results, and communicating findings in a way
                        that supports practical decisions.
                    </p>

                </div>

                <div class="hero-tags">
                    <span class="hero-tag">Machine Learning</span>
                    <span class="hero-tag">Business Analytics</span>
                    <span class="hero-tag">Academic Research</span>
                    <span class="hero-tag">Data Visualisation</span>
                    <span class="hero-tag">Industry Experience</span>
                </div>

            </div>

            {photo_html}

        </div>

    </div>
""")


# ============================================================
# AT A GLANCE
# ============================================================

section_heading(
    "At a Glance",
    "Academic achievement, research recognition, and applied industry experience."
)

metrics = [

    metric_card(
        "6.56 / 7",
        "UTS Master GPA",
        "Completed July 2026 · WAM 87.33"
    ),

    metric_card(
        "Merit Award",
        "Academic Recognition",
        "2026 TD School Outstanding Academic Achievement"
    ),

    metric_card(
        "2 Accepted",
        "Research Papers",
        "AusDM 2026 conference + MDPI Risks journal"
    ),

    metric_card(
        "≈200h",
        "Industry Placement",
        "Sports consultancy and data analytics experience"
    )

]

render_grid("grid-4", metrics)


# ============================================================
# PROFESSIONAL PROFILE
# ============================================================

section_heading(
    "Professional Profile",
    "The strengths that connect my technical background with business needs."
)

profile_cards = [

    info_card(
        "Analytical Foundation",
        "Business-first data thinking",
        """
        My undergraduate background in business analytics
        helps me approach technical problems in terms of
        organisational needs, stakeholder questions, and
        measurable outcomes. I aim to understand the
        decision first, then choose the right analysis.
        """
    ),

    info_card(
        "Technical Capability",
        "Machine learning and applied modelling",
        """
        My postgraduate work and research cover predictive
        modelling, deep learning, computer vision, temporal
        event data, and statistical evaluation. I am
        comfortable comparing complex ML models with
        simpler baselines rather than relying on
        model complexity alone.
        """
    ),

    info_card(
        "Professional Development",
        "Research and industry experience",
        """
        Academic research developed my experimental
        discipline and critical thinking, while
        industry analytics strengthened my approach
        to data quality, business reporting, teamwork,
        and communicating results to stakeholders.
        """
    )

]

render_grid("grid-3", profile_cards)


# ============================================================
# EDUCATION & EXPERIENCE
# ============================================================

section_heading(
    "Education & Experience",
    "The academic and professional experiences shaping my approach to analytics."
)

education_cards = [

    timeline_card(
        "Master of Data Science and Innovation",
        "University of Technology Sydney · Conferred July 2026",
        """
        Completed with a GPA of 6.56/7 and WAM of 87.33.
        Awarded the 2026 TD School Merit Award for
        Outstanding Academic Achievement. Developed
        advanced capabilities in machine learning,
        artificial intelligence, data innovation,
        research methods, and applied modelling.
        """
    ),

    timeline_card(
        "Bachelor of Business (Business Analytics)",
        "University of Wollongong · Completed December 2024",
        """
        Graduated with Distinction and a WAM of 75.5.
        Built a foundation in business analytics,
        data analysis, statistics, visualisation,
        business problem-solving, and communicating
        analytical findings within an organisational context.
        """
    ),

    timeline_card(
        "Sports Consultancy & Data Analyst Intern",
        "Futures Sport & Entertainment · September–November 2025",
        """
        Supported sponsorship analytics, brand exposure
        tracking, broadcast visibility validation,
        media monitoring, and stakeholder reporting.
        Contributed to workflows involving more than
        160,000 Supercars broadcast frame outputs,
        marathon-related analysis, and athlete media insights.
        """
    ),

    timeline_card(
        "Data Analytics Assistant",
        "Sportsyear · August–November 2024",
        """
        Analysed web and booking-related interactions
        using Google Analytics 4, focusing on promotional
        and event-calendar functionality. Prepared
        analytical summaries and presentations to help
        communicate user engagement and booking behaviour.
        """
    )

]

render_grid("grid-2", education_cards)


# ============================================================
# RESEARCH & PUBLICATIONS
# ============================================================

section_heading(
    "Research & Publications",
    "Cyber-risk research spanning temporal modelling, predictive evaluation, "
    "and actuarial frequency–severity analysis."
)

research_cards = [

    research_card(
        label="Phase 1 · Conference",
        status="Accepted",
        title="A Hawkes–Transformer Model for Cyber Risk Prediction",
        description="""
        Research on short-horizon cyber-risk prediction
        using a synthetic multivariate marked Hawkes
        benchmark with six interacting entities.
        Compared Transformer Hawkes Process,
        Neural Hawkes-based models, statistical baselines,
        and retrieval-style approaches to predict the
        highest-risk entity in the next time window.
        """,
        methods="""
        Hawkes Processes · Transformer Models ·
        Neural Hawkes · Temporal Dependence ·
        Controlled Model Evaluation
        """,
        outcome="""
        Accepted at AusDM 2026. The Transformer Hawkes
        Process achieved 0.8913 accuracy on the primary
        top-risk entity task within the synthetic benchmark.
        """
    ),

    research_card(
        label="Phase 2 · Journal",
        status="Accepted",
        title="Cyber Risk Frequency–Severity Modelling",
        description="""
        Extended the cyber-risk research toward
        system-wide event frequency, monetary loss severity,
        and aggregate cyber-risk assessment. Reconstructed
        the frequency target from the synthetic Hawkes
        event stream and independently calibrated severity
        assumptions using published cyber-loss information.
        """,
        methods="""
        Count Modelling · Frequency–Severity Framework ·
        Aggregate Loss · VaR · TVaR · Model Validation
        """,
        outcome="""
        Accepted by the MDPI journal Risks.
        The work considers aggregate loss and tail-risk
        measures while recognising the limitations
        of synthetic data and frequency forecasting.
        """
    )

]

render_grid("grid-2", research_cards)


# ============================================================
# WHAT I BRING
# ============================================================

section_heading(
    "What I Bring",
    "Four principles that guide the way I approach analytical work."
)

bring_cards = [

    info_card(
        "01 · Business Context",
        "Understand the decision",
        """
        I begin by defining what the analysis
        should achieve, which stakeholders need
        the output, and what evidence would make
        the result useful for business decisions.
        """
    ),

    info_card(
        "02 · Technical Execution",
        "Build reliable analytical workflows",
        """
        I work through data cleaning, validation,
        exploratory analysis, feature preparation,
        modelling, evaluation, and presentation
        with attention to reproducibility and clarity.
        """
    ),

    info_card(
        "03 · Communication",
        "Make results understandable",
        """
        I aim to explain findings through
        dashboards, visualisations, structured
        reports, and concise recommendations
        suitable for technical and business audiences.
        """
    ),

    info_card(
        "04 · Research Mindset",
        "Evaluate evidence critically",
        """
        Research experience has taught me to
        question assumptions, compare alternatives,
        validate results carefully, and distinguish
        promising experimental findings from
        reliable practical conclusions.
        """
    )

]

render_grid("grid-4", bring_cards)


# ============================================================
# TECHNICAL CAPABILITIES
# ============================================================

section_heading(
    "Technical Capabilities",
    "A practical overview of my programming, modelling, "
    "visualisation, and research skills."
)

capability_cards = [

    capability_card(
        "Data Preparation",
        "Data Cleaning & Analysis",
        "Python · SQL · Excel · pandas · NumPy · Power Query",
        """
        Cleaning and transforming data, performing
        exploratory analysis, validating records,
        engineering features, and preparing datasets
        for dashboards and predictive modelling.
        """
    ),

    capability_card(
        "Machine Learning",
        "Predictive & Deep Learning",
        "scikit-learn · PyTorch · Keras · CNNs · Transformers",
        """
        Classification, regression, transfer learning,
        sequence modelling, model comparison,
        statistical baselines, and performance evaluation.
        """
    ),

    capability_card(
        "Visualisation & BI",
        "Dashboards & Data Storytelling",
        "Streamlit · Plotly · Matplotlib · Tableau · Power BI",
        """
        Building interactive dashboards and analytical
        visualisations to explain KPIs, trends,
        model results, customer behaviour,
        and business performance.
        """
    ),

    capability_card(
        "Research & Communication",
        "Technical and Business Reporting",
        "Experimental Design · Literature Review · Research Writing",
        """
        Structuring research questions, testing
        analytical methods, identifying limitations,
        presenting results, and translating technical
        information into stakeholder-ready communication.
        """
    )

]

render_grid("grid-4", capability_cards)


# ============================================================
# HOW I WORK
# ============================================================

section_heading(
    "How I Work",
    "A practical, evidence-driven approach to solving data problems."
)

work_cards = [

    info_card(
        "Step 01",
        "Frame the problem",
        """
        Define the business or research question,
        the relevant outcome, and the criteria
        for evaluating success before starting
        detailed technical work.
        """
    ),

    info_card(
        "Step 02",
        "Develop and validate",
        """
        Prepare the data, establish suitable baselines,
        select appropriate techniques, test assumptions,
        and evaluate whether the results are reliable
        enough for the intended use.
        """
    ),

    info_card(
        "Step 03",
        "Communicate the outcome",
        """
        Present findings clearly, explain uncertainty
        and limitations, and identify practical next
        steps using charts, dashboards, reports,
        or research outputs.
        """
    )

]

render_grid("grid-3", work_cards)


# ============================================================
# CURRENT DIRECTION — UPDATED
# ============================================================

section_heading(
    "Current Direction",
    "Building on my academic research and applying those skills to practical analytics."
)

direction_cards = [

    timeline_card(
        "Applied Analytics & Data Products",
        "Streamlit · Python · Dashboarding · Business KPIs",
        """
        Developing practical data products that combine
        clean data pipelines, interactive visualisations,
        clear metrics, and business interpretation.

        My portfolio includes an integrated Retail
        Intelligence project combining sales analytics,
        RFM customer segmentation, and machine learning
        for historical purchase-inactivity prediction.

        Its KPIs and model results are calculated from
        the underlying retail transaction data.
        """
    ),

    timeline_card(
        "Research-Led Data Science",
        "Temporal Modelling · Cyber Risk · Statistical Evaluation",
        """
        Building on my accepted cyber-risk research
        through deeper understanding of model validation,
        temporal dependence, probabilistic modelling,
        uncertainty, and the relationship between
        advanced methods and practical use.
        """
    ),

    timeline_card(
        "Early-Career Opportunities",
        "Data Scientist · Data Analyst · Business Analyst",
        """
        Pursuing opportunities where I can combine
        technical analysis, business understanding,
        and stakeholder communication. I am interested
        in analytics and modelling roles that encourage
        continued technical development and meaningful
        problem-solving.
        """
    ),

    timeline_card(
        "Continued Learning",
        "Machine Learning · BI · Research Communication",
        """
        Strengthening my ability to choose suitable
        analytical methods, interpret models,
        communicate limitations, and deliver
        reliable solutions across different
        industries and data environments.
        """
    )

]

render_grid("grid-2", direction_cards)


# ============================================================
# RESUME & CONTACT
# ============================================================

render_html("""
    <div class="resume-panel">

        <div class="resume-title">
            Resume & Professional Links
        </div>

        <div class="resume-text">
            Download my resume for a summary of my education,
            technical skills, industry experience,
            and research background.

            You can also connect with me through
            LinkedIn or explore my work on GitHub.
        </div>

    </div>
""")

b1, b2, b3 = st.columns([1.2, 1, 1])

with b1:

    if RESUME_FILE.exists():

        with open(RESUME_FILE, "rb") as file:

            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Thomas_Nguyen_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    else:

        st.warning(
            "Resume not found: assets/resume.pdf"
        )

with b2:

    st.link_button(
        "💻 GitHub",
        GITHUB_URL,
        use_container_width=True
    )

with b3:

    st.link_button(
        "🔗 LinkedIn",
        LINKEDIN_URL,
        use_container_width=True
    )
