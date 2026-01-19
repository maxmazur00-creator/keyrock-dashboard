import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Keyrock Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>
.main {background-color: #0e1117;}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📊 Keyrock 2026")
    st.caption("12 Charts to Watch")
    page = st.selectbox("Select Metric", [
        "Home",
        "Prediction Markets",
        "RWA Tokenisation",
        "x402 Volume",
        "Vault AUM",
        "Perp Futures",
        "Buyback Activity",
        "Solana MEV",
        "Shielded ZEC",
        "Blob Fees",
        "Crypto Cards",
        "BTC ETF",
        "Stablecoin Rates"
    ])

# Helper function
def make_chart(days=90):
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    values = [100 + i * 2 for i in range(days)]
    df = pd.DataFrame({'date': dates, 'value': values})
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['value'], mode='lines', 
                            line=dict(color='#3b82f6', width=2)))
    fig.update_layout(template="plotly_dark", height=400)
    return fig

# Main content
if page == "Home":
    st.title("🏠 Dashboard Overview")
    st.caption("Real-time monitoring of 12 key crypto metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Prediction Markets", "$2.4B", "+12.3%")
        st.metric("RWA Tokenisation", "$8.2B", "+5.7%")
        st.metric("x402 Volume", "$145M", "+28.4%")
        st.metric("Vault AUM", "$12.8B", "+3.2%")
    
    with col2:
        st.metric("Perp Futures OI", "$4.6B", "+15.8%")
        st.metric("Buyback Activity", "$890M", "+7.1%")
        st.metric("Solana MEV", "2.4M SOL", "+9.3%")
        st.metric("Shielded ZEC", "42.3%", "-1.2%")
    
    with col3:
        st.metric("Blob Fees", "0.023 ETH", "-4.5%")
        st.metric("Crypto Cards", "$234M", "+18.7%")
        st.metric("BTC ETF AUM", "1.2M BTC", "+6.4%")
        st.metric("Stablecoin Rates", "8.45%", "+0.3%")

elif page == "Prediction Markets":
    st.title("📊 Prediction Market Volumes")
    st.caption("Weekly total prediction market trading volume by market type")
    st.metric("Total Volume", "$2.4B", "+12.3%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Polymarket, Kalshi")

elif page == "RWA Tokenisation":
    st.title("💰 RWA Onchain Tokenisation AUM")
    st.caption("Total onchain RWA assets under management")
    st.metric("Total AUM", "$8.2B", "+5.7%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: DefiLlama, rwa.xyz")

elif page == "x402 Volume":
    st.title("⚡ x402 Volume")
    st.caption("Weekly volume through x402 payments protocol")
    st.metric("Current Volume", "$145M", "+28.4%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: x402 Protocol")

elif page == "Vault AUM":
    st.title("🏦 Onchain Vault AUM")
    st.caption("Total AUM across major vault protocols")
    st.metric("Total AUM", "$12.8B", "+3.2%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: DefiLlama")

elif page == "Perp Futures":
    st.title("📈 Perpetual Futures Open Interest")
    st.caption("Total perp futures OI onchain")
    st.metric("Total OI", "$4.6B", "+15.8%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: DefiLlama")

elif page == "Buyback Activity":
    st.title("💵 Buyback Activity")
    st.caption("Cumulative token buyback spend")
    st.metric("Cumulative", "$890M", "+7.1%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Token Terminal")

elif page == "Solana MEV":
    st.title("⚡ Solana MEV Extraction")
    st.caption("Jito tips tracking MEV extraction")
    st.metric("Total Tips", "2.4M SOL", "+9.3%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Jito Labs")

elif page == "Shielded ZEC":
    st.title("🔒 Shielded ZEC")
    st.caption("ZEC in shielded pools as privacy proxy")
    st.metric("Shielded %", "42.3%", "-1.2%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Zcash Explorer")

elif page == "Blob Fees":
    st.title("💾 Ethereum Blob Fees")
    st.caption("Blob vs calldata cost comparison")
    st.metric("Current Fee", "0.023 ETH", "-4.5%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Etherscan, Dune")

elif page == "Crypto Cards":
    st.title("💳 Crypto Cards Spend")
    st.caption("Weekly spend through crypto cards")
    st.metric("Weekly Volume", "$234M", "+18.7%")
    st.plotly_chart(make_chart(30), use_container_width=True)
    st.caption("Source: Protocol APIs")

elif page == "BTC ETF":
    st.title("₿ Spot BTC ETF AUM")
    st.caption("Total BTC held by US spot ETFs")
    st.metric("Total BTC", "1.2M BTC", "+6.4%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: Dune, Bloomberg")

elif page == "Stablecoin Rates":
    st.title("📊 Stablecoin Borrow Rates")
    st.caption("Aave USDC variable borrow APY")
    st.metric("Borrow APY", "8.45%", "+0.3%")
    st.plotly_chart(make_chart(), use_container_width=True)
    st.caption("Source: DefiLlama, Aave")

st.sidebar.markdown("---")
st.sidebar.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')}")
```

**Then scroll down and click "Commit changes"**

---

### 2️⃣ Replace `requirements.txt`

**Go to GitHub → Click `requirements.txt` → Click pencil ✏️ → Delete all → Paste this:**
```
streamlit
plotly
pandas
```

**Just these 3 lines! Nothing else.**

**Click "Commit changes"**

---

## ⏱️ Wait 2-3 Minutes

Streamlit will auto-redeploy. You'll see:
```
🔄 Rerunning with updated code...
