import streamlit as st
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Sports Broadcast Analytics | Thomas Nguyen",
    page_icon="🏟️",
    layout="wide"
)

# ============================================================
# Helper functions
# ============================================================
def metric_card(value, label, note):
    return dedent(f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-note">{note}</div>
    </div>
    """)


def info_card(label, title, text):
    return dedent(f"""
    <div class="info-card">
        <div class="card-label">{label}</div>
        <div class="card-title">{title}</div>
        <div class="card-text">{text}</div>
    </div>
    """)


def process_card(step, title, text):
    return dedent(f"""
    <div class="process-card">
        <div class="step-badge">{step}</div>
        <div class="process-title">{title}</div>
        <div class="process-text">{text}</div>
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
    --indigo: #4f46e5;
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
    font-size: 3.65rem;
    font-weight: 950;
    letter-spacing: -2px;
    color: #0f172a;
    margin-bottom: 0.45rem;
    line-height: 1.05;
}

.gradient-text {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 1.22rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 1rem;
}

.body-text {
    font-size: 1.03rem;
    line-height: 1.82;
    color: #334155;
    max-width: 980px;
}

.hero-tags {
    margin-top: 1.25rem;
}

.hero-tag {
    display: inline-block;
    padding: 0.42rem 0.74rem;
    margin: 0.25rem 0.2rem 0.1rem 0;
    border-radius: 999px;
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(167, 139, 250, 0.28);
    color: #334155;
    font-size: 0.84rem;
    font-weight: 800;
    box-shadow: 0 8px 18px rgba(59, 130, 246, 0.08);
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
   Grid layout
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
   Shared cards
-------------------------------------------------------- */
.info-card,
.metric-card,
.process-card,
.timeline-card,
.capability-card {
    position: relative;
    overflow: hidden;
    height: 100%;
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    backdrop-filter: blur(10px);
}

.info-card:before,
.metric-card:before,
.process-card:before,
.timeline-card:before,
.capability-card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
}

/* --------------------------------------------------------
   Info cards
-------------------------------------------------------- */
.info-card {
    padding: 1.55rem 1.6rem;
    border-radius: 28px;
    background:
        radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    min-height: 245px;
    display: flex;
    flex-direction: column;
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
   Metric cards
-------------------------------------------------------- */
.metric-card {
    padding: 1.35rem 1.4rem;
    border-radius: 26px;
    background:
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(248,250,252,0.92));
    min-height: 160px;
}

.metric-value {
    font-size: 2.1rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.25rem;
    letter-spacing: -0.8px;
}

.metric-label {
    font-size: 0.92rem;
    font-weight: 900;
    color: #4f46e5;
    margin-bottom: 0.45rem;
}

.metric-note {
    font-size: 0.82rem;
    line-height: 1.45;
    color: #64748b;
}

/* --------------------------------------------------------
   Process cards
-------------------------------------------------------- */
.process-card {
    padding: 1.5rem 1.55rem;
    border-radius: 28px;
    background:
        radial-gradient(circle at top right, rgba(124, 58, 237, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    min-height: 250px;
}

.step-badge {
    width: fit-content;
    padding: 0.38rem 0.78rem;
    border-radius: 999px;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    color: white;
    font-size: 0.8rem;
    font-weight: 950;
    margin-bottom: 0.9rem;
}

.process-title {
    font-size: 1.13rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.55rem;
}

.process-text {
    font-size: 0.93rem;
    line-height: 1.66;
    color: #475569;
}

/* --------------------------------------------------------
   Timeline cards
-------------------------------------------------------- */
.timeline-card {
    padding: 1.4rem 1.5rem;
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    min-height: 230px;
}

.timeline-title {
    font-size: 1.07rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.35rem;
}

.timeline-meta {
    font-size: 0.88rem;
    font-weight: 850;
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
    min-height: 245px;
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
   Highlight panel
-------------------------------------------------------- */
.highlight-panel {
    padding: 1.6rem 1.7rem;
    border-radius: 30px;
    background:
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.10), transparent 28%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(239,246,255,0.94));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 16px 42px rgba(59, 130, 246, 0.10);
    color: #334155;
    line-height: 1.75;
    margin-top: 1.25rem;
}

.highlight-title {
    font-size: 1.15rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.55rem;
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

st.markdown(
    """
    <div class="eyebrow">Industry Analytics Project · Internship Experience</div>
    <div class="page-title">Sports Broadcast <span class="gradient-text">Analytics</span></div>
    <div class="subtitle">Sponsor Visibility · Brand Exposure · Media Analytics · Commercial Reporting</div>
    <div class="body-text">
        This project was completed during my internship at <b>Futures Sport & Entertainment</b>, where I supported 
        real-world sports sponsorship analytics across broadcast exposure, brand visibility, media monitoring, data validation, 
        and commercial reporting.
        <br><br>
        The work involved reviewing and organising large volumes of sports broadcast and media exposure outputs, including 
        frame-level visibility data, sponsor logo appearances, event coverage, and athlete-related media insights. The goal was 
        to help transform raw exposure data into reliable reporting material that could support sponsorship evaluation and 
        commercial decision-making.
        <br><br>
        Unlike a classroom project, this work required attention to data quality, consistency, business context, and stakeholder 
        communication. The final outputs contributed to understanding how brands appeared across sports events and how media 
        exposure could be interpreted as commercial sponsorship value.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Internship Project</span>
        <span class="hero-tag">Sports Analytics</span>
        <span class="hero-tag">Sponsorship Exposure</span>
        <span class="hero-tag">Broadcast Frames</span>
        <span class="hero-tag">Data Validation</span>
        <span class="hero-tag">Stakeholder Reporting</span>
        <span class="hero-tag">Commercial Insights</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# Project snapshot
# ============================================================
st.markdown('<div class="section-title">Project Snapshot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A quick overview of the industry context, analytics focus, and business value.</div>',
    unsafe_allow_html=True
)

snapshot_html = dedent(f"""
<div class="grid-4">
    {metric_card("160k+", "Broadcast frames", "Supported analysis and QA work involving large-scale sports broadcast frame outputs.")}
    {metric_card("Multiple", "Sports events", "Worked across motorsport, marathon, and athlete-related media analytics contexts.")}
    {metric_card("Real", "Industry data", "Handled practical media exposure data in an internship environment, not a simulated dataset.")}
    {metric_card("Business", "Commercial value", "Outputs supported sponsorship visibility reporting and brand exposure interpretation.")}
</div>
""")
st.markdown(snapshot_html, unsafe_allow_html=True)

# ============================================================
# Business problem
# ============================================================
st.markdown('<div class="section-title">Business Problem</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Sports sponsors need evidence of visibility, exposure, and brand value from broadcast and event media.</div>',
    unsafe_allow_html=True
)

problem_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Sponsorship Value",
        "How visible was the brand?",
        "Sponsors need to understand whether their brand appeared clearly and frequently across event broadcasts, media coverage, athlete content, and event-related outputs."
    )}

    {info_card(
        "Data Complexity",
        "Large volumes of media exposure data",
        "Sports broadcast data can involve thousands of frames, sponsor logo detections, event clips, visibility examples, and manual review points. The challenge is turning this raw data into reliable reporting evidence."
    )}

    {info_card(
        "Commercial Reporting",
        "From exposure data to business insight",
        "The final goal is not only to count visibility, but to support commercial conversations about sponsorship performance, brand presence, media value, and event impact."
    )}
</div>
""")
st.markdown(problem_html, unsafe_allow_html=True)

# ============================================================
# Internship context
# ============================================================
st.markdown('<div class="section-title">Internship Context</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project reflects practical analytics work completed in a real sports consultancy environment.</div>',
    unsafe_allow_html=True
)

context_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Futures Sport & Entertainment",
        "Sports Consultancy & Data Analyst Intern",
        "Worked in a sports consultancy environment supporting sponsorship analytics, media exposure reporting, broadcast visibility validation, fan insights, and commercial analysis for sports and entertainment clients."
    )}

    {timeline_card(
        "Supercars Broadcast Exposure",
        "The Bend · Bathurst · Frame-level visibility outputs",
        "Supported work on Supercars broadcast exposure data, including exemplar collection, output checking, frame-level review, quality assurance, and final reporting support. This helped assess how sponsor brands appeared across major motorsport broadcast coverage."
    )}

    {timeline_card(
        "Marathon Sponsorship Visibility",
        "Sydney Marathon · Berlin Marathon",
        "Supported sponsor visibility and event media analytics work involving marathon-related exposure outputs. The focus was on organising and validating visibility evidence that could be used in reporting and commercial interpretation."
    )}

    {timeline_card(
        "Athlete and Fan Insight Support",
        "New Balance athlete-related analysis",
        "Supported fan and athlete insight work involving sports figures and audience contexts. This strengthened my experience in connecting media data, athlete relevance, audience interest, and brand value."
    )}
</div>
""")
st.markdown(context_html, unsafe_allow_html=True)

# ============================================================
# Data and workflow
# ============================================================
st.markdown('<div class="section-title">Data & Workflow</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The workflow focused on cleaning, validating, organising, and interpreting sports media exposure data.</div>',
    unsafe_allow_html=True
)

workflow_html = dedent(f"""
<div class="grid-4">
    {process_card(
        "01",
        "Review raw exposure outputs",
        "Worked with broadcast and media exposure outputs such as frame-level results, detected sponsor appearances, event references, and exemplar materials."
    )}

    {process_card(
        "02",
        "Clean and structure data",
        "Organised files, checked naming consistency, reviewed exposure records, and helped prepare data so that it could be used reliably in analysis and reporting."
    )}

    {process_card(
        "03",
        "Validate brand visibility",
        "Checked whether detected brand appearances were accurate, relevant, and suitable for inclusion in sponsorship reports. This included identifying potential errors, unclear detections, or inconsistent outputs."
    )}

    {process_card(
        "04",
        "Support insight delivery",
        "Helped convert validated data and examples into clearer reporting outputs that could support sponsorship evaluation, commercial storytelling, and stakeholder communication."
    )}
</div>
""")
st.markdown(workflow_html, unsafe_allow_html=True)

# ============================================================
# My contribution
# ============================================================
st.markdown('<div class="section-title">My Contribution</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The specific types of work I contributed during the internship project.</div>',
    unsafe_allow_html=True
)

contribution_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Data Preparation",
        "Organised exposure files and outputs",
        "Prepared and organised sports media exposure files so that data could be reviewed, checked, and used more efficiently in reporting workflows."
    )}

    {info_card(
        "Quality Assurance",
        "Checked visibility accuracy",
        "Reviewed broadcast and media outputs to help confirm whether sponsor appearances were correctly detected and relevant for commercial reporting."
    )}

    {info_card(
        "Exemplar Collection",
        "Selected useful visibility examples",
        "Helped identify and organise examples of brand exposure that could support final reporting and make visibility evidence easier to communicate."
    )}

    {info_card(
        "Reporting Support",
        "Helped prepare stakeholder-ready material",
        "Supported the preparation of final outputs by ensuring data, examples, and visibility evidence were clean, consistent, and understandable."
    )}

    {info_card(
        "Commercial Interpretation",
        "Connected media data to sponsorship value",
        "Developed a stronger understanding of how exposure data can be used to explain brand presence, event value, and sponsorship performance."
    )}

    {info_card(
        "Professional Collaboration",
        "Worked in a real analytics team",
        "Gained experience working with analysts and project stakeholders in a professional sports consultancy environment."
    )}
</div>
""")
st.markdown(contribution_html, unsafe_allow_html=True)

# ============================================================
# Analytical focus
# ============================================================
st.markdown('<div class="section-title">Analytical Focus</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The work combined data accuracy, commercial interpretation, and stakeholder-ready reporting.</div>',
    unsafe_allow_html=True
)

focus_html = dedent(f"""
<div class="grid-3">
    {capability_card(
        "Brand Visibility",
        "Sponsor exposure tracking",
        "Broadcast frames · logo visibility · media exposure",
        "Reviewed brand appearances across event broadcasts and media outputs to support sponsor visibility measurement."
    )}

    {capability_card(
        "Data Quality",
        "Validation and quality assurance",
        "Cleaning · checking · consistency · exemplar review",
        "Focused on making sure exposure outputs were accurate, consistent, and suitable for stakeholder reporting."
    )}

    {capability_card(
        "Commercial Insight",
        "Sponsorship performance interpretation",
        "Brand value · event visibility · reporting evidence",
        "Helped connect media exposure data with business questions about sponsorship performance and brand presence."
    )}
</div>
""")
st.markdown(focus_html, unsafe_allow_html=True)

# ============================================================
# Deliverables
# ============================================================
st.markdown('<div class="section-title">Project Deliverables</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The outputs supported real-world sponsorship analytics and commercial reporting workflows.</div>',
    unsafe_allow_html=True
)

deliverables_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Validated Exposure Data",
        "Cleaner data for reporting",
        "Prepared and checked exposure-related outputs so that final reporting could be based on more reliable media evidence."
    )}

    {info_card(
        "Brand Visibility Examples",
        "Evidence for sponsor reporting",
        "Supported the collection and review of examples showing how sponsor brands appeared across broadcast or event media."
    )}

    {info_card(
        "Quality Assurance Notes",
        "Accuracy and consistency checks",
        "Helped identify inconsistencies, unclear detections, or areas requiring review before exposure data was used in reporting."
    )}

    {info_card(
        "Reporting Support",
        "Stakeholder-ready material",
        "Supported the preparation of reporting outputs that explained brand exposure, event visibility, and sponsorship performance."
    )}

    {info_card(
        "Fan and Athlete Insight Support",
        "Audience and athlete context",
        "Contributed to insight work connecting sports figures, fan interest, and brand relevance."
    )}

    {info_card(
        "Commercial Analytics Experience",
        "Real-world business application",
        "Gained practical experience in how analytics supports commercial decision-making in sport, sponsorship, and media."
    )}
</div>
""")
st.markdown(deliverables_html, unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-panel">
        <div class="highlight-title">Main Business Value</div>
        This project helped turn complex broadcast and media exposure data into clearer evidence for sponsorship performance. 
        The value came from improving data reliability, supporting brand visibility analysis, and helping transform raw media 
        outputs into reporting material that could be used in commercial sports conversations.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# What this project demonstrates
# ============================================================
st.markdown('<div class="section-title">What This Project Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project demonstrates practical analytics experience in a real business and sports media context.</div>',
    unsafe_allow_html=True
)

demonstrates_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Industry Experience",
        "Real workplace analytics",
        "The project was completed in an internship environment, requiring practical data handling, accuracy, and professional communication."
    )}

    {info_card(
        "Commercial Thinking",
        "Analytics connected to sponsorship value",
        "The work was not only technical. It supported commercial interpretation of sponsor visibility, media exposure, and event value."
    )}

    {info_card(
        "Data Reliability",
        "Cleaning and validation",
        "The project required careful checking of exposure data so that the final outputs were accurate, useful, and credible."
    )}

    {info_card(
        "Communication",
        "Stakeholder-ready outputs",
        "The work supported reporting material that needed to be understandable for business and non-technical audiences."
    )}
</div>
""")
st.markdown(demonstrates_html, unsafe_allow_html=True)

# ============================================================
# Skills used
# ============================================================
st.markdown('<div class="section-title">Skills Used</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Key practical and analytical capabilities demonstrated through this internship project.</div>',
    unsafe_allow_html=True
)

skills_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Data Handling",
        "Cleaning and organisation",
        "Excel · structured files · media outputs",
        "Prepared, organised, checked, and structured exposure-related data for analysis and reporting."
    )}

    {capability_card(
        "Media Analytics",
        "Broadcast exposure analysis",
        "Frame-level review · sponsor visibility · event coverage",
        "Worked with sports broadcast and media outputs to support sponsor visibility and brand exposure analysis."
    )}

    {capability_card(
        "Quality Assurance",
        "Validation and checking",
        "Accuracy · consistency · exemplar review",
        "Reviewed data outputs and visibility examples to help ensure reporting quality and credibility."
    )}

    {capability_card(
        "Business Reporting",
        "Commercial communication",
        "Stakeholder reports · insights · sponsorship value",
        "Helped translate technical exposure outputs into clearer reporting material for business and non-technical audiences."
    )}

    {capability_card(
        "Sports Business Context",
        "Sponsorship and brand value",
        "Events · athletes · sponsors · media exposure",
        "Developed a stronger understanding of how sports sponsorship value is measured and communicated."
    )}

    {capability_card(
        "Analytical Thinking",
        "From raw outputs to insight",
        "Data review · interpretation · decision support",
        "Practised turning unstructured or semi-structured media outputs into more usable analytical evidence."
    )}

    {capability_card(
        "Attention to Detail",
        "Accuracy in real reporting",
        "QA · consistency · manual review",
        "Learned how small data quality issues can affect final commercial reporting and stakeholder confidence."
    )}

    {capability_card(
        "Professional Workflow",
        "Working in an analytics team",
        "Collaboration · deadlines · communication",
        "Gained experience contributing to analytics tasks within a professional sports consultancy environment."
    )}
</div>
""")
st.markdown(skills_html, unsafe_allow_html=True)

# ============================================================
# Reflection
# ============================================================
st.markdown('<div class="section-title">Reflection</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">What this project added to my development as a data professional.</div>',
    unsafe_allow_html=True
)

reflection_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Real-World Data Experience",
        "Working beyond clean classroom datasets",
        "This project gave me experience with practical industry data that required cleaning, validation, interpretation, and business judgement."
    )}

    {info_card(
        "Commercial Awareness",
        "Understanding why the analysis matters",
        "I learned how analytics can support sponsorship evaluation, brand reporting, and commercial decision-making in the sports industry."
    )}

    {info_card(
        "Quality and Accuracy",
        "Data reliability affects business trust",
        "The project showed me that accurate validation is essential because reporting outputs may influence stakeholder understanding and commercial conversations."
    )}

    {info_card(
        "Communication",
        "Making data usable for stakeholders",
        "I strengthened my ability to think about how analytical outputs should be structured and explained for non-technical business users."
    )}

    {info_card(
        "Industry Confidence",
        "Applying analytics in a professional setting",
        "The internship helped me become more confident working with real tasks, deadlines, feedback, and practical business expectations."
    )}

    {info_card(
        "Career Relevance",
        "Data analyst and business analyst preparation",
        "This project directly strengthened skills relevant to graduate roles in data analytics, business analytics, BI, and analytics consulting."
    )}
</div>
""")
st.markdown(reflection_html, unsafe_allow_html=True)