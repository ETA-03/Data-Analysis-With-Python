import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

df_hour = pd.read_csv('https://raw.githubusercontent.com/ETA-03/Data-Analysis-with-Python/refs/heads/main/data/hour.csv')
df_day = pd.read_csv('https://raw.githubusercontent.com/ETA-03/Data-Analysis-with-Python/refs/heads/main/data/day.csv')
df_hr_selected = df_hour[['hr','cnt']]
df_day_selected = df_day[['dteday','temp','cnt']]

st.title("PROYEK ANALISIS DATA")
st.write("Data yang digunakan adalah data penyewaan sepeda yang tersaji di dua taebl ini")

col1, col2 = st.columns(2)

with col1:
    st.write("Table Hours")
    st.write(df_hr_selected)

with col2:
    st.write("Table Day")
    st.write(df_day_selected)

st.title("Pertanyaan 1")
st.write("Jam berapa penyewaan sepeda akan ramai (Bussiest hour)?")
hourly_counts = df_hr_selected.groupby('hr')['cnt'].sum().reset_index()

st.title("Bike Rented By Hours")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_counts, color='b', ax=ax)
plt.title('Total Bike Rentals by Hour (Time Series)', fontsize=14)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Total Bike Rentals', fontsize=12)
plt.xticks(range(0, 24))
st.pyplot(fig)
