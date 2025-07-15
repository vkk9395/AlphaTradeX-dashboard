import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AlphaTradex – Indian Market Dashboard", layout="wide")
st.title("📊 AlphaTradex – Indian Market Dashboard 🇮🇳")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# === INDEX DATA from NSE ===
st.subheader("📈 Live Indices – TradingView Widget")

st.components.v1.html("""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_xxx&symbols=NSE:NIFTY,INDEX:NSEBANK,INDEX:BSESN&theme=light&style=1&locale=en" 
  width="100%" height="100" frameborder="0"></iframe>
</div>
<!-- TradingView Widget END -->
""", height=100)


st.subheader("📈 Live Indices (NSE)")
st.dataframe(get_nse_index_data(), use_container_width=True)

# === NEWS PLACEHOLDER ===
st.subheader("📰 Market News (Coming Soon)")
st.info("News feature will be added shortly using RSS or Telegram Bot.")

# === CHART ===
st.subheader("📊 TradingView Chart")
symbol = st.text_input("Enter NSE stock symbol (e.g., RELIANCE)", value="RELIANCE")
st.components.v1.html(f"""
    <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_xxx&symbol=NSE:{symbol.upper()}&interval=15&theme=light&style=1&locale=en" 
    width="100%" height="500" frameborder="0"></iframe>
""", height=500)

st.markdown("---")
st.markdown("Made with ❤️ by @AlphaTradex")


