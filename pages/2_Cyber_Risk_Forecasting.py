
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from textwrap import dedent
from html import escape

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cyber Risk Research | Thomas Nguyen",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_DOI = "https://dx.doi.org/10.21227/8drm-jz27"

# ============================================================
# COLOUR PALETTE
# ============================================================

BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#0891b2"
INDIGO = "#4f46e5"

TEXT_DARK = "#0f172a"
TEXT_MAIN = "#334155"
TEXT_MUTED = "#475569"
GRID_COLOR = "rgba(148,163,184,0.22)"


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


# ============================================================
# CARD COMPONENTS
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


def process_card(step, title, text):
    return compact_html(f"""
        <div class="process-card">
            <div class="step-badge">{step}</div>
            <div class="process-title">{title}</div>
            <div class="process-text">{text}</div>
        </div>
    """)


def publication_card(phase, status, title, description, outcome):
    return compact_html(f"""
        <div class="publication-card">
            <div class="publication-topline">
                <span class="card-label">{phase}</span>
                <span class="publication-status">{status}</span>
            </div>
            <div class="publication-title">{title}</div>
            <div class="publication-description">{description}</div>
            <div class="publication-outcome">{outcome}</div>
        </div>
    """)


def highlight_panel(title, text):
    return compact_html(f"""
        <div class="highlight-panel">
            <div class="highlight-title">{title}</div>
            <div class="highlight-text">{text}</div>
        </div>
    """)


def data_table(headers, rows, highlight_rows=None):

    if highlight_rows is None:
        highlight_rows = []

    header_html = "".join(
        f"<th>{escape(str(header))}</th>"
        for header in headers
    )

    body = ""

    for index, row in enumerate(rows):

        row_class = (
            ' class="best-row"'
            if index in highlight_rows
            else ""
        )

        cells = "".join(
            f"<td>{escape(str(value))}</td>"
            for value in row
        )

        body += f"<tr{row_class}>{cells}</tr>"

    return compact_html(f"""
        <div class="table-wrap">
            <table class="result-table">
                <thead>
                    <tr>{header_html}</tr>
                </thead>
                <tbody>{body}</tbody>
            </table>
        </div>
    """)


def research_note(text):
    render_html(f"""
        <div class="research-note">{text}</div>
    """)


def source_note(text):
    render_html(f"""
        <div class="source-note">{text}</div>
    """)


# ============================================================
# PLOTLY CHART STYLING — FIXES ALL LIGHT TEXT
# ============================================================

def style_chart(fig, height=390):
    """
    Central Plotly styling.

    Forces dark typography for:
    - Chart titles
    - Axis titles
    - Tick values
    - Category names
    - Legends
    - Bar data labels
    - Scatter text
    - Annotations
    - Hover labels

    This is applied to every chart through show_chart().
    """

    fig.update_layout(
        template="plotly_white",
        height=height,

        margin=dict(
            l=30,
            r=40,
            t=105,
            b=50
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.45)",

        font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=13,
            color=TEXT_MAIN
        ),

        title=dict(
            font=dict(
                family="Inter, Segoe UI, Arial, sans-serif",
                size=18,
                color=TEXT_DARK
            ),
            x=0.02,
            xanchor="left",
            y=0.985,
            yanchor="top"
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,

            font=dict(
                family="Inter, Segoe UI, Arial, sans-serif",
                size=13,
                color=TEXT_DARK
            ),

            bgcolor="rgba(0,0,0,0)",
            borderwidth=0
        ),

        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#cbd5e1",

            font=dict(
                family="Inter, Segoe UI, Arial, sans-serif",
                size=12,
                color=TEXT_DARK
            )
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor=GRID_COLOR,
        zeroline=False,
        linecolor="#cbd5e1",

        title_font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=13,
            color=TEXT_MAIN
        ),

        tickfont=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=12,
            color=TEXT_MUTED
        ),

        automargin=True,
        ticks=""
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID_COLOR,
        zeroline=False,
        linecolor="#cbd5e1",

        title_font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=13,
            color=TEXT_MAIN
        ),

        tickfont=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=12,
            color=TEXT_MUTED
        ),

        automargin=True,
        ticks=""
    )

    fig.update_traces(
        selector=dict(type="bar"),
        textfont=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=12,
            color=TEXT_DARK
        ),
        cliponaxis=False
    )

    fig.update_traces(
        selector=dict(type="scatter"),
        textfont=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=12,
            color=TEXT_DARK
        )
    )

    fig.update_annotations(
        font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=12,
            color=TEXT_DARK
        )
    )

    return fig


def show_chart(fig, height=390):

    styled_fig = style_chart(fig, height=height)

    st.plotly_chart(
        styled_fig,
        use_container_width=True,

        # Critical: prevent Streamlit from overriding colours
        theme=None,

        config={
            "displayModeBar": False,
            "responsive": True
        }
    )



# ============================================================
# CSS — CONSISTENT LIGHT FUTURISTIC DESIGN
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
        radial-gradient(circle at 8% 8%,
            rgba(79,70,229,0.18), transparent 28%),
        radial-gradient(circle at 90% 10%,
            rgba(6,182,212,0.22), transparent 26%),
        radial-gradient(circle at 50% 92%,
            rgba(37,99,235,0.14), transparent 34%),
        linear-gradient(
            135deg,
            #edf4ff 0%,
            #f7f1ff 46%,
            #e9feff 100%
        );
}

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
        radial-gradient(circle at top left,
            rgba(37,99,235,0.35), transparent 30%),
        radial-gradient(circle at bottom right,
            rgba(124,58,237,0.25), transparent 34%),
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
    padding: 2.7rem 2.8rem;
    border-radius: 36px;

    background:
        radial-gradient(circle at 10% 0%,
            rgba(37,99,235,0.22), transparent 28%),
        radial-gradient(circle at 100% 0%,
            rgba(6,182,212,0.20), transparent 24%),
        radial-gradient(circle at 85% 80%,
            rgba(124,58,237,0.16), transparent 30%),
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
    padding: 0.46rem 0.9rem;
    border-radius: 999px;

    background:
        linear-gradient(90deg,
            #dbeafe, #ede9fe, #ccfbf1);

    border: 1px solid rgba(37,99,235,0.28);
    color: #0f172a;

    font-size: 0.84rem;
    font-weight: 850;
    margin-bottom: 1rem;
}

.page-title {
    font-size: 3.5rem;
    font-weight: 950;
    letter-spacing: -1.8px;
    line-height: 1.1;
    color: #0f172a;
    margin-bottom: 0.7rem;
}

.gradient-text {
    background:
        linear-gradient(90deg,
            #2563eb, #7c3aed, #06b6d4);

    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 1.18rem;
    font-weight: 850;
    color: #1e293b;
    line-height: 1.5;
    margin-bottom: 1.2rem;
}

.body-text {
    font-size: 1rem;
    color: #334155;
    line-height: 1.82;
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
    margin: 0.22rem 0.18rem 0.1rem;

    border-radius: 999px;
    background: rgba(255,255,255,0.75);
    border: 1px solid rgba(167,139,250,0.3);

    color: #334155;
    font-size: 0.82rem;
    font-weight: 850;
}

/* ========================================================
   SECTIONS
======================================================== */

.section-title {
    font-size: 1.92rem;
    font-weight: 950;
    letter-spacing: -0.5px;
    color: #0f172a;

    margin-top: 2.75rem;
    margin-bottom: 0.35rem;
}

.section-subtitle {
    font-size: 1rem;
    color: #64748b;
    line-height: 1.65;
    margin-bottom: 1.3rem;
}

/* ========================================================
   GRIDS
======================================================== */

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0,1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0,1fr));
    gap: 1.25rem;
    align-items: stretch;
}

.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, minmax(0,1fr));
    gap: 1.2rem;
    align-items: stretch;
}

/* ========================================================
   SHARED CARDS
======================================================== */

.metric-card,
.info-card,
.process-card,
.publication-card,
.highlight-panel {
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at top right,
            rgba(124,58,237,0.07), transparent 30%),
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
.process-card::before,
.publication-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 6px;

    background:
        linear-gradient(90deg,
            #2563eb, #7c3aed, #06b6d4);
}

/* ========================================================
   METRIC CARDS
======================================================== */

.metric-card {
    padding: 1.35rem;
    border-radius: 26px;
    min-height: 162px;
    height: 100%;
}

.metric-value {
    color: #0f172a;
    font-size: 1.92rem;
    font-weight: 950;
    line-height: 1.2;
    margin-bottom: 0.45rem;
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

/* ========================================================
   LABELS
======================================================== */

.card-label {
    display: inline-block;
    width: fit-content;
    padding: 0.32rem 0.72rem;
    border-radius: 999px;

    background:
        linear-gradient(90deg,
            #dbeafe, #ede9fe, #ccfbf1);

    border: 1px solid rgba(167,139,250,0.42);
    color: #0f172a;

    font-size: 0.76rem;
    font-weight: 900;
    margin-bottom: 0.8rem;
}

/* ========================================================
   INFORMATION CARDS
======================================================== */

.info-card {
    padding: 1.5rem 1.55rem;
    border-radius: 28px;
    min-height: 232px;
    height: 100%;
}

.card-title {
    color: #0f172a;
    font-size: 1.15rem;
    font-weight: 950;
    line-height: 1.45;
    margin-bottom: 0.55rem;
}

.card-text {
    color: #475569;
    font-size: 0.94rem;
    line-height: 1.72;
}

/* ========================================================
   PROCESS CARDS
======================================================== */

.process-card {
    padding: 1.5rem;
    border-radius: 27px;
    min-height: 245px;
    height: 100%;
}

.step-badge {
    display: inline-block;
    padding: 0.36rem 0.78rem;
    border-radius: 999px;

    background:
        linear-gradient(90deg,
            #2563eb, #7c3aed, #06b6d4);

    color: #ffffff;
    font-size: 0.8rem;
    font-weight: 950;
    margin-bottom: 0.9rem;
}

.process-title {
    color: #0f172a;
    font-size: 1.1rem;
    font-weight: 950;
    margin-bottom: 0.55rem;
}

.process-text {
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.7;
}

/* ========================================================
   PUBLICATION CARDS
======================================================== */

.publication-card {
    padding: 1.65rem;
    border-radius: 30px;
    min-height: 360px;
    height: 100%;

    display: flex;
    flex-direction: column;
}

.publication-topline {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 0.85rem;
}

.publication-topline .card-label {
    margin-bottom: 0;
}

.publication-status {
    padding: 0.32rem 0.7rem;
    border-radius: 999px;
    background: #dcfce7;
    border: 1px solid #86efac;

    color: #166534;
    font-size: 0.75rem;
    font-weight: 900;
}

.publication-title {
    color: #0f172a;
    font-size: 1.18rem;
    font-weight: 950;
    line-height: 1.45;
    margin-bottom: 0.8rem;
}

.publication-description {
    color: #475569;
    font-size: 0.94rem;
    line-height: 1.72;
    margin-bottom: 1rem;
}

.publication-outcome {
    margin-top: auto;
    padding: 0.95rem 1rem;
    border-radius: 18px;

    background:
        linear-gradient(
            90deg,
            rgba(219,234,254,0.84),
            rgba(237,233,254,0.78)
        );

    border: 1px solid rgba(167,139,250,0.25);
    color: #334155;
    font-size: 0.87rem;
    line-height: 1.65;
}

/* ========================================================
   TABLES
======================================================== */

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
    min-width: 850px;
    border-collapse: collapse;
}

.result-table th {
    padding: 0.95rem 0.8rem;
    text-align: left;

    background:
        linear-gradient(90deg,
            #2563eb, #7c3aed, #06b6d4);

    color: white;
    font-size: 0.83rem;
    font-weight: 850;
    white-space: nowrap;
}

.result-table td {
    padding: 0.88rem 0.8rem;
    color: #334155;
    font-size: 0.87rem;
    line-height: 1.5;

    border-bottom:
        1px solid rgba(167,139,250,0.16);
}

.result-table tr:last-child td {
    border-bottom: none;
}

.result-table tbody tr:hover {
    background: rgba(238,242,255,0.55);
}

.best-row {
    background: rgba(219,234,254,0.52);
    font-weight: 850;
}

/* ========================================================
   HIGHLIGHT PANELS
======================================================== */

.highlight-panel {
    padding: 1.5rem 1.7rem;
    border-radius: 27px;
    margin-top: 1.25rem;
}

.highlight-title {
    color: #0f172a;
    font-size: 1.15rem;
    font-weight: 950;
    margin-bottom: 0.55rem;
}

.highlight-text {
    color: #334155;
    font-size: 0.95rem;
    line-height: 1.78;
}

/* ========================================================
   NOTES
======================================================== */

.research-note {
    margin-top: 1rem;
    padding: 1rem 1.2rem;
    border-left: 4px solid #6366f1;
    border-radius: 0 18px 18px 0;

    background: rgba(238,242,255,0.85);
    color: #475569;

    font-size: 0.89rem;
    line-height: 1.7;
}

.source-note {
    color: #64748b;
    font-size: 0.82rem;
    line-height: 1.55;
    margin-top: 0.55rem;
}

/* ========================================================
   PLOTLY CONTAINERS
======================================================== */

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.86);
    border: 1px solid rgba(129,140,248,0.22);
    border-radius: 23px;
    padding: 0.65rem;

    box-shadow:
        0 12px 28px rgba(59,130,246,0.06);
}

/* ========================================================
   BUTTONS
======================================================== */

div.stLinkButton > a {
    border-radius: 999px !important;
    font-weight: 850 !important;

    border:
        1px solid rgba(37,99,235,0.35) !important;

    background: rgba(255,255,255,0.85) !important;
    color: #0f172a !important;
}

div.stLinkButton > a * {
    color: #0f172a !important;
}

/* ========================================================
   MOBILE
======================================================== */

@media (max-width: 1050px) {
    .grid-4 {
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }
}

@media (max-width: 760px) {

    .block-container {
        padding-top: 4.5rem;
    }

    .hero-card {
        padding: 1.8rem 1.5rem;
    }

    .page-title {
        font-size: 2.45rem;
    }

    .grid-2,
    .grid-3,
    .grid-4 {
        grid-template-columns: 1fr;
    }

    .metric-card,
    .info-card,
    .process-card,
    .publication-card {
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
# FINAL MANUSCRIPT RESULTS — SOURCE-ALIGNED
# ============================================================

# Conference manuscript, Section 5 / Table 1 (14-page AusDM PDF).
# The main task is top-risk entity over the next FIVE simulator units.
CONFERENCE_RESULTS = [
    {"Model": "Poisson baseline", "Accuracy": 0.3873, "Macro-F1": 0.2290, "Weighted-F1": 0.3470, "Top-2": None, "Top-3": None, "Severity": 0.3307, "Time": 0.2553},
    {"Model": "Hawkes-informed supervised GRU", "Accuracy": 0.8621, "Macro-F1": 0.8565, "Weighted-F1": 0.8625, "Top-2": 0.9598, "Top-3": 0.9893, "Severity": 0.3414, "Time": 0.3956},
    {"Model": "Likelihood-based Neural Hawkes-style", "Accuracy": 0.2753, "Macro-F1": 0.0987, "Weighted-F1": 0.1426, "Top-2": 0.4773, "Top-3": 0.6667, "Severity": 0.3327, "Time": 0.3520},
    {"Model": "Transformer Hawkes Process", "Accuracy": 0.9023, "Macro-F1": 0.8951, "Weighted-F1": 0.9024, "Top-2": 0.9839, "Top-3": 0.9940, "Severity": 0.3400, "Time": 0.3809},
    {"Model": "MCP-Titan retrieval", "Accuracy": 0.2567, "Macro-F1": 0.2206, "Weighted-F1": 0.2491, "Top-2": 0.4873, "Top-3": 0.6400, "Severity": 0.3560, "Time": 0.3700},
]

# Revised Risks manuscript, Section 5.1 / Table 1.
# This is a NEW chronological, boundary-purged evaluation, not a
# second estimate of the AusDM random-split experimental design.
JOURNAL_CLASSIFICATION = [
    {"Model": "Poisson baseline", "Accuracy": 0.3940, "Macro-F1": 0.1332, "Weighted-F1": 0.3176, "Top-2": 0.5160, "Top-3": 0.6967},
    {"Model": "Hawkes-informed supervised GRU", "Accuracy": 0.3207, "Macro-F1": 0.1975, "Weighted-F1": 0.3384, "Top-2": 0.4867, "Top-3": 0.6453},
    {"Model": "Likelihood-based Neural Hawkes", "Accuracy": 0.4540, "Macro-F1": 0.1293, "Weighted-F1": 0.3100, "Top-2": 0.5653, "Top-3": 0.6200},
    {"Model": "Transformer Hawkes Process", "Accuracy": 0.2473, "Macro-F1": 0.1255, "Weighted-F1": 0.2609, "Top-2": 0.4767, "Top-3": 0.6107},
    {"Model": "MCP-Titan-style retrieval", "Accuracy": 0.0980, "Macro-F1": 0.0298, "Weighted-F1": 0.0175, "Top-2": 0.1120, "Top-3": 0.5807},
]

# Revised Risks manuscript, Section 5.2 / Table 2.
FREQUENCY_RESULTS = [
    {"Model": "Training Mean", "Validation MAE": 10.3629, "Test MAE": 13.3518},
    {"Model": "Persistence", "Validation MAE": 8.5251, "Test MAE": 8.5654},
    {"Model": "Rolling Mean (m=8)", "Validation MAE": 6.8173, "Test MAE": 6.9875},
    {"Model": "Fitted classical Hawkes", "Validation MAE": 6.7673, "Test MAE": 7.2542},
    {"Model": "Poisson regression", "Validation MAE": 8.0451, "Test MAE": 8.5109},
    {"Model": "Negative Binomial regression", "Validation MAE": 8.0790, "Test MAE": 8.5257},
    {"Model": "GRU-NB", "Validation MAE": 6.5815, "Test MAE": 7.4234},
    {"Model": "LSTM-NB", "Validation MAE": 6.6981, "Test MAE": 7.6139},
    {"Model": "THP-Poisson", "Validation MAE": 7.1353, "Test MAE": 7.3357},
    {"Model": "THP-NB", "Validation MAE": 7.3153, "Test MAE": 7.0519},
]

# Revised Risks manuscript, Section 5.2.3 / Table 3.
JOINT_TRAJECTORIES = [
    {"Model": "Training Mean", "J1 MAE": 7.1507, "J2 MAE": 10.9547},
    {"Model": "Persistence", "J1 MAE": 8.1065, "J2 MAE": 7.4163},
    {"Model": "Rolling Mean", "J1 MAE": 5.9829, "J2 MAE": 7.3394},
    {"Model": "Poisson regression", "J1 MAE": 7.3088, "J2 MAE": 7.2629},
    {"Model": "Negative Binomial regression", "J1 MAE": 7.3249, "J2 MAE": 7.2486},
    {"Model": "GRU-NB", "J1 MAE": 6.8172, "J2 MAE": 6.7321},
]

# Revised Risks manuscript, Section 5.3 / Table 4.
SEVERITY_RESULTS = [
    {"Specification": "Full lognormal", "VaR99_USD": 1902438, "TVaR99_USD": 2991261, "P10M": 6.90e-5, "P100M": 2.14e-9, "Variance": "Finite"},
    {"Specification": "Spliced GPD ξ=0.25", "VaR99_USD": 1916074, "TVaR99_USD": 2958632, "P10M": 6.06e-5, "P100M": 9.12e-9, "Variance": "Finite"},
    {"Specification": "Spliced GPD ξ=0.50", "VaR99_USD": 1737200, "TVaR99_USD": 3211599, "P10M": 2.29e-4, "P100M": 2.19e-6, "Variance": "Infinite"},
    {"Specification": "Spliced GPD ξ=0.75", "VaR99_USD": 1449305, "TVaR99_USD": 3534421, "P10M": 3.17e-4, "P100M": 1.34e-5, "Variance": "Infinite"},
]

# Revised Risks manuscript, Section 5.4.1 / Table 5.
# Values are manuscript-reported rounded summaries, not recomputed estimates.
THINNING_RESULTS = [
    {"q": 1.0, "Retained": 47.4318, "P_positive": 0.99999996, "ExpectedLoss": 12521984},
    {"q": 0.1, "Retained": 4.7432, "P_positive": 0.978037, "ExpectedLoss": 1252198},
    {"q": 0.01, "Retained": 0.4743, "P_positive": 0.370143, "ExpectedLoss": 125220},
    {"q": 0.001, "Retained": 0.04743, "P_positive": 0.046206, "ExpectedLoss": 12522},
    {"q": 0.0001, "Retained": 0.004743, "P_positive": 0.004731, "ExpectedLoss": 1252},
]

# Revised Risks manuscript, Section 5.4.2; all at q=0.01.
EXPECTED_LOSS_Q001 = [
    {"Model": "Training Mean", "USD": 99881},
    {"Model": "Persistence", "USD": 135346},
    {"Model": "Rolling Mean", "USD": 128420},
    {"Model": "Fitted classical Hawkes", "USD": 123077},
    {"Model": "Poisson regression", "USD": 122203},
    {"Model": "Negative Binomial regression", "USD": 122599},
    {"Model": "GRU-NB", "USD": 125220},
    {"Model": "LSTM-NB", "USD": 124620},
    {"Model": "THP-Poisson", "USD": 127452},
    {"Model": "THP-NB", "USD": 131853},
]

# Revised Risks manuscript, Section 5.4.3 / Table 6.
COMPOUND_LOSS = [
    {"Model": "Poisson regression", "Expected loss (USD k)": 122.203, "VaR99 (USD M)": 1.495, "TVaR99 (USD M)": 2.370, "P(L>=10M)": 2.60e-5},
    {"Model": "Negative Binomial regression", "Expected loss (USD k)": 122.599, "VaR99 (USD M)": 1.497, "TVaR99 (USD M)": 2.374, "P(L>=10M)": 3.10e-5},
    {"Model": "GRU-NB", "Expected loss (USD k)": 125.220, "VaR99 (USD M)": 1.526, "TVaR99 (USD M)": 2.419, "P(L>=10M)": 3.07e-5},
    {"Model": "LSTM-NB", "Expected loss (USD k)": 124.620, "VaR99 (USD M)": 1.522, "TVaR99 (USD M)": 2.412, "P(L>=10M)": 2.87e-5},
    {"Model": "THP-Poisson", "Expected loss (USD k)": 127.452, "VaR99 (USD M)": 1.528, "TVaR99 (USD M)": 2.425, "P(L>=10M)": 3.33e-5},
    {"Model": "THP-NB", "Expected loss (USD k)": 131.853, "VaR99 (USD M)": 1.573, "TVaR99 (USD M)": 2.478, "P(L>=10M)": 3.93e-5},
]

# Revised Risks manuscript, Section 5.5 / Table 7.
URLHAUS_RESULTS = [
    {"Model": "Training Mean", "MAE": 254.620, "RMSE": 281.337, "NMAE": 0.5491, "NRMSE": 0.6067, "Pearson": None},
    {"Model": "Poisson regression", "MAE": 260.939, "RMSE": 303.843, "NMAE": 0.5627, "NRMSE": 0.6553, "Pearson": -0.2383},
    {"Model": "Persistence", "MAE": 283.606, "RMSE": 630.167, "NMAE": 0.6116, "NRMSE": 1.3590, "Pearson": -0.0295},
    {"Model": "Negative Binomial regression", "MAE": 287.973, "RMSE": 343.009, "NMAE": 0.6210, "NRMSE": 0.7397, "Pearson": -0.0795},
    {"Model": "THP count model", "MAE": 416.519, "RMSE": 434.606, "NMAE": 0.8982, "NRMSE": 0.9373, "Pearson": -0.0865},
]


# ============================================================
# ADDITIONAL STYLES FOR REVISED RESEARCH PRESENTATION
# ============================================================

st.markdown("""
<style>
.block-container { padding-top: 5.5rem !important; }
@media(max-width:760px){.block-container{padding-top:4.5rem !important;}}
.research-note, .source-note {line-height:1.75;}
[data-testid="stTabs"] button[data-baseweb="tab"] {
    color:#475569 !important; font-weight:800 !important;
}
[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    color:#4338ca !important;
}
[data-testid="stDataFrame"] {
    border:1px solid rgba(129,140,248,.25);
    border-radius:16px; overflow:hidden;
}
.block-container [data-testid="stMarkdownContainer"] > p {color:#334155;}
.block-container [data-testid="stWidgetLabel"] p {color:#334155 !important;}
</style>
""", unsafe_allow_html=True)


def frame(rows, columns=None):
    df = pd.DataFrame(rows)
    if columns is not None:
        df = df[columns]
    return df


def table(rows, columns=None, formats=None):
    df = frame(rows, columns)
    if formats:
        display = df.copy()
        for column, function in formats.items():
            display[column] = display[column].map(function)
        st.dataframe(display, use_container_width=True, hide_index=True)
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)


def caption(text):
    research_note(text)


def bar_chart(names, values, title, unit="", horizontal=True, highlight=None, height=400):
    colors = [VIOLET if name == highlight else BLUE for name in names]
    if horizontal:
        fig = go.Figure(go.Bar(
            x=values, y=names, orientation="h", marker_color=colors,
            hovertemplate=f"%{{y}}<br>%{{x:,.4f}} {unit}<extra></extra>",
        ))
        fig.update_layout(title=title, xaxis_title=unit or None, yaxis_title=None,
                          yaxis=dict(autorange="reversed"))
    else:
        fig = go.Figure(go.Bar(x=names, y=values, marker_color=colors))
        fig.update_layout(title=title, yaxis_title=unit or None)
    show_chart(fig, height=height)


def kpi(cards):
    render_grid("grid-4", [metric_card(*card) for card in cards])


# ============================================================
# HERO & RESEARCH SUMMARY
# ============================================================

render_html("""
<div class="hero-card">
    <div class="eyebrow">Two connected research studies · AusDM 2026 · MDPI Risks · Accepted</div>
    <div class="page-title">Cyber Risk <span class="gradient-text">Modelling &amp; Forecasting</span></div>
    <div class="subtitle">From top-risk entity prediction to event frequency, monetary severity and conditional aggregate loss</div>
    <div class="body-text">
        <p>My cyber-risk research investigates <b>temporal clustering, self-excitation and cross-entity dependence</b> using Hawkes processes, neural sequence models and statistical benchmarks. The project has produced two accepted research papers: an <b>AusDM 2026 conference study</b> and a <b>journal paper accepted by MDPI <i>Risks</i></b>.</p>
        <p><b>Phase 1</b> examines which of six cyber entities is likely to accumulate the most activity over a future five-unit risk window. Under the conference protocol, the Transformer Hawkes Process (THP) achieved <b>90.23% top-risk entity accuracy</b> on the controlled synthetic benchmark.</p>
        <p><b>Phase 2</b> extends the work to task-aware chronological re-evaluation, system-wide frequency forecasting, separately calibrated monetary severity, conditional aggregate loss and URLhaus external testing. Its results also reveal the limits of relying on complex models without strong baselines and robust validation.</p>
        <p>All reported scores belong to <b>their own data, target and evaluation protocol</b>; neither conference classification performance nor synthetic financial scenarios should be presented as real-world insurance prediction performance.</p>
    </div>
    <div class="hero-tags">
        <span class="hero-tag">Hawkes Processes</span><span class="hero-tag">Temporal Prediction</span>
        <span class="hero-tag">Transformer &amp; GRU</span><span class="hero-tag">Chronological Validation</span>
        <span class="hero-tag">Frequency–Severity Risk</span><span class="hero-tag">URLhaus External Evaluation</span>
    </div>
</div>
""")

section_heading(
    "Research at a Glance",
    "Figures below come from different tasks and must not be compared as if they share a common test protocol.",
)

kpi([
    ("90.23%", "AusDM top-risk accuracy", "THP · conference benchmark · h = 5"),
    ("45.40%", "Journal re-evaluation", "Best fitted-model accuracy; majority reference = 46.87%"),
    ("6.9875", "Frequency test MAE", "Rolling Mean · primary synthetic trajectory"),
    ("USD 125,220", "Conditional expected loss", "GRU-NB · q = 0.01 · one dimensionless window"),
])

caption("<b>Publication status:</b> Both Phase 1 (AusDM 2026) and Phase 2 (MDPI <i>Risks</i>) are reported as <b>accepted</b>. Numerical results for Phase 2 come from the supplied 13 November 2026 revised manuscript. Neither work is labelled published without a confirmed publication record.")


# ============================================================
# TABBED RESEARCH EXPLORER
# ============================================================

tab_overview, tab_conference, tab_recheck, tab_frequency, tab_financial, tab_external = st.tabs([
    "🧭 Overview",
    "🏆 Conference study",
    "🔎 Journal re-evaluation",
    "📈 Frequency forecasts",
    "💰 Financial scenarios",
    "🌐 URLhaus & limitations",
])


with tab_overview:
    section_heading("One benchmark, distinct research questions", "A research programme connecting predictive targets without treating them as interchangeable.")
    section_heading(
        "Research Problem",
        "Why cyber risk needs temporal, network-aware and financially qualified models.",
    )
    render_grid("grid-3", [
        info_card(
            "Temporal dependence", "Incidents do not always arrive independently",
            "Cyber events can cluster and follow self-exciting patterns. Event order, timing and earlier activity can inform short-horizon prediction."
        ),
        info_card(
            "Interconnected exposure", "Risk is shared between entities",
            "Related systems can experience directional spillovers and delayed contagion. The six-entity Hawkes benchmark represents these stylised interactions."
        ),
        info_card(
            "Monetary consequences", "Technical events are not insurance claims",
            "A count of synthetic events cannot directly be converted into financial losses. The journal paper introduces explicit event-to-loss assumptions and independent severity calibration."
        ),
    ])

    section_heading(
        "Research Framework",
        "The original end-to-end workflow, now aligned with the latest two manuscripts.",
    )
    render_grid("grid-4", [
        process_card(
            "01", "Hawkes event benchmark",
            "Simulate clustered activity across six entities with variable background intensity, directional excitation, propagation delays and synthetic marks."
        ),
        process_card(
            "02", "Phase 1 · entity ranking",
            "Compare five model families on the five-unit top-risk entity classification task under the AusDM conference protocol."
        ),
        process_card(
            "03", "Phase 2 · frequency",
            "Evaluate ten families for three-unit system-wide event counts, with chronological splits, baselines and trajectory robustness."
        ),
        process_card(
            "04", "Financial and external risk",
            "Combine count forecasts with monetary severity and event-to-loss sensitivity; separately test forecast transfer using URLhaus data."
        ),
    ])
    caption("<b>Research design:</b> Synthetic marks influence the Hawkes excitation process and do not represent monetary loss. Phase 1 classification and Phase 2 event-count forecasting are distinct targets with horizons of five and three dimensionless time units, respectively.")

    section_heading("Why the two classification numbers differ", "These are separate experiments—not a before-and-after improvement or evidence that a model deteriorated only because of a different split.")
    render_grid("grid-2", [
        info_card("Conference · AusDM 2026", "Top-risk prediction: 90.23%", "The conference THP experiment uses a stratified random train/validation/test design, a five-unit risk window and its own dataset/preprocessing/model configuration. The primary conference THP test accuracy is 0.9023."),
        info_card("Journal · revised Risks manuscript", "Chronological re-evaluation: 45.40%", "The journal uses chronological, boundary-purged classification evaluation. Neural Hawkes has the highest fitted-model accuracy (0.4540), below the majority-class reference (0.4687). Class imbalance and other metrics qualify the result."),
    ])
    caption("<b>Interpretation:</b> The journal explicitly states that differences include the data, horizons, preprocessing, model configurations and evaluation protocol. Do not attribute the entire gap to random versus chronological splitting alone.")

    section_heading("Synthetic benchmark specification", "Both studies involve six interdependent entities, but the journal documents a corrected jump-aware simulator and additional checks.")
    kpi([
        ("6", "Interacting entities", "Directional self- and cross-excitation with propagation lags"),
        ("10,000", "Simulated events", "Primary synthetic trajectory"),
        ("0.92125", "Kernel mass", "Integral of the two-component excitation kernel"),
        ("≈0.3425", "Reference spectral radius", "Subcriticality diagnostic under the journal approximation"),
    ])
    render_grid("grid-3", [
        info_card("Event record", "Multivariate marked point process", "Events retain entity identity, occurrence time and mark; a six-entity system supports interdependence and future-window targets."),
        info_card("Simulation correction", "Jump-aware thinning and five seeds", "The journal validates the corrected simulator's local proposal bound, event ordering, marks and stability across five independently generated event streams."),
        info_card("Scientific limitation", "Controlled data, not observed claims", "Simulator time is dimensionless, synthetic marks are non-monetary, and matching a Hawkes data generator may favour Hawkes-aligned learners."),
    ])
    caption("<b>Horizon:</b> The conference classification target uses h = 5, whereas the journal frequency target uses h = 3. Synthetic simulator time units are not real hours, days or annual insurance exposure.")


with tab_conference:
    section_heading("AusDM 2026 · Conference Results", "A Hawkes–Transformer Model for Cyber Risk Prediction: Comparative Evaluation on a Synthetic Hawkes Benchmark")
    kpi([
        ("0.9023", "THP accuracy", "Highest reported primary-task accuracy"),
        ("0.8951", "THP macro-F1", "Best class-balanced F1 in this comparison"),
        ("0.9839", "THP top-2", "True entity included in two highest-ranked predictions"),
        ("0.9940", "THP top-3", "Primary future-window ranking metric"),
    ])
    st.markdown("**Table 1 — Primary top-risk entity comparison**")
    conference_display = frame(CONFERENCE_RESULTS, ["Model", "Accuracy", "Macro-F1", "Weighted-F1", "Top-2", "Top-3"])
    st.dataframe(conference_display, hide_index=True, use_container_width=True,
                 column_config={"Accuracy": st.column_config.NumberColumn(format="%.4f"),
                                "Macro-F1": st.column_config.NumberColumn(format="%.4f"),
                                "Weighted-F1": st.column_config.NumberColumn(format="%.4f"),
                                "Top-2": st.column_config.NumberColumn(format="%.4f"),
                                "Top-3": st.column_config.NumberColumn(format="%.4f")})

    names = [r["Model"] for r in CONFERENCE_RESULTS]
    vals = [r["Accuracy"] * 100 for r in CONFERENCE_RESULTS]
    bar_chart(names, vals, "Conference primary-task accuracy", "Accuracy (%)", highlight="Transformer Hawkes Process", height=450)

    render_grid("grid-2", [
        info_card("Model design", "Transformer Hawkes Process (THP)", "An established attention-based temporal point-process formulation adapted and evaluated in a cyber-risk setting. This study does not claim to invent the THP architecture."),
        info_card("Evaluation protocol", "Future-window risk classification", "10,000 synthetic events; horizon h = 5; sequence history length 50. THP and supervised GRU use stratified random partitions, rather than the later journal's common chronological protocol."),
    ])
    caption("<b>Source:</b> Final AusDM 2026 manuscript, Section 5, Table 1. Severity/time accuracies are separate auxiliary diagnostic tasks. The 90.23% figure is not a real-world cybersecurity accuracy estimate.")


with tab_recheck:
    section_heading("Journal Re-evaluation · Phase 1", "Five classification families evaluated on 1,500 shared chronological, boundary-purged held-out origins.")
    kpi([
        ("46.87%", "Majority reference", "Always predict C3; diagnostic baseline"),
        ("45.40%", "Highest fitted accuracy", "Likelihood-based Neural Hawkes"),
        ("0.1975", "Best macro-F1", "Hawkes-informed supervised GRU"),
        ("0.6967", "Best top-3", "Poisson baseline"),
    ])
    st.markdown("**Table 1 — Journal chronological classification**")
    table(JOURNAL_CLASSIFICATION)

    names = [r["Model"] for r in JOURNAL_CLASSIFICATION]
    accuracies = [100 * r["Accuracy"] for r in JOURNAL_CLASSIFICATION]
    fig = go.Figure(go.Bar(
        x=accuracies, y=names, orientation="h",
        marker_color=[VIOLET if "Neural Hawkes" in x else BLUE for x in names],
        hovertemplate="%{y}<br>%{x:.2f}%<extra></extra>",
    ))
    fig.add_vline(x=46.87, line_color="#dc2626", line_dash="dash",
                  annotation_text="Majority-class reference 46.87%", annotation_position="top")
    fig.update_layout(title="Held-out accuracy versus majority-class reference", xaxis_title="Accuracy (%)",
                      yaxis=dict(autorange="reversed"))
    show_chart(fig, 440)

    render_grid("grid-2", [
        info_card("Class imbalance", "C3 dominates the test labels", "C3 represents 46.87% of test outcomes. The Neural Hawkes model predicts C3 as its first choice for 93.2% of origins, which raises raw accuracy without ensuring balanced six-class discrimination."),
        info_card("Metric trade-off", "No universal classification winner", "The supervised GRU leads macro- and weighted-F1, Poisson leads top-3, and Neural Hawkes leads accuracy and top-2. No fitted model exceeds the constant-C3 accuracy reference."),
    ])
    caption("<b>Not a direct score comparison:</b> The conference and revised journal studies differ in multiple experimental choices. No causal claim about the cause of their accuracy difference is justified by these tables.")


with tab_frequency:
    section_heading("Phase 2 · System-wide Frequency Forecasting", "Predict the number of events across all six entities in the next three dimensionless simulator-time units.")
    kpi([
        ("10", "Model families", "Simple, Hawkes, regression, recurrent and Transformer"),
        ("6.5815", "Best learned validation MAE", "GRU-NB · selected on validation"),
        ("6.9875", "Lowest primary test MAE", "Rolling Mean (m=8)"),
        ("7.2542", "Fitted Hawkes test MAE", "Primary trajectory, not all robustness runs"),
    ])
    st.markdown("**Table 2 — Validation and held-out test MAE (lower is better)**")
    table(FREQUENCY_RESULTS)

    sorted_rows = sorted(FREQUENCY_RESULTS, key=lambda r: r["Test MAE"])
    bar_chart([r["Model"] for r in sorted_rows], [r["Test MAE"] for r in sorted_rows],
              "Primary-trajectory held-out MAE", "Events", highlight="Rolling Mean (m=8)", height=490)
    caption("<b>Model selection versus evaluation:</b> GRU-NB was the prespecified validation-selected learned family (mean validation MAE 6.5815). Rolling Mean had the lowest final test MAE (6.9875); the held-out test was not used to change the frozen selection.")

    section_heading("Out-of-trajectory robustness", "The leading model changes when the simulator's event path and covariate path change.")
    st.markdown("**Table 3 — Joint event-and-covariate realisations**")
    table(JOINT_TRAJECTORIES)
    render_grid("grid-3", [
        info_card("J1", "Rolling Mean leads", "Held-out MAE 5.9829; GRU-NB follows with MAE 6.8172."),
        info_card("J2", "GRU-NB leads", "Held-out MAE 6.7321; Rolling Mean records 7.3394."),
        info_card("Numerical qualification", "No accepted fitted Hawkes forecast", "The frozen optimiser acceptance criterion was not met on J1 or J2. Fitted Hawkes is unavailable, not a zero-score baseline."),
    ])

    section_heading("Forecast calibration matters", "Reasonable average count forecasts do not automatically imply suitable uncertainty intervals.")
    render_grid("grid-3", [
        metric_card("0.9406", "GRU-NB mean calibration ratio", "Primary test · average underprediction"),
        metric_card("0.2781", "GRU-NB predicted-mean variance ratio", "Conditional mean variation relative to observed counts"),
        metric_card("98.6%", "Observed coverage of nominal 80% interval", "GRU-NB · substantial overcoverage on primary test"),
    ])
    caption("<b>Further robustness:</b> Across three shared-covariate event trajectories, fitted classical Hawkes has the lowest descriptive mean MAE. The manuscript does not assert population-level or universal superiority for any family.")


with tab_financial:
    section_heading("Frequency–Severity Financial Scenarios", "Separately calibrated monetary severity is combined with technical event-frequency forecasts using explicit thinning assumptions.")
    kpi([
        ("USD 264k", "Mean retained-incident severity", "Theoretical common mean across four severity specifications"),
        ("4%", "Severe-loss tail entry", "P(single-incident loss ≥ USD 1 million)"),
        ("0.01", "Illustrative q reference", "Not an empirically estimated claim-conversion probability"),
        ("2 / 10", "Stable heavy-tail combinations", "Reference Monte Carlo screen; infinite-variance scenarios"),
    ])

    st.markdown("**Explore the manuscript's five event-to-loss scenarios**")
    q_values = [r["q"] for r in THINNING_RESULTS]
    selected_q = st.select_slider(
        "Independent event-to-loss thinning parameter (q)",
        options=q_values, value=0.01, format_func=lambda value: f"{value:g}",
        help="The values are prespecified scenario assumptions, not estimated claim probabilities.",
    )
    chosen = next(r for r in THINNING_RESULTS if r["q"] == selected_q)
    kpi([
        (f"{chosen['Retained']:.4f}", "Expected retained count", "GRU-NB · one three-unit window"),
        (f"{chosen['P_positive'] * 100:.2f}%", "P(at least one retained event)", "Model-derived under the scenario"),
        (f"USD {chosen['ExpectedLoss']:,.0f}", "Expected aggregate loss", "Analytical GRU-NB scenario mean"),
        (f"{selected_q:g}", "Selected conversion scenario", "Independent thinning; not calibrated from claims"),
    ])
    table(THINNING_RESULTS, ["q", "Retained", "P_positive", "ExpectedLoss"], formats={
        "q": lambda x: f"{x:g}", "Retained": lambda x: f"{x:,.6f}",
        "P_positive": lambda x: f"{x:.6f}", "ExpectedLoss": lambda x: f"USD {x:,.0f}"})

    section_heading("Scenario sensitivity across frequency models", "All ten families share the same assumed severity mean; model-level differences reflect frequency forecasts.")
    st.markdown("**Analytical expected aggregate loss at q = 0.01**")
    sorted_losses = sorted(EXPECTED_LOSS_Q001, key=lambda r: r["USD"])
    bar_chart([r["Model"] for r in sorted_losses], [r["USD"] for r in sorted_losses],
              "Expected loss per dimensionless three-unit window", "USD",
              highlight="GRU-NB", height=475)
    caption("<b>Range:</b> approximately USD 99,881–135,346 across ten frequency families at q = 0.01. A larger scenario loss is not evidence that a forecasting model is better or worse.")

    section_heading("Severity-tail sensitivity", "Four specifications match the same mean and tail-entry probability but imply different extremes.")
    st.markdown("**Table 4 — Single-incident severity tails (analytical)**")
    severity_display = [
        {"Specification": r["Specification"], "VaR99 (USD M)": round(r["VaR99_USD"]/1e6, 3),
         "TVaR99 (USD M)": round(r["TVaR99_USD"]/1e6, 3),
         "P(Z≥10M)": f"{r['P10M']:.2e}", "P(Z≥100M)": f"{r['P100M']:.2e}", "Variance": r["Variance"]}
        for r in SEVERITY_RESULTS
    ]
    table(severity_display)
    bar_chart([r["Specification"] for r in SEVERITY_RESULTS],
              [r["TVaR99_USD"] / 1e6 for r in SEVERITY_RESULTS],
              "Single-incident TVaR at 99%", "USD millions", horizontal=False, height=390)

    st.markdown("**Table 6 — Compound-loss comparison at q = 0.01, GPD ξ = 0.25**")
    table(COMPOUND_LOSS, formats={"P(L>=10M)": lambda x: f"{x:.2e}"})
    caption("<b>Monte Carlo precision:</b> In the ten infinite-variance severity/q configurations, only ξ = 0.50 at q = 1 and q = 0.001 pass the manuscript's full reference stability screen. Other extreme-tail estimates must not be represented as converged. The six-family compound-loss table above uses a passing finite-variance reference configuration.")
    caption("<b>Financial interpretation:</b> These are conditional scenarios per <i>dimensionless simulator-time window</i>. They are not annualised loss projections, insurance premiums, observed claims or monetary predictions for real businesses. Synthetic marks and URLhaus URL counts are not claim severities.")


with tab_external:
    section_heading("URLhaus · External Evaluation", "A separate observational test of forecasting malicious-URL counts, not a claim or loss dataset.")
    kpi([
        ("24 hours", "Primary observational horizon", "Chronological URLhaus count forecasting"),
        ("254.620", "Lowest held-out MAE", "Training Mean baseline"),
        ("416.519", "THP held-out MAE", "L=64 count configuration"),
        ("No", "Reproducible prospective skill", "Not established by evaluated URLhaus models"),
    ])
    st.markdown("**Table 7 — URLhaus canonical 24-hour comparison**")
    url_display = []
    for r in URLHAUS_RESULTS:
        d = r.copy()
        d["Pearson"] = "Undefined (constant prediction)" if r["Pearson"] is None else f"{r['Pearson']:.4f}"
        url_display.append(d)
    table(url_display)
    sorted_url = sorted(URLHAUS_RESULTS, key=lambda r: r["MAE"])
    bar_chart([r["Model"] for r in sorted_url], [r["MAE"] for r in sorted_url],
              "URLhaus 24-hour held-out MAE", "URLs", highlight="Training Mean", height=400)
    render_grid("grid-2", [
        info_card("Primary result", "Simple baseline is strongest", "Training Mean records MAE 254.620. THP has MAE 416.519 and Pearson correlation −0.0865, with substantial underprediction and compressed forecast variation."),
        info_card("External validity", "No reliable forecasting transfer", "Context variants and later 1-, 3-, 6- and 12-hour diagnostics do not establish reproducible prospective forecasting signal. Those exploratory diagnostics are not an independent confirmation set."),
    ])
    caption("<b>Scope:</b> URLhaus malicious URLs are operational threat-intelligence observations. They are not insurance claims, and do not calibrate the simulator-time scale, event-to-loss q, monetary severity or aggregate-loss component.")

    section_heading("Research limitations and responsible interpretation", "Transparency about what each source supports is central to the contribution.")
    render_grid("grid-4", [
        info_card("Synthetic design", "Controlled, not calibrated to practice", "A Hawkes-generated benchmark may favour suitably matched models. It is not a real cyber-claims portfolio."),
        info_card("Protocol sensitivity", "Targets and splits differ", "Random-split conference accuracy and chronological journal accuracy have distinct experimental designs and cannot be treated as a single universal ranking."),
        info_card("Financial assumptions", "Event-to-loss mapping is a scenario", "Independent thinning and severity-tail specifications are assumptions; q and exposure duration are not estimated from linked event-and-claim data."),
        info_card("Numerical stability", "Heavy tails demand caution", "Many infinite-variance simulation settings fail the reference precision criteria; reporting more draws does not by itself demonstrate convergence."),
    ])


# ============================================================
# RESEARCH FINDINGS — NARRATIVE FROM ORIGINAL PORTFOLIO
# ============================================================

section_heading(
    "Overall Research Findings",
    "The two papers demonstrate why the task, validation protocol and benchmark must determine the model comparison.",
)
render_grid("grid-3", [
    info_card(
        "Finding 01", "Temporal structure is learnable in the conference benchmark",
        "Under the AusDM conference experiment, THP led all five reported primary classification metrics, including 0.9023 accuracy and 0.8951 macro-F1. This is a controlled synthetic result."
    ),
    info_card(
        "Finding 02", "Chronological evaluation changes the evidence",
        "In the journal re-evaluation, the most accurate fitted classifier reached 0.4540, below the 0.4687 majority-class reference. No method dominated every classification metric."
    ),
    info_card(
        "Finding 03", "Simple baselines remain competitive",
        "GRU-NB was validation-selected for frequency prediction, but Rolling Mean delivered the lowest primary held-out test MAE. Fitted Hawkes performance varied by trajectory and numerical acceptance."
    ),
    info_card(
        "Finding 04", "Uncertainty and calibration matter",
        "Prediction-interval overcoverage and compressed conditional-mean variation show why low point error alone cannot validate a probabilistic frequency forecast."
    ),
    info_card(
        "Finding 05", "Equal means do not imply equal tail risks",
        "A full lognormal and three spliced GPD severity distributions share USD 264,000 theoretical mean severity but differ in extreme quantiles and tail expectations. Some Monte Carlo configurations fail stability screening."
    ),
    info_card(
        "Finding 06", "Observational transfer is not established",
        "The URLhaus evaluation does not support reproducible prospective count-forecasting skill. Malicious-URL records were not used as insurance claims or monetary-severity observations."
    ),
])

section_heading(
    "Technical & Research Capabilities",
    "The methods and professional skills demonstrated across both accepted research papers.",
)
render_grid("grid-3", [
    info_card("Data science", "Python research pipelines", "Event simulation, chronological sample construction, cleaning, feature preparation, model fitting, structured validation and reproducible reporting."),
    info_card("Temporal modelling", "Hawkes and neural sequence methods", "Multivariate marked Hawkes processes, directional excitation, Transformer Hawkes Process, Neural Hawkes-style encoders, GRU and LSTM models."),
    info_card("Statistical modelling", "Count forecasts and likelihoods", "Poisson and Negative Binomial regression, simple and rolling baselines, fitted Hawkes, count distributions, calibration and prediction intervals."),
    info_card("Research validation", "Protocol-aware empirical testing", "Chronological and boundary-purged splits, multiple trajectories, baseline comparisons, stability acceptance criteria and numerical uncertainty."),
    info_card("Risk analytics", "Frequency–severity loss scenarios", "Event-to-loss thinning, separately calibrated monetary loss distributions, expected aggregate loss, VaR, TVaR, exceedance and Monte Carlo precision."),
    info_card("Communication", "Research reporting and interpretation", "Two accepted research outputs, critical discussion of negative results and careful separation of simulated, observed and scenario-based evidence."),
])

section_heading(
    "Research Contribution",
    "From forecasting where cyber activity concentrates to conditional financial-risk quantification.",
)
render_html(highlight_panel(
    "From Prediction to Loss Quantification",
    "The conference study demonstrates that an attention-based Hawkes representation can be effective for future-window <b>entity-risk classification</b> in a controlled synthetic benchmark. "
    "The journal extension investigates a different but connected question: <b>how many events occur system-wide</b>, how count-model performance depends on evaluation and trajectory, and how expected and extreme monetary consequences change under stated <b>frequency–severity assumptions</b>. "
    "The observational URLhaus results and numerical stability checks are part of the contribution, because they define where the evidence does—and does not—support inference."
))

# ============================================================
# RESEARCH SOURCES & NAVIGATION
# ============================================================

section_heading("Research Publications & Sources", "Both research outputs are accepted; numerical summaries follow the supplied final conference paper and revised journal manuscript.")
render_grid("grid-2", [
    publication_card(
        "Phase 1 · AusDM 2026", "Accepted",
        "A Hawkes–Transformer Model for Cyber Risk Prediction: Comparative Evaluation on a Synthetic Hawkes Benchmark",
        "Final 14-page paper. Primary experiment: five-unit top-risk entity classification. Table 1 reports THP accuracy 0.9023, macro-F1 0.8951 and top-3 accuracy 0.9940.",
        "All conference results above are attributed to this source, not the journal re-evaluation."
    ),
    publication_card(
        "Phase 2 · MDPI Risks", "Accepted",
        "From Cyber-Risk Prediction to Loss Quantification: A Task-Aware Frequency–Severity Framework with Hawkes Benchmarking and External Evaluation",
        "Accepted journal paper. The 13 November 2026 manuscript supplies the latest revised results: chronological classification, ten frequency families, severity and compound-loss scenarios, robustness and URLhaus evaluation.",
        "Accepted by MDPI Risks; no publication date or final article DOI is asserted."
    ),
])

caption("<b>Data and attribution:</b> The synthetic Hawkes benchmark is referenced through its IEEE DataPort DOI. This page summarises the research outputs; it does not claim the journal manuscript has been formally published.")
left, right = st.columns(2, gap="medium")
with left:
    st.link_button("Synthetic benchmark · IEEE DataPort", "https://dx.doi.org/10.21227/8drm-jz27", use_container_width=True)
with right:
    st.link_button("URLhaus project · abuse.ch", "https://urlhaus.abuse.ch/", use_container_width=True)

st.write("")
st.page_link("Home.py", label="← Back to Portfolio Home")
