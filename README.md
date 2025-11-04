# 📊 Bike Sharing Data Analysis  
Dashboard Interaktif dengan Python & Streamlit

Proyek ini merupakan analisis data penyewaan sepeda menggunakan dataset publik *Bike Sharing Dataset*. Analisis ini dilakukan untuk mengidentifikasi pola penggunaan sepeda berdasarkan waktu, musim, kondisi cuaca, serta jenis pelanggan. Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit untuk memudahkan eksplorasi data.

---

## 🚀 Live Dashboard
🔗 Streamlit App: https://abrar-bike-sharing-dicoding.streamlit.app/

## 📁 Repository
🔗 Google Colab Notebook:  
https://github.com/abrarargya/Proyek-Analisis-Data-Belajar-Analisis-Data-dengan-Python-Bike-Sharing/blob/main/Proyek_Analisis_Data_Bike_Sharing.ipynb

---

## 📌 Tujuan Proyek
- Menganalisis faktor-faktor yang memengaruhi jumlah peminjaman sepeda
- Mengetahui pola penggunaan sepeda sepanjang waktu
- Menyajikan hasil analisis secara visual dan interaktif

---

## 📍 Dataset
Dataset bersumber dari Kaggle:  
https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset  
Jumlah data: 17.389 baris

Fitur penting meliputi:
- `dteday` → Tanggal
- `season`, `weathersit` → Informasi musim dan cuaca
- `cnt` → Jumlah total peminjaman sepeda
- `casual`, `registered` → Kategori pengguna
- Variabel waktu: jam, hari, bulanan, tahunan

---

## 🔍 Insight Utama

Berikut beberapa temuan dari hasil analisis:

1. **Tren tahunan meningkat di 2012**, dengan puncak penyewaan rata-rata sebanyak **7.286** pada bulan **September**, sebelum akhirnya menurun di akhir tahun.
2. **Musim gugur** memiliki rata-rata peminjaman tertinggi (**5.644** peminjaman), sedangkan **musim semi** terendah (**2.604** peminjaman).
3. Kondisi cuaca sangat berpengaruh:
   - Cuaca **cerah atau cerah berawan** → rata-rata **201** peminjaman
   - Cuaca **hujan/salju lebat** → rata-rata hanya **74** peminjaman
4. Mayoritas pengguna merupakan **registered users** dengan persentase **81,64%**, sedangkan **casual users** hanya **18,4%**.

---

## 🛠️ Tools & Technologies

| Tools / Library | Keterangan |
|----------------|-----------|
| Python | Bahasa pemrograman utama |
| Pandas, NumPy | Data wrangling & data manipulation |
| Matplotlib, Seaborn | Visualisasi data |
| Streamlit | Dashboard interaktif |
| Scikit-Learn | (opsional) Analisis lanjutan |

---

## 📌 Cara Menjalankan Dashboard

```bash
# Clone repository
git clone <repo-url>

# Masuk ke direktori proyek
cd bike-sharing-analysis

# Install dependencies
pip install -r requirements.txt

# Jalankan dashboard
streamlit run dashboard_bike_sharing.py

```

👤 Tentang Saya

Saya Abrar Argya Adana, seorang Data Analyst Enthusiast dengan ketertarikan pada Data Visualization dan Insight Storytelling.

🔗 LinkedIn: www.linkedin.com/in/abrar-argya-adana

📬 Kontak

Untuk kerja sama atau diskusi terkait data, silakan hubungi saya melalui LinkedIn ☺️


