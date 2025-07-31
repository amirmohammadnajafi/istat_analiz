import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# خواندن فایل CSV خروجی از تحلیل قبلی
df = pd.read_csv("C:/Users/amiii/BA/istat_data/disoccupazione_completa.csv")

# تبدیل نرخ بیکاری به عدد (از درصد به float)
df["Tasso di Disoccupazione (%)"] = df["Tasso di Disoccupazione"].str.replace('%', '').astype(float)

# عنوان صفحه
st.title("📊 تحلیل نرخ بیکاری فصلی در ایتالیا")

# فیلتر انتخاب سال
anni_disponibili = sorted(df["Anno"].unique())
anno_scelto = st.selectbox("🗓 انتخاب سال", anni_disponibili)

df_filtrato = df[df["Anno"] == anno_scelto]

# نمایش جدول
st.subheader("📋 جدول نرخ بیکاری")
st.dataframe(df_filtrato)

# نمودار خطی
st.subheader("📈 نمودار نرخ بیکاری فصلی")
fig, ax = plt.subplots()
ax.plot(df_filtrato["Trimestre"], df_filtrato["Tasso di Disoccupazione (%)"], marker='o')
ax.set_ylabel("نرخ بیکاری (%)")
ax.set_xlabel("فصل")
ax.set_title(f"نرخ بیکاری در سال {anno_scelto}")
st.pyplot(fig)
