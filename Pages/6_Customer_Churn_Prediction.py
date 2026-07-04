import streamlit as st
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Customer Churn Prediction | Thomas Nguyen",
    page_icon="📉",
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
   Results table
-------------------------------------------------------- */
.table-wrap {
    border-radius: 26px;
    overflow: hidden;
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 18px 45px rgba(59, 130, 246, 0.10);
    background: rgba(255,255,255,0.94);
}

.result-table {
    width: 100%;
    border-collapse: collapse;
}

.result-table th {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    color: white;
    padding: 0.95rem;
    font-size: 0.88rem;
    text-align: left;
    white-space: nowrap;
}

.result-table td {
    padding: 0.9rem 0.95rem;
    font-size: 0.9rem;
    color: #334155;
    border-bottom: 1px solid rgba(167, 139, 250, 0.18);
}

.result-table tr:last-child td {
    border-bottom: none;
}

.best-row {
    background: rgba(219, 234, 254, 0.48);
    font-weight: 850;
}

/* --------------------------------------------------------
   Highlight panel and note
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

.demo-note {
    padding: 1rem 1.15rem;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid rgba(167, 139, 250, 0.26);
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.6;
    box-shadow: 0 10px 24px rgba(59, 130, 246, 0.08);
    margin-bottom: 1.25rem;
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
    <div class="eyebrow">Self-Built Machine Learning Project · Demo Metrics</div>
    <div class="page-title">Customer Churn <span class="gradient-text">Prediction</span></div>
    <div class="subtitle">Classification · Customer Retention · Machine Learning · Business Analytics</div>
    <div class="body-text">
        This project is a self-built machine learning case study using public customer data to predict customer churn risk, 
        identify key drivers of attrition, and support retention-focused business decisions.
        <br><br>
        The workflow covers data preparation, feature engineering, model comparison, classification evaluation, and business 
        interpretation. The goal is not only to build a predictive model, but also to translate model outputs into practical 
        retention actions for high-risk customer groups.
        <br><br>
        The demo results show how the final dashboard and portfolio case study will present model performance, churn drivers, 
        and actionable customer retention insights.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Customer Analytics</span>
        <span class="hero-tag">Churn Prediction</span>
        <span class="hero-tag">Classification</span>
        <span class="hero-tag">scikit-learn</span>
        <span class="hero-tag">Feature Importance</span>
        <span class="hero-tag">Retention Strategy</span>
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
    '<div class="section-subtitle">A quick overview of the churn problem, dataset scale, and demo model results.</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="demo-note">
        <b>Note:</b> The metrics on this page are demo portfolio results and will be updated after the final project is fully trained and validated.
    </div>
    """,
    unsafe_allow_html=True
)

snapshot_html = dedent(f"""
<div class="grid-4">
    {metric_card("7,043", "Customers", "Demo dataset size for the customer churn prediction case study.")}
    {metric_card("26.5%", "Churn rate", "Approximate share of customers labelled as churned in the demo dataset.")}
    {metric_card("80/20", "Train-test split", "Planned split used to train models and evaluate unseen test performance.")}
    {metric_card("0.86", "Best ROC-AUC", "Demo best model result from the gradient boosting classifier.")}
</div>
""")
st.markdown(snapshot_html, unsafe_allow_html=True)

# ============================================================
# Business problem
# ============================================================
st.markdown('<div class="section-title">Business Problem</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Customer churn prediction helps businesses identify which customers are likely to leave and why.</div>',
    unsafe_allow_html=True
)

problem_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Retention Challenge",
        "Which customers are likely to leave?",
        "Businesses often lose revenue when customers cancel, stop purchasing, or switch to competitors. Predicting churn helps identify customers who may need retention attention."
    )}

    {info_card(
        "Driver Analysis",
        "Why are customers leaving?",
        "A churn model should not only produce predictions. It should also help identify important churn drivers such as contract type, tenure, monthly charges, support services, and engagement patterns."
    )}

    {info_card(
        "Business Action",
        "How can the business respond?",
        "The final objective is to support retention strategies, such as targeted offers, improved service support, contract upgrades, or proactive communication with high-risk customers."
    )}
</div>
""")
st.markdown(problem_html, unsafe_allow_html=True)

# ============================================================
# Dataset and target
# ============================================================
st.markdown('<div class="section-title">Dataset & Target Variable</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project uses customer-level records to predict whether a customer is likely to churn.</div>',
    unsafe_allow_html=True
)

dataset_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Customer-Level Dataset",
        "7,043 customer records · demo portfolio dataset",
        "Each row represents a customer and includes account information, service usage, billing attributes, contract details, and churn status."
    )}

    {timeline_card(
        "Target Variable",
        "Churn: Yes / No",
        "The target is a binary classification label indicating whether the customer churned. This allows the problem to be framed as a supervised classification task."
    )}

    {timeline_card(
        "Example Predictors",
        "Tenure · contract type · monthly charges · services",
        "Potential predictors include customer tenure, contract type, payment method, monthly charges, online security, tech support, internet service, and add-on services."
    )}

    {timeline_card(
        "Business Output",
        "Churn probability and risk segment",
        "The model output can be translated into churn probability, risk level, top churn drivers, and recommended retention actions."
    )}
</div>
""")
st.markdown(dataset_html, unsafe_allow_html=True)

# ============================================================
# Machine learning workflow
# ============================================================
st.markdown('<div class="section-title">Machine Learning Workflow</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project follows a practical supervised learning workflow from raw customer data to business-ready churn insights.</div>',
    unsafe_allow_html=True
)

workflow_html = dedent(f"""
<div class="grid-4">
    {process_card(
        "01",
        "Clean customer data",
        "Inspect missing values, fix inconsistent fields, prepare numeric variables, and remove or correct unusable records."
    )}

    {process_card(
        "02",
        "Prepare features",
        "Encode categorical variables, scale numeric variables where needed, and prepare churn-related predictors for model training."
    )}

    {process_card(
        "03",
        "Train model candidates",
        "Compare logistic regression, decision tree, random forest, and gradient boosting models using the same train-test split."
    )}

    {process_card(
        "04",
        "Evaluate and interpret",
        "Compare performance using accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix, and feature importance."
    )}
</div>
""")
st.markdown(workflow_html, unsafe_allow_html=True)

# ============================================================
# Feature engineering
# ============================================================
st.markdown('<div class="section-title">Feature Engineering</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Feature preparation is designed to make customer attributes usable for machine learning and business interpretation.</div>',
    unsafe_allow_html=True
)

feature_html = dedent(f"""
<div class="grid-3">
    {capability_card(
        "Categorical Encoding",
        "Prepare non-numeric customer attributes",
        "Contract type · payment method · internet service",
        "Convert categorical customer attributes into model-ready variables using encoding techniques."
    )}

    {capability_card(
        "Numeric Features",
        "Prepare continuous customer measures",
        "Tenure · monthly charges · total charges",
        "Clean and scale numeric variables where appropriate so models can use them effectively."
    )}

    {capability_card(
        "Risk-Oriented Features",
        "Support churn interpretation",
        "Tenure bands · charge level · service count",
        "Create or group features that make churn patterns easier to interpret for retention decisions."
    )}
</div>
""")
st.markdown(feature_html, unsafe_allow_html=True)

# ============================================================
# Models compared
# ============================================================
st.markdown('<div class="section-title">Models Compared</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project compares interpretable baseline models with stronger tree-based classifiers.</div>',
    unsafe_allow_html=True
)

models_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Baseline",
        "Logistic Regression",
        "Interpretable linear classifier",
        "Useful for establishing a baseline and understanding directional relationships between features and churn probability."
    )}

    {capability_card(
        "Tree Model",
        "Decision Tree",
        "Rule-based classification",
        "Provides a simple non-linear model that can capture rule-like customer churn patterns."
    )}

    {capability_card(
        "Ensemble",
        "Random Forest",
        "Bagging-based tree ensemble",
        "Improves stability and performance by combining many decision trees and reducing overfitting risk."
    )}

    {capability_card(
        "Best Demo Model",
        "Gradient Boosting",
        "Boosting-based classifier",
        "Demo best performer, balancing predictive performance with useful feature importance interpretation."
    )}
</div>
""")
st.markdown(models_html, unsafe_allow_html=True)

# ============================================================
# Demo results
# ============================================================
st.markdown('<div class="section-title">Demo Model Results</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Demo portfolio metrics show how model performance will be presented after final training.</div>',
    unsafe_allow_html=True
)

results_table = """
<div class="table-wrap">
<table class="result-table">
    <tr>
        <th>Model</th>
        <th>Accuracy</th>
        <th>Precision</th>
        <th>Recall</th>
        <th>F1-score</th>
        <th>ROC-AUC</th>
        <th>Interpretation</th>
    </tr>
    <tr>
        <td>Logistic Regression</td>
        <td>0.78</td>
        <td>0.66</td>
        <td>0.61</td>
        <td>0.63</td>
        <td>0.82</td>
        <td>Strong interpretable baseline for churn probability modelling.</td>
    </tr>
    <tr>
        <td>Decision Tree</td>
        <td>0.74</td>
        <td>0.59</td>
        <td>0.58</td>
        <td>0.58</td>
        <td>0.73</td>
        <td>Simple rule-based model but weaker overall generalisation.</td>
    </tr>
    <tr>
        <td>Random Forest</td>
        <td>0.80</td>
        <td>0.70</td>
        <td>0.65</td>
        <td>0.67</td>
        <td>0.84</td>
        <td>Improved ensemble performance and more stable predictions.</td>
    </tr>
    <tr class="best-row">
        <td>Gradient Boosting</td>
        <td>0.81</td>
        <td>0.72</td>
        <td>0.68</td>
        <td>0.70</td>
        <td>0.86</td>
        <td>Best demo model, with strongest balance of recall, F1, and ROC-AUC.</td>
    </tr>
</table>
</div>
"""
st.markdown(results_table, unsafe_allow_html=True)

results_html = dedent(f"""
<div class="grid-4" style="margin-top: 1.35rem;">
    {metric_card("0.81", "Accuracy", "Demo best model accuracy from gradient boosting.")}
    {metric_card("0.68", "Churn recall", "Demo recall for identifying churned customers.")}
    {metric_card("0.70", "F1-score", "Demo balance between churn precision and recall.")}
    {metric_card("0.86", "ROC-AUC", "Demo ranking performance for separating churn and non-churn customers.")}
</div>
""")
st.markdown(results_html, unsafe_allow_html=True)

# ============================================================
# Evaluation metrics
# ============================================================
st.markdown('<div class="section-title">Evaluation Metrics</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Churn prediction should be evaluated beyond accuracy because missing churned customers can be costly.</div>',
    unsafe_allow_html=True
)

metrics_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Accuracy",
        "Overall correctness",
        "Measures the proportion of correct predictions, but can be misleading if churned customers are a minority class."
    )}

    {info_card(
        "Recall",
        "Finding churned customers",
        "Recall is important because the business wants to detect as many customers at risk of leaving as possible."
    )}

    {info_card(
        "Precision",
        "Avoiding false alarms",
        "Precision matters because retention campaigns cost money, so the business should avoid targeting too many low-risk customers."
    )}

    {info_card(
        "F1-score",
        "Balance between precision and recall",
        "F1-score is useful when the business cares about both detecting churn and keeping targeting efficient."
    )}

    {info_card(
        "ROC-AUC",
        "Risk ranking quality",
        "ROC-AUC measures how well the model separates high-risk and low-risk customers across different probability thresholds."
    )}

    {info_card(
        "Confusion Matrix",
        "Business error analysis",
        "The confusion matrix helps explain false positives and false negatives, which can be translated into retention cost and missed churn risk."
    )}
</div>
""")
st.markdown(metrics_html, unsafe_allow_html=True)

# ============================================================
# Business insights
# ============================================================
st.markdown('<div class="section-title">Business Insights</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project translates model outputs into business-readable churn drivers and retention actions.</div>',
    unsafe_allow_html=True
)

insights_html = dedent(f"""
<div class="grid-3">
    {timeline_card(
        "High-Risk Segment",
        "Month-to-month contract customers with high monthly charges",
        "Demo analysis suggests that customers on flexible contracts with high monthly payments are more likely to churn, especially when they have shorter tenure or fewer support services."
    )}

    {timeline_card(
        "Top Churn Drivers",
        "Contract type · tenure · monthly charges · online security · tech support",
        "The key churn drivers are designed to be translated into retention strategies rather than treated only as model features."
    )}

    {timeline_card(
        "Retention Strategy",
        "Targeted outreach and service bundling",
        "High-risk customers could be targeted with contract incentives, personalised support, loyalty offers, or service bundles that improve perceived value."
    )}
</div>
""")
st.markdown(insights_html, unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-panel">
        <div class="highlight-title">Main Business Value</div>
        This project demonstrates how machine learning can support customer retention by identifying who is likely to churn, 
        explaining the main drivers of churn risk, and helping the business prioritise high-risk customers. The strongest demo 
        model achieves a ROC-AUC of <b>0.86</b>, suggesting that the model can rank customers by churn risk and support targeted 
        retention campaigns.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# What this project demonstrates
# ============================================================
st.markdown('<div class="section-title">What This Project Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project demonstrates end-to-end machine learning, business interpretation, and customer analytics capability.</div>',
    unsafe_allow_html=True
)

demonstrates_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Machine Learning",
        "Classification modelling",
        "The project demonstrates how to build and compare multiple classification models for customer churn prediction."
    )}

    {info_card(
        "Customer Analytics",
        "Understanding churn behaviour",
        "The work connects customer attributes, usage behaviour, billing information, and churn outcomes."
    )}

    {info_card(
        "Business Translation",
        "From model output to retention action",
        "The project shows how predictions and churn drivers can be converted into practical retention recommendations."
    )}

    {info_card(
        "Model Evaluation",
        "Choosing metrics for the business problem",
        "The model is evaluated using accuracy, recall, precision, F1-score, ROC-AUC, and business error interpretation."
    )}
</div>
""")
st.markdown(demonstrates_html, unsafe_allow_html=True)

# ============================================================
# Skills used
# ============================================================
st.markdown('<div class="section-title">Skills Used</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Key technical and analytical capabilities demonstrated through this churn prediction project.</div>',
    unsafe_allow_html=True
)

skills_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Python Analytics",
        "Data preparation and modelling",
        "Python · pandas · NumPy",
        "Used Python to clean customer data, prepare features, split data, and build a repeatable machine learning workflow."
    )}

    {capability_card(
        "Machine Learning",
        "Classification model comparison",
        "Logistic Regression · Random Forest · Gradient Boosting",
        "Compared multiple classification models to predict customer churn risk and select the best-performing approach."
    )}

    {capability_card(
        "Feature Engineering",
        "Customer attribute preparation",
        "Encoding · scaling · tenure bands · service features",
        "Prepared numeric and categorical variables so they could be used effectively by machine learning models."
    )}

    {capability_card(
        "Evaluation",
        "Classification performance analysis",
        "Accuracy · precision · recall · F1 · ROC-AUC",
        "Used multiple metrics to evaluate performance, especially because churn is a business-sensitive classification problem."
    )}

    {capability_card(
        "Business Analytics",
        "Retention-focused interpretation",
        "Churn drivers · risk segments · retention strategy",
        "Translated technical model outputs into business insights about customer risk and possible retention actions."
    )}

    {capability_card(
        "Explainability",
        "Feature importance analysis",
        "Driver ranking · model interpretation · stakeholder explanation",
        "Identified the most important churn drivers and explained how they connect to business behaviour."
    )}

    {capability_card(
        "Dashboard Thinking",
        "Potential risk monitoring tool",
        "Risk score · customer segment · model output",
        "Designed the project so it could be extended into a dashboard for monitoring high-risk customers."
    )}

    {capability_card(
        "Communication",
        "Model results for non-technical users",
        "Clear metrics · business value · recommendations",
        "Presented model performance and churn insights in a way that can be understood by business stakeholders."
    )}
</div>
""")
st.markdown(skills_html, unsafe_allow_html=True)

# ============================================================
# Future improvements
# ============================================================
st.markdown('<div class="section-title">Future Improvements</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Possible next steps to make the project stronger, more reliable, and more business-ready.</div>',
    unsafe_allow_html=True
)

future_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Final Training Results",
        "Replace demo metrics with real validated scores",
        "After final model training, update the demo results with actual scores from the selected public churn dataset."
    )}

    {info_card(
        "Threshold Optimisation",
        "Tune for retention strategy",
        "Adjust the churn probability threshold based on business trade-offs between campaign cost and missed churn risk."
    )}

    {info_card(
        "Customer Segmentation",
        "Group high-risk customers",
        "Segment customers by churn risk, contract type, tenure, monthly spend, and service usage to support targeted retention actions."
    )}

    {info_card(
        "Explainability",
        "Add SHAP or feature impact views",
        "Use SHAP values or other explainability methods to show why individual customers are predicted as high risk."
    )}

    {info_card(
        "Deployment",
        "Interactive churn risk dashboard",
        "Build a Streamlit dashboard where users can view churn KPIs, upload customer data, and inspect high-risk customer segments."
    )}

    {info_card(
        "Business Experimentation",
        "Measure retention campaign impact",
        "Connect churn predictions to A/B testing or campaign tracking to evaluate whether retention actions reduce churn."
    )}
</div>
""")
st.markdown(future_html, unsafe_allow_html=True)