
import streamlit as st
import plotly.graph_objects as go
from textwrap import dedent
from html import escape

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sports Broadcast Analytics | Thomas Nguyen",
    page_icon="🏟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# COLOURS
# ============================================================

BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#0891b2"
INDIGO = "#4f46e5"

TEXT_DARK = "#0f172a"
TEXT_MAIN = "#334155"
TEXT_MUTED = "#475569"


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
# CARDS
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


def step_card(number, title, text):
    return compact_html(f"""
        <div class="step-card">
            <div class="step-badge">{number}</div>
            <div class="step-title">{title}</div>
            <div class="step-text">{text}</div>
        </div>
    """)


def highlight_panel(title, text):
    return compact_html(f"""
        <div class="highlight-panel">
            <div class="highlight-title">{title}</div>
            <div class="highlight-text">{text}</div>
        </div>
    """)


def data_table(headers, rows):
    header_html = "".join(
        f"<th>{escape(str(header))}</th>"
        for header in headers
    )

    body = ""

    for row in rows:
        cells = "".join(
            f"<td>{escape(str(value))}</td>"
            for value in row
        )
        body += f"<tr>{cells}</tr>"

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


# ============================================================
# EVIDENCE DATA
# ============================================================

# These numbers describe documented project scope.
# They are not sponsor ROI, campaign impressions,
# validation accuracy, or personally reviewed frame counts.

BROADCAST_FRAMES_LABEL = "160K+"
PLACEMENT_HOURS_LABEL = "≈200h"

event_contexts = [
    {
        "type": "Motorsport",
        "event": "The Bend",
        "scope": "Supercars broadcast exposure"
    },
    {
        "type": "Motorsport",
        "event": "Bathurst",
        "scope": "Supercars broadcast exposure"
    },
    {
        "type": "Marathon",
        "event": "Sydney Marathon",
        "scope": "Sponsorship visibility"
    },
    {
        "type": "Marathon",
        "event": "Berlin Marathon",
        "scope": "Sponsorship visibility"
    }
]

athlete_groups = {
    "Basketball": [
        "Kawhi Leonard",
        "Jamal Murray",
        "Cooper Flagg"
    ],
    "Tennis": [
        "Coco Gauff",
        "Tommy Paul"
    ],
    "Baseball": [
        "Shohei Ohtani"
    ],
    "American Football": [
        "Josh Allen"
    ],
    "Football / Soccer": [
        "Bukayo Saka"
    ]
}

ATHLETE_COUNT = sum(
    len(names) for names in athlete_groups.values()
)

SPORT_COUNT = len(athlete_groups)
EVENT_CONTEXT_COUNT = len(event_contexts)


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
    font-size: 3.5rem;
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
    font-size: 1rem;
    color: #334155;
    line-height: 1.8;
    max-width: 1050px;
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

/* SECTION HEADINGS */

.section-title {
    font-size: 1.92rem;
    font-weight: 950;
    letter-spacing: -0.5px;
    color: #0f172a;

    margin-top: 2.65rem;
    margin-bottom: 0.35rem;
}

.section-subtitle {
    font-size: 1rem;
    line-height: 1.65;
    color: #64748b;
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
.step-card,
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
.step-card::before {
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

/* METRICS */

.metric-card {
    padding: 1.4rem;
    border-radius: 26px;
    min-height: 165px;
    height: 100%;
}

.metric-value {
    color: #0f172a;
    font-size: 2.12rem;
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
    font-size: 0.83rem;
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
    color: #0f172a;
    font-size: 1.16rem;
    font-weight: 950;
    line-height: 1.45;
    margin-bottom: 0.55rem;
}

.card-text {
    color: #475569;
    font-size: 0.94rem;
    line-height: 1.7;
}

/* PROCESS STEPS */

.step-card {
    padding: 1.5rem;
    border-radius: 27px;
    min-height: 215px;
    height: 100%;
}

.step-badge {
    display: inline-block;
    padding: 0.36rem 0.78rem;
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

.step-title {
    color: #0f172a;
    font-size: 1.1rem;
    font-weight: 950;
    margin-bottom: 0.55rem;
}

.step-text {
    color: #475569;
    font-size: 0.92rem;
    line-height: 1.7;
}

/* EVIDENCE TABLE */

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
    min-width: 750px;
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

/* HIGHLIGHT */

.highlight-panel {
    padding: 1.55rem 1.7rem;
    border-radius: 28px;
    margin-top: 1.25rem;
}

.highlight-title {
    color: #0f172a;
    font-size: 1.16rem;
    font-weight: 950;
    margin-bottom: 0.55rem;
}

.highlight-text {
    color: #334155;
    font-size: 0.95rem;
    line-height: 1.75;
}

/* NOTES */

.evidence-note {
    padding: 0.95rem 1.1rem;
    margin-top: 1rem;

    border-left: 4px solid #6366f1;
    border-radius: 0 18px 18px 0;

    background: rgba(238,242,255,0.85);
    color: #475569;

    font-size: 0.87rem;
    line-height: 1.65;
}

.small-note {
    color: #64748b;
    font-size: 0.84rem;
    line-height: 1.6;
    margin-top: 0.6rem;
}

/* PLOTLY */

[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(129,140,248,0.24);

    border-radius: 24px;
    padding: 0.65rem;

    box-shadow:
        0 12px 28px rgba(59,130,246,0.06);
}

/* RESPONSIVE */

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
        padding: 1.7rem 1.5rem;
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
    .step-card {
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
            Industry Analytics · Futures Sport &amp; Entertainment
        </div>

        <div class="page-title">
            Sports Broadcast
            <span class="gradient-text">Analytics</span>
        </div>

        <div class="subtitle">
            Sponsor Exposure · Data Quality · Media Monitoring ·
            Commercial Reporting
        </div>

        <div class="body-text">

            <p>
                During my internship at
                <b>Futures Sport &amp; Entertainment</b>,
                I supported sports sponsorship and
                media analytics across broadcast
                exposure, brand visibility, and
                athlete-related media monitoring.
            </p>

            <p>
                My work included preparing and
                validating exposure data within a
                workflow involving <b>160,000+
                Supercars broadcast frame outputs</b>,
                as well as supporting marathon
                sponsorship analysis and athlete
                media-insight reporting.
            </p>

            <p>
                The focus was on making raw media
                data more reliable and useful for
                commercial reporting through
                <b>Excel-based analysis, quality
                assurance, media monitoring,
                and reporting support</b>.
            </p>

        </div>

        <div class="hero-tags">
            <span class="hero-tag">Industry Internship</span>
            <span class="hero-tag">Excel</span>
            <span class="hero-tag">Power BI</span>
            <span class="hero-tag">TVEyes</span>
            <span class="hero-tag">Broadcast Exposure</span>
            <span class="hero-tag">Brand Visibility</span>
            <span class="hero-tag">Data Validation</span>
        </div>

    </div>
""")


# ============================================================
# 2. QUANTITATIVE SNAPSHOT
# ============================================================

section_heading(
    "Project by the Numbers",
    "Evidence of project scale, placement experience, "
    "and the assignments represented in this portfolio."
)

render_grid("grid-4", [

    metric_card(
        BROADCAST_FRAMES_LABEL,
        "Broadcast Frame Outputs",
        "Scale of the Supercars exposure workflow."
    ),

    metric_card(
        PLACEMENT_HOURS_LABEL,
        "Internship Experience",
        "Approximate placement hours during September–November 2025."
    ),

    metric_card(
        str(EVENT_CONTEXT_COUNT),
        "Named Event Contexts",
        "Two motorsport and two marathon assignments."
    ),

    metric_card(
        str(ATHLETE_COUNT),
        "Athlete Monitoring Examples",
        f"Named examples across {SPORT_COUNT} sports."
    )
])

render_html("""
    <div class="evidence-note">
        <b>How to interpret these numbers:</b>
        The 160K+ figure describes the scale
        of broadcast frame outputs involved in
        the wider analysis workflow, not the
        number of frames I personally validated.
        Placement hours are approximate.
        Event and athlete counts refer to
        named work examples, not total
        company-wide project activity.
    </div>
""")


# ============================================================
# 3. PROJECT COVERAGE
# ============================================================

section_heading(
    "Industry Project Coverage",
    "Three principal analytics workstreams "
    "across broadcast exposure, events, and athletes."
)

render_grid("grid-3", [

    info_card(
        "Supercars · Motorsport",
        "Broadcast Brand Exposure",
        """
        Supported frame-level review,
        sponsor-logo organisation,
        visibility examples,
        and quality assurance
        for Supercars exposure outputs.
        """
    ),

    info_card(
        "Marathon Events",
        "Sponsorship Visibility",
        """
        Supported the organisation
        and checking of sponsorship
        exposure evidence involving
        the Sydney and Berlin marathons.
        """
    ),

    info_card(
        "Athlete Media Monitoring",
        "Media &amp; Fan Insights",
        """
        Tracked athlete-related media
        visibility and mentions, including
        work with TVEyes, to support
        brand and athlete insight reporting.
        """
    )
])


# ============================================================
# 4. EVENT EVIDENCE TABLE
# ============================================================

section_heading(
    "Event-Level Evidence",
    "Named event contexts and the types of "
    "analytical work involved."
)

event_rows = [
    [
        "Supercars",
        "The Bend",
        "Broadcast visibility and exposure-output QA"
    ],
    [
        "Supercars",
        "Bathurst",
        "Frame-level review and sponsor exposure examples"
    ],
    [
        "Marathon",
        "Sydney Marathon",
        "Sponsor visibility and event-media analysis"
    ],
    [
        "Marathon",
        "Berlin Marathon",
        "Exposure review and reporting support"
    ]
]

render_html(
    data_table(
        ["Sport / Series", "Event", "Analytical Focus"],
        event_rows
    )
)

render_html("""
    <div class="small-note">
        This table lists four named event contexts.
        It does not represent a complete inventory
        of all projects undertaken by the consultancy.
    </div>
""")


# ============================================================
# 5. ATHLETE MONITORING — NUMERICAL VIEW
# ============================================================

section_heading(
    "Athlete Media Monitoring",
    "Eight named athlete-monitoring examples "
    "across five sporting categories."
)

render_grid("grid-3", [

    metric_card(
        str(ATHLETE_COUNT),
        "Athlete Examples",
        "Named examples from media monitoring work."
    ),

    metric_card(
        str(SPORT_COUNT),
        "Sports Represented",
        "Basketball, tennis, baseball, American football, and soccer."
    ),

    metric_card(
        "3",
        "Basketball Examples",
        "Largest group among the eight named examples."
    )
])

# ------------------------------------------------------------
# CHART — ATHLETE EXAMPLES BY SPORT
# ------------------------------------------------------------

sport_names = list(athlete_groups.keys())
sport_counts = [
    len(names)
    for names in athlete_groups.values()
]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=sport_counts,
        y=sport_names,
        orientation="h",

        marker_color=[
            VIOLET, BLUE, CYAN, INDIGO, "#64748b"
        ],

        text=[
            str(count)
            for count in sport_counts
        ],

        textposition="outside",

        textfont=dict(
            size=14,
            color=TEXT_DARK
        ),

        hovertemplate=(
            "%{y}<br>"
            "Named athlete examples: %{x}"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    template="plotly_white",
    title=dict(
        text="Named athlete-monitoring examples by sport",
        font=dict(
            size=18,
            color=TEXT_DARK
        ),
        x=0.02
    ),

    height=390,
    margin=dict(l=25, r=45, t=80, b=45),

    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.45)",

    font=dict(
        family="Inter, Segoe UI, Arial, sans-serif",
        size=13,
        color=TEXT_MAIN
    ),

    xaxis=dict(
        title=dict(
            text="Number of named examples",
            font=dict(color=TEXT_MAIN, size=13)
        ),
        tickfont=dict(color=TEXT_MUTED, size=12),
        tickmode="linear",
        tick0=0,
        dtick=1,
        range=[0, 3.65],
        showgrid=True,
        gridcolor="rgba(148,163,184,0.20)",
        zeroline=False
    ),

    yaxis=dict(
        title=None,
        tickfont=dict(color=TEXT_DARK, size=12),
        autorange="reversed",
        showgrid=False,
        automargin=True
    ),

    showlegend=False,

    hoverlabel=dict(
        bgcolor="#ffffff",
        font=dict(color=TEXT_DARK, size=12)
    )
)

st.plotly_chart(
    fig,
    use_container_width=True,
    theme=None,
    config={
        "displayModeBar": False,
        "responsive": True
    }
)

render_html("""
    <div class="small-note">
        Chart values count named athlete
        examples only. They are not media
        mention volumes, impressions,
        sponsor exposure shares, or
        evidence of campaign performance.
    </div>
""")


# ============================================================
# 6. ATHLETE EXAMPLES TABLE
# ============================================================

section_heading(
    "Athlete Monitoring Examples",
    "Public athlete names representing "
    "the media-monitoring contexts."
)

athlete_rows = [
    [
        sport,
        str(len(names)),
        ", ".join(names)
    ]
    for sport, names in athlete_groups.items()
]

render_html(
    data_table(
        [
            "Sport",
            "Examples",
            "Athletes"
        ],
        athlete_rows
    )
)


# ============================================================
# 7. DATA ANALYTICS WORKFLOW
# ============================================================

section_heading(
    "My Analytics Workflow",
    "Four steps summarising how I contributed "
    "to preparing reliable commercial evidence."
)

render_grid("grid-4", [

    step_card(
        "01",
        "Collect &amp; Organise",
        """
        Worked with broadcast outputs,
        sponsor-logo references,
        event materials,
        and media-monitoring information.
        """
    ),

    step_card(
        "02",
        "Clean &amp; Validate",
        """
        Checked consistency,
        reviewed relevant brand appearances,
        and flagged unclear or
        potentially inaccurate outputs.
        """
    ),

    step_card(
        "03",
        "Structure &amp; Analyse",
        """
        Used Excel and analytical
        reporting tools to organise
        exposure information and
        support interpretation.
        """
    ),

    step_card(
        "04",
        "Support Reporting",
        """
        Prepared validated records,
        useful visibility examples,
        and analytical material
        for stakeholder-facing reporting.
        """
    )
])


# ============================================================
# 8. SPECIFIC CONTRIBUTIONS
# ============================================================

section_heading(
    "Specific Contributions",
    "Concrete work completed during "
    "the industry placement."
)

render_grid("grid-3", [

    info_card(
        "Excel &amp; Data Preparation",
        "Structured Sponsor-Exposure Data",
        """
        Organised sponsor-logo information
        and exposure outputs into
        more usable structured records,
        supporting review and reporting.
        """
    ),

    info_card(
        "Quality Assurance",
        "Reviewed Detection Quality",
        """
        Checked brand visibility examples
        for consistency, relevance,
        and potential detection issues
        before their use in reporting.
        """
    ),

    info_card(
        "Automation Support",
        "Prepared Logo Examples",
        """
        Helped collect and structure
        sponsor-logo references and
        exemplar data supporting
        automation-related workflows.
        """
    ),

    info_card(
        "Media Monitoring",
        "Tracked Athlete Coverage",
        """
        Worked with media-monitoring
        information, including TVEyes,
        to support athlete-related
        visibility and media insights.
        """
    ),

    info_card(
        "Commercial Reporting",
        "Supported Sponsorship Analysis",
        """
        Helped prepare evidence
        that analysts could use
        to interpret sponsor visibility
        and event exposure.
        """
    ),

    info_card(
        "Industry Collaboration",
        "Worked with Analytics Teams",
        """
        Contributed within a professional
        sports consultancy workflow,
        responding to feedback and
        practical reporting requirements.
        """
    )
])


# ============================================================
# 9. ANALYTICAL METRICS
# ============================================================

section_heading(
    "Commercial Analytics Framework",
    "Examples of useful sponsorship metrics "
    "and the evidence required to calculate them."
)

kpi_rows = [
    [
        "Sponsor appearance count",
        "Validated sponsor detections",
        "Indicates observed appearances in analysed media"
    ],
    [
        "Event-level exposure",
        "Event and broadcast references",
        "Compares visibility across events or coverage"
    ],
    [
        "Visibility exemplars",
        "Verified frames or clips",
        "Provides supporting evidence for reports"
    ],
    [
        "Athlete media mentions",
        "Monitoring records and search results",
        "Supports athlete-related media reporting"
    ],
    [
        "Exposure-data quality",
        "Manual checks and validation records",
        "Supports confidence in reported outputs"
    ]
]

render_html(
    data_table(
        [
            "Analytical Measure",
            "Required Evidence",
            "Commercial Use"
        ],
        kpi_rows
    )
)

render_html("""
    <div class="evidence-note">
        <b>Metric availability:</b>
        These are relevant measurement concepts,
        not additional claimed numerical results.
        Client-specific exposure counts, detection
        accuracy, audience impressions, sponsorship
        values, and return on investment are
        not reported here because verified,
        publicly shareable figures have not
        been provided.
    </div>
""")


# ============================================================
# 10. TOOLS & TECHNICAL SKILLS
# ============================================================

section_heading(
    "Tools & Technical Skills",
    "The practical analytics stack and "
    "methods used in the placement."
)

render_grid("grid-4", [

    info_card(
        "Spreadsheet Analytics",
        "Microsoft Excel",
        """
        Data cleaning, structuring,
        validation, formula-based
        checks, and reporting preparation.
        """
    ),

    info_card(
        "Business Intelligence",
        "Power BI",
        """
        Dashboard and visual
        reporting workflows
        supporting analytical
        communication.
        """
    ),

    info_card(
        "Media Intelligence",
        "TVEyes",
        """
        Media tracking and
        athlete-related monitoring
        for visibility and
        coverage analysis.
        """
    ),

    info_card(
        "Commercial Analytics",
        "Exposure &amp; Reporting",
        """
        Sponsor visibility,
        event analysis, QA,
        stakeholder reporting,
        and business interpretation.
        """
    )
])


# ============================================================
# 11. BUSINESS VALUE
# ============================================================

section_heading(
    "Business Value",
    "How the work contributed to "
    "practical sponsorship analytics."
)

render_html(
    highlight_panel(
        "From Raw Media Outputs to Reliable Reporting",
        """
        My contribution was focused on improving
        the <b>usability and reliability of
        sports media exposure evidence</b>.

        The work supported a broader analytics
        process covering more than
        <b>160,000 Supercars broadcast frame outputs</b>,
        event visibility work across named
        motorsport and marathon contexts,
        and athlete media-monitoring examples.

        By organising data, reviewing potential
        visibility errors, and preparing useful
        evidence, I supported the transformation
        of complex exposure outputs into
        material suitable for commercial
        interpretation and reporting.

        No independent revenue uplift,
        financial ROI, detection accuracy,
        or productivity improvement
        is claimed without verified evidence.
        """
    )
)


# ============================================================
# 12. PROFESSIONAL TAKEAWAYS
# ============================================================

section_heading(
    "What This Experience Demonstrates",
    "Capabilities relevant to Data Analyst, "
    "Business Analyst, and BI positions."
)

render_grid("grid-3", [

    info_card(
        "Real Industry Data",
        "Working with operational datasets",
        """
        Experience with substantial
        media exposure outputs and
        data that required practical
        checking rather than assuming
        every record was accurate.
        """
    ),

    info_card(
        "Business Context",
        "Understanding commercial questions",
        """
        Exposure data becomes useful
        when linked to clear questions
        about sponsor presence,
        event coverage, and brand value.
        """
    ),

    info_card(
        "Analytical Communication",
        "Supporting stakeholder-ready evidence",
        """
        Developed experience making
        complex source material
        more structured, traceable,
        and suitable for professional
        reporting.
        """
    )
])


# ============================================================
# 13. FINAL NOTE
# ============================================================

render_html("""
    <div class="evidence-note">
        <b>Portfolio evidence policy:</b>
        This page summarises internship assignments
        and named work examples. Quantitative claims
        reflect available project context.
        Confidential client data and unverified
        sponsorship-performance metrics
        are intentionally excluded.
    </div>
""")

st.write("")

st.page_link(
    "Home.py",
    label="← Back to Portfolio Home"
)
