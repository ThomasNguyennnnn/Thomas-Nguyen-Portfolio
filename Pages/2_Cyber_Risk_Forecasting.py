import streamlit as st
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Cyber Risk Forecasting | Thomas Nguyen",
    page_icon="🛡️",
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


def model_card(label, title, role, text):
    return dedent(f"""
    <div class="model-card">
        <div class="card-label">{label}</div>
        <div class="model-title">{title}</div>
        <div class="model-role">{role}</div>
        <div class="model-text">{text}</div>
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

/* --------------------------------------------------------
   Global style
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
   Generic information cards
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
    min-height: 245px;
    height: 100%;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    display: flex;
    flex-direction: column;
}

.info-card:before,
.metric-card:before,
.model-card:before,
.process-card:before,
.timeline-card:before {
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
   Metric cards
-------------------------------------------------------- */
.metric-card {
    padding: 1.35rem 1.4rem;
    border-radius: 26px;
    background:
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow:
        0 16px 38px rgba(59, 130, 246, 0.08),
        0 0 0 1px rgba(255,255,255,0.24) inset;
    min-height: 160px;
    height: 100%;
    position: relative;
    overflow: hidden;
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
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 16px 38px rgba(59, 130, 246, 0.08);
    min-height: 230px;
    height: 100%;
    position: relative;
    overflow: hidden;
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
   Model cards
-------------------------------------------------------- */
.model-card {
    padding: 1.5rem 1.55rem;
    border-radius: 28px;
    background:
        radial-gradient(circle at top right, rgba(6, 182, 212, 0.08), transparent 26%),
        linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.92));
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 16px 38px rgba(59, 130, 246, 0.08);
    min-height: 260px;
    height: 100%;
    position: relative;
    overflow: hidden;
}

.model-title {
    font-size: 1.1rem;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 0.35rem;
}

.model-role {
    font-size: 0.88rem;
    color: #4f46e5;
    font-weight: 900;
    margin-bottom: 0.7rem;
}

.model-text {
    font-size: 0.92rem;
    line-height: 1.62;
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
    border: 1px solid rgba(167, 139, 250, 0.22);
    box-shadow: 0 14px 34px rgba(59, 130, 246, 0.08);
    min-height: 200px;
    height: 100%;
    position: relative;
    overflow: hidden;
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
   Results table
-------------------------------------------------------- */
.table-wrap {
    border-radius: 26px;
    overflow: hidden;
    border: 1px solid rgba(167, 139, 250, 0.24);
    box-shadow: 0 18px 45px rgba(59, 130, 246, 0.10);
    background: rgba(255,255,255,0.94);
}

.model-table {
    width: 100%;
    border-collapse: collapse;
}

.model-table th {
    background: linear-gradient(90deg, #2563eb, #7c3aed, #06b6d4);
    color: white;
    padding: 0.95rem;
    font-size: 0.88rem;
    text-align: left;
    white-space: nowrap;
}

.model-table td {
    padding: 0.88rem 0.95rem;
    font-size: 0.88rem;
    color: #334155;
    border-bottom: 1px solid rgba(167, 139, 250, 0.18);
}

.model-table tr:last-child td {
    border-bottom: none;
}

.best-row {
    background: rgba(219, 234, 254, 0.48);
    font-weight: 850;
}

/* --------------------------------------------------------
   Highlight statement
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
    <div class="eyebrow">Academic Research Project · Advanced Machine Learning</div>
    <div class="page-title">Cyber Risk <span class="gradient-text">Forecasting</span></div>
    <div class="subtitle">Hawkes Processes · Transformer Hawkes · Neural Hawkes · Temporal Point Processes</div>
    <div class="body-text">
        This research project investigates whether Hawkes-process-based and Transformer-based sequence models can support 
        effective short-horizon cyber-risk prediction. The study uses a synthetic multivariate marked Hawkes benchmark to model 
        temporal clustering, severity variation, self-excitation, and propagation across six interacting entities.
        <br><br>
        The main forecasting task is to identify the <b>top-risk entity in the next risk window</b>. The proposed Transformer 
        Hawkes Process is compared with a Poisson count baseline, a Neural Hawkes-style supervised GRU/LSTM model, a real 
        likelihood-based Neural Hawkes Process, and an MCP-Titan memory retrieval baseline.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Research Design</span>
        <span class="hero-tag">Synthetic Benchmark</span>
        <span class="hero-tag">Temporal Modelling</span>
        <span class="hero-tag">Sequence Learning</span>
        <span class="hero-tag">Model Evaluation</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# Project Snapshot
# ============================================================
st.markdown('<div class="section-title">Project Snapshot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A quick overview of the research scope, modelling setup, and strongest results.</div>',
    unsafe_allow_html=True
)

snapshot_html = dedent(f"""
<div class="grid-4">
    {metric_card("0.8913", "Best main accuracy", "Transformer Hawkes Process achieved the strongest result on top-risk entity prediction.")}
    {metric_card("0.9700", "Top-2 accuracy", "The correct high-risk entity was usually ranked within the model's top two predictions.")}
    {metric_card("6", "Interacting entities", "The synthetic benchmark models cyber-risk propagation across six connected entities.")}
    {metric_card("5", "Model families", "The study compares statistical, recurrent, Transformer, likelihood-based, and retrieval baselines.")}
</div>
""")
st.markdown(snapshot_html, unsafe_allow_html=True)

# ============================================================
# Research Problem
# ============================================================
st.markdown('<div class="section-title">Research Problem</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Cyber incidents are dynamic, clustered, and interconnected, which makes static risk modelling insufficient.</div>',
    unsafe_allow_html=True
)

problem_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Motivation",
        "Cyber risk is not independent",
        "Cyber incidents often emerge in bursts, propagate across shared infrastructure, and create accumulation effects. A breach, vulnerability, or exploit affecting one entity can raise the risk for connected entities."
    )}

    {info_card(
        "Research Gap",
        "Limited temporal dependence modelling",
        "Traditional actuarial and static models often struggle to represent self-excitation, inter-entity dependence, and time-varying cyber-risk dynamics. The project addresses this gap through Hawkes-inspired modelling."
    )}

    {info_card(
        "Main Question",
        "Can Hawkes + Transformer models forecast risk?",
        "The study evaluates whether a Hawkes process coupled with a Transformer-based model can effectively predict future cyber risk and outperform relevant Neural Hawkes and count-based baselines."
    )}
</div>
""")
st.markdown(problem_html, unsafe_allow_html=True)

# ============================================================
# Benchmark Design
# ============================================================
st.markdown('<div class="section-title">Synthetic Hawkes Benchmark</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The dataset was designed as a controlled environment for testing temporal cyber-risk forecasting models.</div>',
    unsafe_allow_html=True
)

benchmark_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Multivariate marked Hawkes process",
        "Temporal clustering · severity variation · self-excitation",
        "The benchmark generates irregular cyber-risk events using a multivariate marked Hawkes process. Each event contains time, entity, severity mark, transformed excitation weight, and label information."
    )}

    {timeline_card(
        "Six interacting entities",
        "Directional contagion structure",
        "The simulation represents six entities connected through strong forward contagion, weaker reverse spillover, and second-hop forward spillover. This creates a controlled representation of propagation across connected systems."
    )}

    {timeline_card(
        "Learnable marks and severity context",
        "Mark-dependent excitation",
        "Severity marks are designed to be partially predictable from entity-level risk, covariate state, and recent event activity, preventing the task from becoming pure noise."
    )}

    {timeline_card(
        "Shared raw event stream",
        "Model-specific preprocessing",
        "The simulator generates a shared raw event stream first. Task-specific labels and model-specific features are created later so that all models begin from the same event history."
    )}
</div>
""")
st.markdown(benchmark_html, unsafe_allow_html=True)

# ============================================================
# Prediction Task
# ============================================================
st.markdown('<div class="section-title">Prediction Task</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The main task is designed around practical short-horizon risk ranking rather than exact next-event prediction.</div>',
    unsafe_allow_html=True
)

task_html = dedent(f"""
<div class="grid-3">
    {process_card(
        "01",
        "Observe recent event history",
        "The model receives a sequence of recent events, including entity identity, event timing, severity mark, and excitation-related information."
    )}

    {process_card(
        "02",
        "Look into the next risk window",
        "For each event time, the future window is examined to identify which entity accumulates the highest number of events."
    )}

    {process_card(
        "03",
        "Predict the top-risk entity",
        "The model predicts the entity expected to be at the highest risk in the next short-horizon window, creating a practical risk-ranking objective."
    )}
</div>
""")
st.markdown(task_html, unsafe_allow_html=True)

# ============================================================
# Methodology
# ============================================================
st.markdown('<div class="section-title">Methodology</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project compares simpler baselines against sequence models designed to learn temporal cyber-risk structure.</div>',
    unsafe_allow_html=True
)

method_html = dedent(f"""
<div class="grid-4">
    {process_card(
        "Step 1",
        "Generate event stream",
        "Simulate a six-entity cyber-risk event stream using a multivariate marked Hawkes process."
    )}

    {process_card(
        "Step 2",
        "Create supervised samples",
        "Use sliding windows to transform the raw event stream into model-ready sequence samples."
    )}

    {process_card(
        "Step 3",
        "Train model families",
        "Train statistical, recurrent, Transformer, likelihood-based, and retrieval-style models on the same benchmark."
    )}

    {process_card(
        "Step 4",
        "Compare results",
        "Evaluate exact prediction, top-k ranking quality, and auxiliary severity and time-window tasks."
    )}
</div>
""")
st.markdown(method_html, unsafe_allow_html=True)

# ============================================================
# Models Compared
# ============================================================
st.markdown('<div class="section-title">Models Compared</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project uses a comparative evaluation design across five model families.</div>',
    unsafe_allow_html=True
)

models_html = dedent(f"""
<div class="grid-3">
    {model_card(
        "Baseline",
        "Poisson Count Baseline",
        "Simple statistical benchmark",
        "Uses count-based history to test how much can be predicted from simpler lagged activity features."
    )}

    {model_card(
        "Sequence Model",
        "Neural Hawkes-style GRU/LSTM",
        "Supervised recurrent benchmark",
        "Uses event history, timing, marks, excitation-related features, and recurrent neural networks for task-specific classification."
    )}

    {model_card(
        "Point Process",
        "Real Neural Hawkes Process",
        "Likelihood-based baseline",
        "Optimises continuous-time event likelihood and provides a theoretically aligned temporal point-process comparison."
    )}

    {model_card(
        "Main Model",
        "Transformer Hawkes Process",
        "Attention-based temporal model",
        "Uses self-attention to capture longer-range dependencies in event sequences and predict future-window risk concentration."
    )}

    {model_card(
        "Retrieval Baseline",
        "MCP-Titan",
        "Memory retrieval approach",
        "Explores whether similarity to historical event windows can support risk prediction."
    )}

    {model_card(
        "Evaluation Design",
        "Shared forecasting framework",
        "Consistent benchmark and task",
        "All models are evaluated on the same synthetic event stream and main top-risk entity prediction task."
    )}
</div>
""")
st.markdown(models_html, unsafe_allow_html=True)

# ============================================================
# Comparative Results
# ============================================================
st.markdown('<div class="section-title">Comparative Results</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The Transformer Hawkes Process achieved the strongest main-task accuracy, while the supervised Neural Hawkes-style model remained highly competitive.</div>',
    unsafe_allow_html=True
)

results_table = """
<div class="table-wrap">
<table class="model-table">
    <tr>
        <th>Model</th>
        <th>Main Acc.</th>
        <th>Macro-F1</th>
        <th>Weighted-F1</th>
        <th>Top-2</th>
        <th>Top-3</th>
        <th>Severity Acc.</th>
        <th>Time Acc.</th>
    </tr>
    <tr>
        <td>Poisson baseline</td>
        <td>0.3873</td>
        <td>0.2290</td>
        <td>0.3470</td>
        <td>–</td>
        <td>–</td>
        <td>0.3307</td>
        <td>0.2553</td>
    </tr>
    <tr>
        <td>Neural Hawkes-style supervised GRU/LSTM</td>
        <td>0.8621</td>
        <td>0.8565</td>
        <td>0.8625</td>
        <td>0.9598</td>
        <td>0.9893</td>
        <td>0.3414</td>
        <td>0.3956</td>
    </tr>
    <tr>
        <td>Real Neural Hawkes Process</td>
        <td>0.2753</td>
        <td>0.0987</td>
        <td>0.1426</td>
        <td>0.4773</td>
        <td>0.6667</td>
        <td>0.3327</td>
        <td>0.3520</td>
    </tr>
    <tr class="best-row">
        <td>Transformer Hawkes Process</td>
        <td>0.8913</td>
        <td>0.8436</td>
        <td>0.8519</td>
        <td>0.9700</td>
        <td>0.9887</td>
        <td>0.3140</td>
        <td>0.3400</td>
    </tr>
    <tr>
        <td>MCP-Titan retrieval baseline</td>
        <td>0.2567</td>
        <td>0.2206</td>
        <td>0.2491</td>
        <td>0.4873</td>
        <td>0.6400</td>
        <td>0.3560</td>
        <td>0.3700</td>
    </tr>
</table>
</div>
"""
st.markdown(results_table, unsafe_allow_html=True)

results_html = dedent(f"""
<div class="grid-3" style="margin-top: 1.35rem;">
    {metric_card("0.8913", "THP main accuracy", "Best exact prediction result on the top-risk entity task.")}
    {metric_card("0.9700", "THP top-2 accuracy", "Strong risk-ranking performance across the test set.")}
    {metric_card("0.9887", "THP top-3 accuracy", "The correct entity was almost always in the top three predictions.")}
</div>
""")
st.markdown(results_html, unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-panel">
        <div class="highlight-title">Main Interpretation</div>
        The results suggest that attention-based temporal sequence modelling can capture useful structure in the simulated 
        cyber-risk event stream. The Transformer Hawkes Process achieved the strongest performance on the primary task, 
        while the supervised Neural Hawkes-style GRU/LSTM model remained highly competitive. The lower performance of the 
        Poisson baseline, real Neural Hawkes Process, and retrieval baseline highlights the importance of matching the 
        modelling objective to the practical forecasting task.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# What the Project Demonstrates
# ============================================================
st.markdown('<div class="section-title">What This Project Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project demonstrates research capability, advanced modelling, and practical evaluation thinking.</div>',
    unsafe_allow_html=True
)

demonstrates_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Research Thinking",
        "From gap to experiment",
        "The project identifies a research gap, designs a synthetic benchmark, and evaluates whether Hawkes-inspired models can support cyber-risk forecasting."
    )}

    {info_card(
        "Temporal Modelling",
        "Events over time",
        "The work uses temporal point-process ideas to represent event clustering, self-excitation, and cross-entity propagation."
    )}

    {info_card(
        "Deep Learning",
        "Sequence learning",
        "The project compares recurrent and attention-based sequence models for forecasting future cyber-risk concentration."
    )}

    {info_card(
        "Evaluation",
        "Model comparison",
        "The study compares multiple model families using consistent tasks and metrics, including accuracy, F1, and top-k ranking quality."
    )}
</div>
""")
st.markdown(demonstrates_html, unsafe_allow_html=True)

# ============================================================
# Skills Used
# ============================================================
st.markdown('<div class="section-title">Skills Used</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Key technical and research capabilities demonstrated through this project.</div>',
    unsafe_allow_html=True
)

skills_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Programming",
        "Python and R",
        "Used for event simulation, preprocessing, modelling, experiment management, and evaluation."
    )}

    {info_card(
        "Machine Learning",
        "Sequence and temporal models",
        "Applied recurrent neural networks, Transformer-based modelling, and temporal point-process concepts."
    )}

    {info_card(
        "Research Design",
        "Synthetic benchmark construction",
        "Designed a controlled experiment that separates data generation, preprocessing, modelling, and evaluation."
    )}

    {info_card(
        "Technical Writing",
        "Academic reporting",
        "Documented the motivation, related work, methodology, results, limitations, and conclusion in a research-paper format."
    )}
</div>
""")
st.markdown(skills_html, unsafe_allow_html=True)

# ============================================================
# Limitations and Future Improvements
# ============================================================
st.markdown('<div class="section-title">Limitations & Future Improvements</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The study provides controlled methodological evidence, with clear directions for extension.</div>',
    unsafe_allow_html=True
)

future_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Synthetic Dataset",
        "Real-world validation needed",
        "The current benchmark is synthetic, so future work should test the framework on empirical cyber incident or security-event datasets where available."
    )}

    {info_card(
        "Network Diversity",
        "Richer dependency structures",
        "Future experiments could vary the number of entities, contagion strength, propagation lags, sparsity, severity dynamics, and noise conditions."
    )}

    {info_card(
        "Deployment Direction",
        "Interactive risk dashboard",
        "The forecasting outputs could be connected to a dashboard showing top-risk entities, model confidence, temporal patterns, and risk-window changes."
    )}
</div>
""")
st.markdown(future_html, unsafe_allow_html=True)