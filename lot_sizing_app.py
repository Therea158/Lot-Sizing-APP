import streamlit as st
import math

st.set_page_config(page_title="Kalkulator Lot Sizing Saham", page_icon="📈")

st.title("📈 Kalkulator Lot Sizing Saham")
st.caption("Berdasarkan manajemen risiko")

# Input
equity = st.number_input("💰 Modal (Equity)", value=5_000_000, step=100_000, format="%i")
risk_percent = st.number_input("⚠️ Risiko per Transaksi (%)", value=1.0, step=0.1)
entry_price = st.number_input("📌 Harga Entry (per lembar)", value=1460)
stop_loss = st.number_input("❌ Harga Stop Loss (per lembar)", value=1370)
target_price = st.number_input("🎯 Target Profit Price (per lembar)", value=1600)
bulatkan = st.radio("🔁 Jenis Pembulatan", ["Konservatif (bawah)", "Agresif (atas)"])

# Proses perhitungan
risk_value = equity * (risk_percent / 100)
selisih_harga = entry_price - stop_loss

if selisih_harga <= 0:
    st.error("Harga entry harus lebih tinggi dari harga stop loss!")
else:
    lot_mentah = (risk_value / selisih_harga) / 100

    if "bawah" in bulatkan:
        lot_final = math.floor(lot_mentah)
    else:
        lot_final = math.ceil(lot_mentah)

    # Output
    st.markdown("## 📊 Hasil Perhitungan")
    st.write(f"🧮 Risk per Trade: Rp{risk_value:,.0f}")
    st.write(f"📉 Selisih Harga: Rp{selisih_harga:,.0f} per lembar")
    st.write(f"🔢 Lot Maksimal: **{lot_final} lot** (dari {round(lot_mentah, 2)} lot)")

    # Estimasi profit
    profit_per_lembar = target_price - entry_price
    total_profit = profit_per_lembar * lot_final * 100  # 100 lembar per lot

    st.markdown("## 💰 Estimasi Profit")
    st.write(f"📈 Profit per Lembar: Rp{profit_per_lembar:,.0f}")
    st.write(f"💸 Estimasi Total Profit: Rp{total_profit:,.0f} (untuk {lot_final} lot)")

st.markdown("---")
st.caption("#INVESTAPORADEPARTMENT #UnssafINIT14TOR")

