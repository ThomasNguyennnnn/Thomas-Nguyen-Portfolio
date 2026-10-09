
import streamlit as st
import plotly.graph_objects as go
from textwrap import dedent
from html import escape

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Food101 CNN Transfer Learning | Thomas Nguyen",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# COLOUR PALETTE
# ============================================================

BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#0891b2"

TEXT_DARK = "#0f172a"
TEXT_MAIN = "#334155"
TEXT_MUTED = "#475569"

# ============================================================
# REPORTED EXPERIMENTAL RESULTS
# ============================================================

# These are the actual test accuracies reported
# in the original Food101 project.

EXPERIMENTS = [
    {
        "name": "Frozen ResNet50",
        "short": "Frozen backbone",
        "accuracy": 0.6186,
        "configuration": "Frozen backbone; classifier trained",
        "part": "Part A"
    },
    {
        "name": "ResNet50 — layer4",
        "short": "Fine-tune layer4",
        "accuracy": 0.8175,
        "configuration": "Final residual block trainable",
        "part": "Part B"
    },
    {
        "name": "ResNet50 — layer3 + layer4",
        "short": "Fine-tune layer3 + layer4",
        "accuracy": 0.8507,
        "configuration": "Last two residual stages trainable",
        "part": "Part B"
    }
]

FROZEN_ACC = EXPERIMENTS[0]["accuracy"]
LAYER4_ACC = EXPERIMENTS[1]["accuracy"]
BEST_ACC = EXPERIMENTS[2]["accuracy"]

GAIN_LAYER4_PP = (LAYER4_ACC - FROZEN_ACC) * 100
GAIN_BEST_PP = (BEST_ACC - FROZEN_ACC) * 100
GAIN_EXTRA_PP = (BEST_ACC - LAYER4_ACC) * 100

RELATIVE_GAIN = (
    (BEST_ACC - FROZEN_ACC) / FROZEN_ACC
) * 100

FROZEN_ERROR = (1 - FROZEN_ACC) * 100
BEST_ERROR = (1 - BEST_ACC) * 100

ERROR_REDUCTION = (
    (FROZEN_ERROR - BEST_ERROR) / FROZEN_ERROR
) * 100

# ============================================================
# STANDARD FOOD-101 DATASET SPECIFICATION
# ============================================================

# The standard public Food-101 benchmark contains:
# 101 classes, 1,000 images per class,
# with 750 training and 250 test images per class.
#
# These are benchmark specifications, not a claim
# about the exact number of samples processed
# in the user's training run.

FOOD_CLASSES = 101
IMAGES_PER_CLASS = 1000

OFFICIAL_TRAIN_IMAGES = 75750
OFFICIAL_TEST_IMAGES = 25250

OFFICIAL_TOTAL_IMAGES = (
    OFFICIAL_TRAIN_IMAGES + OFFICIAL_TEST_IMAGES
)


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


def process_card(step, title, text):
    return compact_html(f"""
        <div class="process-card">
            <div class="step-badge">{step}</div>
            <div class="process-title">{title}</div>
            <div class="process-text">{text}</div>
        </div>
    """)


def highlight_panel(title, text):
    return compact_html(f"""
        <div class="highlight-panel">
            <div class="highlight-title">{title}</div>
            <div class="highlight-text">{text}</div>
        </div>
    """)


def note_panel(text):
    render_html(f"""
        <div class="research-note">{text}</div>
    """)


def data_table(headers, rows, best_row=None):
    head = "".join(
        f"<th>{escape(str(h))}</th>"
        for h in headers
    )

    body = ""

    for index, row in enumerate(rows):
        css_class = (
            ' class="best-row"'
            if index == best_row
            else ""
        )

        cells = "".join(
            f"<td>{escape(str(value))}</td>"
            for value in row
        )

        body += f"<tr{css_class}>{cells}</tr>"

    return compact_html(f"""
        <div class="table-wrap">
            <table class="result-table">
                <thead><tr>{head}</tr></thead>
                <tbody>{body}</tbody>
            </table>
        </div>
    """)


# ============================================================
# CENTRAL PLOTLY STYLING — DARK READABLE TEXT
# ============================================================

def style_chart(fig, height=410):

    fig.update_layout(
        template="plotly_white",
        height=height,

        margin=dict(
            l=35,
            r=45,
            t=90,
            b=45
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.48)",

        font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=13,
            color=TEXT_MAIN
        ),

        title=dict(
            font=dict(
                size=18,
                color=TEXT_DARK
            ),
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top"
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,

            font=dict(
                size=13,
                color=TEXT_DARK
            ),

            bgcolor="rgba(0,0,0,0)"
        ),

        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#cbd5e1",

            font=dict(
                color=TEXT_DARK,
                size=12
            )
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.20)",
        zeroline=False,

        title_font=dict(
            color=TEXT_MAIN,
            size=13
        ),

        tickfont=dict(
            color=TEXT_MUTED,
            size=12
        ),

        automargin=True
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.20)",
        zeroline=False,

        title_font=dict(
            color=TEXT_MAIN,
            size=13
        ),

        tickfont=dict(
            color=TEXT_MUTED,
            size=12
        ),

        automargin=True
    )

    fig.update_traces(
        selector=dict(type="bar"),

        textfont=dict(
            size=13,
            color=TEXT_DARK
        ),

        cliponaxis=False
    )

    return fig


def show_chart(fig, height=410):
    st.plotly_chart(
        style_chart(fig, height),

        use_container_width=True,

        # Disable Streamlit automatic chart theming.
        theme=None,

        config={
            "displayModeBar": False,
            "responsive": True
        }
    )


# ============================================================
# CSS — LIGHT FUTURISTIC THEME
# ============================================================

st.markdown(
    """
<style>

:root {
    --text-900: #0f172a;
    --text-700: #334155;
    --text-500: #64748b;
    --card-border: rgba(129,140,248,0.28);
}

/* GLOBAL */

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
    padding-top: 3.5rem;
    padding-bottom: 4rem;
    max-width: 1280px;
}

footer {
    visibility: hidden;
}

/* SIDEBAR */

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

/* HERO */

.hero-card {
    padding: 2.65rem 2.8rem;
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
    margin-bottom: 0.7rem;
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
    font-size: 1.2rem;
    font-weight: 850;
    color: #1e293b;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.body-text {
    color: #334155;
    font-size: 1rem;
    line-height: 1.8;
    max-width: 1060px;
}

.body-text p {
    margin: 0 0 1rem;
}

.hero-tags {
    margin-top: 1.2rem;
}

.hero-tag {
    display: inline-block;

    padding: 0.4rem 0.72rem;
    margin: 0.2rem 0.18rem 0.1rem 0;

    border-radius: 999px;

    background: rgba(255,255,255,0.75);
    border: 1px solid rgba(167,139,250,0.3);

    color: #334155;
    font-size: 0.82rem;
    font-weight: 850;
}

/* SECTION TITLES */

.section-title {
    font-size: 1.92rem;
    font-weight: 950;
    letter-spacing: -0.5px;

    color: #0f172a;

    margin-top: 2.65rem;
    margin-bottom: 0.35rem;
}

.section-subtitle {
    color: #64748b;
    font-size: 1rem;
    line-height: 1.65;
    margin-bottom: 1.3rem;
}

/* GRIDS */

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-4 {
    display: grid;
    grid-template-columns: repeat(4,minmax(0,1fr));
    gap: 1.2rem;
    align-items: stretch;
}

/* SHARED CARDS */

.metric-card,
.info-card,
.process-card,
.highlight-panel {
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
.process-card::before {
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

/* METRIC CARDS */

.metric-card {
    border-radius: 26px;
    padding: 1.4rem;

    min-height: 170px;
    height: 100%;
}

.metric-value {
    font-size: 2.05rem;
    font-weight: 950;
    line-height: 1.2;

    color: #0f172a;
    margin-bottom: 0.4rem;
}

.metric-label {
    font-size: 0.9rem;
    font-weight: 900;

    color: #4f46e5;
    margin-bottom: 0.4rem;
}

.metric-note {
    color: #64748b;
    font-size: 0.82rem;
    line-height: 1.55;
}

/* INFO CARDS */

.info-card {
    padding: 1.5rem 1.55rem;
    border-radius: 28px;

    min-height: 210px;
    height: 100%;
}

.card-label {
    display: inline-block;
    width: fit-content;

    padding: 0.32rem 0.72rem;
    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #dbeafe,
            #ede9fe,
            #ccfbf1
        );

    border: 1px solid rgba(167,139,250,0.4);

    color: #0f172a;
    font-size: 0.76rem;
    font-weight: 900;

    margin-bottom: 0.8rem;
}

.card-title {
    font-size: 1.16rem;
    font-weight: 950;
    line-height: 1.45;

    color: #0f172a;
    margin-bottom: 0.55rem;
}

.card-text {
    font-size: 0.93rem;
    line-height: 1.7;
    color: #475569;
}

/* PROCESS CARDS */

.process-card {
    padding: 1.5rem;
    border-radius: 27px;

    min-height: 210px;
    height: 100%;
}

.step-badge {
    display: inline-block;

    padding: 0.37rem 0.77rem;
    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );

    color: #ffffff;
    font-size: 0.8rem;
    font-weight: 950;

    margin-bottom: 0.9rem;
}

.process-title {
    font-size: 1.1rem;
    font-weight: 950;
    color: #0f172a;

    margin-bottom: 0.55rem;
}

.process-text {
    font-size: 0.92rem;
    line-height: 1.7;
    color: #475569;
}

/* RESULTS TABLE */

.table-wrap {
    width: 100%;
    overflow-x: auto;

    border-radius: 25px;
    border: 1px solid var(--card-border);

    background: rgba(255,255,255,0.95);

    box-shadow:
        0 18px 45px rgba(59,130,246,0.10);
}

.result-table {
    width: 100%;
    min-width: 780px;
    border-collapse: collapse;
}

.result-table th {
    padding: 0.95rem;
    text-align: left;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #06b6d4
        );

    color: #ffffff;
    font-size: 0.85rem;
    font-weight: 850;
    white-space: nowrap;
}

.result-table td {
    padding: 0.95rem;

    color: #334155;
    font-size: 0.9rem;
    line-height: 1.55;

    border-bottom:
        1px solid rgba(167,139,250,0.18);
}

.result-table tr:last-child td {
    border-bottom: none;
}

.best-row {
    background: rgba(219,234,254,0.53);
    font-weight: 850;
}

/* HIGHLIGHT */

.highlight-panel {
    padding: 1.55rem 1.7rem;
    border-radius: 28px;
    margin-top: 1.25rem;
}

.highlight-title {
    font-size: 1.17rem;
    font-weight: 950;
    color: #0f172a;

    margin-bottom: 0.55rem;
}

.highlight-text {
    color: #334155;
    font-size: 0.95rem;
    line-height: 1.77;
}

/* RESEARCH NOTES */

.research-note {
    margin-top: 1rem;
    padding: 1rem 1.15rem;

    border-left: 4px solid #6366f1;
    border-radius: 0 18px 18px 0;

    background: rgba(238,242,255,0.85);

    color: #475569;
    font-size: 0.89rem;
    line-height: 1.7;
}

/* CHARTS */

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.88);

    border: 1px solid rgba(129,140,248,0.24);
    border-radius: 24px;

    padding: 0.65rem;

    box-shadow:
        0 12px 28px rgba(59,130,246,0.06);
}

/* MOBILE */

@media (max-width: 1050px) {
    .grid-4 {
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }
}

@media (max-width: 760px) {

    .block-container {
        padding-top: 2rem;
    }

    .hero-card {
        padding: 1.8rem 1.5rem;
    }

    .page-title {
        font-size: 2.5rem;
    }

    .grid-2,
    .grid-3,
    .grid-4 {
        grid-template-columns: 1fr;
    }

    .metric-card,
    .info-card,
    .process-card {
        min-height: auto;
    }

    .section-title {
        font-size: 1.65rem;
    }
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# 1. HERO
# ============================================================

render_html(f"""
    <div class="hero-card">

        <div class="eyebrow">
            Deep Learning Project · Computer Vision
        </div>

        <div class="page-title">
            Food101 CNN
            <span class="gradient-text">
                Transfer Learning
            </span>
        </div>

        <div class="subtitle">
            ResNet50 · Image Classification ·
            Transfer Learning · Fine-Tuning
        </div>

        <div class="body-text">

            <p>
                This project investigates how
                <b>fine-tuning a pre-trained CNN</b>
                affects image-classification
                performance on Food101.
            </p>

            <p>
                I compared three ResNet50
                training configurations:
                frozen feature extraction,
                fine-tuning layer4, and
                fine-tuning both layer3 and layer4.
            </p>

            <p>
                The best configuration achieved
                <b>{BEST_ACC:.2%} test accuracy</b>,
                compared with
                <b>{FROZEN_ACC:.2%}</b>
                for the frozen baseline.
                This represents an improvement
                of <b>{GAIN_BEST_PP:.2f} percentage points</b>.
            </p>

            <p>
                The experiment demonstrates
                the value of controlled
                model comparison and adapting
                pre-trained visual representations
                to a specialised classification task.
            </p>

        </div>

        <div class="hero-tags">
            <span class="hero-tag">Food101</span>
            <span class="hero-tag">101 Classes</span>
            <span class="hero-tag">ResNet50</span>
            <span class="hero-tag">PyTorch</span>
            <span class="hero-tag">CNN</span>
            <span class="hero-tag">Transfer Learning</span>
            <span class="hero-tag">Fine-Tuning</span>
            <span class="hero-tag">Model Evaluation</span>
        </div>

    </div>
""")


# ============================================================
# 2. PROJECT SNAPSHOT
# ============================================================

section_heading(
    "Project by the Numbers",
    "The main experimental results and model comparison."
)

render_grid("grid-4", [

    metric_card(
        f"{BEST_ACC:.2%}",
        "Best Test Accuracy",
        "ResNet50 with layer3 and layer4 fine-tuned."
    ),

    metric_card(
        f"{FROZEN_ACC:.2%}",
        "Frozen Baseline",
        "Best frozen ResNet50 feature extractor."
    ),

    metric_card(
        f"+{GAIN_BEST_PP:.2f} pp",
        "Absolute Accuracy Gain",
        "Best fine-tuned model versus frozen baseline."
    ),

    metric_card(
        str(len(EXPERIMENTS)),
        "Reported Configurations",
        "Frozen, layer4, and layer3 + layer4."
    )
])


# ============================================================
# 3. DATASET OVERVIEW
# ============================================================

section_heading(
    "Food101 Dataset",
    "A public benchmark for multi-class food-image classification."
)

render_grid("grid-4", [

    metric_card(
        str(FOOD_CLASSES),
        "Food Categories",
        "Distinct food labels in the benchmark."
    ),

    metric_card(
        f"{OFFICIAL_TOTAL_IMAGES:,}",
        "Total Images",
        "Standard Food-101 dataset specification."
    ),

    metric_card(
        f"{OFFICIAL_TRAIN_IMAGES:,}",
        "Official Training Images",
        "750 training images per category."
    ),

    metric_card(
        f"{OFFICIAL_TEST_IMAGES:,}",
        "Official Test Images",
        "250 test images per category."
    )
])

note_panel("""
    <b>Dataset versus experiment:</b>
    These image counts describe the standard
    Food-101 benchmark. They do not establish
    the exact subset, validation split,
    or total number of images used in
    every training run in this project.
    The accuracy numbers on this page
    come from the reported experiments.
""")


# ============================================================
# 4. DATASET DISTRIBUTION
# ============================================================

section_heading(
    "Standard Dataset Distribution",
    "The official Food-101 training and test partitions."
)

left, right = st.columns(
    [1.15, 1],
    gap="medium"
)

with left:

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=[
                "Official training set",
                "Official test set"
            ],

            values=[
                OFFICIAL_TRAIN_IMAGES,
                OFFICIAL_TEST_IMAGES
            ],

            hole=0.62,

            marker=dict(
                colors=[BLUE, VIOLET]
            ),

            textinfo="percent",

            textfont=dict(
                size=13,
                color="#ffffff"
            ),

            hovertemplate=(
                "%{label}<br>"
                "%{value:,} images<br>"
                "%{percent}"
                "<extra></extra>"
            )
        )
    )

    fig.update_layout(
        title="Food-101 official image distribution",
        showlegend=True,

        annotations=[
            dict(
                text="101K",
                x=0.5,
                y=0.5,

                showarrow=False,

                font=dict(
                    size=25,
                    color=TEXT_DARK
                )
            )
        ]
    )

    show_chart(fig, height=390)


with right:

    render_grid("grid-2", [

        info_card(
            "Training Partition",
            "75% of images",
            """
            Standard Food-101 provides
            750 training images for
            each of its 101 categories.
            """
        ),

        info_card(
            "Test Partition",
            "25% of images",
            """
            The standard benchmark
            provides 250 test images
            per category.
            """
        )
    ])

    note_panel("""
        <b>Interpretation:</b>
        This chart visualises the public
        benchmark specification.
        It is not a training-history chart
        or a measurement of the project's
        actual computational workload.
    """)


# ============================================================
# 5. COMPUTER VISION PROBLEM
# ============================================================

section_heading(
    "Computer Vision Problem",
    "Why food classification is a useful transfer-learning task."
)

render_grid("grid-3", [

    info_card(
        "Prediction Task",
        "101-Class Image Classification",
        """
        Given an input image,
        the model predicts the
        most likely food category
        among 101 possible labels.
        """
    ),

    info_card(
        "Visual Complexity",
        "Similar Appearance Across Classes",
        """
        Food images can contain
        overlapping textures,
        ingredients, colours,
        and presentation styles.
        """
    ),

    info_card(
        "Modelling Question",
        "How Much Fine-Tuning Helps?",
        """
        The experiment tests whether
        adapting more of ResNet50's
        pre-trained feature hierarchy
        improves classification accuracy.
        """
    )
])


# ============================================================
# 6. MODELLING WORKFLOW
# ============================================================

section_heading(
    "Model Development Workflow",
    "From image preparation to controlled model comparison."
)

render_grid("grid-4", [

    process_card(
        "01",
        "Prepare Images",
        """
        Load food images and prepare
        them as appropriately resized
        and normalised tensors
        for ResNet50.
        """
    ),

    process_card(
        "02",
        "Frozen Baseline",
        """
        Keep the pre-trained ResNet50
        backbone frozen and train
        a classifier for Food101.
        """
    ),

    process_card(
        "03",
        "Fine-Tune Features",
        """
        Compare unfreezing layer4
        with unfreezing both
        layer3 and layer4.
        """
    ),

    process_card(
        "04",
        "Evaluate Accuracy",
        """
        Compare reported test
        accuracy across the
        three configurations
        and select the best result.
        """
    )
])


# ============================================================
# 7. EXPERIMENTAL RESULTS
# ============================================================

section_heading(
    "Experimental Results",
    "Actual reported test accuracies for three ResNet50 configurations."
)

result_rows = []

for experiment in EXPERIMENTS:

    accuracy = experiment["accuracy"]

    gain_pp = (
        accuracy - FROZEN_ACC
    ) * 100

    error_rate = (1 - accuracy) * 100

    result_rows.append([
        experiment["part"],
        experiment["name"],
        experiment["configuration"],
        f"{accuracy * 100:.2f}%",
        f"+{gain_pp:.2f} pp",
        f"{error_rate:.2f}%"
    ])

render_html(
    data_table(
        [
            "Experiment",
            "Model Strategy",
            "Backbone Configuration",
            "Test Accuracy",
            "Gain vs Frozen",
            "Error Rate"
        ],
        result_rows,
        best_row=2
    )
)

note_panel("""
    <b>Metric definition:</b>
    All three accuracy figures are
    reported test results from the
    Food101 project. Accuracy gain
    and error rate are calculated
    directly from those figures.
    No additional test runs
    have been invented.
""")


# ============================================================
# 8. MODEL ACCURACY CHART
# ============================================================

section_heading(
    "Visual Model Comparison",
    "Fine-tuning produced a substantial increase in test accuracy."
)

model_labels = [
    experiment["short"]
    for experiment in EXPERIMENTS
]

accuracy_values = [
    experiment["accuracy"] * 100
    for experiment in EXPERIMENTS
]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=accuracy_values,
        y=model_labels,

        orientation="h",

        marker_color=[
            "#94a3b8",
            BLUE,
            VIOLET
        ],

        text=[
            f"{value:.2f}%"
            for value in accuracy_values
        ],

        textposition="outside",

        hovertemplate=(
            "%{y}<br>"
            "Test accuracy: %{x:.2f}%"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title="ResNet50 — Reported test accuracy",
    xaxis_title="Test accuracy (%)",
    yaxis_title=None,

    xaxis_range=[0, 100],
    yaxis=dict(
        autorange="reversed"
    ),

    showlegend=False
)

show_chart(fig, height=380)


# ============================================================
# 9. ACCURACY IMPROVEMENT
# ============================================================

section_heading(
    "Accuracy Improvement Analysis",
    "Quantifying the benefit of fine-tuning more CNN layers."
)

render_grid("grid-4", [

    metric_card(
        f"+{GAIN_LAYER4_PP:.2f} pp",
        "Layer4 Gain",
        "Improvement over frozen ResNet50."
    ),

    metric_card(
        f"+{GAIN_EXTRA_PP:.2f} pp",
        "Additional Layer3 Gain",
        "Improvement beyond layer4-only fine-tuning."
    ),

    metric_card(
        f"+{GAIN_BEST_PP:.2f} pp",
        "Total Accuracy Gain",
        "Best configuration compared with frozen baseline."
    ),

    metric_card(
        f"{ERROR_REDUCTION:.1f}%",
        "Relative Error Reduction",
        "Reduction in misclassification rate from baseline."
    )
])

render_html(
    highlight_panel(
        "Main Experimental Finding",
        f"""
        The frozen ResNet50 baseline achieved
        <b>{FROZEN_ACC:.2%} test accuracy</b>.

        Fine-tuning the final residual stage
        increased accuracy to
        <b>{LAYER4_ACC:.2%}</b>,
        a gain of <b>{GAIN_LAYER4_PP:.2f}
        percentage points</b>.

        Fine-tuning both layer3 and layer4
        increased accuracy further to
        <b>{BEST_ACC:.2%}</b>.

        The total gain was
        <b>{GAIN_BEST_PP:.2f} percentage points</b>,
        equivalent to approximately
        <b>{RELATIVE_GAIN:.1f}% relative
        accuracy improvement</b>.

        The associated misclassification
        rate declined from
        <b>{FROZEN_ERROR:.2f}%</b>
        to <b>{BEST_ERROR:.2f}%</b>.
        """
    )
)


# ============================================================
# 10. EXPERIMENT INTERPRETATION
# ============================================================

section_heading(
    "What the Experiments Show",
    "Three observations supported by the reported results."
)

render_grid("grid-3", [

    info_card(
        "Finding 01",
        "Pre-Trained Features Are Transferable",
        """
        The frozen ResNet50 model
        achieved 61.86% accuracy,
        demonstrating useful
        feature transfer without
        changing the backbone.
        """
    ),

    info_card(
        "Finding 02",
        "Fine-Tuning Layer4 Gives the Largest Gain",
        f"""
        Adapting the final residual
        stage raised accuracy to 81.75%,
        a {GAIN_LAYER4_PP:.2f}-percentage-point
        improvement over the frozen baseline.
        """
    ),

    info_card(
        "Finding 03",
        "Deeper Adaptation Performed Best",
        f"""
        Unfreezing both layer3
        and layer4 reached 85.07%,
        improving on layer4-only
        fine-tuning by another
        {GAIN_EXTRA_PP:.2f} percentage points.
        """
    )
])


# ============================================================
# 11. TECHNICAL CAPABILITIES
# ============================================================

section_heading(
    "Technical Skills Demonstrated",
    "The practical machine-learning capabilities behind the experiments."
)

render_grid("grid-4", [

    info_card(
        "Deep Learning",
        "CNN Image Classification",
        """
        Worked with ResNet50
        for multi-class food
        image recognition.
        """
    ),

    info_card(
        "Transfer Learning",
        "Pre-Trained Feature Extraction",
        """
        Reused a pre-trained
        backbone and adapted
        its classifier for
        Food101.
        """
    ),

    info_card(
        "Fine-Tuning",
        "Selective Layer Unfreezing",
        """
        Compared training the
        final residual block
        with training the
        last two residual stages.
        """
    ),

    info_card(
        "Experimentation",
        "Model Comparison",
        """
        Used a frozen baseline
        and progressively more
        trainable layers to
        compare configurations.
        """
    ),

    info_card(
        "Programming",
        "Python &amp; PyTorch",
        """
        Implemented image
        preparation, model
        configuration, training,
        and evaluation workflows.
        """
    ),

    info_card(
        "Data Preparation",
        "Image Preprocessing",
        """
        Prepared image tensors
        for pre-trained CNN
        input requirements.
        """
    ),

    info_card(
        "Evaluation",
        "Test Accuracy Analysis",
        """
        Compared measured
        accuracy and calculated
        absolute and relative
        performance improvements.
        """
    ),

    info_card(
        "Communication",
        "Experimental Reporting",
        """
        Presented training
        strategies, numerical
        results, and practical
        conclusions clearly.
        """
    )
])


# ============================================================
# 12. EXPERIMENTAL LIMITATIONS
# ============================================================

section_heading(
    "Limitations",
    "What the reported evidence does and does not establish."
)

render_grid("grid-3", [

    info_card(
        "Metric Coverage",
        "Accuracy Is Not the Whole Picture",
        """
        Overall accuracy alone
        does not show which
        individual food classes
        are most frequently
        confused.
        """
    ),

    info_card(
        "Training Efficiency",
        "Cost of Additional Trainable Layers",
        """
        Fine-tuning more
        backbone layers can
        increase computational
        and memory requirements.
        The reported comparison
        does not quantify these costs.
        """
    ),

    info_card(
        "Generalisation",
        "Evaluation Beyond Food101",
        """
        These test results
        do not establish
        performance on food
        images collected
        outside the benchmark.
        """
    )
])

note_panel("""
    <b>Reporting boundary:</b>
    Per-class F1 scores, confusion matrices,
    training time, model size,
    and learning curves are not included
    because verified values were not
    supplied in the current project summary.
    These can be added when the original
    training notebooks and outputs
    are available.
""")


# ============================================================
# 13. FUTURE DEVELOPMENT
# ============================================================

section_heading(
    "Future Improvements",
    "Practical next steps for extending the computer-vision project."
)

render_grid("grid-3", [

    info_card(
        "Error Analysis",
        "Confusion Matrix &amp; Per-Class Metrics",
        """
        Examine the categories
        with the highest error
        rates and identify
        visually similar classes.
        """
    ),

    info_card(
        "Model Comparison",
        "Modern Architectures",
        """
        Compare ResNet50
        against EfficientNet,
        ConvNeXt, or
        Vision Transformers.
        """
    ),

    info_card(
        "Explainability",
        "Grad-CAM Visualisations",
        """
        Explore which image
        regions influence
        the classifier's
        final predictions.
        """
    ),

    info_card(
        "Deployment",
        "Interactive Streamlit Classifier",
        """
        Develop a separate
        inference demo that
        accepts food images
        and returns predicted
        categories.
        """
    ),

    info_card(
        "Model Optimisation",
        "Training Efficiency",
        """
        Measure GPU time,
        fine-tuning cost,
        inference latency,
        and memory usage.
        """
    ),

    info_card(
        "Robustness",
        "External Image Evaluation",
        """
        Test against images
        with different lighting,
        backgrounds, angles,
        and food presentation.
        """
    )
])


# ============================================================
# 14. FINAL PROJECT TAKEAWAY
# ============================================================

section_heading(
    "Project Takeaway",
    "A measured demonstration of adapting pre-trained models."
)

render_html(
    highlight_panel(
        "From Frozen Features to Fine-Tuned Representation",
        f"""
        This project demonstrates that
        a pre-trained ResNet50 backbone
        can be adapted progressively
        to a specialised image
        classification problem.

        Across the three reported
        configurations, test accuracy
        increased from
        <b>{FROZEN_ACC:.2%}</b>
        to <b>{BEST_ACC:.2%}</b>.

        The strongest result came from
        fine-tuning <b>layer3 and layer4</b>,
        improving classification accuracy
        by <b>{GAIN_BEST_PP:.2f}
        percentage points</b>
        relative to frozen features.

        The main skill demonstrated is
        <b>evidence-based transfer learning:
        establishing a baseline,
        modifying the training strategy,
        and evaluating whether
        the change improves performance.</b>
        """
    )
)


# ============================================================
# 15. NAVIGATION
# ============================================================

st.write("")

st.page_link(
    "Home.py",
    label="← Back to Portfolio Home"
)
