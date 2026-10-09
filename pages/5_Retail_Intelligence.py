
import io
import zipfile
from pathlib import Path
from textwrap import dedent
from html import escape

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from sklearn.ensemble import (
    RandomForestClassifier,
    HistGradientBoostingClassifier,
)
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    confusion_matrix,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Retail Intelligence | Thomas Nguyen",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

UCI_URL = (
    "https://archive.ics.uci.edu/dataset/352/"
    "online+retail"
)

LOOKBACK_DAYS = 90
HORIZON_DAYS = 60
SNAPSHOT_STEP_DAYS = 21

TARGET = "InactiveNext60D"

FEATURES = [
    "RecencyDays",
    "Orders90D",
    "Spend90D",
    "Units90D",
    "ProductLines90D",
    "AverageOrderValue90D",
    "LifetimeOrders",
    "LifetimeSpend",
    "TenureDays",
]


# ============================================================
# 2. COLOURS
# ============================================================

BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#0891b2"
INDIGO = "#4f46e5"

TEXT_DARK = "#0f172a"
TEXT_MAIN = "#334155"
TEXT_MUTED = "#475569"


# ============================================================
# 3. HTML HELPERS
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
        unsafe_allow_html=True,
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


def process_card(number, title, text):
    return compact_html(f"""
        <div class="process-card">
            <div class="step-badge">{number}</div>
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


def money(value, decimals=0):
    if pd.isna(value):
        return "—"
    return f"£{value:,.{decimals}f}"


def percent(value, decimals=1):
    if pd.isna(value):
        return "—"
    return f"{value * 100:.{decimals}f}%"


# ============================================================
# 4. CHART STYLING
# ============================================================

def style_chart(fig, height=380):

    fig.update_layout(
        template="plotly_white",
        height=height,

        margin=dict(
            l=30,
            r=45,
            t=95,
            b=45,
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.55)",

        font=dict(
            family="Inter, Segoe UI, Arial, sans-serif",
            size=13,
            color=TEXT_MAIN,
        ),

        title=dict(
            font=dict(
                size=18,
                color=TEXT_DARK,
            ),
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top",
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(
                size=12,
                color=TEXT_DARK,
            ),
            bgcolor="rgba(0,0,0,0)",
        ),

        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#cbd5e1",
            font=dict(
                size=12,
                color=TEXT_DARK,
            ),
        ),
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.20)",
        zeroline=False,
        title_font=dict(
            size=13,
            color=TEXT_MAIN,
        ),
        tickfont=dict(
            size=12,
            color=TEXT_MUTED,
        ),
        automargin=True,
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.20)",
        zeroline=False,
        title_font=dict(
            size=13,
            color=TEXT_MAIN,
        ),
        tickfont=dict(
            size=12,
            color=TEXT_MUTED,
        ),
        automargin=True,
    )

    fig.update_traces(
        selector=dict(type="bar"),
        textfont=dict(
            size=12,
            color=TEXT_DARK,
        ),
        cliponaxis=False,
    )

    return fig


def show_chart(fig, height=380):
    st.plotly_chart(
        style_chart(fig, height),
        use_container_width=True,
        theme=None,
        config={
            "displayModeBar": False,
            "responsive": True,
        },
    )


# ============================================================
# 5. CSS — FUTURISTIC LIGHT THEME
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

/* --------------------------------------------------------
   BACKGROUND
-------------------------------------------------------- */

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
    padding-top: 5.5rem !important;
    padding-bottom: 4rem;
    max-width: 1280px;
}

footer {
    visibility: hidden;
}

/* --------------------------------------------------------
   SIDEBAR
-------------------------------------------------------- */

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

/* --------------------------------------------------------
   HERO
-------------------------------------------------------- */

.hero-card {
    padding: 2.7rem 2.8rem;
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
    line-height: 1.12;

    color: #0f172a;
    margin-bottom: 0.8rem;
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
    font-size: 1.18rem;
    font-weight: 850;
    color: #1e293b;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.body-text {
    color: #334155;
    font-size: 1rem;
    line-height: 1.8;
    max-width: 1050px;
}

.body-text p {
    margin: 0 0 0.95rem;
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

/* --------------------------------------------------------
   SECTION HEADINGS
-------------------------------------------------------- */

.section-title {
    color: #0f172a;
    font-size: 1.9rem;
    font-weight: 950;
    letter-spacing: -0.5px;

    margin-top: 2.6rem;
    margin-bottom: 0.4rem;
}

.section-subtitle {
    color: #64748b;
    font-size: 1rem;
    line-height: 1.65;
    margin-bottom: 1.3rem;
}

/* --------------------------------------------------------
   GRIDS
-------------------------------------------------------- */

.grid-2 {
    display: grid;
    grid-template-columns:
        repeat(2,minmax(0,1fr));
    gap: 1.2rem;
    align-items: stretch;
}

.grid-3 {
    display: grid;
    grid-template-columns:
        repeat(3,minmax(0,1fr));
    gap: 1.2rem;
    align-items: stretch;
}

.grid-4 {
    display: grid;
    grid-template-columns:
        repeat(4,minmax(0,1fr));
    gap: 1.2rem;
    align-items: stretch;
}

/* --------------------------------------------------------
   CARDS
-------------------------------------------------------- */

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
        0 16px 38px rgba(59,130,246,0.08);

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

.metric-card {
    padding: 1.35rem;
    border-radius: 26px;

    min-height: 165px;
    height: 100%;
}

.metric-value {
    color: #0f172a;
    font-size: 1.95rem;
    font-weight: 950;
    line-height: 1.2;

    margin-bottom: 0.4rem;
}

.metric-label {
    color: #4f46e5;
    font-size: 0.9rem;
    font-weight: 900;
    margin-bottom: 0.4rem;
}

.metric-note {
    color: #64748b;
    font-size: 0.82rem;
    line-height: 1.55;
}

.info-card {
    padding: 1.5rem;
    border-radius: 28px;
    min-height: 195px;
    height: 100%;
}

.card-label {
    display: inline-block;

    padding: 0.32rem 0.7rem;
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
    color: #0f172a;
    font-size: 1.1rem;
    font-weight: 950;
    margin-bottom: 0.5rem;
}

.card-text {
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.68;
}

.process-card {
    padding: 1.5rem;
    border-radius: 27px;
    min-height: 210px;
    height: 100%;
}

.step-badge {
    display: inline-block;

    padding: 0.38rem 0.78rem;
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

    margin-bottom: 0.85rem;
}

.process-title {
    color: #0f172a;
    font-size: 1.08rem;
    font-weight: 950;
    margin-bottom: 0.5rem;
}

.process-text {
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.68;
}

.highlight-panel {
    padding: 1.5rem 1.7rem;
    border-radius: 28px;
    margin-top: 1.15rem;
}

.highlight-title {
    color: #0f172a;
    font-size: 1.13rem;
    font-weight: 950;
    margin-bottom: 0.55rem;
}

.highlight-text {
    color: #334155;
    font-size: 0.94rem;
    line-height: 1.75;
}

.research-note {
    padding: 0.95rem 1.15rem;
    margin: 1rem 0;

    border-left: 4px solid #6366f1;
    border-radius: 0 18px 18px 0;

    background: rgba(238,242,255,0.85);

    color: #475569;
    font-size: 0.87rem;
    line-height: 1.7;
}

/* --------------------------------------------------------
   FIX WHITE TEXT ON LIGHT BACKGROUND
-------------------------------------------------------- */

.block-container > div [data-testid="stMarkdownContainer"] > p,
.block-container [data-testid="stWidgetLabel"] p,
.block-container [data-testid="stCaptionContainer"] p {
    color: #334155 !important;
}

.block-container [data-testid="stWidgetLabel"] {
    color: #334155 !important;
}

.block-container label {
    color: #334155 !important;
}

.block-container [data-testid="stMarkdownContainer"] > p strong {
    color: #0f172a !important;
}

.block-container [data-testid="stNotification"] p {
    color: #334155 !important;
}

.block-container [data-testid="stExpander"] summary {
    color: #334155 !important;
}

/* --------------------------------------------------------
   FILE UPLOADER
-------------------------------------------------------- */

[data-testid="stFileUploaderDropzone"] {
    background: rgba(255,255,255,0.94) !important;

    border: 1px dashed
        rgba(99,102,241,0.45) !important;

    border-radius: 18px !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #334155 !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background: #ffffff !important;
    border: 1px solid #c7d2fe !important;
    color: #0f172a !important;
}

/* --------------------------------------------------------
   TABS
-------------------------------------------------------- */

button[data-baseweb="tab"] {
    color: #475569 !important;
    font-weight: 850 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #4338ca !important;
}

/* --------------------------------------------------------
   INPUTS
-------------------------------------------------------- */

.block-container [data-baseweb="select"],
.block-container [data-baseweb="input"] {
    color: #0f172a;
}

.block-container [data-testid="stMetricValue"] {
    color: #0f172a !important;
}

.block-container [data-testid="stMetricLabel"] {
    color: #475569 !important;
}

/* --------------------------------------------------------
   CHARTS
-------------------------------------------------------- */

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.88);

    border: 1px solid rgba(129,140,248,0.24);
    border-radius: 24px;

    padding: 0.6rem;

    box-shadow:
        0 12px 28px rgba(59,130,246,0.06);
}

/* --------------------------------------------------------
   RESPONSIVE
-------------------------------------------------------- */

@media (max-width: 1050px) {

    .grid-4 {
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }
}

@media (max-width: 760px) {

    .block-container {
        padding-top: 4.5rem !important;
    }

    .hero-card {
        padding: 1.7rem 1.5rem;
    }

    .page-title {
        font-size: 2.4rem;
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
        font-size: 1.6rem;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# 6. DATA FILE UTILITIES
# ============================================================

def find_local_dataset():
    """
    Search the portfolio's assets folder.

    The first matching file becomes the default
    source unless the user uploads another file.
    """

    candidates = [
        ASSETS / "Online Retail.xlsx",
        ASSETS / "online_retail.xlsx",
        ASSETS / "Online Retail.csv",
        ASSETS / "online_retail.csv",
        ASSETS / "online_retail.zip",
    ]

    for path in candidates:
        if path.is_file():
            return path

    return None


def read_retail_file(raw_bytes, filename):
    """
    Read the actual UCI dataset.

    Supports Excel, CSV, and ZIP.

    Raises descriptive exceptions instead of
    silently displaying a generic error.
    """

    filename = str(filename).lower()

    if filename.endswith(".zip"):

        if not zipfile.is_zipfile(
            io.BytesIO(raw_bytes)
        ):
            raise ValueError(
                "The selected ZIP file is invalid."
            )

        with zipfile.ZipFile(
            io.BytesIO(raw_bytes)
        ) as archive:

            members = [
                name
                for name in archive.namelist()
                if name.lower().endswith(
                    (".xlsx", ".csv")
                )
                and not Path(name).name.startswith("~$")
                and not name.startswith("__MACOSX/")
            ]

            if not members:
                raise ValueError(
                    "No Excel or CSV dataset was found "
                    "inside the ZIP file."
                )

            selected = members[0]

            return read_retail_file(
                archive.read(selected),
                selected,
            )

    if filename.endswith(".xlsx"):

        # XLSX files are ZIP-based internally.
        # This catches incorrectly downloaded files.

        if not zipfile.is_zipfile(
            io.BytesIO(raw_bytes)
        ):
            raise ValueError(
                "The file has an .xlsx extension, "
                "but is not a valid Excel workbook. "
                "Please download Online Retail.xlsx "
                "again from the official UCI page."
            )

        try:
            import openpyxl

        except ImportError as exc:
            raise RuntimeError(
                "openpyxl is missing. "
                "Add openpyxl to requirements.txt "
                "and install the dependencies."
            ) from exc

        return pd.read_excel(
            io.BytesIO(raw_bytes),
            engine="openpyxl",
        )

    if filename.endswith(".csv"):

        try:
            return pd.read_csv(
                io.BytesIO(raw_bytes),
                low_memory=False,
            )

        except UnicodeDecodeError:
            return pd.read_csv(
                io.BytesIO(raw_bytes),
                encoding="cp1252",
                low_memory=False,
            )

    raise ValueError(
        "Unsupported dataset format. "
        "Use XLSX, CSV, or ZIP."
    )


# ============================================================
# 7. CLEANING AND VALIDATION
# ============================================================

def prepare_retail_data(raw):
    """
    Return:
        sales, orders, diagnostics

    Sales definition:
    - Valid invoice date
    - Positive quantity
    - Positive unit price
    - No cancellation-prefixed invoice

    The result represents positive recorded
    sales, not net sales after refunds.
    """

    columns = {
        "".join(
            character
            for character in str(name).lower()
            if character.isalnum()
        ): name
        for name in raw.columns
    }

    required = [
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "CustomerID",
        "Country",
    ]

    rename = {}

    for field in required:

        key = "".join(
            char
            for char in field.lower()
            if char.isalnum()
        )

        if key not in columns:

            raise ValueError(
                f"Missing required column: {field}. "
                f"Available columns: {list(raw.columns)}"
            )

        rename[columns[key]] = field

    df = (
        raw.rename(columns=rename)[required]
        .copy()
    )

    raw_rows = len(df)

    df["InvoiceNo"] = (
        df["InvoiceNo"]
        .astype("string")
        .str.strip()
    )

    df["StockCode"] = (
        df["StockCode"]
        .astype("string")
        .str.strip()
    )

    df["Description"] = (
        df["Description"]
        .astype("string")
        .fillna("Unknown product")
        .str.strip()
    )

    df["Country"] = (
        df["Country"]
        .astype("string")
        .fillna("Unknown")
        .str.strip()
    )

    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce",
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce",
    )

    df["UnitPrice"] = pd.to_numeric(
        df["UnitPrice"],
        errors="coerce",
    )

    numeric_customer = pd.to_numeric(
        df["CustomerID"],
        errors="coerce",
    )

    df["CustomerID"] = (
        numeric_customer
        .astype("Int64")
        .astype("string")
    )

    cancelled = (
        df["InvoiceNo"]
        .str.upper()
        .str.startswith("C")
        .fillna(False)
    )

    valid = (
        df["InvoiceNo"].notna()
        & df["InvoiceDate"].notna()
        & (df["Quantity"] > 0)
        & (df["UnitPrice"] > 0)
        & (~cancelled)
    )

    sales = df.loc[valid].copy()

    if sales.empty:
        raise ValueError(
            "No valid positive invoice lines "
            "remain after cleaning."
        )

    sales["LineSales"] = (
        sales["Quantity"]
        * sales["UnitPrice"]
    )

    sales["Month"] = (
        sales["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )

    # Group invoice lines to construct orders.

    orders = (
        sales.groupby(
            ["InvoiceNo", "CustomerID"],
            dropna=False,
        )
        .agg(
            InvoiceDate=("InvoiceDate", "min"),
            OrderValue=("LineSales", "sum"),
            Items=("Quantity", "sum"),
            ProductLines=("StockCode", "nunique"),
            Country=("Country", "first"),
        )
        .reset_index()
    )

    orders = (
        orders.sort_values("InvoiceDate")
        .reset_index(drop=True)
    )

    diagnostics = {
        "raw_rows": raw_rows,
        "valid_rows": len(sales),
        "excluded_rows": raw_rows - len(sales),
        "orders": len(orders),
        "identified_customers": (
            orders["CustomerID"].nunique()
        ),
    }

    return sales, orders, diagnostics


@st.cache_data(
    show_spinner="Reading and preparing the retail dataset...",
    max_entries=2,
)
def load_prepared_dataset(raw_bytes, filename):
    """
    Cache the prepared data instead of
    caching multiple large raw workbooks.
    """

    raw = read_retail_file(
        raw_bytes,
        filename,
    )

    return prepare_retail_data(raw)


# ============================================================
# 8. CUSTOMER RFM
# ============================================================

def calculate_rfm(orders, reference_date):

    known = (
        orders.dropna(
            subset=["CustomerID"]
        )
        .copy()
    )

    if known.empty:
        return pd.DataFrame()

    rfm = (
        known.groupby("CustomerID")
        .agg(
            LastPurchase=("InvoiceDate", "max"),
            Frequency=("InvoiceNo", "nunique"),
            Monetary=("OrderValue", "sum"),
        )
    )

    rfm["Recency"] = (
        reference_date - rfm["LastPurchase"]
    ).dt.total_seconds() / 86400

    if len(rfm) < 8:

        rfm["Segment"] = "Insufficient sample"
        return rfm.reset_index()

    rfm["RScore"] = pd.qcut(
        rfm["Recency"].rank(method="first"),
        4,
        labels=[4, 3, 2, 1],
    ).astype(int)

    rfm["FScore"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        4,
        labels=[1, 2, 3, 4],
    ).astype(int)

    rfm["MScore"] = pd.qcut(
        rfm["Monetary"].rank(method="first"),
        4,
        labels=[1, 2, 3, 4],
    ).astype(int)

    conditions = [
        (
            (rfm["RScore"] >= 3)
            & (rfm["FScore"] >= 3)
            & (rfm["MScore"] >= 3)
        ),
        (
            (rfm["RScore"] <= 2)
            & (rfm["FScore"] >= 3)
        ),
        (
            (rfm["RScore"] >= 3)
            & (rfm["FScore"] <= 2)
        ),
    ]

    rfm["Segment"] = np.select(
        conditions,
        [
            "Champions",
            "At-risk regulars",
            "Recent occasional",
        ],
        default="Other customers",
    )

    return rfm.reset_index()


# ============================================================
# 9. CUSTOMER SNAPSHOT CONSTRUCTION
# ============================================================

@st.cache_data(
    show_spinner="Constructing historical customer snapshots...",
    max_entries=2,
)
def create_customer_snapshots(orders):

    known = (
        orders.dropna(
            subset=["CustomerID"]
        )
        .sort_values("InvoiceDate")
        .copy()
    )

    if known.empty:
        return pd.DataFrame()

    first_date = (
        known["InvoiceDate"]
        .min()
        .normalize()
    )

    last_date = (
        known["InvoiceDate"]
        .max()
        .normalize()
    )

    first_snapshot = (
        first_date
        + pd.Timedelta(days=LOOKBACK_DAYS)
    )

    last_snapshot = (
        last_date
        - pd.Timedelta(days=HORIZON_DAYS)
    )

    if first_snapshot >= last_snapshot:
        return pd.DataFrame()

    dates = pd.date_range(
        first_snapshot,
        last_snapshot,
        freq=f"{SNAPSHOT_STEP_DAYS}D",
    )

    rows = []

    for snapshot in dates:

        past = known.loc[
            known["InvoiceDate"] <= snapshot
        ]

        recent = past.loc[
            past["InvoiceDate"]
            > snapshot
            - pd.Timedelta(days=LOOKBACK_DAYS)
        ]

        if recent.empty:
            continue

        recent_features = (
            recent.groupby("CustomerID")
            .agg(
                LastPurchase=("InvoiceDate", "max"),
                Orders90D=("InvoiceNo", "nunique"),
                Spend90D=("OrderValue", "sum"),
                Units90D=("Items", "sum"),
                ProductLines90D=("ProductLines", "sum"),
                AverageOrderValue90D=("OrderValue", "mean"),
            )
        )

        lifetime_features = (
            past.groupby("CustomerID")
            .agg(
                FirstPurchase=("InvoiceDate", "min"),
                LifetimeOrders=("InvoiceNo", "nunique"),
                LifetimeSpend=("OrderValue", "sum"),
            )
        )

        features = recent_features.join(
            lifetime_features,
            how="left",
        )

        features["RecencyDays"] = (
            snapshot - features["LastPurchase"]
        ).dt.total_seconds() / 86400

        features["TenureDays"] = (
            snapshot - features["FirstPurchase"]
        ).dt.total_seconds() / 86400

        future_end = (
            snapshot
            + pd.Timedelta(days=HORIZON_DAYS)
        )

        future_buyers = known.loc[
            (
                known["InvoiceDate"] > snapshot
            )
            & (
                known["InvoiceDate"] <= future_end
            ),
            "CustomerID",
        ].unique()

        features[TARGET] = (
            ~features.index.isin(future_buyers)
        ).astype(int)

        features["SnapshotDate"] = snapshot

        rows.append(
            features.reset_index()[
                [
                    "CustomerID",
                    "SnapshotDate",
                    *FEATURES,
                    TARGET,
                ]
            ]
        )

    if not rows:
        return pd.DataFrame()

    return pd.concat(
        rows,
        ignore_index=True,
    )


# ============================================================
# 10. ML MODEL DEFINITIONS
# ============================================================

def make_models():

    return {

        "Logistic Regression": Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
            (
                "model",
                LogisticRegression(
                    max_iter=800,
                    random_state=42,
                ),
            ),
        ]),

        "Random Forest": Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=100,
                    max_depth=10,
                    min_samples_leaf=8,
                    n_jobs=-1,
                    random_state=42,
                ),
            ),
        ]),

        "Gradient Boosting": Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "model",
                HistGradientBoostingClassifier(
                    max_iter=110,
                    max_leaf_nodes=15,
                    learning_rate=0.06,
                    l2_regularization=0.2,
                    early_stopping=False,
                    random_state=42,
                ),
            ),
        ]),
    }


def calculate_auc(actual, probabilities):

    if len(np.unique(actual)) < 2:
        return np.nan

    return roc_auc_score(
        actual,
        probabilities,
    )


# ============================================================
# 11. CHRONOLOGICAL ML EVALUATION
# ============================================================

@st.cache_resource(
    show_spinner="Training the customer inactivity models...",
    max_entries=2,
)
def evaluate_models(snapshots):

    dates = sorted(
        pd.to_datetime(
            snapshots["SnapshotDate"]
        ).unique()
    )

    dates = [
        pd.Timestamp(date)
        for date in dates
    ]

    if len(dates) < 5:
        raise ValueError(
            "Not enough snapshot dates for "
            "chronological evaluation."
        )

    test_date = dates[-1]

    validation_candidates = [
        date
        for date in dates[:-1]
        if date + pd.Timedelta(
            days=HORIZON_DAYS
        ) <= test_date
    ]

    if not validation_candidates:
        raise ValueError(
            "No suitable validation snapshot "
            "remains after enforcing the "
            "60-day outcome separation."
        )

    validation_date = (
        validation_candidates[-1]
    )

    training_dates = [
        date
        for date in dates
        if date + pd.Timedelta(
            days=HORIZON_DAYS
        ) <= validation_date
    ]

    if not training_dates:
        raise ValueError(
            "No training snapshots remain "
            "after chronological separation."
        )

    train = snapshots.loc[
        snapshots["SnapshotDate"].isin(
            training_dates
        )
    ].copy()

    validation = snapshots.loc[
        snapshots["SnapshotDate"]
        == validation_date
    ].copy()

    test = snapshots.loc[
        snapshots["SnapshotDate"]
        == test_date
    ].copy()

    X_train = train[FEATURES]
    y_train = train[TARGET].astype(int)

    X_validation = validation[FEATURES]
    y_validation = validation[TARGET].astype(int)

    X_test = test[FEATURES]
    y_test = test[TARGET].astype(int)

    if (
        y_train.nunique() < 2
        or y_validation.nunique() < 2
        or y_test.nunique() < 2
    ):
        raise ValueError(
            "One chronological split contains "
            "only one target class. "
            "ROC-AUC cannot be evaluated reliably."
        )

    validation_results = []

    for name, model in make_models().items():

        model.fit(
            X_train,
            y_train,
        )

        probability = (
            model.predict_proba(
                X_validation
            )[:, 1]
        )

        validation_results.append({
            "Model": name,
            "Validation ROC-AUC": calculate_auc(
                y_validation,
                probability,
            ),
        })

    validation_table = (
        pd.DataFrame(validation_results)
        .sort_values(
            "Validation ROC-AUC",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    selected_name = (
        validation_table.iloc[0]["Model"]
    )

    development = pd.concat(
        [train, validation],
        ignore_index=True,
    )

    final_models = {}
    predictions = {}
    test_results = []

    for name, model in make_models().items():

        model.fit(
            development[FEATURES],
            development[TARGET].astype(int),
        )

        probability = (
            model.predict_proba(
                X_test
            )[:, 1]
        )

        predicted = (
            probability >= 0.5
        ).astype(int)

        final_models[name] = model
        predictions[name] = probability

        test_results.append({
            "Model": name,
            "ROC-AUC": calculate_auc(
                y_test,
                probability,
            ),
            "Accuracy": accuracy_score(
                y_test,
                predicted,
            ),
            "Precision": precision_score(
                y_test,
                predicted,
                zero_division=0,
            ),
            "Recall": recall_score(
                y_test,
                predicted,
                zero_division=0,
            ),
            "F1": f1_score(
                y_test,
                predicted,
                zero_division=0,
            ),
        })

    return {
        "models": final_models,
        "predictions": predictions,
        "validation": validation_table,
        "test_results": pd.DataFrame(test_results),
        "selected": selected_name,
        "test_data": test,
        "training_rows": len(train),
        "validation_rows": len(validation),
        "test_rows": len(test),
        "training_end": max(training_dates),
        "validation_date": validation_date,
        "test_date": test_date,
    }


# ============================================================
# 12. HERO
# ============================================================

render_html("""
    <div class="hero-card">

        <div class="eyebrow">
            Business Intelligence · Machine Learning Project
        </div>

        <div class="page-title">
            Retail Intelligence
            <span class="gradient-text">
                Sales &amp; Customer Analytics
            </span>
        </div>

        <div class="subtitle">
            Revenue Analytics · RFM Segmentation ·
            Inactivity Prediction · Decision Support
        </div>

        <div class="body-text">

            <p>
                This project combines
                <b>descriptive business analytics</b>
                and <b>predictive machine learning</b>
                using the same retail transaction dataset.
            </p>

            <p>
                The interactive dashboard explores
                revenue performance, product demand,
                customer purchasing patterns,
                and RFM segments.
            </p>

            <p>
                A separate predictive workflow uses
                historical purchasing features to
                estimate whether a customer will
                <b>make no further purchase during
                the next 60 days</b>.
            </p>

            <p>
                All business metrics and model results
                are calculated directly from
                the loaded data.
            </p>

        </div>

        <div class="hero-tags">
            <span class="hero-tag">Python</span>
            <span class="hero-tag">Pandas</span>
            <span class="hero-tag">Plotly</span>
            <span class="hero-tag">Streamlit</span>
            <span class="hero-tag">RFM Analysis</span>
            <span class="hero-tag">Scikit-learn</span>
            <span class="hero-tag">Time-Aware Validation</span>
        </div>

    </div>
""")


# ============================================================
# 13. DATA SOURCE
# ============================================================

section_heading(
    "Data Source",
    "Load the UCI Online Retail dataset from your "
    "portfolio assets or upload a replacement."
)

local_dataset = find_local_dataset()

col1, col2 = st.columns(
    [1.2, 1],
    gap="large",
)

with col1:

    st.markdown(
        "**UCI Online Retail — Historical Transactions**"
    )

    st.caption(
        "Retail transactions recorded in 2010–2011. "
        "Amounts are expressed in GBP."
    )

    st.link_button(
        "View official dataset and attribution",
        UCI_URL,
    )

    if local_dataset is not None:

        st.success(
            f"Local dataset found: "
            f"assets/{local_dataset.name}"
        )

    else:

        st.info(
            "No local dataset found. "
            "Upload Online Retail.xlsx to continue."
        )

with col2:

    uploaded_file = st.file_uploader(
        "Upload a retail dataset (optional)",
        type=["xlsx", "csv", "zip"],
        help=(
            "An uploaded file replaces the "
            "repository dataset for this session."
        ),
    )


# ============================================================
# 14. LOAD DATA
# ============================================================

source_bytes = None
source_filename = None
source_label = None

try:

    if uploaded_file is not None:

        source_bytes = uploaded_file.getvalue()
        source_filename = uploaded_file.name

        source_label = (
            f"Uploaded file: {uploaded_file.name}"
        )

    elif local_dataset is not None:

        source_bytes = local_dataset.read_bytes()
        source_filename = local_dataset.name

        source_label = (
            f"Repository file: assets/"
            f"{local_dataset.name}"
        )

    else:

        st.warning(
            "Upload Online Retail.xlsx or place "
            "it inside the assets folder."
        )

        st.stop()

    sales, orders, diagnostics = (
        load_prepared_dataset(
            source_bytes,
            source_filename,
        )
    )

except Exception as exc:

    st.error(
        "The retail dataset could not be loaded."
    )

    st.warning(
        f"{type(exc).__name__}: {exc}"
    )

    with st.expander(
        "Detailed technical error"
    ):
        st.exception(exc)

    st.info(
        "Check that the Excel workbook is valid "
        "and that pandas and openpyxl "
        "are installed in your environment."
    )

    st.stop()


st.success(
    f"Dataset loaded successfully: "
    f"{diagnostics['raw_rows']:,} raw rows "
    f"and {diagnostics['valid_rows']:,} "
    f"valid positive sales lines."
)

render_grid("grid-4", [

    metric_card(
        f"{diagnostics['raw_rows']:,}",
        "Raw Records",
        "Rows in the original loaded dataset."
    ),

    metric_card(
        f"{diagnostics['valid_rows']:,}",
        "Valid Sales Lines",
        "Positive, non-cancelled invoice lines."
    ),

    metric_card(
        f"{diagnostics['orders']:,}",
        "Positive Orders",
        "Aggregated invoice records."
    ),

    metric_card(
        f"{diagnostics['identified_customers']:,}",
        "Known Customers",
        "Distinct identified customers."
    ),
])

note_panel(f"""
    <b>Active dataset:</b>
    {escape(source_label)}.

    <b>Cleaning:</b>
    {diagnostics['excluded_rows']:,}
    rows were excluded because they contained
    cancellations, invalid dates,
    non-positive quantities, non-positive
    prices, or unusable invoice identifiers.

    Customer analysis uses records with
    valid customer identifiers.
""")


# ============================================================
# 15. DATA FILTERS
# ============================================================

section_heading(
    "Interactive Filters",
    "The descriptive dashboard responds to your selections."
)

countries = sorted(
    sales["Country"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

minimum_date = (
    sales["InvoiceDate"].min().date()
)

maximum_date = (
    sales["InvoiceDate"].max().date()
)

filter_a, filter_b = st.columns(
    2,
    gap="large",
)

with filter_a:

    selected_countries = st.multiselect(
        "Countries",
        options=countries,
        default=countries,
    )

with filter_b:

    date_selection = st.date_input(
        "Transaction period",
        value=(
            minimum_date,
            maximum_date,
        ),
        min_value=minimum_date,
        max_value=maximum_date,
    )

if len(date_selection) != 2:

    st.info(
        "Select a start and end date."
    )

    st.stop()

start_date, end_date = date_selection

if start_date > end_date:

    st.error(
        "Start date must be before end date."
    )

    st.stop()

start_time = pd.Timestamp(start_date)

end_time = (
    pd.Timestamp(end_date)
    + pd.Timedelta(days=1)
)

filtered_sales = sales.loc[
    sales["Country"].isin(
        selected_countries
    )
    & (
        sales["InvoiceDate"]
        >= start_time
    )
    & (
        sales["InvoiceDate"]
        < end_time
    )
].copy()

filtered_orders = orders.loc[
    orders["Country"].isin(
        selected_countries
    )
    & (
        orders["InvoiceDate"]
        >= start_time
    )
    & (
        orders["InvoiceDate"]
        < end_time
    )
].copy()

if filtered_sales.empty:

    st.warning(
        "No transactions match the filters."
    )

    st.stop()


# ============================================================
# 16. DASHBOARD TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive Overview",
    "🛒 Sales & Products",
    "👥 Customer Insights",
    "🧠 Inactivity Prediction",
    "🎯 Recommendations",
])


# ============================================================
# TAB 1 — EXECUTIVE OVERVIEW
# ============================================================

with tab1:

    section_heading(
        "Executive Overview",
        "Sales and customer KPIs calculated "
        "from the selected transactions."
    )

    revenue = (
        filtered_sales["LineSales"].sum()
    )

    order_count = (
        filtered_orders["InvoiceNo"].nunique()
    )

    customer_count = (
        filtered_orders["CustomerID"].nunique()
    )

    average_order_value = (
        revenue / order_count
        if order_count
        else np.nan
    )

    render_grid("grid-4", [

        metric_card(
            money(revenue),
            "Positive Sales",
            "Recorded positive invoice-line sales."
        ),

        metric_card(
            f"{order_count:,}",
            "Orders",
            "Distinct positive invoices."
        ),

        metric_card(
            f"{customer_count:,}",
            "Known Customers",
            "Distinct identified customers."
        ),

        metric_card(
            money(average_order_value, 2),
            "Average Order Value",
            "Positive sales divided by orders."
        ),
    ])

    monthly_sales = (
        filtered_sales
        .groupby("Month", as_index=False)
        ["LineSales"]
        .sum()
        .sort_values("Month")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly_sales["Month"],
            y=monthly_sales["LineSales"],

            mode="lines+markers",

            line=dict(
                color=BLUE,
                width=3,
            ),

            marker=dict(
                size=8,
                color=VIOLET,
            ),

            fill="tozeroy",
            fillcolor="rgba(37,99,235,0.08)",

            hovertemplate=(
                "%{x}<br>"
                "Sales: £%{y:,.2f}"
                "<extra></extra>"
            ),
        )
    )

    fig.update_layout(
        title="Monthly positive sales",
        xaxis_title="Month",
        yaxis_title="Sales (£)",
        yaxis_tickprefix="£",
        showlegend=False,
    )

    show_chart(fig)

    left, right = st.columns(
        2,
        gap="medium",
    )

    with left:

        country_sales = (
            filtered_sales
            .groupby(
                "Country",
                as_index=False,
            )["LineSales"]
            .sum()
            .nlargest(
                10,
                "LineSales",
            )
            .sort_values("LineSales")
        )

        fig = go.Figure(
            go.Bar(
                x=country_sales["LineSales"],
                y=country_sales["Country"],
                orientation="h",
                marker_color=VIOLET,
            )
        )

        fig.update_layout(
            title="Top markets by positive sales",
            xaxis_title="Sales (£)",
            xaxis_tickprefix="£",
            yaxis_title=None,
        )

        show_chart(fig, height=360)

    with right:

        monthly_orders = (
            filtered_orders
            .assign(
                Month=filtered_orders[
                    "InvoiceDate"
                ]
                .dt.to_period("M")
                .astype(str)
            )
            .groupby(
                "Month",
                as_index=False,
            )["InvoiceNo"]
            .nunique()
        )

        fig = go.Figure(
            go.Bar(
                x=monthly_orders["Month"],
                y=monthly_orders["InvoiceNo"],
                marker_color=CYAN,
            )
        )

        fig.update_layout(
            title="Monthly order volume",
            xaxis_title="Month",
            yaxis_title="Number of orders",
        )

        show_chart(fig, height=360)

    note_panel("""
        Positive sales exclude cancellations
        and non-positive invoice lines.
        This is not net sales after refunds,
        operating profit, or net revenue.
    """)


# ============================================================
# TAB 2 — SALES & PRODUCTS
# ============================================================

with tab2:

    section_heading(
        "Product & Sales Intelligence",
        "Rank products by sales, quantity, "
        "and number of orders."
    )

    product_table = (
        filtered_sales
        .groupby(
            [
                "StockCode",
                "Description",
            ],
            as_index=False,
        )
        .agg(
            Sales=("LineSales", "sum"),
            Units=("Quantity", "sum"),
            Orders=("InvoiceNo", "nunique"),
        )
        .sort_values(
            "Sales",
            ascending=False,
        )
    )

    render_grid("grid-3", [

        metric_card(
            f"{filtered_sales['StockCode'].nunique():,}",
            "Product Codes",
            "Distinct stock codes."
        ),

        metric_card(
            f"{filtered_sales['Quantity'].sum():,.0f}",
            "Units Sold",
            "Total positive quantity."
        ),

        metric_card(
            f"{len(product_table):,}",
            "Product Records",
            "Stock-code and description combinations."
        ),
    ])

    controls_a, controls_b = st.columns(
        2,
        gap="medium",
    )

    with controls_a:

        product_metric = st.selectbox(
            "Rank products by",
            [
                "Sales",
                "Units",
                "Orders",
            ],
        )

    with controls_b:

        top_n = st.slider(
            "Number of products",
            min_value=5,
            max_value=20,
            value=10,
        )

    top_products = (
        product_table
        .nlargest(
            top_n,
            product_metric,
        )
        .sort_values(product_metric)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=top_products[product_metric],
            y=top_products["Description"],
            orientation="h",
            marker_color=BLUE,
        )
    )

    fig.update_layout(
        title=(
            f"Top {top_n} products "
            f"by {product_metric.lower()}"
        ),
        xaxis_title=product_metric,
        yaxis_title=None,
    )

    show_chart(
        fig,
        height=max(
            380,
            top_n * 32 + 125,
        ),
    )

    st.markdown(
        "**Detailed product performance**"
    )

    display_products = (
        product_table.head(100).copy()
    )

    display_products["Sales"] = (
        display_products["Sales"].round(2)
    )

    st.dataframe(
        display_products,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# TAB 3 — CUSTOMER INSIGHTS
# ============================================================

with tab3:

    section_heading(
        "Customer Analytics & RFM",
        "Understand customer spending, repeat purchasing, "
        "and recency–frequency–monetary segments."
    )

    known_orders = (
        filtered_orders.dropna(
            subset=["CustomerID"]
        )
        .copy()
    )

    if known_orders.empty:

        st.info(
            "No identified customers are available "
            "for the selected filters."
        )

    else:

        reference_date = end_time

        rfm = calculate_rfm(
            known_orders,
            reference_date,
        )

        purchases_by_customer = (
            known_orders
            .groupby("CustomerID")
            ["InvoiceNo"]
            .nunique()
        )

        repeat_rate = (
            purchases_by_customer >= 2
        ).mean()

        render_grid("grid-4", [

            metric_card(
                f"{len(rfm):,}",
                "Customers",
                "Identified customer records."
            ),

            metric_card(
                percent(repeat_rate),
                "Repeat Purchase Share",
                "Customers with at least two observed orders."
            ),

            metric_card(
                f"{rfm['Recency'].median():.1f}",
                "Median Recency (Days)",
                "Days since the last observed purchase."
            ),

            metric_card(
                money(
                    rfm["Monetary"].median(),
                    2,
                ),
                "Median Customer Spend",
                "Recorded positive spending."
            ),
        ])

        segments = (
            rfm["Segment"]
            .value_counts()
            .reset_index()
        )

        segments.columns = [
            "Segment",
            "Customers",
        ]

        fig = go.Figure(
            go.Bar(
                x=segments["Customers"],
                y=segments["Segment"],
                orientation="h",
                marker_color=VIOLET,
            )
        )

        fig.update_layout(
            title="Customer segmentation by RFM",
            xaxis_title="Customers",
            yaxis_title=None,
            yaxis=dict(
                autorange="reversed"
            ),
        )

        show_chart(fig)

        left, right = st.columns(
            2,
            gap="medium",
        )

        with left:

            fig = go.Figure(
                go.Histogram(
                    x=rfm["Frequency"],
                    nbinsx=35,
                    marker_color=BLUE,
                )
            )

            fig.update_layout(
                title="Orders per customer",
                xaxis_title="Observed orders",
                yaxis_title="Customers",
            )

            show_chart(fig, height=350)

        with right:

            fig = go.Figure(
                go.Histogram(
                    x=rfm["Monetary"],
                    nbinsx=40,
                    marker_color=CYAN,
                )
            )

            fig.update_layout(
                title="Customer spending distribution",
                xaxis_title="Positive spend (£)",
                yaxis_title="Customers",
            )

            show_chart(fig, height=350)

        st.markdown(
            "**RFM segment summary**"
        )

        summary = (
            rfm.groupby("Segment")
            .agg(
                Customers=("CustomerID", "nunique"),
                MedianRecency=("Recency", "median"),
                MedianOrders=("Frequency", "median"),
                MedianSpend=("Monetary", "median"),
            )
            .reset_index()
        )

        st.dataframe(
            summary.round(2),
            use_container_width=True,
            hide_index=True,
        )

        note_panel("""
            RFM groups are descriptive
            classifications calculated from
            the selected period.
            They are not churn labels
            or causal measures of retention.
        """)


# ============================================================
# TAB 4 — INACTIVITY PREDICTION
# ============================================================

with tab4:

    section_heading(
        "Customer Inactivity Prediction",
        "Estimate whether recently active customers "
        "will make no purchase in the next 60 days."
    )

    render_grid("grid-3", [

        metric_card(
            "90 days",
            "Feature Window",
            "Recent customer purchasing history."
        ),

        metric_card(
            "60 days",
            "Prediction Window",
            "Future purchase-inactivity outcome."
        ),

        metric_card(
            "3 models",
            "Model Comparison",
            "Logistic Regression, Random Forest, Gradient Boosting."
        ),
    ])

    render_grid("grid-3", [

        process_card(
            "01",
            "Historical Features",
            """
            Construct RFM-like purchasing
            features using information
            available at each snapshot.
            """
        ),

        process_card(
            "02",
            "Future Labels",
            """
            Determine whether each
            customer makes another
            purchase during the
            next 60 days.
            """
        ),

        process_card(
            "03",
            "Chronological Testing",
            """
            Separate model selection
            from the final held-out
            test period and avoid
            using unobserved future labels.
            """
        ),
    ])

    note_panel("""
        <b>Prediction target:</b>
        This model estimates purchasing
        inactivity, not confirmed customer
        cancellation or contractual churn.

        Model training uses the complete
        cleaned dataset independently of
        the sales-dashboard filters.
    """)

    if st.button(
        "Train and evaluate models",
        type="primary",
    ):

        st.session_state[
            "retail_training_requested"
        ] = True

    if not st.session_state.get(
        "retail_training_requested",
        False,
    ):

        st.info(
            "Click the training button to "
            "calculate real model results "
            "from the dataset."
        )

    else:

        try:

            snapshots = (
                create_customer_snapshots(
                    orders
                )
            )

            if snapshots.empty:
                raise ValueError(
                    "Insufficient customer history "
                    "to construct complete 60-day labels."
                )

            model_result = (
                evaluate_models(snapshots)
            )

            st.success(
                "Model training and evaluation completed."
            )

            section_heading(
                "Evaluation Summary",
                "Chronologically separated training, "
                "validation, and test samples."
            )

            render_grid("grid-4", [

                metric_card(
                    f"{model_result['training_rows']:,}",
                    "Training Rows",
                    "Historical customer snapshots."
                ),

                metric_card(
                    f"{model_result['validation_rows']:,}",
                    "Validation Rows",
                    "Separate model-selection snapshot."
                ),

                metric_card(
                    f"{model_result['test_rows']:,}",
                    "Test Rows",
                    "Later held-out customer snapshot."
                ),

                metric_card(
                    model_result["selected"],
                    "Selected Model",
                    "Selected by validation ROC-AUC."
                ),
            ])

            st.caption(
                "Training end: "
                f"{model_result['training_end']:%Y-%m-%d}"
                " | Validation: "
                f"{model_result['validation_date']:%Y-%m-%d}"
                " | Test: "
                f"{model_result['test_date']:%Y-%m-%d}"
            )

            st.markdown(
                "**Validation model selection**"
            )

            st.dataframe(
                model_result["validation"].round(4),
                use_container_width=True,
                hide_index=True,
            )

            st.markdown(
                "**Held-out test results**"
            )

            st.dataframe(
                model_result["test_results"].round(4),
                use_container_width=True,
                hide_index=True,
            )

            note_panel("""
                The model was selected using
                validation ROC-AUC.

                Test results are reported
                separately rather than
                selecting whichever model
                happens to perform best
                on the test set.
            """)

            model_names = list(
                model_result["models"].keys()
            )

            selected_model = st.selectbox(
                "Inspect model",
                options=model_names,
                index=model_names.index(
                    model_result["selected"]
                ),
            )

            threshold = st.slider(
                "Risk classification threshold",
                min_value=0.10,
                max_value=0.90,
                value=0.50,
                step=0.05,
            )

            test = model_result[
                "test_data"
            ].copy()

            actual = (
                test[TARGET]
                .astype(int)
                .to_numpy()
            )

            probabilities = (
                model_result["predictions"][
                    selected_model
                ]
            )

            predicted = (
                probabilities >= threshold
            ).astype(int)

            auc = calculate_auc(
                actual,
                probabilities,
            )

            precision = precision_score(
                actual,
                predicted,
                zero_division=0,
            )

            recall = recall_score(
                actual,
                predicted,
                zero_division=0,
            )

            f1 = f1_score(
                actual,
                predicted,
                zero_division=0,
            )

            accuracy = accuracy_score(
                actual,
                predicted,
            )

            render_grid("grid-4", [

                metric_card(
                    f"{auc:.3f}",
                    "ROC-AUC",
                    "Held-out ranking performance."
                ),

                metric_card(
                    f"{accuracy:.3f}",
                    "Accuracy",
                    "Correct binary classifications."
                ),

                metric_card(
                    f"{precision:.3f}",
                    "Precision",
                    "Correctness of inactivity alerts."
                ),

                metric_card(
                    f"{recall:.3f}",
                    "Recall",
                    "Share of actual inactive cases identified."
                ),
            ])

            left, right = st.columns(
                2,
                gap="medium",
            )

            # --------------------------------------------
            # ROC CURVE
            # --------------------------------------------

            with left:

                fpr, tpr, _ = roc_curve(
                    actual,
                    probabilities,
                )

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=fpr,
                        y=tpr,
                        mode="lines",
                        line=dict(
                            color=VIOLET,
                            width=3,
                        ),
                        name=selected_model,
                    )
                )

                fig.add_trace(
                    go.Scatter(
                        x=[0, 1],
                        y=[0, 1],
                        mode="lines",
                        line=dict(
                            color="#94a3b8",
                            dash="dash",
                        ),
                        name="Random reference",
                    )
                )

                fig.update_layout(
                    title="Held-out ROC curve",
                    xaxis_title="False positive rate",
                    yaxis_title="True positive rate",
                    xaxis_range=[0, 1],
                    yaxis_range=[0, 1],
                )

                show_chart(fig)

            # --------------------------------------------
            # CONFUSION MATRIX
            # --------------------------------------------

            with right:

                cm = confusion_matrix(
                    actual,
                    predicted,
                    labels=[0, 1],
                )

                fig = go.Figure(
                    go.Heatmap(
                        z=cm,
                        x=[
                            "Predicted active",
                            "Predicted inactive",
                        ],
                        y=[
                            "Actual active",
                            "Actual inactive",
                        ],
                        colorscale=[
                            [0, "#eff6ff"],
                            [1, "#6366f1"],
                        ],
                        text=cm,
                        texttemplate="%{text}",
                        textfont=dict(
                            size=16,
                        ),
                        showscale=False,
                    )
                )

                # Light background, dark numeric labels.
                fig.update_layout(
                    title="Held-out confusion matrix",
                    xaxis_title=None,
                    yaxis_title=None,
                    yaxis=dict(
                        autorange="reversed"
                    ),
                )

                show_chart(fig)

            # --------------------------------------------
            # PREDICTED RISK DISTRIBUTION
            # --------------------------------------------

            fig = go.Figure()

            fig.add_trace(
                go.Histogram(
                    x=probabilities[
                        actual == 0
                    ],
                    name="Purchased again",
                    marker_color=CYAN,
                    opacity=0.7,
                    nbinsx=25,
                )
            )

            fig.add_trace(
                go.Histogram(
                    x=probabilities[
                        actual == 1
                    ],
                    name="No purchase in 60 days",
                    marker_color=VIOLET,
                    opacity=0.7,
                    nbinsx=25,
                )
            )

            fig.update_layout(
                title="Held-out risk probability distribution",
                barmode="overlay",
                xaxis_title="Predicted inactivity probability",
                yaxis_title="Customer observations",
                xaxis_range=[0, 1],
            )

            show_chart(fig)

            # --------------------------------------------
            # FEATURE IMPORTANCE
            # --------------------------------------------

            pipeline = (
                model_result["models"][
                    selected_model
                ]
            )

            estimator = (
                pipeline.named_steps["model"]
            )

            importances = None

            if hasattr(
                estimator,
                "feature_importances_",
            ):

                importances = (
                    estimator.feature_importances_
                )

            elif hasattr(
                estimator,
                "coef_",
            ):

                importances = np.abs(
                    estimator.coef_[0]
                )

            if importances is not None:

                importance_table = (
                    pd.DataFrame({
                        "Feature": FEATURES,
                        "Importance": importances,
                    })
                    .sort_values(
                        "Importance",
                        ascending=False,
                    )
                )

                fig = go.Figure(
                    go.Bar(
                        x=importance_table[
                            "Importance"
                        ][::-1],

                        y=importance_table[
                            "Feature"
                        ][::-1],

                        orientation="h",
                        marker_color=BLUE,
                    )
                )

                fig.update_layout(
                    title="Model feature importance",
                    xaxis_title="Model-specific importance",
                    yaxis_title=None,
                )

                show_chart(fig)

                st.caption(
                    "Importance is model-specific. "
                    "Random Forest uses impurity-based "
                    "importance; Logistic Regression "
                    "uses absolute standardised coefficients. "
                    "These do not establish causality."
                )

            # --------------------------------------------
            # HISTORICAL CUSTOMER RISK TABLE
            # --------------------------------------------

            section_heading(
                "Historical Customer Risk Ranking",
                "Illustrative prioritisation using "
                "held-out historical predictions."
            )

            risk_table = pd.DataFrame({
                "Customer": [
                    f"Customer {i+1}"
                    for i in range(len(test))
                ],
                "Inactivity Probability": probabilities,
                "Observed Inactivity": actual,
                "Orders (90D)": test[
                    "Orders90D"
                ].to_numpy(),
                "Spend (90D, £)": test[
                    "Spend90D"
                ].to_numpy(),
            })

            risk_table["Risk Level"] = np.select(
                [
                    risk_table[
                        "Inactivity Probability"
                    ] >= 0.70,

                    risk_table[
                        "Inactivity Probability"
                    ] >= 0.40,
                ],
                [
                    "High",
                    "Moderate",
                ],
                default="Low",
            )

            risk_table = (
                risk_table
                .sort_values(
                    "Inactivity Probability",
                    ascending=False,
                )
                .head(20)
                .copy()
            )

            risk_table[
                "Inactivity Probability"
            ] = risk_table[
                "Inactivity Probability"
            ].round(4)

            risk_table[
                "Spend (90D, £)"
            ] = risk_table[
                "Spend (90D, £)"
            ].round(2)

            st.dataframe(
                risk_table,
                use_container_width=True,
                hide_index=True,
            )

            note_panel("""
                <b>Interpretation:</b>
                These predictions relate to
                historical purchase-inactivity
                outcomes in the public dataset.

                They are not live customer
                risk scores, verified cancellations,
                or evidence that a marketing
                intervention would improve retention.
            """)

        except Exception as exc:

            st.error(
                "The predictive experiment "
                "could not be completed."
            )

            st.warning(
                f"{type(exc).__name__}: {exc}"
            )

            with st.expander(
                "Technical details"
            ):
                st.exception(exc)


# ============================================================
# TAB 5 — BUSINESS RECOMMENDATIONS
# ============================================================

with tab5:

    section_heading(
        "Business Recommendations",
        "Potential analytical applications "
        "and practical decision-support use cases."
    )

    render_grid("grid-3", [

        info_card(
            "Revenue Analysis",
            "Identify Sales Concentration",
            """
            Evaluate which products,
            customers, and markets
            contribute most to
            positive recorded sales.
            """
        ),

        info_card(
            "Customer Analytics",
            "Understand Repeat Purchasing",
            """
            Monitor recency and
            purchase frequency to
            identify differing
            customer behaviours.
            """
        ),

        info_card(
            "Prediction",
            "Review Inactivity Risk",
            """
            Use historical risk
            estimates to investigate
            customers who may not
            purchase again soon.
            """
        ),

        info_card(
            "Business Intelligence",
            "Track Commercial Changes",
            """
            Analyse monthly trends
            and changes across
            selected countries
            and products.
            """
        ),

        info_card(
            "Machine Learning",
            "Monitor Predictive Quality",
            """
            Compare models using
            ROC-AUC, recall, precision,
            and chronological
            evaluation results.
            """
        ),

        info_card(
            "Decision Science",
            "Test Retention Strategies",
            """
            Evaluate proposed
            interventions through
            appropriate experiments
            rather than assuming
            prediction implies causality.
            """
        ),
    ])

    section_heading(
        "End-to-End Analytics Workflow",
        "A single dataset supporting both "
        "descriptive and predictive analysis."
    )

    render_grid("grid-4", [

        process_card(
            "01",
            "Collect & Clean",
            """
            Validate invoice dates,
            customers, quantities,
            prices, and cancellations.
            """
        ),

        process_card(
            "02",
            "Analyse Sales",
            """
            Calculate revenue,
            order volume, average
            order value, and product
            performance.
            """
        ),

        process_card(
            "03",
            "Segment Customers",
            """
            Use recency, frequency,
            and monetary value
            to understand customer
            purchasing behaviour.
            """
        ),

        process_card(
            "04",
            "Predict Inactivity",
            """
            Construct historical
            features, evaluate
            three ML models, and
            report held-out results.
            """
        ),
    ])

    render_html(
        highlight_panel(
            "Overall Project Contribution",
            """
            Retail Intelligence demonstrates
            an integrated analytics workflow.

            <b>Descriptive analytics</b>
            explains historical sales and
            customer behaviour.

            <b>RFM segmentation</b>
            identifies different
            purchasing patterns.

            <b>Machine learning</b>
            estimates future purchasing
            inactivity under a clearly
            defined historical outcome.

            The key objective is to
            support decisions using
            measured results, transparent
            assumptions, and appropriate
            model validation.
            """
        )
    )


# ============================================================
# 17. DATASET ATTRIBUTION
# ============================================================

section_heading(
    "Dataset & Methodology",
    "Data source, assumptions, and "
    "limitations of the dashboard."
)

render_grid("grid-3", [

    info_card(
        "Data Source",
        "UCI Online Retail",
        """
        Public historical transaction
        data from a UK non-store
        retailer covering 2010–2011.
        """
    ),

    info_card(
        "Sales Metric",
        "Positive Recorded Sales",
        """
        Sales charts exclude cancelled
        and non-positive lines and
        do not account for all
        refunds or operating costs.
        """
    ),

    info_card(
        "Prediction Target",
        "60-Day Purchase Inactivity",
        """
        Classification labels measure
        whether a recently active
        customer makes another
        recorded purchase during
        the next 60 days.
        """
    ),
])

st.link_button(
    "🔗 UCI Online Retail Dataset",
    UCI_URL,
)

note_panel("""
    <b>Dataset attribution:</b>
    Chen, D. (2015), Online Retail,
    UCI Machine Learning Repository.
    DOI: 10.24432/C5BW33.

    This is a historical analytical
    demonstration, not a live
    production retail system.
""")

st.write("")

st.page_link(
    "Home.py",
    label="← Back to Portfolio Home",
)
