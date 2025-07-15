import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AlphaTradex – Indian Market Dashboard", layout="wide")
st.title("📊 AlphaTradex – Indian Market Dashboard 🇮🇳")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# === INDEX DATA from NSE ===
def get_nse_index_data():
    try:
        url = "https://api.brotherslab.in/indices"  # Public proxy API
        res = requests.get(url, timeout=10)
        json_data = res.json()

        indexes = {
            "NIFTY 50": "NIFTY 50",
            "NIFTY BANK": "NIFTY BANK",
            "SENSEX": "SENSEX"
        }

        data = {}
        for item in json_data:
            if item['indexName'] in indexes.values():
                data[item['indexName']] = {
                    "Last Price": item['last'],
                    "Change": item['variation'],
                    "Change %": item['percentChange']
                }

        return pd.DataFrame(data).T

    except Exception as e:
        st.error(f"Could not fetch index data: {e}")
        return pd.DataFrame()


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


