
import streamlit as st
from pathlib import Path
from textwrap import dedent
from html import escape

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Thomas Nguyen | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# PATHS AND LINKS
# ============================================================

ROOT = Path(__file__).resolve().parent
RESUME = ROOT / "assets" / "resume.pdf"

GITHUB_URL = "https://github.com/ThomasNguyennnnn"
LINKEDIN_URL = (
    "https://www.linkedin.com/in/thomas-tuan-nguyen/"
)
EMAIL = "thomas.nttn.au@gmail.com"

ABOUT_PAGE = "pages/1_About_Me.py"

PROJECT_PAGES = [
    "pages/2_Cyber_Risk_Forecasting.py",
    "pages/3_Sports_Broadcast_Analytics.py",
    "pages/4_Food101_CNN_Transfer_Learning.py",
    "pages/5_Retail_Intelligence.py",
]


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
        unsafe_allow_html=True,
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


# ============================================================
# COMPONENTS
# ============================================================

def metric_card(value, label, note):
    return compact_html(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-note">{note}</div>
        </div>
    """)


def project_card(
    number,
    category,
    title,
    description,
    skills,
    result,
    result_label,
):
    return compact_html(f"""
        <div class="project-card">

            <div class="project-heading">
                <span class="project-number">{escape(number)}</span>
                <span class="project-category">{escape(category)}</span>
            </div>

            <div class="project-title">
                {escape(title)}
            </div>

            <div class="project-description">
                {escape(description)}
            </div>

            <div class="project-skills">
                {escape(skills)}
            </div>

            <div class="project-result">
                <div class="result-label">
                    {escape(result_label)}
                </div>
                <div class="result-text">
                    {escape(result)}
                </div>
            </div>

        </div>
    """)


def render_project(
    number,
    category,
    title,
    description,
    skills,
    result,
    result_label,
    page,
):
    render_html(
        project_card(
            number,
            category,
            title,
            description,
            skills,
            result,
            result_label,
        )
    )

    if (ROOT / page).exists():
        st.page_link(
            page,
            label="Explore case study →",
            use_container_width=True,
        )
    else:
        st.caption(
            f"Page not found: {page}"
        )


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

/* --------------------------------------------------------
   GLOBAL
-------------------------------------------------------- */

:root {
    --text-dark: #0f172a;
    --text-main: #334155;
    --text-muted: #64748b;
    --blue: #2563eb;
    --violet: #7c3aed;
    --cyan: #0891b2;
    --border: rgba(129,140,248,0.28);
}

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

.block-container {
    padding-top: 5rem;
    padding-bottom: 4rem;
    max-width: 1240px;
}

footer {
    visibility: hidden;
}

/* --------------------------------------------------------
   SIDEBAR
-------------------------------------------------------- */

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

/* --------------------------------------------------------
   HERO
-------------------------------------------------------- */

.hero-card {
    padding: 3.2rem 3rem;
    border-radius: 38px;

    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(6,182,212,0.19),
            transparent 35%
        ),
        radial-gradient(
            circle at 0% 100%,
            rgba(124,58,237,0.12),
            transparent 38%
        ),
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97),
            rgba(239,246,255,0.90)
        );

    border: 1px solid rgba(129,140,248,0.34);

    box-shadow:
        0 28px 75px rgba(30,41,59,0.12),
        0 0 0 1px rgba(255,255,255,0.3) inset;

    backdrop-filter: blur(14px);
}

.hero-eyebrow {
    display: inline-block;
    padding: 0.43rem 0.9rem;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #dbeafe,
            #ede9fe,
            #ccfbf1
        );

    border: 1px solid rgba(99,102,241,0.25);

    color: #1e293b;
    font-size: 0.82rem;
    font-weight: 900;

    margin-bottom: 1.15rem;
}

.hero-name {
    color: #0f172a;
    font-size: 4.1rem;
    font-weight: 950;
    letter-spacing: -2px;
    line-height: 1.1;

    margin-bottom: 0.45rem;
}

.hero-gradient {
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

.hero-role {
    color: #1e293b;
    font-size: 1.25rem;
    font-weight: 900;
    line-height: 1.5;

    margin-bottom: 1.15rem;
}

.hero-description {
    max-width: 820px;
    color: #475569;
    font-size: 1.05rem;
    line-height: 1.82;
}

.hero-description p {
    margin: 0 0 0.75rem;
}

.hero-description b {
    color: #0f172a;
}

.hero-tags {
    margin-top: 1.3rem;
}

.hero-tag {
    display: inline-block;
    padding: 0.4rem 0.74rem;

    margin: 0.2rem 0.2rem 0.1rem 0;

    border-radius: 999px;

    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(167,139,250,0.28);

    color: #334155;
    font-size: 0.81rem;
    font-weight: 850;
}

/* --------------------------------------------------------
   SECTION HEADINGS
-------------------------------------------------------- */

.section-title {
    color: #0f172a;
    font-size: 1.95rem;
    font-weight: 950;
    letter-spacing: -0.5px;

    margin-top: 2.6rem;
    margin-bottom: 0.35rem;
}

.section-subtitle {
    color: #64748b;
    font-size: 1rem;
    line-height: 1.65;

    margin-bottom: 1.3rem;
}

/* --------------------------------------------------------
   METRICS
-------------------------------------------------------- */

.metric-grid {
    display: grid;
    grid-template-columns:
        repeat(4,minmax(0,1fr));

    gap: 1.15rem;
    align-items: stretch;
}

.metric-card {
    position: relative;
    overflow: hidden;

    padding: 1.35rem 1.35rem;
    min-height: 156px;
    height: 100%;

    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97),
            rgba(248,250,252,0.93)
        );

    border: 1px solid var(--border);

    box-shadow:
        0 14px 34px rgba(59,130,246,0.07);
}

.metric-card::before {
    content: "";

    position: absolute;
    top: 0;
    left: 0;

    width: 100%;
    height: 5px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );
}

.metric-value {
    color: #0f172a;
    font-size: 2rem;
    font-weight: 950;
    letter-spacing: -0.5px;

    margin-bottom: 0.3rem;
}

.metric-label {
    color: #4f46e5;
    font-size: 0.88rem;
    font-weight: 900;

    margin-bottom: 0.4rem;
}

.metric-note {
    color: #64748b;
    font-size: 0.81rem;
    line-height: 1.55;
}

/* --------------------------------------------------------
   PROJECT CARDS
-------------------------------------------------------- */

.project-card {
    position: relative;
    overflow: hidden;

    padding: 1.65rem 1.7rem;
    min-height: 320px;

    border-radius: 30px;

    background:
        radial-gradient(
            circle at 100% 0%,
            rgba(124,58,237,0.08),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97),
            rgba(248,250,252,0.93)
        );

    border: 1px solid var(--border);

    box-shadow:
        0 16px 38px rgba(59,130,246,0.08);

    display: flex;
    flex-direction: column;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.project-card::before {
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

.project-card:hover {
    transform: translateY(-3px);

    box-shadow:
        0 23px 54px rgba(79,70,229,0.13);
}

.project-heading {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.65rem;

    margin-bottom: 0.95rem;
}

.project-number {
    display: inline-block;

    padding: 0.36rem 0.7rem;
    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );

    color: #ffffff;
    font-size: 0.77rem;
    font-weight: 950;
}

.project-category {
    color: #4f46e5;
    font-size: 0.81rem;
    font-weight: 900;
}

.project-title {
    color: #0f172a;

    font-size: 1.28rem;
    font-weight: 950;
    line-height: 1.4;

    margin-bottom: 0.7rem;
}

.project-description {
    color: #475569;

    font-size: 0.94rem;
    line-height: 1.72;

    margin-bottom: 0.85rem;
}

.project-skills {
    color: #3730a3;

    font-size: 0.84rem;
    font-weight: 850;
    line-height: 1.6;

    margin-bottom: 1rem;
}

.project-result {
    margin-top: auto;

    padding: 0.9rem 1rem;
    border-radius: 18px;

    background:
        linear-gradient(
            90deg,
            rgba(219,234,254,0.85),
            rgba(237,233,254,0.82)
        );

    border: 1px solid rgba(167,139,250,0.25);
}

.result-label {
    color: #4f46e5;

    font-size: 0.75rem;
    font-weight: 950;
    letter-spacing: 0.4px;

    text-transform: uppercase;
    margin-bottom: 0.38rem;
}

.result-text {
    color: #334155;

    font-size: 0.9rem;
    font-weight: 750;
    line-height: 1.6;
}

/* --------------------------------------------------------
   PORTFOLIO NAVIGATION
-------------------------------------------------------- */

div[data-testid="stPageLink"] {
    margin-top: 0.2rem;
    margin-bottom: 1.6rem;
}

div[data-testid="stPageLink"] a {
    font-weight: 850 !important;
    color: #2563eb !important;
}

/* --------------------------------------------------------
   ABOUT TEASER
-------------------------------------------------------- */

.about-teaser {
    padding: 1.7rem 1.8rem;
    border-radius: 29px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.96),
            rgba(239,246,255,0.91)
        );

    border: 1px solid var(--border);

    box-shadow:
        0 15px 36px rgba(59,130,246,0.08);
}

.about-teaser-title {
    color: #0f172a;
    font-size: 1.2rem;
    font-weight: 950;

    margin-bottom: 0.65rem;
}

.about-teaser-text {
    color: #475569;
    font-size: 0.96rem;
    line-height: 1.75;
}

/* --------------------------------------------------------
   BUTTONS
-------------------------------------------------------- */

div.stDownloadButton > button,
div.stLinkButton > a {
    border-radius: 999px !important;

    font-weight: 850 !important;

    border:
        1px solid rgba(37,99,235,0.35) !important;

    background:
        rgba(255,255,255,0.88) !important;

    color: #0f172a !important;

    box-shadow:
        0 8px 20px rgba(59,130,246,0.10);
}

div.stDownloadButton > button *,
div.stLinkButton > a * {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

/* --------------------------------------------------------
   NATIVE TEXT CONTRAST
-------------------------------------------------------- */

.block-container [data-testid="stMarkdownContainer"] > p {
    color: #334155;
}

.block-container [data-testid="stCaptionContainer"] p {
    color: #475569 !important;
}

/* --------------------------------------------------------
   RESPONSIVE
-------------------------------------------------------- */

@media (max-width: 1050px) {

    .metric-grid {
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }

    .hero-name {
        font-size: 3.3rem;
    }
}

@media (max-width: 760px) {

    .block-container {
        padding-top: 4.5rem;
    }

    .hero-card {
        padding: 1.8rem 1.5rem;
    }

    .hero-name {
        font-size: 2.65rem;
    }

    .hero-role {
        font-size: 1.06rem;
    }

    .metric-grid {
        grid-template-columns: 1fr;
    }

    .metric-card,
    .project-card {
        min-height: auto;
    }

    .section-title {
        font-size: 1.65rem;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO — SHORT INTRODUCTION
# ============================================================

render_html("""
    <div class="hero-card">

        <div class="hero-eyebrow">
            Thomas Nguyen · Data Science Portfolio
        </div>

        <div class="hero-name">
            Turning data into
            <span class="hero-gradient">
                evidence-driven decisions.
            </span>
        </div>

        <div class="hero-role">
            Data Science · Machine Learning · Business Analytics
        </div>

        <div class="hero-description">

            <p>
                I'm <b>Thomas Nguyen</b>, a
                <b>University of Technology Sydney
                Data Science and Innovation graduate</b>,
                with experience across academic research,
                industry analytics, and practical
                machine-learning projects.
            </p>

            <p>
                Explore four selected projects spanning
                <b>cyber-risk research, sports analytics,
                computer vision, and interactive
                business intelligence</b>.
                Each case study highlights the methods,
                evidence, and limitations behind the work.
            </p>

        </div>

        <div class="hero-tags">
            <span class="hero-tag">Machine Learning</span>
            <span class="hero-tag">Data Analytics</span>
            <span class="hero-tag">Business Intelligence</span>
            <span class="hero-tag">Applied Research</span>
        </div>

    </div>
""")

st.write("")

cta1, cta2, cta3 = st.columns(
    [1, 1, 1],
    gap="medium",
)

with cta1:
    if (ROOT / ABOUT_PAGE).exists():
        st.page_link(
            ABOUT_PAGE,
            label="👤 More About Me",
            use_container_width=True,
        )

with cta2:
    if RESUME.exists():
        with open(RESUME, "rb") as file:
            st.download_button(
                "📄 Download Resume",
                data=file,
                file_name="Thomas_Nguyen_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

with cta3:
    st.link_button(
        "💻 View GitHub",
        GITHUB_URL,
        use_container_width=True,
    )


# ============================================================
# PORTFOLIO IN NUMBERS
# ============================================================

section_heading(
    "Portfolio at a Glance",
    "A few measurable highlights from the featured work."
)

render_grid("metric-grid", [

    metric_card(
        "4",
        "Featured Projects",
        "Research, industry, deep learning, and BI."
    ),

    metric_card(
        "2",
        "Accepted Research Papers",
        "AusDM 2026 conference and MDPI Risks journal."
    ),

    metric_card(
        "85.07%",
        "Food101 Test Accuracy",
        "Best fine-tuned ResNet50 configuration."
    ),

    metric_card(
        "160K+",
        "Broadcast Frame Outputs",
        "Scope of the Supercars analytics workflow."
    ),
])


# ============================================================
# FEATURED PROJECTS
# ============================================================

section_heading(
    "Featured Projects",
    "Four case studies, each demonstrating a different "
    "part of the data science and analytics workflow."
)

# ------------------------------------------------------------
# ROW 1
# ------------------------------------------------------------

left, right = st.columns(
    2,
    gap="large",
)

with left:

    render_project(
        number="01",
        category="Advanced Research · Machine Learning",
        title="Cyber Risk Modelling & Forecasting",
        description=(
            "Two-phase research investigating cyber-event "
            "dependence, entity-risk prediction, numerical "
            "frequency forecasting, and aggregate-loss risk."
        ),
        skills=(
            "Python · Hawkes Processes · Transformers · "
            "GRU · Statistical Modelling"
        ),
        result=(
            "89.13% top-risk entity accuracy in Phase 1; "
            "17.6% MAE improvement in the independent "
            "synthetic GRU evaluation in Phase 2."
        ),
        result_label="Research evidence",
        page=PROJECT_PAGES[0],
    )

with right:

    render_project(
        number="02",
        category="Industry Experience · Commercial Analytics",
        title="Sports Broadcast Analytics",
        description=(
            "Sponsorship and broadcast-exposure analysis "
            "during an industry placement at Futures Sport "
            "& Entertainment, including data validation "
            "and media-monitoring support."
        ),
        skills=(
            "Excel · Power BI · TVEyes · "
            "Data Quality · Commercial Reporting"
        ),
        result=(
            "Approximately 200 placement hours; "
            "worked within a Supercars analytics workflow "
            "involving 160K+ broadcast frame outputs."
        ),
        result_label="Industry scope",
        page=PROJECT_PAGES[1],
    )


# ------------------------------------------------------------
# ROW 2
# ------------------------------------------------------------

left, right = st.columns(
    2,
    gap="large",
)

with left:

    render_project(
        number="03",
        category="Deep Learning · Computer Vision",
        title="Food101 CNN Transfer Learning",
        description=(
            "Compared frozen ResNet50 feature extraction "
            "with selective layer fine-tuning to improve "
            "multi-class food-image classification."
        ),
        skills=(
            "Python · PyTorch · ResNet50 · "
            "Transfer Learning · Model Evaluation"
        ),
        result=(
            "Test accuracy improved from 61.86% "
            "to 85.07% — a gain of 23.21 "
            "percentage points."
        ),
        result_label="Measured improvement",
        page=PROJECT_PAGES[2],
    )

with right:

    render_project(
        number="04",
        category="Business Intelligence · Applied ML",
        title="Retail Intelligence",
        description=(
            "An interactive retail analytics dashboard "
            "combining sales KPIs, product performance, "
            "RFM customer segmentation, and historical "
            "purchase-inactivity prediction."
        ),
        skills=(
            "Python · pandas · Plotly · Streamlit · "
            "scikit-learn · Customer Analytics"
        ),
        result=(
            "Real UCI transaction data, calculated KPIs, "
            "and three-model evaluation for a defined "
            "60-day purchasing-inactivity target."
        ),
        result_label="Interactive analytics",
        page=PROJECT_PAGES[3],
    )


# ============================================================
# ABOUT ME TEASER — NOT A SECOND BIOGRAPHY
# ============================================================

section_heading(
    "Behind the Projects",
    "A brief introduction here; the full background "
    "is available on the About Me page."
)

render_html("""
    <div class="about-teaser">

        <div class="about-teaser-title">
            Research discipline meets business understanding.
        </div>

        <div class="about-teaser-text">

            My approach combines careful data preparation,
            measurable model evaluation, and clear communication
            of results.

            For more detail on my education, industry
            experience, research publications, academic
            recognition, and technical capabilities,
            visit the dedicated About Me page.

        </div>

    </div>
""")

st.write("")

if (ROOT / ABOUT_PAGE).exists():
    st.page_link(
        ABOUT_PAGE,
        label="Read my full professional background →",
    )


# ============================================================
# SIMPLE CONTACT SECTION
# ============================================================

section_heading(
    "Connect",
    "Interested in data science, analytics, research, "
    "or graduate opportunities? Let's connect."
)

col1, col2, col3 = st.columns(
    3,
    gap="medium",
)

with col1:
    st.link_button(
        "✉️ Email",
        f"mailto:{EMAIL}",
        use_container_width=True,
    )

with col2:
    st.link_button(
        "🔗 LinkedIn",
        LINKEDIN_URL,
        use_container_width=True,
    )

with col3:
    st.link_button(
        "💻 GitHub",
        GITHUB_URL,
        use_container_width=True,
    )
