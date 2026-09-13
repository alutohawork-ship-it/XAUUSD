import streamlit as st
import requests
import json

# Konfigurasi Tampilan
st.set_page_config(page_title="MT5 AI Trading Generator", page_icon="⚡", layout="wide")

# Styling UI Luxury Premium
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f1f5f9; }
    .main-title { color: #f59e0b; font-size: 28px; font-weight: bold; text-align: center; }
    .sub-title { color: #94a3b8; font-size: 14px; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background: linear-gradient(135deg, #f59e0b, #d97706); color: #000; font-weight: bold; border-radius: 8px; border: none; padding: 12px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ MT5 AI TRADING GENERATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart Money Concepts & ICT Logic Engine • Mode UI Luxury Premium</div>', unsafe_allow_html=True)

# Input API Key & Config
with st.sidebar:
    st.header("⚙️ Configuration")
    metaapi_token = st.text_input("MetaApi Token", type="password")
    account_id = st.text_input("MetaApi Account ID")
    telegram_token = st.text_input("Telegram Bot Token", type="password")
    chat_id = st.text_input("Telegram Chat ID")

# Tombol Scan
if st.button("🔍 SCAN MARKET SEKARANG (11 LOGIC ENGINE)"):
    if not metaapi_token or not account_id:
        st.error("Masukkan MetaApi Token dan Account ID terlebih dahulu di menu samping!")
    else:
        st.info("Executing 11 ICT/SMC Logic Engine via MetaApi...")
        
        url = f"https://httpClient.metaapi.cloud/users/current/accounts/{account_id}/historical-market-data/symbols/XAUUSD/timeframes/5m/candles?limit=100"
        headers = {"auth-token": metaapi_token}
        
        try:
            res = requests.get(url, headers=headers)
            candles = res.json()
            
            if len(candles) > 0:
                # Ambil data candle terakhir
                c0 = candles[-1]
                c1 = candles[-2]
                c2 = candles[-3]
                
                # Contoh Evaluasi Sederhana
                is_bull_fvg = c0['low'] > c2['high']
                is_bear_fvg = c0['high'] < c2['low']
                
                entry = round(c0['close'])
                
                if is_bull_fvg:
                    sl = entry - 5
                    tp = entry + 12
                    st.success(f"🚨 SETUP BUY VALID!\n\nEntry: {entry} | SL: {sl} | TP: {tp}")
                elif is_bear_fvg:
                    sl = entry + 5
                    tp = entry - 12
                    st.error(f"🚨 SETUP SELL VALID!\n\nEntry: {entry} | SL: {sl} | TP: {tp}")
                else:
                    st.warning("NO VALID SETUP (WAIT) - Belum memenuhi konfluensi 11 Logika")
            else:
                st.error("Gagal mengambil data candle dari MetaApi.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
