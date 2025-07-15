import streamlit as st
import requests
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="AlphaTradex – Indian Market Dashboard", layout="wide")

st.title("📊 AlphaTradex – Indian Market Dashboard 🇮🇳")
st.caption(f"Live market overview – Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# === INDEX DATA ===
st.subheader("📈 Live Indices")

def get_index_data():
    indices = {
        "Nifty 50": "^NSEI",
        "Bank Nifty": "^NSEBANK",
        "Sensex": "^BSESN"
    }
    data = {}
    for name, symbol in indices.items():
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=1d&interval=1m"
        r = requests.get(url)
        json_data = r.json()
        try:
            current = json_data["chart"]["result"][0]["meta"]["regularMarketPrice"]
            prev_close = json_data["chart"]["result"][0]["meta"]["chartPreviousClose"]
            change = current - prev_close
            pct = (change / prev_close) * 100
            data[name] = {"Price": round(current, 2), "Change": round(change, 2), "Change (%)": round(pct, 2)}
        except:
            data[name] = {"Price": "N/A", "Change": "N/A", "Change (%)": "N/A"}
    return pd.DataFrame(data).T

st.dataframe(get_index_data(), use_container_width=True)

# === NEWS ===
st.subheader("📰 Market News (Moneycontrol)")
def get_news():
    url = "https://newsapi.org/v2/top-headlines?sources=moneycontrol&apiKey=demo"  # Replace demo with your key
    try:
        res = requests.get(url)
        articles = res.json()["articles"]
        for article in articles[:5]:
            st.markdown(f"🔹 [{article['title']}]({article['url']})")
    except:
        st.write("⚠️ Could not fetch news.")

# Optional: Replace with RSS feed parsing for free if needed

# === CHART VIEW ===
st.subheader("📊 TradingView Chart")
selected_symbol = st.text_input("Enter NSE stock symbol (e.g., RELIANCE, INFY, SBIN)", value="RELIANCE")
st.components.v1.html(f"""
    <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_xxx&symbol=NSE:{selected_symbol.upper()}&interval=15&theme=light&style=1&locale=en" 
    width="100%" height="500" frameborder="0"></iframe>
""", height=500)

st.markdown("---")
st.markdown("Made with ❤️ by @AlphaTradex")

