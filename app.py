
import html
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="E-Waste Intelligence", page_icon="◎", layout="wide", initial_sidebar_state="collapsed")

DATA_FILE = Path(__file__).parent / "e-waste_data_2022_complete.csv"
GENERATED = "E-Waste Generated (Kt)"
RECYCLED = "E-Waste Recycled (Kt)"
RATE = "Recycling Rate (%)"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#e9f2ef; --muted:#8b9b9b; --line:rgba(220,245,237,.12); --glass:rgba(255,255,255,.045); --glass-hi:rgba(255,255,255,.075); --green:#7de2a3; --cyan:#62d9e6; --amber:#f1bd72; --red:#ef8e82; }
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
.stApp { color:var(--ink); background:#07100f; font-family:'Manrope',sans-serif; background-image:radial-gradient(circle at 78% 8%,rgba(27,126,120,.18),transparent 29%),radial-gradient(circle at 5% 35%,rgba(68,147,84,.14),transparent 25%),linear-gradient(rgba(130,210,187,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(130,210,187,.025) 1px,transparent 1px); background-size:auto,auto,48px 48px,48px 48px; }
.stApp:before { content:''; position:fixed; inset:-20%; pointer-events:none; background:radial-gradient(ellipse,rgba(75,177,119,.08),transparent 42%); filter:blur(40px); animation:drift 18s ease-in-out infinite alternate; }
@keyframes drift { to { transform:translate(5%,3%) scale(1.08); } }
.block-container { max-width:1600px; padding:2.5rem 4.5rem 5rem; position:relative; }
header[data-testid="stHeader"] { background:transparent!important; pointer-events:none!important; z-index:1!important; }
[data-testid="stToolbar"] { display:none!important; }
.anchor { scroll-margin-top:110px; }
.top-nav { width:94%; max-width:1420px; margin:0 auto 22px; padding:10px 13px 10px 19px; display:flex; align-items:center; justify-content:space-between; gap:20px; position:fixed; top:15px; left:50%; transform:translateX(-50%); z-index:100; background:rgba(10,25,23,.76); border:1px solid rgba(255,255,255,.1); border-radius:18px; box-shadow:0 12px 40px rgba(0,0,0,.25); backdrop-filter:blur(20px); }
.top-nav + .anchor { display:block; height:70px; }
.brand { display:flex; align-items:center; gap:10px; color:var(--ink); font:500 .69rem 'DM Mono',monospace; letter-spacing:.1em; white-space:nowrap; }.brand strong { color:#f4fbf7; font-weight:500; }.brand small { color:var(--muted); border-left:1px solid var(--line); padding-left:10px; }.status-dot { width:6px; height:6px; background:var(--green); border-radius:50%; box-shadow:0 0 11px var(--green); }
.nav-links { display:flex; align-items:center; gap:3px; }.nav-links a, .mobile-menu a { color:var(--muted); text-decoration:none; font:500 .64rem 'DM Mono',monospace; letter-spacing:.08em; padding:9px 11px; border-radius:8px; transition:background .2s,color .2s,box-shadow .2s; }.nav-links a:hover, .nav-links a:focus, .mobile-menu a:hover, .mobile-menu a:focus { color:var(--ink); background:rgba(125,226,163,.13); box-shadow:0 0 18px rgba(98,217,230,.08); outline:none; }.nav-links a span { color:rgba(98,217,230,.7); margin-right:4px; }.mobile-menu { display:none; }
[data-baseweb="select"] > div, [data-testid="stSlider"] { background:var(--glass)!important; border-color:var(--line)!important; }
[data-baseweb="select"] * { color:var(--ink)!important; }
[data-baseweb="tag"] { background:rgba(125,226,163,.16)!important; border:1px solid rgba(125,226,163,.28)!important; border-radius:5px!important; }
[data-baseweb="tag"] span { color:var(--green)!important; }
[data-baseweb="tag"] svg { fill:var(--green)!important; }
[data-testid="stSlider"] [role="slider"] { background:var(--green)!important; border-color:var(--green)!important; }
[data-testid="stSlider"] [data-testid="stTickBar"] > div { background:var(--green)!important; }
.st-key-control-bar [data-baseweb="slider"] > div > div { background:var(--green)!important; }
button[kind="secondary"], [data-testid="stDownloadButton"] button { color:var(--ink)!important; background:var(--glass)!important; border:1px solid var(--line)!important; }
.metadata { display:flex; gap:13px; align-items:center; margin:18px 3px 0; color:var(--muted); font:500 .68rem 'DM Mono',monospace; letter-spacing:.14em; text-transform:uppercase; }
.metadata span { color:var(--green); }.metadata b { color:rgba(220,245,237,.35); font-weight:400; }
.st-key-control-bar { margin-top:29px; padding:22px 25px 20px; position:sticky; top:12px; z-index:10; background:rgba(15,30,27,.84); border:1px solid var(--line); border-radius:20px; box-shadow:0 20px 60px rgba(0,0,0,.25); backdrop-filter:blur(20px); }
.control-title { display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; }.control-title h3 { margin:0; font-size:.82rem; letter-spacing:.08em; text-transform:uppercase; }.control-title .micro { color:var(--green); }
.st-key-control-bar [data-testid="stMultiSelect"] [data-baseweb="tag"] { display:none!important; }.st-key-control-bar [data-testid="stMultiSelect"] input { color:var(--ink)!important; }.st-key-control-bar [data-testid="stMultiSelect"] > div { min-height:42px; }
.st-key-control-bar [data-testid="stRadio"] > div { gap:5px; }.st-key-control-bar [data-testid="stRadio"] label { border:1px solid transparent; border-radius:8px; padding:7px 10px; transition:background .2s,border .2s; }.st-key-control-bar [data-testid="stRadio"] label:hover { background:var(--glass-hi); border-color:var(--line); }.st-key-control-bar [data-testid="stRadio"] label:has(input:checked) { background:rgba(125,226,163,.13); border-color:rgba(125,226,163,.25); }.st-key-control-bar [data-testid="stRadio"] label p { font:500 .66rem 'DM Mono',monospace; color:var(--muted); letter-spacing:.04em; }.st-key-control-bar [data-testid="stRadio"] label:has(input:checked) p { color:var(--green); }
.control-actions { display:flex; gap:8px; margin-top:7px; }.control-actions button { min-height:28px!important; padding:3px 9px!important; font-size:.64rem!important; }
.hero, .glass { background:var(--glass); border:1px solid var(--line); border-radius:22px; box-shadow:0 24px 70px rgba(0,0,0,.24); backdrop-filter:blur(22px); }
.hero { min-height:390px; padding:44px 48px; display:flex; align-items:center; overflow:hidden; position:relative; animation:rise .7s ease both; }
.hero-copy { width:57%; position:relative; z-index:1; }
.eyebrow, .micro { color:var(--cyan); font:500 .68rem 'DM Mono',monospace; letter-spacing:.16em; text-transform:uppercase; }
.hero h1 { font-size:clamp(3.5rem,7vw,7.6rem); line-height:.88; letter-spacing:-.08em; margin:18px 0 24px; max-width:700px; }
.hero p { color:#b0c0bc; font-size:1rem; line-height:1.7; max-width:480px; }
.hero-orbit { position:absolute; right:7%; top:12%; width:310px; height:310px; border:1px solid rgba(98,217,230,.28); border-radius:50%; box-shadow:0 0 70px rgba(98,217,230,.09); }
.hero-orbit:before,.hero-orbit:after { content:''; position:absolute; inset:17%; border:1px solid rgba(125,226,163,.24); border-radius:50%; transform:rotate(55deg) scaleX(1.5); }
.hero-orbit:after { inset:35% -7%; transform:rotate(-35deg); }
.particle { position:absolute; width:7px; height:7px; border-radius:50%; background:var(--green); box-shadow:0 0 18px var(--green); }
.p1 { top:14%; left:54%; }.p2 { top:65%; left:20%; background:var(--cyan); box-shadow:0 0 18px var(--cyan); }.p3 { top:48%; right:2%; background:var(--amber); box-shadow:0 0 18px var(--amber); }.p4 { bottom:9%; left:52%; }
.hero-grid { position:absolute; right:0; bottom:0; width:46%; height:38%; opacity:.26; background:linear-gradient(rgba(98,217,230,.25) 1px,transparent 1px),linear-gradient(90deg,rgba(98,217,230,.25) 1px,transparent 1px); background-size:27px 27px; mask-image:linear-gradient(90deg,transparent,black); }
@keyframes rise { from { opacity:0; transform:translateY(14px); } to { opacity:1; transform:none; } }
.section-kicker { margin:68px 0 20px; display:flex; align-items:end; gap:17px; }
.section-kicker .number { color:var(--cyan); font:500 .75rem 'DM Mono',monospace; }
.section-kicker h2 { font-size:clamp(1.8rem,3vw,3rem); letter-spacing:-.07em; margin:0; }
.section-kicker p { color:var(--muted); margin:0 0 4px 10px; font-size:.88rem; }
.kpi { padding:25px 24px 22px; min-height:157px; transition:transform .3s,border .3s; position:relative; overflow:hidden; }
.kpi:hover,.glass:hover { transform:translateY(-3px); border-color:rgba(220,245,237,.23); }
.kpi:after { content:''; position:absolute; left:24px; bottom:15px; width:48px; height:2px; background:var(--cyan); box-shadow:20px 0 0 rgba(98,217,230,.35),35px 0 0 rgba(98,217,230,.18); }
.kpi.green:after { background:var(--green); box-shadow:20px 0 0 rgba(125,226,163,.35),35px 0 0 rgba(125,226,163,.18); }
.label { color:var(--muted); font:500 .67rem 'DM Mono',monospace; letter-spacing:.14em; text-transform:uppercase; }
.value { font-size:clamp(1.65rem,2.8vw,2.6rem); font-weight:700; letter-spacing:-.07em; margin:16px 0 7px; white-space:nowrap; }
.sub { color:#80928f; font-size:.74rem; }
.story { padding:32px 36px; border-left:2px solid var(--green); margin-top:22px; }
.story .statement { font-size:clamp(1.3rem,2.5vw,2.4rem); letter-spacing:-.06em; line-height:1.1; max-width:900px; }
.story strong { color:var(--green); }
.chart-panel { padding:25px 27px 13px; }
.panel-heading { display:flex; justify-content:space-between; align-items:start; gap:1rem; }
.panel-heading h3 { margin:0 0 5px; font-size:1.15rem; letter-spacing:-.04em; }
.panel-heading p { color:var(--muted); font-size:.78rem; margin:0; }
.leaderboard { padding:8px 18px 14px; }
.rank-row { display:grid; grid-template-columns:38px minmax(130px,1.6fr) 1fr 86px 86px; gap:14px; align-items:center; padding:15px 10px; border-bottom:1px solid rgba(220,245,237,.07); transition:background .25s,transform .25s; }
.rank-row:hover { background:var(--glass-hi); transform:translateX(3px); border-radius:9px; }
.rank-row.top { color:#f7fff9; }.rank { color:var(--muted); font:500 .7rem 'DM Mono',monospace; }.country { font-weight:700; font-size:.9rem; }.bar { height:5px; background:rgba(255,255,255,.08); border-radius:5px; overflow:hidden; }.bar span { display:block; height:100%; width:var(--rate); background:linear-gradient(90deg,var(--green),var(--cyan)); border-radius:5px; animation:grow .8s ease both; transform-origin:left; }.rate { color:var(--green); font:500 .9rem 'DM Mono',monospace; text-align:right; }.row-stat { color:var(--muted); font:400 .68rem 'DM Mono',monospace; text-align:right; }
@keyframes grow { from { transform:scaleX(0); } to { transform:scaleX(1); } }
.leader { padding:31px; min-height:275px; border-color:rgba(125,226,163,.25); box-shadow:0 0 60px rgba(66,177,106,.11),0 24px 70px rgba(0,0,0,.24); }.leader .country-name { font-size:clamp(2rem,4vw,4rem); letter-spacing:-.09em; line-height:1; margin:16px 0 4px; }.leader-rate { color:var(--green); font:500 3.1rem 'DM Mono',monospace; }.ring { float:right; width:116px; height:116px; border-radius:50%; display:grid; place-items:center; background:conic-gradient(var(--green) calc(var(--rate) * 1%),rgba(125,226,163,.1) 0); }.ring:after { content:''; position:absolute; width:91px; height:91px; border-radius:50%; background:#0d1a17; }.ring b { position:relative; z-index:1; font:500 .85rem 'DM Mono',monospace; }
.insight { padding:20px 22px; margin-bottom:12px; border-left:2px solid var(--cyan); }.insight.win { border-color:var(--green); }.insight.warn { border-color:var(--amber); }.insight h4 { font:500 .68rem 'DM Mono',monospace; color:var(--cyan); letter-spacing:.13em; margin:0 0 9px; }.insight.win h4{color:var(--green)}.insight.warn h4{color:var(--amber)}.insight p { color:#c3d0cc; font-size:.82rem; line-height:1.5; margin:0; }
.versus { text-align:center; display:grid; place-items:center; min-height:275px; }.versus strong { color:var(--cyan); font:500 1.5rem 'DM Mono',monospace; }.face { padding:28px; min-height:275px; }.face .country-name { font-size:2rem; font-weight:800; letter-spacing:-.08em; }.face .face-rate { color:var(--green); font:500 2.2rem 'DM Mono',monospace; margin:17px 0; }.face li { display:flex; justify-content:space-between; color:var(--muted); font-size:.75rem; padding:6px 0; border-bottom:1px solid rgba(255,255,255,.07); }.face li b { color:var(--ink); font-family:'DM Mono',monospace; font-weight:400; }
.data-note { color:var(--muted); font-size:.75rem; line-height:1.7; }.footer { border-top:1px solid var(--line); margin-top:75px; padding-top:22px; color:var(--muted); font:500 .68rem 'DM Mono',monospace; display:flex; justify-content:space-between; }
@media (max-width:800px) { .block-container{padding:1.5rem 1rem 3rem}.top-nav{width:100%;margin-bottom:18px;padding:10px 11px 10px 14px;top:7px}.top-nav + .anchor{height:58px}.brand{font-size:.6rem;gap:7px}.brand small{display:none}.nav-links{display:none}.mobile-menu{display:block;position:relative}.mobile-menu summary{list-style:none;cursor:pointer;color:var(--green);font:500 .65rem 'DM Mono',monospace;letter-spacing:.1em;padding:9px 8px}.mobile-menu summary::-webkit-details-marker{display:none}.mobile-menu[open] summary{background:var(--glass-hi);border-radius:8px}.mobile-menu nav{position:absolute;right:0;top:42px;display:grid;gap:3px;min-width:165px;padding:8px;background:rgba(10,25,23,.95);border:1px solid var(--line);border-radius:12px;box-shadow:0 16px 45px rgba(0,0,0,.35);backdrop-filter:blur(20px)}.mobile-menu a{display:block}.mobile-menu a span{color:rgba(98,217,230,.7);margin-right:5px}.hero{min-height:520px;padding:29px 25px;align-items:start}.hero-copy{width:100%}.hero h1{font-size:3.7rem}.hero-orbit{top:54%;right:10%;width:230px;height:230px}.hero-grid{width:100%;height:36%}.metadata{gap:8px;font-size:.59rem;flex-wrap:wrap}.control-bar{top:5px;padding:18px 16px}.control-title{margin-bottom:11px}.rank-row{grid-template-columns:27px 1fr 70px}.rank-row .row-stat{display:none}.leader{min-height:300px}.ring{width:92px;height:92px}.ring:after{width:71px;height:71px}.section-kicker{margin-top:45px;display:block}.section-kicker p{margin:7px 0 0}.footer{display:block;line-height:2.2} }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_FILE)
    data.columns = [column.strip() for column in data.columns]
    for column in [GENERATED, RECYCLED, RATE]:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data["Country"] = data["Country"].astype(str).str.strip()
    data["Year"] = pd.to_numeric(data["Year"], errors="coerce").astype("Int64")
    return data

def safe(value):
    return html.escape(str(value))

def fmt(value):
    return f"{value:,.1f}"

def section(number, title, subtitle):
    st.markdown(f'<div class="section-kicker"><span class="number">{number}</span><h2>{title}</h2><p>{subtitle}</p></div>', unsafe_allow_html=True)

def chart_layout(fig, height=430):
    fig.update_layout(template="plotly_dark", height=height, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Manrope", color="#aebdb8", size=11), margin=dict(l=8,r=8,t=18,b=12), legend=dict(orientation="h", y=1.08, x=0, bgcolor="rgba(0,0,0,0)"), hoverlabel=dict(bgcolor="#12221f", bordercolor="#5b9f8e", font=dict(family="DM Mono")))
    fig.update_xaxes(showgrid=True, gridcolor="rgba(170,220,205,.08)", zeroline=False, linecolor="rgba(220,245,237,.12)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(170,220,205,.08)", zeroline=False, linecolor="rgba(220,245,237,.12)")
    return fig

df = load_data()
countries = sorted(df["Country"].unique().tolist())
max_rate = float(df[RATE].max())

def select_all_countries():
    st.session_state.country_filter = countries

def clear_countries():
    st.session_state.country_filter = []

if "country_filter" not in st.session_state:
    st.session_state.country_filter = countries

st.markdown('''<nav class="top-nav" aria-label="Primary navigation"><div class="brand"><i class="status-dot"></i><span>♻ <strong>E-WASTE INTELLIGENCE</strong></span><small>2022</small></div><div class="nav-links"><a href="#overview"><span>01</span>OVERVIEW</a><a href="#rankings"><span>02</span>RANKINGS</a><a href="#analysis"><span>03</span>ANALYSIS</a><a href="#compare"><span>04</span>COMPARE</a><a href="#data"><span>05</span>DATA</a></div><details class="mobile-menu"><summary>MENU ≡</summary><nav><a href="#overview"><span>01</span>OVERVIEW</a><a href="#rankings"><span>02</span>RANKINGS</a><a href="#analysis"><span>03</span>ANALYSIS</a><a href="#compare"><span>04</span>COMPARE</a><a href="#data"><span>05</span>DATA</a></nav></details></nav>''', unsafe_allow_html=True)
st.markdown('<div id="overview" class="anchor"></div>', unsafe_allow_html=True)
st.markdown('''<div class="hero"><div class="hero-copy"><div class="eyebrow">2022 / E-WASTE INTELLIGENCE</div><h1>WHO'S<br>ACTUALLY<br>RECYCLING?</h1><p>20 countries. One dataset. A closer look at where electronic waste ends up, and who turns the problem into progress.</p><div class="micro" style="margin-top:30px">DATASET / GLOBAL COMPARISON / 20 COUNTRIES</div></div><div class="hero-grid"></div><div class="hero-orbit"><i class="particle p1"></i><i class="particle p2"></i><i class="particle p3"></i><i class="particle p4"></i></div></div>''', unsafe_allow_html=True)

st.markdown('<div class="metadata"><span>2022 DATASET</span><b>•</b><span>20 COUNTRIES</span><b>•</b><span>KILOTONNES</span></div>', unsafe_allow_html=True)
with st.container(key="control-bar"):
    st.markdown('<div class="control-title"><h3>Explore data</h3><span class="micro">FILTERS / OPTIONAL</span></div>', unsafe_allow_html=True)
    control_columns = st.columns([1.35, 1.1, 1.4])
    with control_columns[0]:
        selected = st.multiselect(f"Countries · {len(st.session_state.country_filter)} selected", countries, key="country_filter", placeholder="Search countries...")
        action_cols = st.columns(2)
        with action_cols[0]: st.button("Select all", on_click=select_all_countries, width="stretch")
        with action_cols[1]: st.button("Clear all", on_click=clear_countries, width="stretch")
    with control_columns[1]:
        rate_range = st.slider("Recycling rate", 0.0, max_rate, (0.0, max_rate), 0.5, format="%.0f%%")
    with control_columns[2]:
        view = st.radio("Sort by", [RATE, GENERATED, RECYCLED], horizontal=True, format_func=lambda x: {RATE:"Rate", GENERATED:"Generated", RECYCLED:"Recycled"}[x])

filtered = df[df["Country"].isin(selected) & df[RATE].between(rate_range[0], rate_range[1])].copy()

if filtered.empty:
    st.error("No countries match these controls. Widen the country or rate selection.")
    st.stop()

total_generated, total_recycled = filtered[GENERATED].sum(), filtered[RECYCLED].sum()
overall_rate = total_recycled / total_generated * 100 if total_generated else 0
best = filtered.loc[filtered[RATE].idxmax()]
largest = filtered.loc[filtered[GENERATED].idxmax()]
worst = filtered.loc[filtered[RATE].idxmin()]

section("01", "THE SCALE", "The first signal is volume.")
st.markdown(f'<div class="glass story"><div class="eyebrow">THE BIGGEST GENERATOR ISN’T THE BEST RECYCLER</div><div class="statement"><strong>{safe(largest["Country"])}</strong> generated <strong>{fmt(largest[GENERATED])} Kt</strong> of e-waste, yet its reported recycling rate is <strong>{largest[RATE]:.1f}%</strong>.</div></div>', unsafe_allow_html=True)
kpis = [("TOTAL GENERATED", f"{fmt(total_generated)} Kt", "Across current selection", ""), ("TOTAL RECYCLED", f"{fmt(total_recycled)} Kt", "Material recovered", "green"), ("WEIGHTED RATE", f"{overall_rate:.1f}%", "Recycled ÷ generated", "green"), ("TOP PERFORMER", safe(best["Country"]), f"{best[RATE]:.1f}% recycling rate", "green")]
cols = st.columns(4)
for col, (label, value, sub, accent) in zip(cols, kpis):
    with col:
        st.markdown(f'<div class="glass kpi {accent}"><div class="label">{label}</div><div class="value">{value}</div><div class="sub">{sub}</div></div>', unsafe_allow_html=True)

st.markdown('<div id="rankings" class="anchor"></div>', unsafe_allow_html=True)
section("02", "THE LEADERS", "Ranking efficiency, not just size.")
ranked = filtered.sort_values(view, ascending=False).reset_index(drop=True)
rows = []
for index, row in ranked.iterrows():
    top = " top" if index < 3 else ""
    rows.append(f'<div class="rank-row{top}"><span class="rank">{index + 1:02d}</span><span class="country">{safe(row["Country"])}</span><span class="bar"><span style="--rate:{min(float(row[RATE]),100)}%"></span></span><span class="rate">{row[RATE]:.1f}%</span><span class="row-stat">{fmt(row[GENERATED])} Kt</span></div>')
st.markdown('<div class="glass leaderboard"><div class="panel-heading"><div><h3>THE RECYCLING LEADERBOARD</h3><p>Hover a row to inspect its position in the field.</p></div><span class="micro">SORT / '+safe({RATE:"RATE",GENERATED:"GENERATED",RECYCLED:"RECYCLED"}[view])+'</span></div>'+''.join(rows)+'</div>', unsafe_allow_html=True)
leader_col, lag_col = st.columns(2)
with leader_col:
    st.markdown(f'<div class="glass leader"><div class="label">THE LEADER</div><div class="ring" style="--rate:{best[RATE]}"><b>{best[RATE]:.1f}%</b></div><div class="country-name">{safe(best["Country"])}</div><div class="leader-rate">{best[RATE]:.1f}%</div><div class="sub">recycling rate · {fmt(best[RECYCLED])} Kt recovered</div></div>', unsafe_allow_html=True)
with lag_col:
    st.markdown('<div class="glass" style="padding:27px 30px;min-height:275px"><div class="label">LEADERS / PROBLEM AREAS</div><div style="display:flex;gap:34px;margin-top:23px"><div><div class="micro">TOP 5</div><div style="line-height:1.9;margin-top:8px">' + '<br>'.join(f'<b>{safe(row["Country"])}</b> <span class="rate">{row[RATE]:.1f}%</span>' for _, row in filtered.nlargest(5, RATE).iterrows()) + '</div></div><div><div class="micro" style="color:var(--amber)">BOTTOM 5</div><div style="line-height:1.9;margin-top:8px">' + '<br>'.join(f'<b>{safe(row["Country"])}</b> <span style="color:var(--amber);font:500 .8rem \'DM Mono\'">{row[RATE]:.1f}%</span>' for _, row in filtered.nsmallest(5, RATE).iterrows()) + '</div></div></div></div>', unsafe_allow_html=True)

st.markdown('<div id="analysis" class="anchor"></div>', unsafe_allow_html=True)
section("03", "THE GAP", "High generation doesn’t necessarily mean high recycling.")
chart_cols = st.columns(2)
with chart_cols[0]:
    st.markdown('<div class="glass chart-panel"><div class="panel-heading"><div><h3>GENERATED ≠ RECYCLED</h3><p>Compare the scale of the problem.</p></div><span class="micro">KT / COUNTRY</span></div>', unsafe_allow_html=True)
    volume = filtered.sort_values(GENERATED, ascending=False)
    fig = go.Figure([go.Bar(x=volume["Country"], y=volume[GENERATED], name="Generated", marker_color="rgba(218,230,224,.65)"), go.Bar(x=volume["Country"], y=volume[RECYCLED], name="Recycled", marker_color="#7de2a3")])
    fig.update_layout(barmode="group", xaxis_title=None, yaxis_title="Kt", xaxis_tickangle=-45)
    st.plotly_chart(chart_layout(fig, 400), width="stretch", config={"displayModeBar":False})
    st.markdown('</div>', unsafe_allow_html=True)
with chart_cols[1]:
    st.markdown('<div class="glass chart-panel"><div class="panel-heading"><div><h3>THE RECYCLING GAP</h3><p>Generation on one axis. Recovery on the other.</p></div><span class="micro">SIGNAL MAP</span></div>', unsafe_allow_html=True)
    fig = go.Figure(go.Scatter(x=filtered[GENERATED], y=filtered[RATE], mode="markers+text", text=filtered["Country"], textposition="top center", marker=dict(size=(filtered[RECYCLED].clip(lower=5) ** .5) * 2.2, color=filtered[RATE], colorscale=[[0,"#ef8e82"],[.45,"#f1bd72"],[1,"#7de2a3"]], line=dict(width=1,color="#d8fff0"), opacity=.9), customdata=filtered[["Country",GENERATED,RECYCLED,RATE]], hovertemplate="<b>%{customdata[0]}</b><br>Generated: %{customdata[1]:,.1f} Kt<br>Recycled: %{customdata[2]:,.1f} Kt<br>Rate: %{customdata[3]:.1f}%<extra></extra>"))
    fig.add_hline(y=filtered[RATE].median(), line_dash="dot", line_color="rgba(98,217,230,.35)"); fig.add_vline(x=filtered[GENERATED].median(), line_dash="dot", line_color="rgba(98,217,230,.35)")
    fig.update_layout(xaxis_title="E-waste generated (Kt)", yaxis_title="Recycling rate (%)")
    st.plotly_chart(chart_layout(fig, 400), width="stretch", config={"displayModeBar":False})
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="compare" class="anchor"></div>', unsafe_allow_html=True)
section("04", "THE FACE-OFF", "Two countries. One efficiency question.")
compare_cols = st.columns([1, .22, 1])
default_a = "India" if "India" in countries else countries[0]; default_b = "Germany" if "Germany" in countries else countries[1]
with compare_cols[0]: country_a = st.selectbox("Country A", countries, index=countries.index(default_a), key="country_a")
with compare_cols[1]: st.markdown('<div class="versus"><strong>VS</strong></div>', unsafe_allow_html=True)
with compare_cols[2]: country_b = st.selectbox("Country B", countries, index=countries.index(default_b), key="country_b")
row_a, row_b = df[df["Country"] == country_a].iloc[0], df[df["Country"] == country_b].iloc[0]
face_a, face_b = st.columns([1,1])
for col, row in [(face_a,row_a),(face_b,row_b)]:
    with col: st.markdown(f'<div class="glass face"><div class="label">COUNTRY PROFILE</div><div class="country-name">{safe(row["Country"])}</div><div class="face-rate">{row[RATE]:.1f}%</div><div class="label">RECYCLING RATE</div><ul style="list-style:none;padding:13px 0 0;margin:0"><li>Generated <b>{fmt(row[GENERATED])} Kt</b></li><li>Recycled <b>{fmt(row[RECYCLED])} Kt</b></li></ul></div>', unsafe_allow_html=True)
winner = row_a["Country"] if row_a[RATE] >= row_b[RATE] else row_b["Country"]
st.markdown(f'<div class="micro" style="text-align:center;margin-top:18px">WINNER IN RECYCLING EFFICIENCY / <span style="color:var(--green)">{safe(winner)}</span></div>', unsafe_allow_html=True)

section("05", "WHAT THE DATA SAYS", "Signals generated from the selected countries.")
largest_recycled = filtered.loc[filtered[RECYCLED].idxmax()]
insights = [("WIN", f"{best['Country']} leads the current field with a {best[RATE]:.1f}% reported recycling rate."), ("DISCOVERY", f"{largest['Country']} produces the most e-waste at {fmt(largest[GENERATED])} Kt, but sits at {largest[RATE]:.1f}% recycling."), ("COMPARISON", f"{largest_recycled['Country']} recycles the most material by volume: {fmt(largest_recycled[RECYCLED])} Kt."), ("WARNING", f"{worst['Country']} is the current low signal at {worst[RATE]:.1f}% recycling rate.")]
insight_cols = st.columns(2)
for index, (kind, text) in enumerate(insights):
    with insight_cols[index % 2]: st.markdown(f'<div class="glass insight {"win" if kind == "WIN" else "warn" if kind == "WARNING" else ""}"><h4>{kind} / DATA SIGNAL</h4><p>{safe(text)}</p></div>', unsafe_allow_html=True)

st.markdown('<div id="data" class="anchor"></div>', unsafe_allow_html=True)
section("06", "DATA EXPLORER", "Inspect and download the filtered source rows.")
with st.expander("EXPLORE THE RAW DATA"):
    st.dataframe(filtered.sort_values(RATE, ascending=False), width="stretch", hide_index=True)
    st.download_button("Download selected CSV", filtered.to_csv(index=False), "ewaste_2022_selection.csv", "text/csv")

st.markdown('<div class="footer"><span>E-WASTE RECYCLING INTELLIGENCE / 2022 DATASET</span><span>Generated from the supplied country-level dataset · Kt = kilotonnes</span></div>', unsafe_allow_html=True)
