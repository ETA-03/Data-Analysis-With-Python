import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df_hour = pd.read_csv('https://raw.githubusercontent.com/ETA-03/Data-Analysis-with-Python/refs/heads/main/data/hour.csv')
df_day = pd.read_csv('https://raw.githubusercontent.com/ETA-03/Data-Analysis-with-Python/refs/heads/main/data/day.csv')
df_hr_selected = df_hour[['hr','cnt']]
df_day_selected = df_day[['dteday','temp','cnt']]

st.title("PROYEK ANALISIS DATA")
st.write("Data yang digunakan adalah data penyewaan sepeda yang tersaji di dua tabel ini")

col1, col2 = st.columns(2)

with col1:
    st.title("Tabel Jam")
    st.write("Tabel berikut menampilkan jumlah sepeda tiap jamnya")
    st.write(df_hr_selected)

with col2:
    st.title("Tabel Hari")
    st.write("Tabel berikut menampilkan jumlah sepeda tiap harinya beserta suhu")
    st.write(df_day_selected)

st.title("Pertanyaan 1")

st.title("Jam berapa penyewaan sepeda ramai?")
st.write("Pertanyaan ini akan dianalisis menggunakan tabel jam")
hourly_counts = df_hr_selected.groupby('hr')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hourly_counts, color='r')
plt.title('Total penyewa sepeda terhadap waktu (Time Series)', fontsize=12)
plt.xlabel('Jam tiap harinya', fontsize=8)
plt.ylabel('Total sepeda yang disewa', fontsize=8)
plt.xticks(range(0, 24))
st.pyplot(fig)

st.title("Penjelasan Grafik 1")
st.write("""
    - Distribusi penyewaan sepeda yang beragam setiap jamnya
    - Jam puncak pertama penyewaan sepeda ada pada pukul 8
    - Pukul 17 merupakan puncak kedua dan puncak keramaian selama satu hari (bussiest hour)
    """)

st.title("Pertanyaan 2")

st.title("Pada suhu berapa penyewaan sepeda ramai?")
st.write("Pertanyaan ini akan dianalisis menggunakan tabel hari")
df_day_selected['temp_label'] = pd.cut(df_day_selected['temp'], bins=3, labels=['Dingin', 'Sedang','Panas'])
temperature_label= df_day_selected.groupby('temp_label')['cnt'].sum().reset_index()

color = ('#3AB0FF','#FFB562','#F87474')
fig, ax = plt.subplots()
ax.pie(temperature_label['cnt'], labels=temperature_label['temp_label'], autopct='%1.1f%%', colors=color)
ax.set_title('Penyewaan sepeda terhadap suhu')
st.pyplot(fig)

st.title("Penjelasan Grafik 2")
st.write("""
    - Penyewaan sepeda yang berbeda pada tiap pergantian suhu
    - Penyewaan sepeda paling banyak terjadi pada suhu panas (antara 0.594-0.862) dengan presentase 45.3%
    """)