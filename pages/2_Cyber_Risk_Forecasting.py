
import streamlit as st
import plotly.graph_objects as go
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
# RESEARCH DATA — PHASE 1
# ============================================================

phase1_results = [
    ["Poisson baseline", "0.3873", "0.2290", "0.3470", "—", "—"],
    ["Supervised GRU/LSTM", "0.8621", "0.8565", "0.8625", "0.9598", "0.9893"],
    ["Real Neural Hawkes Process", "0.2753", "0.0987", "0.1426", "0.4773", "0.6667"],
    ["Transformer Hawkes Process", "0.8913", "0.8436", "0.8519", "0.9700", "0.9887"],
    ["MCP-Titan", "0.2567", "0.2206", "0.2491", "0.4873", "0.6400"]
]


# ============================================================
# RESEARCH DATA — PHASE 2
# ============================================================

# Manuscript Table 2 — Seven-model frequency comparison

frequency_results = [
    ["Persistence", "8.1467", "9.7221", "3.6880", "1.0215", "0.1361", "0.1385"],
    ["Poisson Regression", "8.1231", "9.9985", "3.9491", "0.8848", "0.1341", "0.1713"],
    ["Negative Binomial Regression", "8.1244", "10.0026", "3.7909", "0.8850", "0.1341", "0.1705"],
    ["GRU", "6.6968", "8.2853", "3.8757", "0.9180", "0.2436", "0.2369"],
    ["LSTM", "7.2260", "8.9889", "3.9028", "0.8983", "0.1955", "0.1874"],
    ["THP–Poisson", "8.7495", "10.9228", "4.2372", "0.8896", "0.0568", "0.0679"],
    ["THP–NB", "8.7831", "10.9580", "4.0150", "0.8822", "0.0719", "0.0856"]
]

# Manuscript Table 3 — Independent synthetic evaluation

independent_results = [
    ["GRU Ensemble", "6.6944", "8.5200", "3.5549", "0.9944", "0.5364", "0.5460", "0.3947"],
    ["Previous-window Persistence", "8.1197", "10.3254", "3.7782", "1.0236", "0.4755", "0.4937", "1.0024"]
]

# Manuscript Table 4 — Monetary severity

severity_results = [
    ["0.25", "0.888485", "1.916074", "2.958632", "6.06e-5", "9.12e-9"],
    ["0.50", "0.888485", "1.737200", "3.211599", "2.29e-4", "2.19e-6"],
    ["0.75", "0.888485", "1.449305", "3.534421", "3.17e-4", "1.34e-5"]
]

# Manuscript Table 5 — Compound-loss sensitivity

aggregate_results = [
    ["Low", "30.958", "0.25", "8.173", "16.983", "19.451"],
    ["Low", "30.958", "0.50", "8.173", "18.260", "25.979"],
    ["Low", "30.958", "0.75", "8.173", "18.846", "43.333"],
    ["Median", "41.112", "0.25", "10.854", "21.024", "23.760"],
    ["Median", "41.112", "0.50", "10.854", "22.689", "31.599"],
    ["Median", "41.112", "0.75", "10.854", "23.861", "53.584"],
    ["High", "48.233", "0.25", "12.734", "23.836", "26.616"],
    ["High", "48.233", "0.50", "12.734", "25.681", "35.172"],
    ["High", "48.233", "0.75", "12.734", "27.299", "59.986"]
]

# Manuscript Table 6 — URLhaus external evaluation

urlhaus_results = [
    ["Mean Baseline", "254.620", "281.337", "0.5491", "0.6067", "0.0000"],
    ["Poisson Regression", "260.939", "303.843", "0.5627", "0.6553", "-0.2383"],
    ["Persistence", "283.606", "630.167", "0.6116", "1.3590", "-0.0295"],
    ["Negative Binomial Regression", "287.973", "343.009", "0.6210", "0.7397", "-0.0795"],
    ["THP Count Model", "416.519", "434.606", "0.8982", "0.9373", "-0.0865"]
]


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
    padding-top: 3.5rem;
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
        padding-top: 2rem;
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
# 1. HERO
# ============================================================

render_html("""
    <div class="hero-card">

        <div class="eyebrow">
            Academic Research · AusDM 2026 · MDPI Risks
        </div>

        <div class="page-title">
            Cyber Risk
            <span class="gradient-text">
                Modelling &amp; Forecasting
            </span>
        </div>

        <div class="subtitle">
            Hawkes Processes · Transformers ·
            Frequency–Severity Modelling ·
            Aggregate Cyber-Loss Analysis
        </div>

        <div class="body-text">

            <p>
                My cyber-risk research investigates
                <b>event clustering, temporal dependence,
                and interactions between entities</b>
                using Hawkes processes, neural sequence
                models, and statistical methods.
            </p>

            <p>
                <b>Phase 1</b> focused on short-horizon
                top-risk entity prediction using a synthetic
                multivariate marked Hawkes benchmark.
                The Transformer Hawkes Process achieved
                <b>89.13% accuracy</b> on the
                primary classification task.
            </p>

            <p>
                <b>Phase 2</b> extended the work to
                system-wide event frequency, independent
                monetary severity modelling, and
                aggregate cyber-loss analysis.
                The GRU model reduced MAE by approximately
                <b>17.6%</b> relative to persistence
                on an independent synthetic trajectory.
            </p>

            <p>
                The actuarial extension demonstrated
                that equal-mean severity distributions
                can produce substantially different
                extreme-loss outcomes.
                URLhaus external evaluation also revealed
                important limits to synthetic-to-real
                forecasting transfer.
            </p>

            <p>
                The research has produced two accepted
                outputs: an <b>AusDM 2026 conference
                paper</b> and a journal manuscript
                accepted by <b>MDPI <i>Risks</i></b>.
            </p>

        </div>

        <div class="hero-tags">
            <span class="hero-tag">Cyber Risk</span>
            <span class="hero-tag">Hawkes Processes</span>
            <span class="hero-tag">Transformers</span>
            <span class="hero-tag">GRU / LSTM</span>
            <span class="hero-tag">Count Forecasting</span>
            <span class="hero-tag">Monetary Severity</span>
            <span class="hero-tag">VaR / TVaR</span>
            <span class="hero-tag">URLhaus</span>
            <span class="hero-tag">Research Validation</span>
        </div>

    </div>
""")


# ============================================================
# 2. RESEARCH SNAPSHOT
# ============================================================

section_heading(
    "Research Snapshot",
    "Quantitative highlights from Phase 1 and Phase 2."
)

render_grid("grid-4", [
    metric_card(
        "89.13%",
        "Phase 1 THP Accuracy",
        "Top-risk entity classification on the synthetic benchmark."
    ),
    metric_card(
        "17.6%",
        "Phase 2 MAE Reduction",
        "Independent GRU evaluation against persistence."
    ),
    metric_card(
        "US$264K",
        "Mean Monetary Severity",
        "Separately calibrated incident-cost assumption."
    ),
    metric_card(
        "US$53.584M",
        "Aggregate TVaR 99%",
        "Median frequency with the heaviest severity tail."
    )
])


# ============================================================
# 3. RESEARCH PUBLICATIONS
# ============================================================

section_heading(
    "Research Publications",
    "Two research phases with distinct analytical objectives."
)

render_grid("grid-2", [

    publication_card(
        "Phase 1 · Conference",
        "Accepted",
        "A Hawkes–Transformer Model for Cyber Risk Prediction: "
        "Comparative Evaluation on a Synthetic Hawkes Benchmark",
        """
        Investigated short-horizon top-risk entity
        prediction using a six-entity marked Hawkes
        benchmark, comparing statistical,
        recurrent, Transformer, likelihood-based,
        and retrieval approaches.
        """,
        """
        AusDM 2026 · Accepted.
        THP classification accuracy: 0.8913.
        """
    ),

    publication_card(
        "Phase 2 · Journal",
        "Accepted",
        "From Cyber-Risk Prediction to Loss Quantification: "
        "A Task-Aware Frequency–Severity Framework with "
        "Hawkes Benchmarking and External Evaluation",
        """
        Extended the original work to
        event-frequency forecasting,
        monetary severity calibration,
        conditional compound-loss modelling,
        and URLhaus external evaluation.
        """,
        """
        MDPI Risks · Accepted.
        Independent GRU MAE: 6.6944.
        Median-frequency TVaR 99%:
        US$23.760M–US$53.584M.
        """
    )
])

research_note("""
    <b>Publication status:</b>
    Both papers are identified as accepted.
    Final publication links can be added once confirmed.
    Numerical results below are research findings,
    not simulated portfolio performance claims.
""")


# ============================================================
# 4. RESEARCH PROBLEM
# ============================================================

section_heading(
    "Research Problem",
    "Cyber risk involves temporal clustering, interconnected systems, "
    "and uncertain financial consequences."
)

render_grid("grid-3", [

    info_card(
        "Temporal Dependence",
        "Cyber incidents may cluster over time",
        """
        Incident arrivals can be temporally related.
        Recent history, timing, and event sequences
        may contain useful information about
        future activity.
        """
    ),

    info_card(
        "Cross-Entity Dependence",
        "Risk can propagate across connected systems",
        """
        Shared infrastructure and technological
        dependencies may create concentrated
        exposure across several entities.
        """
    ),

    info_card(
        "Financial Consequences",
        "Technical activity is not equivalent to monetary loss",
        """
        Event counts, loss-producing incidents,
        and monetary severity must be distinguished
        before aggregate financial risk can
        be interpreted.
        """
    )
])


# ============================================================
# 5. RESEARCH FRAMEWORK
# ============================================================

section_heading(
    "Research Framework",
    "How the study progresses from event dependence "
    "to risk prediction and loss quantification."
)

render_grid("grid-4", [

    process_card(
        "01",
        "Synthetic Hawkes Benchmark",
        """
        Construct six interacting event streams
        with self-excitation, cross-entity effects,
        time-varying background intensity,
        and event-specific marks.
        """
    ),

    process_card(
        "02",
        "Phase 1: Entity Ranking",
        """
        Predict which entity accumulates
        the greatest future activity over
        the next five simulator time units.
        """
    ),

    process_card(
        "03",
        "Phase 2: Frequency Prediction",
        """
        Reconstruct total future event counts
        across the six-entity system
        within the next three simulator
        time units.
        """
    ),

    process_card(
        "04",
        "Financial Risk Analysis",
        """
        Combine a probabilistic frequency
        specification with independently
        calibrated severity assumptions
        to estimate conditional aggregate-loss
        and tail-risk measures.
        """
    )
])

research_note("""
    <b>Target distinction:</b>
    Phase 1 predicts the highest-risk entity;
    Phase 2 predicts total system-wide frequency.
    Synthetic simulator time units are not
    real calendar hours, days, or insurance years.
""")


# ============================================================
# 6. SYNTHETIC HAWKES BENCHMARK
# ============================================================

section_heading(
    "Synthetic Hawkes Benchmark",
    "A controlled event-generation environment "
    "for investigating temporal and cross-entity dependence."
)

render_grid("grid-4", [

    metric_card(
        "6",
        "Entities",
        "Interacting event streams."
    ),

    metric_card(
        "10,000",
        "Benchmark Events",
        "Retained trajectory in the journal study."
    ),

    metric_card(
        "0.92125",
        "Kernel Mass",
        "Integral of the excitation kernel."
    ),

    metric_card(
        "0.3408",
        "Spectral Radius",
        "Reference branching diagnostic."
    )
])

render_grid("grid-3", [

    info_card(
        "Data Structure",
        "Multivariate marked Hawkes process",
        """
        Each event includes entity identity,
        occurrence time, synthetic mark,
        and excitation-related information.
        """
    ),

    info_card(
        "Network Behaviour",
        "Directional interaction effects",
        """
        The simulation incorporates
        self-excitation, forward propagation,
        weaker reverse effects, and
        second-hop interactions.
        """
    ),

    info_card(
        "Scientific Interpretation",
        "Controlled benchmark, not real claims",
        """
        Synthetic marks represent excitation
        behaviour and do not correspond
        to actual monetary cyber losses.
        """
    )
])


# ============================================================
# 7. PHASE 1 RESULTS
# ============================================================

section_heading(
    "Phase 1 — Model Comparison",
    "Top-risk entity classification on the "
    "synthetic Hawkes benchmark."
)

render_html(
    data_table(
        [
            "Model",
            "Main Accuracy",
            "Macro-F1",
            "Weighted-F1",
            "Top-2",
            "Top-3"
        ],
        phase1_results,
        highlight_rows=[3]
    )
)

source_note("""
    Phase 1 conference study results.
    The task concerns top-risk entity classification,
    not numerical frequency prediction.
""")

render_grid("grid-4", [

    metric_card(
        "0.8913",
        "THP Accuracy",
        "Highest primary-task accuracy."
    ),

    metric_card(
        "0.8621",
        "GRU/LSTM Accuracy",
        "Competitive supervised recurrent model."
    ),

    metric_card(
        "0.9700",
        "THP Top-2",
        "Correct entity within top two predictions."
    ),

    metric_card(
        "0.9887",
        "THP Top-3",
        "Correct entity within top three predictions."
    )
])

render_html(
    highlight_panel(
        "Phase 1 — Main Finding",
        """
        The <b>Transformer Hawkes Process</b>
        achieved the highest accuracy
        on the primary synthetic
        top-risk entity classification task.

        The supervised GRU/LSTM model
        remained competitive and produced
        higher macro-F1 and weighted-F1
        scores in the reported comparison.

        The results demonstrate learnable
        temporal structure within the
        controlled synthetic environment.
        """
    )
)


# ============================================================
# 8. PHASE 2 RESEARCH OBJECTIVES
# ============================================================

section_heading(
    "Phase 2 — Research Objectives",
    "Extending the earlier classification study "
    "to event frequency and monetary risk."
)

render_grid("grid-3", [

    info_card(
        "Frequency",
        "System-wide count forecasting",
        """
        Predict the number of events occurring
        across all six entities within
        the fixed future window (t,t+3].
        """
    ),

    info_card(
        "Severity",
        "Independent financial-loss modelling",
        """
        Use external cyber-loss information
        to calibrate monetary severity
        separately from synthetic marks.
        """
    ),

    info_card(
        "Aggregate Loss",
        "Expected and extreme financial outcomes",
        """
        Evaluate expected aggregate cost,
        VaR, TVaR, and exceedance probabilities
        under different assumptions.
        """
    )
])


# ============================================================
# 9. PHASE 2 FREQUENCY RESULTS
# ============================================================

section_heading(
    "Phase 2 — Frequency Model Comparison",
    "Seven models evaluated on 1,452 chronological validation origins."
)

render_grid("grid-4", [

    metric_card(
        "1,452",
        "Validation Origins",
        "Common chronological evaluation sample."
    ),

    metric_card(
        "6.6968",
        "GRU MAE",
        "Lowest point-prediction error."
    ),

    metric_card(
        "8.2853",
        "GRU RMSE",
        "Lowest squared-error measure."
    ),

    metric_card(
        "0.2436",
        "GRU Pearson",
        "Highest correlation in the comparison."
    )
])

render_html(
    data_table(
        [
            "Model",
            "MAE ↓",
            "RMSE ↓",
            "NLL ↓",
            "Calibration",
            "Pearson ↑",
            "Spearman ↑"
        ],
        frequency_results,
        highlight_rows=[3]
    )
)

source_note("""
    Risks manuscript, Table 2, page 30.
    Lower MAE, RMSE, and NLL are preferred;
    calibration should be close to 1.
""")

# ------------------------------------------------------------
# CHART 1 — FREQUENCY MAE
# ------------------------------------------------------------

frequency_names = [row[0] for row in frequency_results]
frequency_mae = [float(row[1]) for row in frequency_results]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=frequency_mae,
        y=frequency_names,
        orientation="h",

        marker_color=[
            VIOLET if name == "GRU" else BLUE
            for name in frequency_names
        ],

        text=[
            f"{value:.3f}"
            for value in frequency_mae
        ],

        textposition="outside",

        hovertemplate=(
            "%{y}<br>"
            "MAE: %{x:.4f}"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title="Phase 2 frequency comparison — Mean absolute error",
    showlegend=False,
    xaxis_title="MAE (events)",
    yaxis_title=None,
    xaxis_range=[0, 11],
    yaxis=dict(autorange="reversed")
)

show_chart(fig, height=420)

render_html(
    highlight_panel(
        "Frequency Comparison — Key Finding",
        """
        The <b>GRU</b> achieved the lowest
        validation MAE (<b>6.6968</b>) and
        RMSE (<b>8.2853</b>).

        Persistence achieved the lowest
        negative log-likelihood
        (<b>3.6880</b>) and mean calibration
        closest to one (<b>1.0215</b>).

        No single model dominated all metrics,
        so independent validation was needed.
        """
    )
)


# ============================================================
# 10. INDEPENDENT GRU EVALUATION
# ============================================================

section_heading(
    "Phase 2 — Independent GRU Evaluation",
    "Testing the selected model on a separately "
    "generated synthetic trajectory."
)

render_grid("grid-4", [

    metric_card(
        "9,885",
        "Forecast Origins",
        "Independent synthetic evaluation."
    ),

    metric_card(
        "6.6944",
        "GRU MAE",
        "Persistence MAE: 8.1197."
    ),

    metric_card(
        "17.6%",
        "MAE Reduction",
        "Relative improvement over persistence."
    ),

    metric_card(
        "0.5364",
        "Pearson Correlation",
        "Positive forecast–outcome association."
    )
])

render_html(
    data_table(
        [
            "Model",
            "MAE",
            "RMSE",
            "NLL",
            "Calibration",
            "Pearson",
            "Spearman",
            "Variance Ratio"
        ],
        independent_results,
        highlight_rows=[0]
    )
)

source_note("""
    Risks manuscript, Table 3, page 31.
    GRU is an equal-weight ensemble of three random seeds.
    Both predictive distributions use the common
    Negative Binomial specification.
""")

# ------------------------------------------------------------
# CHART 2 — GRU VS PERSISTENCE
# ------------------------------------------------------------

fig = go.Figure()

fig.add_trace(
    go.Bar(
        name="GRU Ensemble",
        x=["MAE", "RMSE"],
        y=[6.6944, 8.5200],
        marker_color=VIOLET,
        text=["6.6944", "8.5200"],
        textposition="outside"
    )
)

fig.add_trace(
    go.Bar(
        name="Persistence",
        x=["MAE", "RMSE"],
        y=[8.1197, 10.3254],
        marker_color=CYAN,
        text=["8.1197", "10.3254"],
        textposition="outside"
    )
)

fig.update_layout(
    title="Independent synthetic evaluation — GRU vs persistence",
    barmode="group",
    yaxis_title="Prediction error (events)",
    yaxis_range=[0, 12]
)

show_chart(fig, height=410)

render_grid("grid-3", [

    info_card(
        "Bootstrap Evidence",
        "MAE improvement: −1.417 events",
        """
        Paired moving-block bootstrap
        95% interval:
        [−1.829, −0.998].
        """
    ),

    info_card(
        "Prediction Intervals",
        "95% coverage: 0.954",
        """
        GRU empirical coverage was
        0.829, 0.912, and 0.954
        for nominal 80%, 90%,
        and 95% intervals.
        """
    ),

    info_card(
        "Model Limitation",
        "Variance ratio: 0.3947",
        """
        Conditional-mean predictions
        were less variable than realised
        event counts, with extreme
        outcomes pulled toward the centre.
        """
    )
])

render_html(
    highlight_panel(
        "Independent Evaluation — Main Result",
        """
        GRU reproduced its improvement
        over persistence on the
        independent synthetic trajectory.

        MAE declined by approximately
        <b>17.6%</b> and RMSE by
        <b>17.5%</b>.

        NLL, calibration, and correlation
        also improved.

        However, compressed forecast
        variability remained a limitation,
        and this does not establish
        equivalent real-world performance.
        """
    )
)


# ============================================================
# 11. MONETARY SEVERITY
# ============================================================

section_heading(
    "Phase 2 — Monetary Severity",
    "Independent severity calibration and "
    "equal-mean tail sensitivity analysis."
)

render_grid("grid-4", [

    metric_card(
        "US$264K",
        "Mean Severity",
        "Held constant across tail scenarios."
    ),

    metric_card(
        "US$1M",
        "Tail Threshold",
        "Generalised Pareto tail splice."
    ),

    metric_card(
        "4%",
        "Tail Entry Probability",
        "Probability of entering the upper-loss tail."
    ),

    metric_card(
        "3",
        "Tail Scenarios",
        "GPD shape: 0.25, 0.50, 0.75."
    )
])

render_html(
    data_table(
        [
            "GPD Shape",
            "VaR 95% (US$M)",
            "VaR 99% (US$M)",
            "TVaR 99% (US$M)",
            "P(Loss ≥ US$10M)",
            "P(Loss ≥ US$100M)"
        ],
        severity_results
    )
)

source_note("""
    Risks manuscript, Table 4, page 33.
    Monetary values are shown in US$ millions.
    GPD shapes are sensitivity assumptions rather
    than estimates from individual loss observations.
""")

# ------------------------------------------------------------
# CHART 3 — INDIVIDUAL SEVERITY TVAR
# ------------------------------------------------------------

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=["0.25", "0.50", "0.75"],
        y=[2.958632, 3.211599, 3.534421],

        mode="lines+markers+text",

        name="Individual-loss TVaR 99%",

        line=dict(
            color=VIOLET,
            width=3
        ),

        marker=dict(
            size=10,
            color=VIOLET
        ),

        text=["2.959", "3.212", "3.534"],
        textposition="top center",

        hovertemplate=(
            "GPD shape: %{x}<br>"
            "TVaR: US$%{y:.3f}M"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title="Individual-loss TVaR 99% — Severity-tail sensitivity",
    xaxis_title="GPD shape parameter",
    yaxis_title="TVaR 99% (US$ millions)",
    yaxis_range=[2.5, 4.0],
    showlegend=False
)

show_chart(fig)

render_html(
    highlight_panel(
        "Severity Sensitivity — Main Finding",
        """
        Mean severity remains fixed at
        <b>US$264,000</b>.

        Individual-loss TVaR at 99%
        increases from approximately
        <b>US$2.959M</b> to <b>US$3.534M</b>
        as the GPD shape increases.

        The probability of losses exceeding
        US$100M increases by more than
        three orders of magnitude,
        demonstrating the importance
        of extreme-tail assumptions.
        """
    )
)


# ============================================================
# 12. AGGREGATE LOSS
# ============================================================

section_heading(
    "Phase 2 — Aggregate Cyber-Loss Results",
    "Nine conditional compound-loss scenarios "
    "across three frequency states and "
    "three severity-tail shapes."
)

render_grid("grid-4", [

    metric_card(
        "US$8.173M",
        "Low-Frequency Expected Cost",
        "Mean count: 30.958."
    ),

    metric_card(
        "US$10.854M",
        "Median-Frequency Expected Cost",
        "Mean count: 41.112."
    ),

    metric_card(
        "US$12.734M",
        "High-Frequency Expected Cost",
        "Mean count: 48.233."
    ),

    metric_card(
        "US$59.986M",
        "Maximum Reported TVaR 99%",
        "High frequency, heaviest tail."
    )
])

render_html(
    data_table(
        [
            "Frequency State",
            "Mean Count",
            "GPD Shape",
            "Expected Cost (US$M)",
            "VaR 99% (US$M)",
            "TVaR 99% (US$M)"
        ],
        aggregate_results,
        highlight_rows=[5, 8]
    )
)

source_note("""
    Risks manuscript, Table 5, page 35.
    One million aggregate losses were simulated
    per seed and scenario, using three seeds.
    These are conditional simulator-time scenarios,
    not annualised insurance losses.
""")

# ------------------------------------------------------------
# CHART 4 — AGGREGATE TVAR SENSITIVITY
# ------------------------------------------------------------

shapes = ["0.25", "0.50", "0.75"]

compound_tvar = {
    "Low Frequency": [19.451, 25.979, 43.333],
    "Median Frequency": [23.760, 31.599, 53.584],
    "High Frequency": [26.616, 35.172, 59.986]
}

fig = go.Figure()

for name, values, colour in [
    ("Low Frequency", compound_tvar["Low Frequency"], BLUE),
    ("Median Frequency", compound_tvar["Median Frequency"], VIOLET),
    ("High Frequency", compound_tvar["High Frequency"], CYAN)
]:

    fig.add_trace(
        go.Scatter(
            x=shapes,
            y=values,

            mode="lines+markers",
            name=name,

            line=dict(
                color=colour,
                width=3
            ),

            marker=dict(
                color=colour,
                size=9
            ),

            hovertemplate=(
                "GPD shape: %{x}<br>"
                "TVaR: US$%{y:.3f}M"
                "<extra>%{fullData.name}</extra>"
            )
        )
    )

fig.update_layout(
    title="Aggregate TVaR 99% — Frequency and severity-tail sensitivity",
    xaxis_title="GPD severity-tail shape",
    yaxis_title="Aggregate TVaR 99% (US$ millions)",
    yaxis_range=[15, 65]
)

show_chart(fig, height=420)

render_grid("grid-3", [

    info_card(
        "Frequency Effect",
        "Higher frequency raises expected loss",
        """
        Expected aggregate cost rises
        from US$8.173M to US$12.734M
        between low- and high-frequency states.
        """
    ),

    info_card(
        "Tail Effect",
        "Extreme risk increases sharply",
        """
        At median frequency, TVaR 99%
        increases from US$23.760M
        to US$53.584M as severity
        tails become heavier.
        """
    ),

    info_card(
        "Exceedance Probability",
        "High-loss scenarios remain tail-sensitive",
        """
        At high frequency, the probability
        of aggregate cost reaching US$50M
        rises from 2.4e-5 to 2.46e-3
        across the lightest and heaviest tails.
        """
    )
])

render_html(
    highlight_panel(
        "Aggregate Risk — Main Finding",
        """
        At median frequency, expected aggregate
        incident cost remains approximately
        <b>US$10.854M</b> across the three
        equal-mean severity scenarios.

        However, aggregate TVaR at 99%
        increases from <b>US$23.760M</b>
        to <b>US$53.584M</b>.

        These are conditional scenarios
        using an illustrative event-to-loss
        conversion probability of one.
        They are not observed insurance
        claims or actual premiums.
        """
    )
)


# ============================================================
# 13. URLHAUS EXTERNAL EVALUATION
# ============================================================

section_heading(
    "Phase 2 — URLhaus External Evaluation",
    "Assessing synthetic-to-real forecasting transfer "
    "using observational cyber-threat data."
)

render_grid("grid-4", [

    metric_card(
        "254.620",
        "Mean Baseline MAE",
        "Best point-error result in the 24-hour comparison."
    ),

    metric_card(
        "416.519",
        "THP MAE",
        "Higher than the simpler comparison models."
    ),

    metric_card(
        "−0.0865",
        "THP Pearson",
        "Negative correlation with observed counts."
    ),

    metric_card(
        "0.0024",
        "THP Variance Ratio",
        "Very low conditional-mean forecast variation."
    )
])

render_html(
    data_table(
        [
            "Model",
            "MAE",
            "RMSE",
            "NMAE",
            "NRMSE",
            "Pearson"
        ],
        urlhaus_results,
        highlight_rows=[0]
    )
)

source_note("""
    Risks manuscript, Table 6, page 36.
    The principal THP configuration uses
    64-event histories and forecasts URLhaus
    record counts over the next 24 hours.
""")

# ------------------------------------------------------------
# CHART 5 — URLHAUS MAE
# ------------------------------------------------------------

urlhaus_names = [row[0] for row in urlhaus_results]
urlhaus_mae = [float(row[1]) for row in urlhaus_results]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=urlhaus_mae,
        y=urlhaus_names,
        orientation="h",

        marker_color=[
            VIOLET if name == "THP Count Model" else BLUE
            for name in urlhaus_names
        ],

        text=[
            f"{value:.1f}"
            for value in urlhaus_mae
        ],

        textposition="outside",

        hovertemplate=(
            "%{y}<br>"
            "MAE: %{x:.3f}"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title="URLhaus — 24-hour forecasting error",
    xaxis_title="MAE (URLhaus records per 24 hours)",
    yaxis_title=None,
    xaxis_range=[0, 490],
    yaxis=dict(autorange="reversed"),
    showlegend=False
)

show_chart(fig, height=410)

render_html(
    highlight_panel(
        "URLhaus — Main Finding",
        """
        The THP count model did not reproduce
        the favourable synthetic forecasting
        relationship on URLhaus.

        Its 24-hour MAE was <b>416.519</b>,
        compared with <b>254.620</b>
        for the Mean Baseline.

        Pearson correlation was
        <b>−0.0865</b>, and the
        forecast variance ratio was
        only <b>0.0024</b>.

        These results demonstrate limitations
        in transferring controlled synthetic
        forecasting behaviour to observational
        cyber-threat data.

        URLhaus is not used for monetary
        severity or insurance-claims analysis.
        """
    )
)


# ============================================================
# 14. OVERALL FINDINGS
# ============================================================

section_heading(
    "Overall Research Findings",
    "The combined experiments show why model selection "
    "must depend on the prediction task."
)

render_grid("grid-3", [

    info_card(
        "Finding 01",
        "Prediction targets matter",
        """
        THP performed best on synthetic
        top-risk entity classification,
        while GRU performed best on
        synthetic system-wide count prediction.
        """
    ),

    info_card(
        "Finding 02",
        "Independent testing matters",
        """
        GRU's advantage over persistence
        was reproduced on a separate
        synthetic trajectory.
        """
    ),

    info_card(
        "Finding 03",
        "Baselines remain essential",
        """
        Persistence and statistical models
        provided important reference
        points when evaluating
        complex neural architectures.
        """
    ),

    info_card(
        "Finding 04",
        "Average loss is insufficient",
        """
        Equal-mean severity scenarios
        produced substantially different
        tail-risk outcomes.
        """
    ),

    info_card(
        "Finding 05",
        "External generalisation is challenging",
        """
        The URLhaus experiments did not
        reproduce the positive forecasting
        association observed in the
        controlled synthetic setting.
        """
    ),

    info_card(
        "Finding 06",
        "Financial interpretation requires assumptions",
        """
        The frequency, monetary severity,
        and event-to-loss conversion
        components must be explicitly
        distinguished and validated.
        """
    )
])


# ============================================================
# 15. TECHNICAL CAPABILITIES
# ============================================================

section_heading(
    "Technical & Research Capabilities",
    "Skills demonstrated through the two-phase research program."
)

render_grid("grid-3", [

    info_card(
        "Programming",
        "Python Research Pipelines",
        """
        Simulation, preprocessing,
        sequence construction,
        feature preparation, model training,
        evaluation, and reporting.
        """
    ),

    info_card(
        "Temporal Modelling",
        "Hawkes and Neural Sequence Models",
        """
        Multivariate Hawkes processes,
        Transformer Hawkes Process,
        GRU/LSTM, temporal dependence,
        and sequence learning.
        """
    ),

    info_card(
        "Statistical Modelling",
        "Count and Probability Models",
        """
        Poisson and Negative Binomial
        regression, probabilistic forecasts,
        likelihood evaluation, and calibration.
        """
    ),

    info_card(
        "Research Validation",
        "Reliable Experimental Design",
        """
        Chronological splitting,
        independent testing,
        moving-block bootstrap,
        baseline comparison,
        and uncertainty analysis.
        """
    ),

    info_card(
        "Risk Analytics",
        "Actuarial Frequency–Severity",
        """
        Monetary severity calibration,
        compound-loss simulations,
        VaR, TVaR, expected aggregate cost,
        and exceedance probabilities.
        """
    ),

    info_card(
        "Communication",
        "Academic Research Reporting",
        """
        Research framing, literature review,
        methodology, results interpretation,
        visualisation, and scientific writing.
        """
    )
])


# ============================================================
# 16. LIMITATIONS
# ============================================================

section_heading(
    "Research Limitations",
    "Important boundaries on the interpretation "
    "of the reported results."
)

render_grid("grid-4", [

    info_card(
        "Synthetic Benchmark",
        "Controlled data-generating mechanism",
        """
        Strong synthetic results do not
        establish universal performance
        on real cyber incidents.
        """
    ),

    info_card(
        "Count Forecasting",
        "Compressed forecast variability",
        """
        Independent GRU results were
        positive, but the predicted
        conditional means remained
        less variable than observed counts.
        """
    ),

    info_card(
        "Financial Assumptions",
        "Illustrative event-to-loss mapping",
        """
        Aggregate-loss scenarios depend
        on independent severity assumptions
        and a specified event-to-loss
        conversion probability.
        """
    ),

    info_card(
        "External Evaluation",
        "Limited URLhaus transfer",
        """
        The observational forecasting
        experiments did not establish
        reproducible predictive transfer
        from the synthetic model environment.
        """
    )
])


# ============================================================
# 17. RESEARCH CONTRIBUTION
# ============================================================

section_heading(
    "Research Contribution",
    "Connecting temporal prediction, model suitability, "
    "and conditional financial-risk analysis."
)

render_html(
    highlight_panel(
        "From Prediction to Loss Quantification",
        """
        The research progresses from
        <b>predicting where event activity
        may concentrate</b> to investigating
        <b>how many events may occur</b>
        and <b>how monetary consequences
        may accumulate</b>.

        Phase 1 demonstrates learnable
        temporal structure within a
        controlled Hawkes benchmark.

        Phase 2 shows that model ranking
        changes when the task changes,
        while tail-risk analysis reveals
        how monetary severity assumptions
        can affect extreme-loss estimates.

        The external evaluation also
        establishes important boundaries
        on synthetic-to-real generalisation.

        Together, the work supports a
        task-aware and transparent approach
        to cyber-risk modelling.
        """
    )
)


# ============================================================
# 18. RESEARCH DATA AND LINKS
# ============================================================

section_heading(
    "Research Data & Supporting Material",
    "Dataset availability and reproducibility."
)

render_grid("grid-2", [

    info_card(
        "Research Dataset",
        "IEEE DataPort",
        """
        Supporting research data
        has been deposited with IEEE DataPort,
        providing an accessible reference
        for research material and
        the benchmark.
        """
    ),

    info_card(
        "Research Outputs",
        "Conference and Journal Papers",
        """
        Results presented in this page
        are drawn from the accepted
        AusDM 2026 conference research
        and Phase 2 manuscript accepted
        by MDPI Risks.
        """
    )
])

st.write("")

st.link_button(
    "🔗 Open Research Dataset DOI",
    DATA_DOI
)

st.write("")

st.page_link(
    "Home.py",
    label="← Back to Portfolio Home"
)

source_note("""
    Phase 2 quantitative results are based on the
    supplied Nguyen et al. Risks manuscript,
    version dated 30 September 2026,
    particularly Tables 2–6 and Section 5.
    Monetary amounts are expressed in US dollars.
""")
