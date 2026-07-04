import streamlit as st
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Retail Sales Analytics Dashboard | Thomas Nguyen",
    page_icon="📊",
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
    min-height: 245px;
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
    min-height: 220px;
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
    min-height: 235px;
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
   Feature table
-------------------------------------------------------- */
.table-wrap {
    border-radius: 26px;
    overflow: hidden;
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 18px 45px rgba(59, 130, 246, 0.10);
    background: rgba(255,255,255,0.94);
}

.feature-table {
    width: 100%;
    border-collapse: collapse;
}

.feature-table th {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    color: white;
    padding: 0.95rem;
    font-size: 0.88rem;
    text-align: left;
    white-space: nowrap;
}

.feature-table td {
    padding: 0.9rem 0.95rem;
    font-size: 0.9rem;
    color: #334155;
    border-bottom: 1px solid rgba(167, 139, 250, 0.18);
}

.feature-table tr:last-child td {
    border-bottom: none;
}

.feature-row {
    background: rgba(219, 234, 254, 0.34);
    font-weight: 850;
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

    .table-wrap {
        overflow-x: auto;
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
    <div class="eyebrow">Self-Built Business Analytics Dashboard</div>
    <div class="page-title">Retail Sales <span class="gradient-text">Analytics Dashboard</span></div>
    <div class="subtitle">Revenue Trends · Customer Behaviour · Product Performance · Commercial KPIs</div>
    <div class="body-text">
        This project is a self-built business analytics dashboard using public retail sales data to analyse revenue trends, 
        customer behaviour, product performance, and commercial KPIs. The dashboard is designed to turn raw transactional 
        data into interactive insights that can support business decision-making.
        <br><br>
        The project focuses on practical dashboard design: KPI cards, trend charts, product rankings, customer-level views, 
        category performance, and business filters. It demonstrates how data cleaning, KPI design, and visual storytelling 
        can be combined into a professional analytics product.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Streamlit</span>
        <span class="hero-tag">pandas</span>
        <span class="hero-tag">Plotly</span>
        <span class="hero-tag">KPI Design</span>
        <span class="hero-tag">Dashboarding</span>
        <span class="hero-tag">Business Analytics</span>
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
    '<div class="section-subtitle">A quick overview of the dashboard purpose, analytics focus, and technical stack.</div>',
    unsafe_allow_html=True
)

snapshot_html = dedent(f"""
<div class="grid-4">
    {metric_card("Public", "Retail dataset", "Uses publicly available retail sales data suitable for business analytics demonstration.")}
    {metric_card("4", "Analysis areas", "Revenue trends, customers, products, and commercial KPI performance.")}
    {metric_card("9+", "Planned KPIs", "Revenue, orders, AOV, top products, categories, customer behaviour, and segment performance.")}
    {metric_card("Streamlit", "Dashboard app", "Interactive dashboard built with Python, pandas, Plotly, and Streamlit.")}
</div>
""")
st.markdown(snapshot_html, unsafe_allow_html=True)

# ============================================================
# Business problem
# ============================================================
st.markdown('<div class="section-title">Business Problem</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Retail businesses need clear visibility into sales performance, customers, products, and growth opportunities.</div>',
    unsafe_allow_html=True
)

problem_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Revenue Visibility",
        "Where is sales performance changing?",
        "Retail teams need to track how revenue changes over time, identify seasonality, and understand which periods are driving growth or decline."
    )}

    {info_card(
        "Customer Behaviour",
        "Who is buying and how often?",
        "Customer-level analysis helps reveal repeat purchasing behaviour, order frequency, average spend, and potential opportunities for retention or segmentation."
    )}

    {info_card(
        "Product Performance",
        "Which products create the most value?",
        "Product and category analysis helps identify best sellers, underperforming items, and product groups that contribute most to revenue."
    )}
</div>
""")
st.markdown(problem_html, unsafe_allow_html=True)

# ============================================================
# Dashboard objectives
# ============================================================
st.markdown('<div class="section-title">Dashboard Objectives</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The dashboard is designed to answer practical business questions that a retail analyst or BI analyst would investigate.</div>',
    unsafe_allow_html=True
)

objectives_html = dedent(f"""
<div class="grid-4">
    {process_card(
        "01",
        "Monitor sales performance",
        "Track core metrics such as total revenue, total orders, average order value, and revenue trend over time."
    )}

    {process_card(
        "02",
        "Identify product drivers",
        "Rank products and categories by revenue, quantity sold, and contribution to overall sales performance."
    )}

    {process_card(
        "03",
        "Understand customer behaviour",
        "Analyse customer purchase frequency, average spend, repeat behaviour, and possible customer segments."
    )}

    {process_card(
        "04",
        "Support decision-making",
        "Use interactive filters and visual summaries to help users explore performance by time period, product, category, region, or customer group."
    )}
</div>
""")
st.markdown(objectives_html, unsafe_allow_html=True)

# ============================================================
# Data and KPI design
# ============================================================
st.markdown('<div class="section-title">Data & KPI Design</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project translates raw transaction records into business-ready metrics and dashboard views.</div>',
    unsafe_allow_html=True
)

kpi_html = dedent(f"""
<div class="grid-3">
    {timeline_card(
        "Transaction-Level Data",
        "Orders · products · customers · dates",
        "The dashboard is based on retail transaction data containing order information, product details, customer identifiers, dates, quantities, prices, and sales values."
    )}

    {timeline_card(
        "Commercial KPI Layer",
        "Revenue · orders · AOV · product ranking",
        "Raw columns are transformed into commercial metrics such as total revenue, total orders, average order value, top products, top categories, and revenue trends."
    )}

    {timeline_card(
        "Interactive Dashboard Layer",
        "Filters · charts · KPI cards · tables",
        "The final dashboard presents KPIs through interactive filters, summary cards, visual trend charts, product rankings, and customer behaviour views."
    )}
</div>
""")
st.markdown(kpi_html, unsafe_allow_html=True)

# ============================================================
# Dashboard workflow
# ============================================================
st.markdown('<div class="section-title">Dashboard Workflow</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The workflow follows a practical business analytics pipeline from raw data to interactive insight.</div>',
    unsafe_allow_html=True
)

workflow_html = dedent(f"""
<div class="grid-4">
    {process_card(
        "01",
        "Load and inspect data",
        "Import the public retail dataset, inspect columns, review missing values, check date fields, and understand transaction-level structure."
    )}

    {process_card(
        "02",
        "Clean and transform",
        "Prepare date variables, calculate revenue fields, clean product and customer information, and create analysis-ready KPI tables."
    )}

    {process_card(
        "03",
        "Build KPI logic",
        "Define key metrics such as revenue, order count, average order value, product contribution, and customer purchase behaviour."
    )}

    {process_card(
        "04",
        "Design dashboard views",
        "Build an interactive Streamlit dashboard with filters, KPI cards, Plotly charts, rankings, and business interpretation sections."
    )}
</div>
""")
st.markdown(workflow_html, unsafe_allow_html=True)

# ============================================================
# Dashboard features
# ============================================================
st.markdown('<div class="section-title">Dashboard Features</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The dashboard is planned around business questions rather than only showing charts.</div>',
    unsafe_allow_html=True
)

features_table = """
<div class="table-wrap">
<table class="feature-table">
    <tr>
        <th>Dashboard Area</th>
        <th>Example KPIs / Views</th>
        <th>Business Question Answered</th>
    </tr>
    <tr class="feature-row">
        <td>Executive Summary</td>
        <td>Total revenue, total orders, average order value, unique customers</td>
        <td>How is the business performing overall?</td>
    </tr>
    <tr>
        <td>Revenue Trends</td>
        <td>Monthly revenue, weekly sales, seasonality, growth patterns</td>
        <td>When is revenue increasing or decreasing?</td>
    </tr>
    <tr>
        <td>Product Performance</td>
        <td>Top products, top categories, quantity sold, revenue share</td>
        <td>Which products or categories drive sales?</td>
    </tr>
    <tr>
        <td>Customer Behaviour</td>
        <td>Purchase frequency, repeat customers, average spend, customer value</td>
        <td>Who are the most valuable customers?</td>
    </tr>
    <tr>
        <td>Segment or Region View</td>
        <td>Revenue by region, segment, store, market, or customer group</td>
        <td>Where are the strongest commercial opportunities?</td>
    </tr>
</table>
</div>
"""
st.markdown(features_table, unsafe_allow_html=True)

# ============================================================
# Analytics features
# ============================================================
st.markdown('<div class="section-title">Analytics Features</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The dashboard combines KPI design, trend analysis, ranking analysis, and interactive exploration.</div>',
    unsafe_allow_html=True
)

features_html = dedent(f"""
<div class="grid-3">
    {capability_card(
        "KPI Cards",
        "Executive-level performance summary",
        "Revenue · orders · AOV · customers",
        "High-level metric cards allow users to quickly understand business performance before exploring deeper charts."
    )}

    {capability_card(
        "Trend Analysis",
        "Time-based sales performance",
        "Monthly revenue · order volume · seasonality",
        "Trend charts help identify growth patterns, seasonal changes, and periods requiring business attention."
    )}

    {capability_card(
        "Product Ranking",
        "Best sellers and category contribution",
        "Top products · categories · revenue share",
        "Ranking views help identify which products and categories contribute most strongly to sales."
    )}

    {capability_card(
        "Customer View",
        "Behaviour and purchase patterns",
        "Repeat customers · purchase frequency · average spend",
        "Customer analytics helps reveal purchasing behaviour and potential retention or segmentation opportunities."
    )}

    {capability_card(
        "Interactive Filters",
        "User-driven exploration",
        "Date range · product · category · region",
        "Filters allow users to explore specific time periods, customer groups, product categories, or regions."
    )}

    {capability_card(
        "Business Commentary",
        "Insight-focused dashboarding",
        "Interpretation · recommendations · decision support",
        "The dashboard is designed to explain what the charts mean, not only display the numbers."
    )}
</div>
""")
st.markdown(features_html, unsafe_allow_html=True)

# ============================================================
# Example insights
# ============================================================
st.markdown('<div class="section-title">Example Insights</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">These are the types of commercial insights the dashboard is designed to produce after connecting the final dataset.</div>',
    unsafe_allow_html=True
)

insight_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Sales Trend Insight",
        "Identify peak and low-performing periods",
        "The dashboard can reveal which months, weeks, or seasons generate stronger revenue, helping managers investigate drivers of growth or decline."
    )}

    {info_card(
        "Product Insight",
        "Find high-value and low-performing products",
        "Product ranking views can show which products generate the highest revenue and which may require pricing, promotion, or inventory review."
    )}

    {info_card(
        "Customer Insight",
        "Understand purchase frequency and value",
        "Customer behaviour views can help identify repeat customers, high-value buyers, and groups that may benefit from retention strategies."
    )}
</div>
""")
st.markdown(insight_html, unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-panel">
        <div class="highlight-title">Main Business Value</div>
        This dashboard is designed to convert retail transaction data into practical business insight. Instead of only producing 
        static charts, the project focuses on KPI design, interactive exploration, and commercial interpretation. It demonstrates 
        how a data analyst can help a retail business monitor performance, understand product and customer behaviour, and identify 
        opportunities for better decisions.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# What this project demonstrates
# ============================================================
st.markdown('<div class="section-title">What This Project Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project is designed to demonstrate business analytics, dashboard development, and data storytelling capability.</div>',
    unsafe_allow_html=True
)

demonstrates_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Business Analytics",
        "Turning sales data into decisions",
        "The project demonstrates the ability to translate raw transaction data into metrics that answer practical business questions."
    )}

    {info_card(
        "Dashboard Design",
        "Interactive and user-focused reporting",
        "The dashboard is structured around KPI cards, filters, charts, and rankings so users can explore data efficiently."
    )}

    {info_card(
        "Commercial Thinking",
        "KPIs linked to business value",
        "Metrics are selected based on commercial relevance, including revenue, orders, product contribution, and customer behaviour."
    )}

    {info_card(
        "Data Storytelling",
        "Explaining what the numbers mean",
        "The project focuses on communicating insights clearly for business users, not only building technical visualisations."
    )}
</div>
""")
st.markdown(demonstrates_html, unsafe_allow_html=True)

# ============================================================
# Skills used
# ============================================================
st.markdown('<div class="section-title">Skills Used</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Key technical and analytical capabilities demonstrated through this business analytics project.</div>',
    unsafe_allow_html=True
)

skills_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Python Analytics",
        "Data cleaning and transformation",
        "Python · pandas · data wrangling",
        "Used pandas to prepare transaction-level data, calculate business metrics, and create analysis-ready tables."
    )}

    {capability_card(
        "Dashboarding",
        "Interactive Streamlit app",
        "Streamlit · layout design · filters",
        "Built a dashboard structure that allows users to interact with data and explore different business views."
    )}

    {capability_card(
        "Visual Analytics",
        "Business charts and trends",
        "Plotly · line charts · bar charts · rankings",
        "Used Plotly to create interactive visualisations for revenue trends, product performance, and customer behaviour."
    )}

    {capability_card(
        "KPI Design",
        "Commercial metric development",
        "Revenue · orders · AOV · customer value",
        "Defined KPIs that connect directly to business performance and decision-making."
    )}

    {capability_card(
        "Business Analysis",
        "Retail performance interpretation",
        "Sales trends · product mix · customer behaviour",
        "Analysed retail performance from multiple angles to support practical business interpretation."
    )}

    {capability_card(
        "Data Storytelling",
        "Insight communication",
        "Dashboard layout · commentary · executive summary",
        "Designed the dashboard to communicate findings clearly for non-technical users."
    )}

    {capability_card(
        "Product Analytics",
        "Product and category performance",
        "Top products · category contribution · revenue share",
        "Created views to understand which products and categories drive commercial performance."
    )}

    {capability_card(
        "Customer Analytics",
        "Behaviour and value analysis",
        "Frequency · repeat purchase · average spend",
        "Built analysis areas focused on customer behaviour, value, and purchase patterns."
    )}
</div>
""")
st.markdown(skills_html, unsafe_allow_html=True)

# ============================================================
# Future improvements
# ============================================================
st.markdown('<div class="section-title">Future Improvements</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Possible extensions to make the dashboard more advanced and business-ready.</div>',
    unsafe_allow_html=True
)

future_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Forecasting Module",
        "Predict future sales",
        "Add time-series forecasting to estimate future revenue, order volume, or demand by product category."
    )}

    {info_card(
        "Customer Segmentation",
        "Group customers by behaviour",
        "Use RFM analysis or clustering to segment customers based on recency, frequency, and monetary value."
    )}

    {info_card(
        "Profitability View",
        "Move beyond revenue",
        "If cost data is available, add gross margin, profit contribution, and product profitability analysis."
    )}

    {info_card(
        "Recommendation Logic",
        "Suggest actions from insights",
        "Add rule-based recommendations such as products to promote, categories to review, or customers to target."
    )}

    {info_card(
        "Deployment",
        "Publish as an interactive app",
        "Deploy the dashboard publicly through Streamlit Cloud and connect it to a GitHub project repository."
    )}

    {info_card(
        "Automated Reporting",
        "Export insights for stakeholders",
        "Add downloadable CSV summaries, PDF reports, or scheduled reporting outputs for business users."
    )}
</div>
""")
st.markdown(future_html, unsafe_allow_html=True)