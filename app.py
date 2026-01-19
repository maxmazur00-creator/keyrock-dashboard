import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(
    page_title="Keyrock 2026 - 12 Charts Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1a1d29; padding: 15px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

def create_chart(df, title, y_col, color='#3b82f6'):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'], y=df[y_col],
        mode='lines', name=y_col,
        line=dict(color=color, width=2),
        fill='tonexty'
    ))
    fig.update_layout(
        title=title,
        template="plotly_dark",
        height=400,
        plot_bgcolor='#1a1d29',
        paper_bgcolor='#1a1d29'
    )
    return fig

def create_stacked_chart(df, title, columns):
    fig = go.Figure()
    colors = ['#3b82f6', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981']
    for i, col in enumerate(columns):
        fig.add_trace(go.Scatter(
            x=df['date'], y=df[col],
            mode='lines', name=col,
            stackgroup='one',
            fillcolor=colors[i % len(colors)]
        ))
    fig.update_layout(
        title=title,
        template="plotly_dark",
        height=400,
        plot_bgcolor='#1a1d29',
        paper_bgcolor='#1a1d29'
    )
    return fig

# Data functions
def get_prediction_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'sports': [50 + i * 2 for i in range(90)],
        'economics': [30 + i * 1.5 for i in range(90)],
        'tech_science': [20 + i for i in range(90)],
        'politics': [40 + i * 1.8 for i in range(90)]
    })

def get_rwa_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'yield_bearing': [2000 + i * 50 for i in range(90)],
        'private_credit': [1500 + i * 40 for i in range(90)],
        'tokenised_equities': [1000 + i * 30 for i in range(90)]
    })

def get_x402_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({'date': dates, 'volume': [100 + i * 5 for i in range(90)]})

def get_vault_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'Morpho': [3000 + i * 40 for i in range(90)],
        'Euler': [2500 + i * 35 for i in range(90)],
        'Yearn': [2000 + i * 25 for i in range(90)]
    })

def get_perp_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'Hyperliquid': [1500 + i * 30 for i in range(90)],
        'Aster': [800 + i * 20 for i in range(90)]
    })

def get_buyback_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({'date': dates, 'cumulative': [500 + i * 8 for i in range(90)]})

def get_mev_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({'date': dates, 'jito_tips': [50000 + i * 1000 for i in range(90)]})

def get_zec_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({'date': dates, 'shielded_pct': [42 + (i % 20) * 0.1 for i in range(90)]})

def get_blob_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'blob_fee': [0.015 + (i % 15) * 0.002 for i in range(90)],
        'calldata': [0.05 + (i % 10) * 0.003 for i in range(90)]
    })

def get_cards_data():
    dates = pd.date_range(end=datetime.now(), periods=30, freq='W')
    return pd.DataFrame({'date': dates, 'volume': [150 + i * 10 for i in range(30)]})

def get_etf_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'BlackRock': [400000 + i * 2000 for i in range(90)],
        'Fidelity': [300000 + i * 1500 for i in range(90)]
    })

def get_rates_data():
    dates = pd.date_range(end=datetime.now(), periods=90, freq='D')
    return pd.DataFrame({
        'date': dates,
        'borrow_apy': [7 + (i % 20) * 0.3 for i in range(90)]
    })

# Main app
with st.sidebar:
    st.title("📊 Keyrock 2026")
    st.caption("12 Charts to Watch")
    st.markdown("---")
    
    page = st.radio("", [
        "🏠 Dashboard Home",
        "1️⃣ Prediction Markets",
        "2️⃣ RWA Tokenisation",
        "3️⃣ x402 Volume",
        "4️⃣ Vault AUM",
        "5️⃣ Perp Futures OI",
        "6️⃣ Buyback Activity",
        "7️⃣ Solana MEV",
        "8️⃣ Shielded ZEC",
        "9️⃣ Blob Fees",
        "🔟 Crypto Cards",
        "1️⃣1️⃣ BTC ETF AUM",
        "1️⃣2️⃣ Stablecoin Rates"
    ])
    
    st.markdown("---")
    st.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')}")

if "🏠" in page:
    st.title("Dashboard Overview")
    st.caption("Real-time monitoring of 12 key crypto metrics for 2026")
    
    cols = st.columns(3)
    metrics = [
        ("Prediction Markets", "$2.4B", "+12.3%"),
        ("RWA Tokenisation", "$8.2B", "+5.7%"),
        ("x402 Volume", "$145M", "+28.4%"),
        ("Vault AUM", "$12.8B", "+3.2%"),
        ("Perp Futures OI", "$4.6B", "+15.8%"),
        ("Buyback Activity", "$890M", "+7.1%"),
        ("Solana MEV", "2.4M SOL", "+9.3%"),
        ("Shielded ZEC", "42.3%", "-1.2%"),
        ("Blob Fees", "0.023 ETH", "-4.5%"),
        ("Crypto Cards", "$234M", "+18.7%"),
        ("BTC ETF AUM", "1.2M BTC", "+6.4%"),
        ("Stablecoin Rates", "8.45%", "+0.3%")
    ]
    
    for idx, (name, value, change) in enumerate(metrics):
        with cols[idx % 3]:
            st.metric(name, value, change)

elif "1️⃣ Prediction" in page:
    st.title("Prediction Market Volumes by Market-Type")
    st.caption("Weekly total prediction market trading volume")
    df = get_prediction_data()
    fig = create_stacked_chart(df, "Market Volume", ['sports', 'economics', 'tech_science', 'politics'])
    st.plotly_chart(fig, use_container_width=True)

elif "2️⃣ RWA" in page:
    st.title("RWA Onchain Tokenisation AUM")
    df = get_rwa_data()
    fig = create_stacked_chart(df, "RWA AUM", ['yield_bearing', 'private_credit', 'tokenised_equities'])
    st.plotly_chart(fig, use_container_width=True)

elif "3️⃣ x402" in page:
    st.title("x402 Volume")
    df = get_x402_data()
    fig = create_chart(df, "x402 Protocol Volume", 'volume')
    st.plotly_chart(fig, use_container_width=True)

elif "4️⃣ Vault" in page:
    st.title("Onchain Vault AUM")
    df = get_vault_data()
    fig = create_stacked_chart(df, "Vault AUM", ['Morpho', 'Euler', 'Yearn'])
    st.plotly_chart(fig, use_container_width=True)

elif "5️⃣ Perp" in page:
    st.title("Perpetual Futures Open Interest")
    df = get_perp_data()
    fig = create_stacked_chart(df, "Perp OI", ['Hyperliquid', 'Aster'])
    st.plotly_chart(fig, use_container_width=True)

elif "6️⃣ Buyback" in page:
    st.title("Buyback Activity")
    df = get_buyback_data()
    fig = create_chart(df, "Token Buybacks", 'cumulative', '#10b981')
    st.plotly_chart(fig, use_container_width=True)

elif "7️⃣ Solana" in page:
    st.title("Solana MEV Extraction")
    df = get_mev_data()
    fig = create_chart(df, "Jito Tips", 'jito_tips', '#8b5cf6')
    st.plotly_chart(fig, use_container_width=True)

elif "8️⃣ Shielded" in page:
    st.title("Shielded ZEC as Privacy Proxy")
    df = get_zec_data()
    fig = create_chart(df, "Shielded %", 'shielded_pct', '#f59e0b')
    st.plotly_chart(fig, use_container_width=True)

elif "9️⃣ Blob" in page:
    st.title("Ethereum's Blob Fee Floor")
    df = get_blob_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['blob_fee'], name='Blob Fee', line=dict(color='#3b82f6')))
    fig.add_trace(go.Scatter(x=df['date'], y=df['calldata'], name='Calldata', line=dict(color='#ec4899')))
    fig.update_layout(template="plotly_dark", height=400, plot_bgcolor='#1a1d29', paper_bgcolor='#1a1d29')
    st.plotly_chart(fig, use_container_width=True)

elif "🔟 Crypto" in page:
    st.title("Crypto Cards Spend Volume")
    df = get_cards_data()
    fig = go.Figure(go.Bar(x=df['date'], y=df['volume'], marker_color='#3b82f6'))
    fig.update_layout(template="plotly_dark", height=400, plot_bgcolor='#1a1d29', paper_bgcolor='#1a1d29')
    st.plotly_chart(fig, use_container_width=True)

elif "1️⃣1️⃣ BTC" in page:
    st.title("Spot BTC ETF AUM")
    df = get_etf_data()
    fig = create_stacked_chart(df, "BTC ETF Holdings", ['BlackRock', 'Fidelity'])
    st.plotly_chart(fig, use_container_width=True)

elif "1️⃣2️⃣ Stablecoin" in page:
    st.title("Onchain Stablecoin Borrow Rates")
    df = get_rates_data()
    fig = create_chart(df, "Aave USDC Borrow APY", 'borrow_apy')
    st.plotly_chart(fig, use_container_width=True)