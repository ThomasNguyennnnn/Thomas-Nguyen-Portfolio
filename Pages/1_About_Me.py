import streamlit as st
from pathlib import Path
import base64
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="About Me | Thomas Nguyen",
    page_icon="👤",
    layout="wide"
)

PROFILE_IMAGE = Path("assets/profile_photo.jpg")
RESUME_FILE = Path("assets/resume.pdf")


# ============================================================
# Helper functions
# ============================================================
def image_to_base64(image_path: Path) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


def get_image_mime(image_path: Path) -> str:
    suffix = image_path.suffix.lower()
    if suffix == ".png":
        return "image/png"
    return "image/jpeg"


def info_card(label, title, text):
    return dedent(f"""
    <div class="info-card">
        <div class="card-label">{label}</div>
        <div class="card-title">{title}</div>
        <div class="card-text">{text}</div>
    </div>
    """)


def timeline_card(title, meta, text):
    return dedent(f"""
    <div class="timeline-card">
        <div class="timeline-title">{title}</div>
        <div class="timeline-meta">{meta}</div>
        <div class="timeline-text">{text}</div>
    </div>
    """)


def capability_card(label, title, tools, text):
    return dedent(f"""
    <div class="capability-card">
        <div class="card-label">{label}</div>
        <div class="capability-title">{title}</div>
        <div class="capability-tools">{tools}</div>
        <div class="capability-text">{text}</div>
    </div>
    """)


# ============================================================
# CSS
# ============================================================
st.markdown(
    """
<style>
:root {
    --text-900: #0f172a;
    --text-700: #334155;
    --text-500: #64748b;
    --blue: #2563eb;
    --cyan: #06b6d4;
    --violet: #7c3aed;
}

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(79, 70, 229, 0.18), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(6, 182, 212, 0.22), transparent 26%),
        radial-gradient(circle at 50% 92%, rgba(37, 99, 235, 0.14), transparent 34%),
        linear-gradient(135deg, #edf4ff 0%, #f7f1ff 46%, #e9feff 100%);
}

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 4rem;
    max-width: 1280px;
}

footer, header {
    visibility: hidden;
}

html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", sans-serif;
}

section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at top left, rgba(37, 99, 235, 0.35), transparent 30%),
        radial-gradient(circle at bottom right, rgba(124, 58, 237, 0.25), transparent 34%),
        linear-gradient(180deg, #020617 0%, #0f172a 55%, #1e1b4b 100%);
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

/* --------------------------------------------------------
   Hero
-------------------------------------------------------- */
.hero-card {
    padding: 2.7rem 2.9rem;
    border-radius: 36px;
    background:
        radial-gradient(circle at 10% 0%, rgba(37, 99, 235, 0.22), transparent 28%),
        radial-gradient(circle at 100% 0%, rgba(6, 182, 212, 0.20), transparent 24%),
        radial-gradient(circle at 85% 80%, rgba(124, 58, 237, 0.16), transparent 30%),
        linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(239, 246, 255, 0.88) 100%);
    border: 1px solid rgba(129, 140, 248, 0.36);
    box-shadow:
        0 30px 80px rgba(30, 41, 59, 0.16),
        0 0 0 1px rgba(255,255,255,0.38) inset;
    margin-bottom: 2.4rem;
    overflow: hidden;
    backdrop-filter: blur(14px);
}

.eyebrow {
    display: inline-block;
    padding: 0.46rem 0.92rem;
    border-radius: 999px;
    background: linear-gradient(90deg, #dbeafe, #ede9fe, #ccfbf1);
    color: #0f172a;
    border: 1px solid rgba(37, 99, 235, 0.28);
    font-size: 0.84rem;
    font-weight: 850;
    margin-bottom: 1rem;
}

.page-title {
    font-size: 3.7rem;
    font-weight: 950;
    letter-spacing: -2px;
    color: #0f172a;
    margin-bottom: 0.4rem;
    line-height: 1.05;
}

.gradient-text {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 1.28rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 1rem;
}

.body-text {
    font-size: 1.03rem;
    line-height: 1.8;
    color: #334155;
}

.profile-image-box {
    width: 310px;
    height: 310px;
    padding: 0.65rem;
    border-radius: 40px;
    background: linear-gradient(135deg, #2563eb, #7c3aed, #06b6d4);
    box-shadow:
        0 28px 72px rgba(37, 99, 235, 0.28),
        0 0 44px rgba(6, 182, 212, 0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: auto;
}

.profile-image-box img {
    width: 290px;
    height: 290px;
    object-fit: cover;
    object-position: center;
    border-radius: 34px;
    display: block;
}

/* --------------------------------------------------------
   Section headers
-------------------------------------------------------- */
.section-title {
    font-size: 1.9rem;
    font-weight: 950;
    color: #0f172a;
    margin-top: 2.5rem;
    margin-bottom: 0.35rem;
    letter-spacing: -0.5px;
}

.section-subtitle {
    font-size: 1rem;
    color: #64748b;
    margin-bottom: 1.4rem;
    line-height: 1.6;
}

/* --------------------------------------------------------
   Grids
-------------------------------------------------------- */
.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.25rem;
    align-items: stretch;
}

/* --------------------------------------------------------
   General cards
-------------------------------------------------------- */
.info-card {
    padding: 1.55rem 1.6rem;
    border-radius: 28px;
    background:
        radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    min-height: 260px;
    height: 100%;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    display: flex;
    flex-direction: column;
}

.info-card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
}

.card-label {
    display: inline-block;
    width: fit-content;
    padding: 0.32rem 0.72rem;
    border-radius: 999px;
    background: linear-gradient(90deg, #dbeafe, #ede9fe, #ccfbf1);
    color: #0f172a;
    border: 1px solid rgba(167, 139, 250, 0.42);
    font-size: 0.77rem;
    font-weight: 900;
    margin-bottom: 0.8rem;
}

.card-title {
    font-size: 1.18rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.55rem;
}

.card-text {
    font-size: 0.95rem;
    line-height: 1.68;
    color: #475569;
}

/* --------------------------------------------------------
   Timeline cards
-------------------------------------------------------- */
.timeline-card {
    padding: 1.35rem 1.5rem;
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.22);
    box-shadow: 0 14px 34px rgba(59, 130, 246, 0.08);
    min-height: 210px;
    height: 100%;
}

.timeline-title {
    font-size: 1.05rem;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 0.3rem;
}

.timeline-meta {
    font-size: 0.88rem;
    font-weight: 800;
    color: #4f46e5;
    margin-bottom: 0.55rem;
}

.timeline-text {
    font-size: 0.94rem;
    line-height: 1.65;
    color: #475569;
}

/* --------------------------------------------------------
   Capability cards
-------------------------------------------------------- */
.capability-card {
    padding: 1.45rem 1.5rem;
    border-radius: 26px;
    background:
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.08), transparent 28%),
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    min-height: 245px;
    height: 100%;
    position: relative;
    overflow: hidden;
}

.capability-card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
}

.capability-title {
    font-size: 1.08rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.55rem;
}

.capability-tools {
    font-size: 0.9rem;
    line-height: 1.55;
    color: #3730a3;
    font-weight: 850;
    margin-bottom: 0.75rem;
}

.capability-text {
    font-size: 0.9rem;
    line-height: 1.62;
    color: #475569;
}

/* --------------------------------------------------------
   Resume panel
-------------------------------------------------------- */
.resume-panel {
    padding: 1.5rem 1.6rem;
    border-radius: 28px;
    background:
        radial-gradient(circle at top left, rgba(124, 58, 237, 0.10), transparent 30%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(239,246,255,0.94));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 16px 42px rgba(59, 130, 246, 0.09);
    color: #334155;
    line-height: 1.75;
    margin-top: 1.8rem;
}

div.stDownloadButton > button {
    border-radius: 999px;
    font-weight: 900;
    height: 2.9rem;
    border: 1px solid rgba(37, 99, 235, 0.35);
    background: rgba(255,255,255,0.82);
    color: #0f172a;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.10);
}

/* --------------------------------------------------------
   Mobile
-------------------------------------------------------- */
@media (max-width: 900px) {
    .page-title {
        font-size: 2.6rem;
    }

    .hero-card {
        padding: 1.8rem 1.5rem;
    }

    .profile-image-box {
        width: 260px;
        height: 260px;
        margin: 1.5rem auto 0 auto;
    }

    .profile-image-box img {
        width: 242px;
        height: 242px;
    }

    .grid-2,
    .grid-3,
    .grid-4 {
        grid-template-columns: 1fr;
    }
}
</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# Hero section
# ============================================================
st.markdown('<div class="hero-card">', unsafe_allow_html=True)

left, right = st.columns([2.2, 1], vertical_alignment="center")

with left:
    st.markdown(
        """
        <div class="eyebrow">About Me</div>
        <div class="page-title">I connect <span class="gradient-text">data science</span> with business decisions.</div>
        <div class="subtitle">Data Scientist · Business Analyst · Data Analyst</div>
        <div class="body-text">
            I am <b>Thomas Nguyen</b>, a Master of Data Science and Innovation student at the 
            <b>University of Technology Sydney</b>, with a background in business analytics, machine learning, 
            data visualisation, and applied analytics.
            <br><br>
            Alongside my coursework, I am also developing academic research experience through a university-supervised 
            research project. This allows me to apply advanced data science methods to a structured research problem, 
            strengthen my technical reasoning, and communicate findings in a rigorous academic format.
            <br><br>
            My goal is to build data solutions that are not only technically sound, but also useful for decision-making. 
            I enjoy working at the intersection of modelling, business insight, and visual communication.
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    if PROFILE_IMAGE.exists():
        img_base64 = image_to_base64(PROFILE_IMAGE)
        img_mime = get_image_mime(PROFILE_IMAGE)

        st.markdown(
            f"""
            <div class="profile-image-box">
                <img src="data:{img_mime};base64,{img_base64}" alt="Thomas Nguyen profile photo">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Add your profile photo to assets/profile_photo.jpg")

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# Professional profile
# ============================================================
st.markdown('<div class="section-title">Professional Profile</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A short overview of my background, strengths, and career direction.</div>',
    unsafe_allow_html=True
)

profile_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Analytical Foundation",
        "Business-first data thinking",
        "My background in business analytics helps me approach data problems from both a technical and commercial perspective. I focus on understanding the decision behind the analysis before choosing the model, metric, or dashboard."
    )}

    {info_card(
        "Technical Development",
        "Machine learning and data products",
        "Through my recent projects, I have worked with predictive modelling, deep learning, time-dependent event data, computer vision, and interactive Streamlit applications. I enjoy building end-to-end workflows from data preparation to evaluation and communication."
    )}

    {info_card(
        "Academic Development",
        "Research-guided data science practice",
        "In addition to applied analytics projects, I am building academic research experience through supervised university research. This has strengthened my ability to work with research questions, literature, experimental design, model evaluation, and structured technical reporting."
    )}
</div>
""")
st.markdown(profile_html, unsafe_allow_html=True)


# ============================================================
# What I bring
# ============================================================
st.markdown('<div class="section-title">What I Bring</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A combination of business understanding, technical execution, communication, and research capability.</div>',
    unsafe_allow_html=True
)

bring_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "01",
        "Business context",
        "I do not treat analysis as just producing charts or model scores. I try to understand the business question, the stakeholder, and the practical decision that the data should support."
    )}

    {info_card(
        "02",
        "Technical execution",
        "I can work across data cleaning, exploratory analysis, feature engineering, model development, evaluation, and visualisation using Python, SQL, Excel, Streamlit, and machine learning libraries."
    )}

    {info_card(
        "03",
        "Clear communication",
        "I aim to communicate findings in a way that is clear, structured, and useful for both technical and non-technical audiences through dashboards, reports, and concise business recommendations."
    )}

    {info_card(
        "04",
        "Research mindset",
        "My supervised academic research experience helps me approach problems with stronger structure, evidence-based reasoning, careful evaluation, and a clearer connection between methodology and results."
    )}
</div>
""")
st.markdown(bring_html, unsafe_allow_html=True)


# ============================================================
# Education and experience
# ============================================================
st.markdown('<div class="section-title">Education & Experience</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The academic, research, and professional experiences shaping my data career.</div>',
    unsafe_allow_html=True
)

education_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Master of Data Science and Innovation",
        "University of Technology Sydney",
        "Postgraduate study focused on machine learning, artificial intelligence, statistical thinking, data innovation, and applied problem-solving. My current work includes advanced modelling projects such as cyber-risk forecasting using Hawkes-based and Transformer-based sequence models."
    )}

    {timeline_card(
        "Supervised Academic Research Project",
        "Cyber Risk Forecasting · Hawkes Processes · Sequence Models",
        "Currently developing a research project under university academic supervision, focusing on cyber-risk forecasting using Hawkes-based and Transformer-based sequence models. This project involves literature review, synthetic data simulation, model comparison, evaluation, and academic-style research reporting."
    )}

    {timeline_card(
        "Bachelor of Business Analytics",
        "University of Wollongong",
        "Developed a business analytics foundation across data analysis, visualisation, statistics, decision-making, and business communication. This background helps me frame technical work around practical organisational value."
    )}

    {timeline_card(
        "Sports Consultancy & Data Analyst Intern",
        "Futures Sport & Entertainment",
        "Worked on sports sponsorship analytics, broadcast visibility, brand exposure tracking, media monitoring, data validation, and stakeholder reporting. This experience strengthened my ability to transform raw media and exposure data into commercial insights."
    )}
</div>
""")
st.markdown(education_html, unsafe_allow_html=True)


# ============================================================
# Technical capabilities
# ============================================================
st.markdown('<div class="section-title">Technical Capabilities</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A broader view of the tools, methods, and analytical capabilities I use across projects.</div>',
    unsafe_allow_html=True
)

capabilities_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Data Preparation",
        "Data cleaning and analysis",
        "Python · SQL · Excel · pandas · NumPy · Power Query",
        "Preparing, cleaning, transforming, validating, and exploring data for analysis, dashboards, and modelling workflows."
    )}

    {capability_card(
        "Machine Learning",
        "Predictive modelling",
        "scikit-learn · PyTorch · classification · regression · model evaluation",
        "Building and evaluating predictive models, comparing baselines, interpreting performance, and connecting outputs to practical decisions."
    )}

    {capability_card(
        "Visualisation & BI",
        "Dashboards and storytelling",
        "Streamlit · Plotly · Matplotlib · Tableau · Power BI",
        "Creating visual outputs and interactive dashboards that communicate trends, comparisons, KPIs, and business insights clearly."
    )}

    {capability_card(
        "Research & Communication",
        "Technical reporting",
        "Literature review · experimental design · research writing · stakeholder reporting",
        "Structuring research questions, explaining methods, presenting results, and translating technical analysis into clear written communication."
    )}
</div>
""")
st.markdown(capabilities_html, unsafe_allow_html=True)


# ============================================================
# How I work
# ============================================================
st.markdown('<div class="section-title">How I Work</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">My preferred approach to analytics and data science problems.</div>',
    unsafe_allow_html=True
)

work_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "01",
        "Frame the decision",
        "I start by asking what decision the analysis is meant to support. This helps define the right metrics, level of detail, and communication style."
    )}

    {info_card(
        "02",
        "Build with transparency",
        "I prefer clear workflows: clean data, documented assumptions, suitable models, and evaluation methods that can be explained rather than treated as a black box."
    )}

    {info_card(
        "03",
        "Translate results into action",
        "I aim to turn technical results into understandable insights, visual outputs, and recommendations that can help stakeholders make better decisions."
    )}
</div>
""")
st.markdown(work_html, unsafe_allow_html=True)


# ============================================================
# Current focus
# ============================================================
st.markdown('<div class="section-title">Current Focus</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">What I am currently building and improving.</div>',
    unsafe_allow_html=True
)

current_focus_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Developing applied analytics products",
        "Streamlit · GitHub · Business analytics · Public datasets",
        "I am building interactive analytics products that demonstrate how raw data can be transformed into dashboards, KPIs, customer insights, and practical business recommendations. The goal is to show not only technical ability, but also decision-oriented thinking."
    )}

    {timeline_card(
        "Strengthening research-led data science skills",
        "Predictive modelling · Sequence models · Academic reporting",
        "I am continuing to develop academic and applied data science skills through supervised research and practical modelling projects. My focus is on building models that are carefully evaluated, clearly explained, and connected to real analytical problems."
    )}
</div>
""")
st.markdown(current_focus_html, unsafe_allow_html=True)


# ============================================================
# Resume panel
# ============================================================
st.markdown(
    """
    <div class="resume-panel">
        <b>Resume</b><br>
        Download my resume for a more detailed summary of my education, experience, technical skills, and project background.
    </div>
    """,
    unsafe_allow_html=True
)

if RESUME_FILE.exists():
    with open(RESUME_FILE, "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Thomas_Nguyen_Resume.pdf",
            mime="application/pdf"
        )
else:
    st.warning("Resume not found. Please add resume.pdf to the assets folder.")