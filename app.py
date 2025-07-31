import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# خواندن فایل CSV
df = pd.read_csv("https://raw.githubusercontent.com/amirmohammadnajafi/istat_analiz/main/disoccupazione_completa.csv")

# تبدیل نرخ بیکاری به float
df["Tasso di Disoccupazione (%)"] = df["Tasso di Disoccupazione"].str.replace('%', '').astype(float)

# عنوان صفحه
st.set_page_config(page_title="نرخ بیکاری در ایتالیا", layout="centered")
st.title("📊 تحلیل نرخ بیکاری فصلی در ایتالیا")

# فیلتر انتخاب سال
anni_disponibili = sorted(df["Anno"].unique())
anno_scelto = st.selectbox("🗓 انتخاب سال", anni_disponibili)

# فیلتر داده‌ها بر اساس سال انتخاب‌شده
df_filtrato = df[df["Anno"] == anno_scelto]

# نمایش جدول
st.subheader("📋 جدول نرخ بیکاری")
st.dataframe(df_filtrato)

# نمودار با Plotly (منحنی صاف و مدرن)
st.subheader("📈 نمودار نرخ بیکاری فصلی")
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_filtrato["Trimestre"],
    y=df_filtrato["Tasso di Disoccupazione (%)"],
    mode='lines+markers',
    line_shape='spline',
    name=str(anno_scelto),
    line=dict(width=3, color='#1f77b4'),
    marker=dict(size=8)
))
fig.update_layout(
    title=f"نرخ بیکاری در سال {anno_scelto}",
    xaxis_title="فصل",
    yaxis_title="درصد بیکاری (%)",
    template="plotly_white",
    font=dict(family="Vazir", size=14),
    height=400
)
st.plotly_chart(fig, use_container_width=True)
