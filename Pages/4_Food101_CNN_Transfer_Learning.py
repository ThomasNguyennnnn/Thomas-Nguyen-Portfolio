import streamlit as st
from textwrap import dedent

# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="Food101 CNN Transfer Learning | Thomas Nguyen",
    page_icon="🍽️",
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
    <div class="eyebrow">Deep Learning Project · Computer Vision</div>
    <div class="page-title">Food101 CNN <span class="gradient-text">Transfer Learning</span></div>
    <div class="subtitle">Computer Vision · CNNs · Transfer Learning · Fine-Tuning · Image Classification</div>
    <div class="body-text">
        This project applies transfer learning to the Food101 image classification task, comparing frozen CNN feature extraction 
        with progressive fine-tuning strategies. The aim was to understand how much performance improvement could be achieved 
        by moving from a frozen pre-trained CNN backbone to deeper trainable layers.
        <br><br>
        The strongest result came from fine-tuning <b>ResNet50 layer3 + layer4</b>, which improved test accuracy from 
        <b>0.6186</b> in the frozen baseline to <b>0.8507</b>. This represents a practical improvement of 
        <b>+0.2321 accuracy points</b>, or approximately <b>37.5% relative improvement</b> compared with the frozen feature extractor.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Food101 Dataset</span>
        <span class="hero-tag">ResNet50</span>
        <span class="hero-tag">Transfer Learning</span>
        <span class="hero-tag">Fine-Tuning</span>
        <span class="hero-tag">Image Classification</span>
        <span class="hero-tag">PyTorch</span>
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
    '<div class="section-subtitle">A quick overview of the dataset, model strategy, and strongest performance result.</div>',
    unsafe_allow_html=True
)

snapshot_html = dedent(f"""
<div class="grid-4">
    {metric_card("Food101", "Dataset", "Food image classification dataset used to evaluate CNN transfer learning.")}
    {metric_card("ResNet50", "Main architecture", "Pre-trained CNN backbone used for frozen feature extraction and fine-tuning.")}
    {metric_card("0.8507", "Best accuracy", "Best result achieved by fine-tuning ResNet50 layer3 and layer4.")}
    {metric_card("+37.5%", "Relative improvement", "Approximate improvement from frozen ResNet50 baseline to best fine-tuned model.")}
</div>
""")
st.markdown(snapshot_html, unsafe_allow_html=True)

# ============================================================
# Computer vision problem
# ============================================================
st.markdown('<div class="section-title">Computer Vision Problem</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Food image classification is challenging because many categories have similar colours, textures, shapes, and plating styles.</div>',
    unsafe_allow_html=True
)

problem_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Classification Task",
        "Predict the food category from an image",
        "The model receives a food image and predicts its class. This requires the CNN to learn visual patterns such as colour, texture, shape, ingredients, and food presentation."
    )}

    {info_card(
        "Visual Similarity",
        "Many food classes look alike",
        "Food categories can share similar backgrounds, ingredients, or plating styles. This makes the task harder than simple object recognition because the visual differences can be subtle."
    )}

    {info_card(
        "Transfer Learning Goal",
        "Reuse visual knowledge from pre-training",
        "Instead of training a CNN from scratch, the project uses a pre-trained ResNet50 model and adapts it to Food101 through feature extraction and fine-tuning."
    )}
</div>
""")
st.markdown(problem_html, unsafe_allow_html=True)

# ============================================================
# Dataset and task
# ============================================================
st.markdown('<div class="section-title">Dataset & Task Setup</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project uses Food101 as a practical benchmark for multi-class food image classification.</div>',
    unsafe_allow_html=True
)

dataset_html = dedent(f"""
<div class="grid-2">
    {timeline_card(
        "Food101 Image Dataset",
        "Multi-class food recognition",
        "The project uses Food101 as the image classification dataset. The task is to classify food images into the correct food category using convolutional neural network models."
    )}

    {timeline_card(
        "Input Representation",
        "Food images as visual tensors",
        "Images are resized, normalised, and passed through a CNN backbone. The model learns hierarchical visual features, starting from edges and textures and progressing to higher-level food patterns."
    )}

    {timeline_card(
        "Model Backbone",
        "ResNet50 pre-trained CNN",
        "ResNet50 was used as the main architecture because it provides a strong pre-trained feature extractor and supports practical fine-tuning strategies."
    )}

    {timeline_card(
        "Evaluation Target",
        "Classification accuracy",
        "The main evaluation metric is accuracy, comparing how often each training strategy correctly predicts the food category on the evaluation set."
    )}
</div>
""")
st.markdown(dataset_html, unsafe_allow_html=True)

# ============================================================
# Modelling strategy
# ============================================================
st.markdown('<div class="section-title">Modelling Strategy</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The project compares frozen feature extraction with progressively deeper fine-tuning.</div>',
    unsafe_allow_html=True
)

strategy_html = dedent(f"""
<div class="grid-3">
    {process_card(
        "01",
        "Frozen feature extraction",
        "Use the pre-trained ResNet50 backbone as a fixed feature extractor. Only the final classifier layers are trained for Food101."
    )}

    {process_card(
        "02",
        "Fine-tune layer4",
        "Unfreeze the final ResNet block to adapt higher-level visual features to food-specific patterns while keeping earlier layers stable."
    )}

    {process_card(
        "03",
        "Fine-tune layer3 + layer4",
        "Unfreeze deeper parts of the network so the model can adapt more of its learned representation to Food101, producing the strongest result."
    )}
</div>
""")
st.markdown(strategy_html, unsafe_allow_html=True)

# ============================================================
# Experiment design
# ============================================================
st.markdown('<div class="section-title">Experiment Design</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The experiment was designed to test how much additional performance comes from unfreezing more CNN layers.</div>',
    unsafe_allow_html=True
)

experiment_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Baseline",
        "Frozen ResNet50",
        "Accuracy: 0.6186",
        "Provides a baseline to test how well pre-trained ImageNet features transfer to food classification without updating the CNN backbone."
    )}

    {capability_card(
        "Fine-Tuning 1",
        "Unfreeze layer4",
        "Accuracy: 0.8175",
        "Allows the final high-level feature block to adapt to Food101, giving a large improvement over the frozen feature extractor."
    )}

    {capability_card(
        "Fine-Tuning 2",
        "Unfreeze layer3 + layer4",
        "Accuracy: 0.8507",
        "Allows a deeper part of the network to adapt to food-specific visual patterns, producing the best performance."
    )}

    {capability_card(
        "Comparison",
        "Performance gain",
        "+0.2321 accuracy points",
        "The best fine-tuned model improved substantially over the frozen ResNet50 baseline, showing the value of targeted fine-tuning."
    )}
</div>
""")
st.markdown(experiment_html, unsafe_allow_html=True)

# ============================================================
# Results
# ============================================================
st.markdown('<div class="section-title">Results</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Fine-tuning deeper ResNet50 layers produced a clear performance improvement over the frozen baseline.</div>',
    unsafe_allow_html=True
)

results_table = """
<div class="table-wrap">
<table class="result-table">
    <tr>
        <th>Model / Strategy</th>
        <th>Trainable Backbone</th>
        <th>Accuracy</th>
        <th>Interpretation</th>
    </tr>
    <tr>
        <td>ResNet50 frozen feature extractor</td>
        <td>Backbone frozen</td>
        <td>0.6186</td>
        <td>Useful baseline, but limited adaptation to food-specific visual patterns.</td>
    </tr>
    <tr>
        <td>ResNet50 fine-tune layer4</td>
        <td>Layer4 trainable</td>
        <td>0.8175</td>
        <td>Large improvement after allowing high-level CNN features to adapt.</td>
    </tr>
    <tr class="best-row">
        <td>ResNet50 fine-tune layer3 + layer4</td>
        <td>Layer3 + Layer4 trainable</td>
        <td>0.8507</td>
        <td>Best result, showing stronger adaptation to food-specific features.</td>
    </tr>
</table>
</div>
"""
st.markdown(results_table, unsafe_allow_html=True)

results_html = dedent(f"""
<div class="grid-3" style="margin-top: 1.35rem;">
    {metric_card("0.6186", "Frozen baseline", "Best Part A result using frozen ResNet50 feature extraction.")}
    {metric_card("0.8175", "Layer4 fine-tuning", "Strong Part B result after unfreezing the final ResNet block.")}
    {metric_card("0.8507", "Layer3 + Layer4 fine-tuning", "Best Part B result after unfreezing deeper CNN layers.")}
</div>
""")
st.markdown(results_html, unsafe_allow_html=True)

st.markdown(
    """
    <div class="highlight-panel">
        <div class="highlight-title">Main Result</div>
        The best model improved from <b>0.6186</b> accuracy with frozen ResNet50 features to <b>0.8507</b> accuracy after 
        fine-tuning layer3 and layer4. This is a gain of <b>+0.2321 accuracy points</b>, showing that Food101 benefits 
        strongly from adapting deeper CNN features rather than relying only on a frozen pre-trained backbone.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# Key findings
# ============================================================
st.markdown('<div class="section-title">Key Findings</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The experiment shows how model performance changes as more of the CNN backbone is allowed to adapt.</div>',
    unsafe_allow_html=True
)

findings_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Finding 1",
        "Frozen features are useful but limited",
        "The frozen ResNet50 model reached 0.6186 accuracy, showing that pre-trained visual features transfer reasonably well, but they do not fully capture food-specific differences."
    )}

    {info_card(
        "Finding 2",
        "Fine-tuning gives major gains",
        "Unfreezing layer4 increased accuracy to 0.8175, showing that adapting high-level CNN features provides a large performance improvement."
    )}

    {info_card(
        "Finding 3",
        "Deeper fine-tuning performed best",
        "Fine-tuning both layer3 and layer4 achieved the best accuracy of 0.8507, suggesting that Food101 benefits from adapting deeper visual representations."
    )}
</div>
""")
st.markdown(findings_html, unsafe_allow_html=True)

# ============================================================
# What this project demonstrates
# ============================================================
st.markdown('<div class="section-title">What This Project Demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This project demonstrates applied deep learning, experimental comparison, and computer vision model improvement.</div>',
    unsafe_allow_html=True
)

demonstrates_html = dedent(f"""
<div class="grid-4">
    {info_card(
        "Computer Vision",
        "Image classification pipeline",
        "The project demonstrates the ability to build and evaluate a CNN-based image classification workflow."
    )}

    {info_card(
        "Transfer Learning",
        "Using pre-trained CNNs effectively",
        "The work shows how pre-trained models can be adapted to a new domain instead of training from scratch."
    )}

    {info_card(
        "Fine-Tuning",
        "Choosing trainable layers",
        "The project compares frozen features, partial fine-tuning, and deeper fine-tuning to understand model improvement."
    )}

    {info_card(
        "Evaluation",
        "Evidence-based model selection",
        "The final model choice is supported by accuracy results across multiple training strategies."
    )}
</div>
""")
st.markdown(demonstrates_html, unsafe_allow_html=True)

# ============================================================
# Skills used
# ============================================================
st.markdown('<div class="section-title">Skills Used</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Key technical capabilities demonstrated through this deep learning project.</div>',
    unsafe_allow_html=True
)

skills_html = dedent(f"""
<div class="grid-4">
    {capability_card(
        "Deep Learning",
        "CNN-based modelling",
        "ResNet50 · convolutional neural networks · image classification",
        "Built image classification models using a pre-trained CNN architecture and compared multiple training strategies."
    )}

    {capability_card(
        "Transfer Learning",
        "Frozen features and fine-tuning",
        "Feature extraction · layer freezing · trainable blocks",
        "Applied transfer learning by first using frozen features and then progressively fine-tuning deeper ResNet50 layers."
    )}

    {capability_card(
        "Experimentation",
        "Model comparison",
        "Baseline · layer4 · layer3 + layer4",
        "Designed experiments to compare how trainable backbone depth affected Food101 classification accuracy."
    )}

    {capability_card(
        "Model Evaluation",
        "Accuracy-based performance analysis",
        "Accuracy · improvement calculation · result interpretation",
        "Compared results across model variants and explained why fine-tuning improved performance."
    )}

    {capability_card(
        "Python Workflow",
        "Deep learning implementation",
        "Python · PyTorch · notebooks",
        "Implemented training, fine-tuning, evaluation, and result tracking in a practical notebook workflow."
    )}

    {capability_card(
        "Data Preparation",
        "Image preprocessing",
        "Resize · normalisation · batching · augmentation context",
        "Prepared image data for CNN training using standard preprocessing steps required for pre-trained models."
    )}

    {capability_card(
        "Technical Reasoning",
        "Why fine-tuning works",
        "Feature hierarchy · domain adaptation · visual representations",
        "Interpreted results in terms of CNN feature hierarchy and the need to adapt high-level food-specific visual features."
    )}

    {capability_card(
        "Communication",
        "Explaining model results",
        "Result table · comparison · conclusion",
        "Presented the experimental results clearly so that the model improvement is easy to understand."
    )}
</div>
""")
st.markdown(skills_html, unsafe_allow_html=True)

# ============================================================
# Future improvements
# ============================================================
st.markdown('<div class="section-title">Future Improvements</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Possible next steps to improve the project further and make it more production-ready.</div>',
    unsafe_allow_html=True
)

future_html = dedent(f"""
<div class="grid-3">
    {info_card(
        "Data Augmentation",
        "Improve robustness",
        "Apply stronger image augmentation strategies such as random cropping, colour jitter, rotation, and mixup to help the model generalise better."
    )}

    {info_card(
        "Error Analysis",
        "Understand confused food classes",
        "Review misclassified images and confusion patterns to identify categories that the model struggles to separate."
    )}

    {info_card(
        "Model Comparison",
        "Test newer architectures",
        "Compare ResNet50 with EfficientNet, ConvNeXt, or Vision Transformer models to evaluate whether newer architectures improve accuracy."
    )}

    {info_card(
        "Deployment",
        "Interactive food classifier",
        "Build a Streamlit image upload app where users can upload a food photo and receive predicted food classes with confidence scores."
    )}

    {info_card(
        "Explainability",
        "Show where the model looks",
        "Use Grad-CAM or saliency maps to visualise image regions that influenced the model's prediction."
    )}

    {info_card(
        "Optimisation",
        "Improve training efficiency",
        "Use learning-rate scheduling, early stopping, mixed precision, and systematic hyperparameter tuning to improve performance and reduce training time."
    )}
</div>
""")
st.markdown(future_html, unsafe_allow_html=True)