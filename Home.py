import streamlit as st
from pathlib import Path
import base64
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Thomas Nguyen | Data Science Portfolio",
    page_icon="📊",
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
    if suffix in [".jpg", ".jpeg"]:
        return "image/jpeg"
    return "image/jpeg"


def project_card(label, status, title, description, skills, value, status_type="completed", extra_class=""):
    status_class = "project-status" if status_type == "completed" else "project-status-upcoming"

    return dedent(f"""
    <div class="project-card {extra_class}">
        <div class="project-topline">
            <span class="project-label">{label}</span>
            <span class="{status_class}">{status}</span>
        </div>
        <div class="project-title">{title}</div>
        <div class="project-desc">{description}</div>
        <div class="project-skills">{skills}</div>
        <div class="project-highlight">{value}</div>
    </div>
    """)


def focus_card(icon, title, text):
    return dedent(f"""
    <div class="focus-card">
        <div class="focus-icon">{icon}</div>
        <div class="focus-title">{title}</div>
        <div class="focus-text">{text}</div>
    </div>
    """)


# ============================================================
# Custom CSS
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
    --indigo: #4f46e5;

    --glass-border: rgba(129, 140, 248, 0.30);
    --glass-card: rgba(255, 255, 255, 0.90);
}

/* --------------------------------------------------------
   Global futuristic background
-------------------------------------------------------- */
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
    color: var(--text-900);
}

/* --------------------------------------------------------
   Sidebar
-------------------------------------------------------- */
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
   Hero section
-------------------------------------------------------- */
.hero-card {
    padding: 2.75rem 2.9rem;
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
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(14px);
}

.hero-card:before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(115deg, transparent 0%, rgba(255,255,255,0.30) 42%, transparent 70%);
    pointer-events: none;
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
    letter-spacing: 0.1px;
    box-shadow: 0 8px 24px rgba(6, 182, 212, 0.10);
}

.hero-title {
    font-size: 4.2rem;
    font-weight: 950;
    letter-spacing: -2.2px;
    color: #0f172a;
    margin-bottom: 0.25rem;
    line-height: 1.02;
}

.hero-gradient {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.36rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 1.2rem;
}

.hero-body {
    font-size: 1.035rem;
    line-height: 1.85;
    color: #334155;
    max-width: 810px;
}

.career-strip {
    margin-top: 1.25rem;
    padding: 1rem 1.1rem;
    border-left: 4px solid #2563eb;
    background: linear-gradient(
        90deg,
        rgba(37, 99, 235, 0.14),
        rgba(124, 58, 237, 0.10),
        rgba(6, 182, 212, 0.10)
    );
    border-radius: 0 18px 18px 0;
    color: #0f172a;
    font-size: 0.96rem;
    font-weight: 800;
}

/* --------------------------------------------------------
   Profile image section - larger image, no repeated card
-------------------------------------------------------- */
.profile-area {
    width: 370px;
    margin-left: auto;
    margin-right: 0;
    transform: translateX(18px);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.profile-image-box {
    width: 305px;
    height: 305px;
    padding: 0.65rem;
    border-radius: 42px;
    background: linear-gradient(135deg, #2563eb, #7c3aed, #06b6d4);
    box-shadow:
        0 28px 72px rgba(37, 99, 235, 0.28),
        0 0 44px rgba(6, 182, 212, 0.18);

    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-image-box img {
    width: 285px;
    height: 285px;
    object-fit: cover;
    object-position: center;
    border-radius: 34px;
    display: block;
}

/* --------------------------------------------------------
   Section headers
-------------------------------------------------------- */
.section-title {
    font-size: 1.95rem;
    font-weight: 950;
    color: var(--text-900);
    margin-top: 2.7rem;
    margin-bottom: 0.35rem;
    letter-spacing: -0.6px;
}

.section-subtitle {
    font-size: 1rem;
    color: var(--text-500);
    margin-bottom: 1.45rem;
    line-height: 1.6;
}

/* --------------------------------------------------------
   Snapshot cards
-------------------------------------------------------- */
.snapshot-card {
    padding: 1.28rem 1.28rem;
    border-radius: 25px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.93), rgba(248,250,252,0.90));
    border: 1px solid rgba(167, 139, 250, 0.26);
    box-shadow:
        0 16px 36px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.26) inset;
    min-height: 142px;
    height: 100%;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
}

.snapshot-card:before {
    content: "";
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
}

.snapshot-label {
    font-size: 0.82rem;
    font-weight: 800;
    color: var(--text-500);
    margin-bottom: 0.45rem;
}

.snapshot-value {
    font-size: 1.42rem;
    line-height: 1.25;
    font-weight: 950;
    color: var(--text-900);
    letter-spacing: -0.4px;
}

.snapshot-note {
    margin-top: 0.45rem;
    font-size: 0.78rem;
    color: var(--text-500);
    line-height: 1.35;
}

/* --------------------------------------------------------
   Focus cards grid
-------------------------------------------------------- */
.focus-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.focus-card {
    padding: 1.55rem 1.55rem;
    border-radius: 28px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.94), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    min-height: 250px;
    height: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    backdrop-filter: blur(10px);
}

.focus-card:before {
    content: "";
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    height: 6px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
}

.focus-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
    line-height: 1;
}

.focus-title {
    font-size: 1.18rem;
    font-weight: 950;
    color: var(--text-900);
    margin-bottom: 0.55rem;
}

.focus-text {
    font-size: 0.95rem;
    line-height: 1.66;
    color: #475569;
}

/* --------------------------------------------------------
   Featured projects grid
-------------------------------------------------------- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.35rem;
    align-items: stretch;
}

.project-card {
    padding: 1.68rem 1.78rem;
    border-radius: 30px;
    background:
        radial-gradient(circle at 100% 0%, rgba(124, 58, 237, 0.10), transparent 24%),
        radial-gradient(circle at 0% 100%, rgba(6, 182, 212, 0.06), transparent 28%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(248,250,252,0.93));
    border: 1px solid rgba(129, 140, 248, 0.34);
    box-shadow:
        0 18px 46px rgba(30, 41, 59, 0.10),
        0 0 0 1px rgba(255,255,255,0.22) inset;
    position: relative;
    overflow: hidden;
    min-height: 340px;
    height: 100%;
    display: flex;
    flex-direction: column;
    backdrop-filter: blur(10px);
}

.project-card:after {
    content: "";
    position: absolute;
    right: -42px;
    top: -42px;
    width: 118px;
    height: 118px;
    border-radius: 50%;
    background: rgba(124, 58, 237, 0.10);
}

.project-card:hover {
    transform: translateY(-4px);
    border-color: rgba(124, 58, 237, 0.55);
    box-shadow:
        0 24px 60px rgba(79, 70, 229, 0.16),
        0 0 28px rgba(6, 182, 212, 0.08);
    transition: 0.18s ease;
}

.project-topline {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.82rem;
    gap: 0.7rem;
    position: relative;
    z-index: 1;
}

.project-label {
    display: inline-block;
    padding: 0.34rem 0.76rem;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(219, 234, 254, 0.96), rgba(237, 233, 254, 0.96));
    color: #3730a3;
    border: 1px solid rgba(167, 139, 250, 0.50);
    font-size: 0.76rem;
    font-weight: 900;
    white-space: nowrap;
}

.project-status {
    display: inline-block;
    padding: 0.31rem 0.7rem;
    border-radius: 999px;
    background: #dcfce7;
    color: #047857;
    border: 1px solid #86efac;
    font-size: 0.74rem;
    font-weight: 900;
    white-space: nowrap;
}

.project-status-upcoming {
    display: inline-block;
    padding: 0.31rem 0.7rem;
    border-radius: 999px;
    background: #fff7ed;
    color: #c2410c;
    border: 1px solid #fdba74;
    font-size: 0.74rem;
    font-weight: 900;
    white-space: nowrap;
}

.project-title {
    font-size: 1.32rem;
    font-weight: 950;
    color: var(--text-900);
    margin-bottom: 0.58rem;
    line-height: 1.25;
    position: relative;
    z-index: 1;
}

.project-desc {
    font-size: 0.97rem;
    line-height: 1.68;
    color: #475569;
    margin-bottom: 0.95rem;
    position: relative;
    z-index: 1;
}

.project-skills {
    font-size: 0.88rem;
    color: #334155;
    font-weight: 750;
    line-height: 1.55;
    position: relative;
    z-index: 1;
}

.project-highlight {
    margin-top: auto;
    padding: 0.82rem 0.94rem;
    border-radius: 18px;
    background: linear-gradient(90deg, rgba(219, 234, 254, 0.84), rgba(237, 233, 254, 0.78));
    border: 1px solid rgba(167, 139, 250, 0.26);
    color: #475569;
    font-size: 0.86rem;
    line-height: 1.5;
    position: relative;
    z-index: 1;
}

.project-card-wide {
    grid-column: span 2;
    min-height: 255px;
}

/* --------------------------------------------------------
   Skills cards
-------------------------------------------------------- */
.skills-card {
    padding: 1.55rem 1.6rem;
    border-radius: 27px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(248,250,252,0.93));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    margin-bottom: 1.15rem;
    position: relative;
    overflow: hidden;
    min-height: 190px;
    backdrop-filter: blur(10px);
}

.skills-card:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 6px;
    height: 100%;
    background: linear-gradient(180deg, #2563eb, #7c3aed, #06b6d4);
}

.skills-category {
    display: inline-block;
    padding: 0.32rem 0.72rem;
    border-radius: 999px;
    background: linear-gradient(90deg, #dbeafe, #ede9fe, #ccfbf1);
    color: var(--text-900);
    border: 1px solid rgba(167, 139, 250, 0.42);
    font-size: 0.77rem;
    font-weight: 900;
    margin-bottom: 0.8rem;
}

.skills-title {
    font-size: 1.16rem;
    font-weight: 950;
    color: var(--text-900);
    margin-bottom: 0.5rem;
}

.skills-list {
    font-size: 0.97rem;
    line-height: 1.7;
    color: #334155;
    font-weight: 750;
    margin-bottom: 0.75rem;
}

.skills-note {
    font-size: 0.88rem;
    line-height: 1.55;
    color: var(--text-500);
}

/* --------------------------------------------------------
   Contact
-------------------------------------------------------- */
.contact-panel {
    padding: 1.75rem 1.85rem;
    border-radius: 29px;
    background:
        radial-gradient(circle at top left, rgba(124, 58, 237, 0.10), transparent 30%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(239,246,255,0.94));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 42px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.22) inset;
    color: #334155;
    line-height: 1.9;
    min-height: 180px;
    backdrop-filter: blur(10px);
}

.contact-title {
    font-size: 1.15rem;
    font-weight: 950;
    color: var(--text-900);
    margin-bottom: 0.7rem;
}

.contact-note {
    padding: 1.48rem 1.58rem;
    border-radius: 27px;
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(167, 139, 250, 0.24);
    color: #475569;
    line-height: 1.72;
    box-shadow:
        0 14px 36px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.22) inset;
    min-height: 180px;
    backdrop-filter: blur(10px);
}

/* --------------------------------------------------------
   Buttons
-------------------------------------------------------- */
div.stDownloadButton > button {
    border-radius: 999px;
    font-weight: 900;
    height: 2.9rem;
    border: 1px solid rgba(37, 99, 235, 0.35);
    background: rgba(255,255,255,0.82);
    color: #0f172a;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.10);
    backdrop-filter: blur(8px);
}

div.stDownloadButton > button,
div.stDownloadButton > button * {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    opacity: 1 !important;
}

div.stDownloadButton > button:hover {
    border-color: #2563eb;
    box-shadow: 0 10px 28px rgba(37, 99, 235, 0.18);
    color: #0f172a;
}

div.stLinkButton > a {
    border-radius: 999px;
    font-weight: 900;
    height: 2.9rem;
    border: 1px solid rgba(37, 99, 235, 0.35);
    background: rgba(255,255,255,0.82);
    color: #0f172a;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.10);
    backdrop-filter: blur(8px);
}

div.stLinkButton > a,
div.stLinkButton > a * {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    opacity: 1 !important;
}

div.stLinkButton > a:hover {
    border-color: #2563eb;
    box-shadow: 0 10px 28px rgba(37, 99, 235, 0.18);
    color: #0f172a;
}

/* --------------------------------------------------------
   Mobile responsiveness
-------------------------------------------------------- */
@media (max-width: 900px) {
    .hero-title {
        font-size: 2.8rem;
    }

    .hero-card {
        padding: 1.8rem 1.5rem;
    }

    .profile-area {
        width: 100%;
        margin-left: 0;
        margin-right: 0;
        transform: translateX(0px);
        align-items: center;
        margin-top: 1.5rem;
    }

    .profile-image-box {
        width: 285px;
        height: 285px;
    }

    .profile-image-box img {
        width: 267px;
        height: 267px;
    }

    .focus-grid {
        grid-template-columns: 1fr;
    }

    .projects-grid {
        grid-template-columns: 1fr;
    }

    .project-card-wide {
        grid-column: span 1;
    }

    .project-topline {
        display: block;
    }

    .project-status,
    .project-status-upcoming {
        margin-top: 0.45rem;
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

hero_left, hero_right = st.columns([2.05, 1.35], vertical_alignment="center")

with hero_left:
    st.markdown(
        """
        <div class="eyebrow">Data Science | Data Analytics | Business Analytics</div>
        <div class="hero-title">Thomas <span class="hero-gradient">Nguyen</span></div>
        <div class="hero-subtitle">Turning data into models, insights, and interactive products.</div>
        <div class="hero-body">
            I am a <b>Master of Data Science and Innovation student at the University of Technology Sydney</b>, 
            with experience across machine learning, business analytics, data visualisation, and applied data science.
            <br><br>
            My portfolio combines advanced research, practical business analytics, and interactive data products, 
            including cyber-risk forecasting, sports broadcast analytics, computer vision, and upcoming self-built 
            analytics projects using public datasets.
        </div>
        <div class="career-strip">
            Target roles: Graduate Data Analyst · Data Scientist · Business Intelligence Analyst · Analytics Consultant · Business Analyst · Applied ML Engineer  · Data Science Researcher
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    b1, b2, b3 = st.columns([1.15, 0.85, 0.95])

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
            st.warning("Resume not found: assets/resume.pdf")

    with b2:
        st.link_button(
            "💻 GitHub",
            "https://github.com/ThomasNguyennnnn",
            use_container_width=True
        )

    with b3:
        st.link_button(
            "🔗 LinkedIn",
            "https://www.linkedin.com/in/thomas-tuan-nguyen/",
            use_container_width=True
        )

with hero_right:
    if PROFILE_IMAGE.exists():
        img_base64 = image_to_base64(PROFILE_IMAGE)
        img_mime = get_image_mime(PROFILE_IMAGE)

        profile_html = dedent(f"""
        <div class="profile-area">
            <div class="profile-image-box">
                <img src="data:{img_mime};base64,{img_base64}" alt="Thomas Nguyen profile photo">
            </div>
        </div>
        """)
        st.markdown(profile_html, unsafe_allow_html=True)
    else:
        st.info("Add your profile photo to assets/profile_photo.jpg")

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# Snapshot section
# ============================================================
st.markdown('<div class="section-title">Portfolio Snapshot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A quick overview of the areas this portfolio is designed to demonstrate.</div>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Project Areas</div>
            <div class="snapshot-value">5</div>
            <div class="snapshot-note">Research, analytics, ML, BI, visualisation</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Main Focus</div>
            <div class="snapshot-value">Analytics + ML</div>
            <div class="snapshot-note">Technical depth with business context</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Core Tools</div>
            <div class="snapshot-value">Python · SQL · BI</div>
            <div class="snapshot-note">Streamlit, Tableau, Excel, Power BI</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s4:
    st.markdown(
        """
        <div class="snapshot-card">
            <div class="snapshot-label">Outcome</div>
            <div class="snapshot-value">Business Impact</div>
            <div class="snapshot-note">Insights, dashboards, modelling, action</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# Focus area section
# ============================================================
st.markdown('<div class="section-title">What This Portfolio Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A balanced combination of technical modelling, business thinking, and visual communication.</div>',
    unsafe_allow_html=True
)

focus_html = dedent(f"""
<div class="focus-grid">
    {focus_card("🤖", "Machine Learning", "Predictive modelling, deep learning, model evaluation, temporal event forecasting, and applied ML workflows designed around measurable outcomes.")}
    {focus_card("📊", "Business Analytics", "Converting raw data into commercial insights through KPIs, segmentation, dashboards, and stakeholder-focused reporting.")}
    {focus_card("📈", "Data Visualisation", "Building clear, interactive, and decision-oriented visual stories with Streamlit, Tableau, Plotly, Power BI, and Python.")}
</div>
""")
st.markdown(focus_html, unsafe_allow_html=True)

# ============================================================
# Featured projects
# ============================================================
st.markdown('<div class="section-title">Featured Projects</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Selected projects showing research, applied analytics, computer vision, and business data science.</div>',
    unsafe_allow_html=True
)

projects_html = dedent(f"""
<div class="projects-grid">
    {project_card(
        "Advanced ML Research",
        "Completed",
        "Cyber Risk Forecasting",
        "Research project using Hawkes processes, Transformer Hawkes, Neural Hawkes, MCP Titan, and statistical baselines to model temporal cyber-risk events across connected entities.",
        "Python · R · temporal point processes · machine learning · model evaluation",
        "Portfolio value: advanced modelling, event simulation, research thinking, and comparative evaluation.",
        "completed"
    )}

    {project_card(
        "Industry Analytics",
        "Completed",
        "Sports Broadcast Sponsorship Analytics",
        "De-identified analytics case study based on broadcast exposure, sponsor visibility, media monitoring, and sponsorship reporting from sports and entertainment analytics experience.",
        "Excel · data cleaning · brand exposure analysis · media analytics · business reporting",
        "Portfolio value: real-world analytics experience and stakeholder-oriented business reporting.",
        "completed"
    )}

    {project_card(
        "Deep Learning",
        "Completed",
        "Food101 CNN Transfer Learning",
        "Computer vision project comparing pre-trained CNN architectures including GoogLeNet, MobileNetV3, and ResNet50, using transfer learning and fine-tuning in PyTorch.",
        "PyTorch · CNNs · transfer learning · fine-tuning · model comparison",
        "Portfolio value: practical deep learning workflow and controlled model experimentation.",
        "completed"
    )}

    {project_card(
        "Business Analytics Project",
        "Completed",
        "Retail Sales Analytics Dashboard",
        "Self-built business analytics dashboard using public retail data to analyse revenue trends, customer behaviour, product performance, and commercial KPIs.",
        "Streamlit · pandas · Plotly · KPI design · dashboarding · business analytics",
        "Portfolio value: dashboard development, business KPI design, and data storytelling.",
        "completed"
    )}

    {project_card(
        "Data Science Project",
        "Completed",
        "Customer Churn Prediction",
        "Practical data science project using public data to predict churn risk, evaluate model performance, and design customer retention recommendations. This project will demonstrate the full applied data science workflow from EDA and feature engineering to model interpretation and business action planning.",
        "Classification · feature engineering · ROC-AUC · precision · recall · retention strategy",
        "Portfolio value: business-focused predictive modelling and model-to-action thinking.",
        "completed",
        "project-card-wide"
    )}
</div>
""")
st.markdown(projects_html, unsafe_allow_html=True)

# ============================================================
# Technical skills
# ============================================================
st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A structured overview of the tools, methods, and analytical capabilities used across my portfolio projects.</div>',
    unsafe_allow_html=True
)

skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.markdown(
        """
        <div class="skills-card">
            <div class="skills-category">Programming & Data Handling</div>
            <div class="skills-title">Data Preparation and Analysis</div>
            <div class="skills-list">
                Python · R · SQL · pandas · NumPy · Excel · Power Query
            </div>
            <div class="skills-note">
                Used for data cleaning, transformation, exploratory analysis, feature engineering, and analytical reporting.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skills-card">
            <div class="skills-category">Machine Learning & Modelling</div>
            <div class="skills-title">Predictive and Deep Learning Methods</div>
            <div class="skills-list">
                scikit-learn · PyTorch · Machine Learning · Deep Learning · Model Evaluation · Classification · Forecasting
            </div>
            <div class="skills-note">
                Applied across cyber-risk forecasting, churn prediction, CNN transfer learning, and comparative model evaluation.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with skills_col2:
    st.markdown(
        """
        <div class="skills-card">
            <div class="skills-category">Visualisation & BI</div>
            <div class="skills-title">Dashboards and Data Storytelling</div>
            <div class="skills-list">
                Streamlit · Plotly · Matplotlib · Tableau · Power BI
            </div>
            <div class="skills-note">
                Used to build interactive dashboards, communicate insights, and translate analysis into stakeholder-facing outputs.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skills-card">
            <div class="skills-category">Business & Research Skills</div>
            <div class="skills-title">Insight Generation and Communication</div>
            <div class="skills-list">
                Business Analytics · Data Visualisation · KPI Design · Model Interpretation · Research Writing · Reporting
            </div>
            <div class="skills-note">
                Focused on connecting technical results with practical recommendations, business value, and clear communication.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# Contact
# ============================================================
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

c1, c2 = st.columns([1.45, 1])

with c1:
    st.markdown(
        """
        <div class="contact-panel">
            <div class="contact-title">Let’s connect</div>
            <b>Email:</b> thomas.nttn.au@gmail.com<br>
            <b>GitHub:</b> github.com/ThomasNguyennnnn<br>
            <b>LinkedIn:</b> linkedin.com/in/thomas-tuan-nguyen
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="contact-note">
            I am interested in graduate opportunities where I can apply data science, analytics, 
            and visualisation to solve practical business problems.
            <br><br>
            My current focus is building a portfolio that combines technical depth with practical business impact.
        </div>
        """,
        unsafe_allow_html=True
    )