# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#C:/Dokumen/Data Science Dicoding/Main Chapter/4 Belajar Analisis Data dengan Python/final project_bike sharing

# create month_rentals() to prepare month_rentals dataframe
def create_month_rentals(day_df):
    month_rentals = day_df.groupby('mnth').agg({'cnt': 'mean'})
    return month_rentals

#create season_rental() to prepare season_rental dataframe
def create_season_rental(day_df):
    season_rental = day_df.groupby(by="season").agg({"cnt": ["mean"]})
    return season_rental

# create weather_rental() to prepare weather_rental dataframe
def create_weather_rental(hour_df):
    weather_rental = hour_df.groupby(by="weathersit").agg({"cnt":["mean"]})
    return weather_rental

# create total_casual_day() to prepare total_casual_day dataframe
def create_total_casual_day(day_df):
    total_casual_day = day_df['casual'].sum()
    return total_casual_day

# create total_registered_day() to prepare total_registered_day dataframe
def create_total_registered_day(day_df):
    total_registered_day = day_df['registered'].sum()
    return total_registered_day

#load files
days_df = pd.read_csv("https://raw.githubusercontent.com/abrarargya/Proyek-Analisis-Data-Belajar-Analisis-Data-dengan-Python-Bike-Sharing/refs/heads/main/day_clean_df.csv")
hours_df = pd.read_csv("https://raw.githubusercontent.com/abrarargya/Proyek-Analisis-Data-Belajar-Analisis-Data-dengan-Python-Bike-Sharing/refs/heads/main/hour_clean_df.csv")

# sort dteday columns and make sure it's in datetime format
datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

#making filter with date input widget 
min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

with st.sidebar:
    # Add logo
    st.image("https://static.vecteezy.com/system/resources/previews/007/535/933/large_2x/bike-sharing-icon-for-apps-and-web-vector.jpg")
    
# Take start_date and end_date balue from date_input
    start_date, end_date = st.date_input(
        label='Linimasa',min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )
#save to main_day_df and main_hour_df, this dataframe serve a purpose to make visualization of our data
main_day_df = days_df[(days_df["dteday"] >= str(start_date)) & 
                       (days_df["dteday"] <= str(end_date))]

main_hour_df = hours_df[(hours_df["dteday"] >= str(start_date)) & 
                        (hours_df["dteday"] <= str(end_date))]

#let's call our function
month_rentals = create_month_rentals(main_day_df)
season_rental = create_season_rental(main_day_df)
weather_rental = create_weather_rental(main_hour_df)
total_casual_day = create_total_casual_day(main_day_df)
total_registered_day = create_total_registered_day(main_day_df)

#add header
st.header('Bike Sharing Dashboard :sparkles:')


#petakan bulan sesuai angka di dataset
month_name_map = {
    '1': 'Jan',
    '2': 'Feb',
    '3': 'Mar',
    '4': 'Apr',
    '5': 'May',
    '6': 'Jun',
    '7': 'Jul',  
    '8': 'Aug',
    '9': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}
#buat visualisasi Rata - Rata Penyewaan Sepeda Bulanan
st.subheader('Rata - Rata Penyewaan Sepeda Bulanan')
#buat format plot kosong
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    month_rentals.index, 
    month_rentals['cnt'],
    marker='o', 
    linewidth=3, 
    color="#90CAF9"
)
#ambil indeks bulan dari dataset dari 1 sampai 12 dan dimasukan ke dalam list
month_indices = month_rentals.index.astype(str).tolist()
#ubah angka indeks menjadi deskriptif
descriptive_month_labels = [month_name_map.get(m, m) for m in month_indices]
ax.set_xticks(month_rentals.index)
ax.set_xticklabels(descriptive_month_labels, rotation=0)
ax.set_xlabel('Bulan', fontsize=20)
ax.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=20)
#tambahkan grid
ax.grid(axis='y', linestyle='--', alpha=0.7) 
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=18) 
st.pyplot(fig)

#petakan musim sesuai angka dataset
season_name_map = {
    '1': 'Semi',
    '2': 'Panas',
    '3': 'Gugur',
    '4': 'Dingin'
}
#buat visualisasi  rata - rata pelanggan paling banyak dan paling sedikit menyewa sepeda di dua tahun terakhir berdasarkan musim
st.subheader("Rata - Rata Penyewaan Sepeda Berdasarkan Musim")
 
fig, ax = plt.subplots(figsize=(35, 15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#F99096"]
#urutkan jumlah rata - rata dari terkecil
season_rental_sorted = season_rental.sort_values(by=('cnt', 'mean'), ascending=True)
#ambil indeks musim dari dataset dari 1 sampai 4 dan dimasukan ke dalam list
numeric_y_labels = season_rental_sorted.index.astype(str).tolist()
#tambahkan deskripsi seperti semi, gugur, dll
descriptive_y_labels = [season_name_map.get(str(s), str(s)) for s in numeric_y_labels]
sns.barplot(
    x=season_rental_sorted['cnt']['mean'], 
    y=numeric_y_labels,  
    orient='h', 
    palette=colors[:len(numeric_y_labels)], 
    ax=ax
)
ax.set_yticklabels(descriptive_y_labels)

ax.set_ylabel('Musim', fontsize=35) 
ax.set_xlabel("Rata-rata Jumlah Penyewaan", fontsize=30)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=30)
fig.tight_layout()
st.pyplot(fig)


#petakan cuaca berdasarkan angka dataset
weather_name_map = {
    '1': 'Cerah/cerah berawan',
    '2': 'Berkabut/berawan',
    '3': 'Hujan/salju ringan',
    '4': 'Hujan/salju lebat'
}
#buat visualisasi  rata - rata pelanggan paling banyak dan paling sedikit menyewa sepeda di dua tahun terakhir berdasarkan cuaca
st.subheader("Rata - Rata Penyewaan Sepeda Berdasarkan Cuaca")
 
fig, ax = plt.subplots(figsize=(35, 15))
 
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#F99096"]
#urutkan jumlah rata - rata dari terkecil
weather_rental_sorted = weather_rental.sort_values(by=('cnt', 'mean'), ascending=True)
#ambil indeks cuaca dari dataset dari 1 sampai 4 dan dimasukan ke dalam list
numeric_y_labels = weather_rental_sorted.index.astype(str).tolist()
#tambahkan deskripsi seperti berawan, hujan, dll
descriptive_y_labels = [weather_name_map.get(str(s), str(s)) for s in numeric_y_labels]
sns.barplot(
    x=weather_rental_sorted['cnt']['mean'], 
    y=numeric_y_labels,  
    orient='h', 
    palette=colors[:len(numeric_y_labels)], 
    ax=ax
)
ax.set_yticklabels(descriptive_y_labels)
ax.set_ylabel('Cuaca', fontsize=35) 
ax.set_xlabel("Rata-rata Jumlah Penyewaan", fontsize=30)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=30)
fig.tight_layout()
st.pyplot(fig)

#buat visualisasi plot pie chart demografi pelanggan berdasarkan status casual atau registered
st.subheader("Demografi Pelanggan Penyewa Sepeda")

labels = 'Registered', 'Casual'
sizes = [81.6, 18.4]
explode = (0, 0.1) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors=["#D3D3D3", "#90CAF9"],
        shadow=True, startangle=90)
ax1.axis('equal')  


st.pyplot(fig1)
