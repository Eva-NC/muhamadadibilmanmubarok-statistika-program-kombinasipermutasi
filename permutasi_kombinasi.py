import streamlit as st
import math
# Konfigurasi Halaman
st.set_page_config(
    page_title="Permutasi dan Kombinasi Pro",
    layout="centered"
)

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Custom CSS (Background & Tombol)
st.markdown("""
<style>
/* Background Gradien Modern */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* Judul Utama */
h1 { color: #1E293B; text-align: center; font-weight: 800; }

/* Styling Tombol Hitung (Utama) */
div.stButton > button:first-child {
    background-color: #4F46E5;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: bold;
    transition: all 0.3s ease;
}

div.stButton > button:first-child:hover {
    background-color: #4338CA;
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);
    transform: translateY(-2px);
}

/* Styling Tombol Hapus Riwayat (Bahaya/Red) */
div.stButton > button:last-child {
    background-color: transparent;
    color: #EF4444;
    border: 1px solid #EF4444;
}

div.stButton > button:last-child:hover {
    background-color: #EF4444;
    color: white;
}

.footer { text-align: center; font-size: 12px; color: #475569; margin-top: 50px; font-weight: 500; }
.block-container { padding-top: 3rem; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>Aplikasi Permutasi dan Kombinasi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#475569;'>Program Statistika untuk menghitung Permutasi dan Kombinasi</p>", unsafe_allow_html=True)

# Input Section
st.divider()
st.subheader("Input Data")

col1, col2 = st.columns(2)
with col1:
    n = st.number_input("Masukkan nilai n", min_value=0, value=5, step=1)
with col2:
    r = st.number_input("Masukkan nilai r", min_value=0, value=2, step=1)

st.subheader("Jenis Perhitungan")
pilihan = st.radio(
    "Pilih salah satu:",
    ("Permutasi", "Kombinasi", "Bandingkan Keduanya"),
    horizontal=True
)

# Logika Perhitungan
if st.button("Hitung", use_container_width=True):
    if r > n:
        st.error("Kesalahan: Nilai r tidak boleh lebih besar dari n")
    else:
        st.divider()
        
        f_n = math.factorial(n)
        f_r = math.factorial(r)
        f_nr = math.factorial(n - r)

        def proses_permutasi():
            hasil_p = f_n // f_nr
            st.success(f"Hasil Permutasi P({n},{r}) = {hasil_p}")
            with st.expander("Lihat Langkah Perhitungan Permutasi"):
                st.latex(rf"P({n},{r}) = \frac{{{n}!}}{{({n}-{r})!}} = \frac{{{f_n}}}{{{f_nr}}} = {hasil_p}")
                st.write("Catatan: Digunakan jika urutan diperhatikan.")
            return hasil_p

        def proses_kombinasi():
            hasil_c = f_n // (f_r * f_nr)
            st.success(f"Hasil Kombinasi C({n},{r}) = {hasil_c}")
            with st.expander("Lihat Langkah Perhitungan Kombinasi"):
                st.latex(rf"C({n},{r}) = \frac{{{n}!}}{{{r}!({n}-{r})!}} = \frac{{{f_n}}}{{{f_r} \times {f_nr}}} = {hasil_c}")
                st.write("Catatan: Digunakan jika urutan tidak diperhatikan.")
            return hasil_c

        if pilihan == "Permutasi":
            res = proses_permutasi()
            st.session_state.history.append(f"P({n},{r}) = {res}")
        elif pilihan == "Kombinasi":
            res = proses_kombinasi()
            st.session_state.history.append(f"C({n},{r}) = {res}")
        else:
            res_p = proses_permutasi()
            res_c = proses_kombinasi()
            st.session_state.history.append(f"P({n},{r}): {res_p} | C({n},{r}): {res_c}")

# Riwayat dan Informasi
st.divider()
col_a, col_b = st.columns([1, 1])

with col_a:
    st.subheader("Riwayat Perhitungan")
    if st.session_state.history:
        for item in reversed(st.session_state.history[-5:]):
            st.text(f"- {item}")
        if st.button("Hapus Riwayat"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("Belum ada riwayat.")

with col_b:
    st.subheader("Panduan Singkat")
    st.write("**Permutasi**")
    st.caption("Contoh: Menyusun pengurus organisasi atau urutan tempat duduk.")
    st.write("**Kombinasi**")
    st.caption("Contoh: Memilih anggota delegasi atau mengambil bola dari kotak.")

# Footer
st.markdown(
    f"<div class='footer'>Tugas Statistika 1 | Muhamad Adib Ilman Mubarok | 50424726</div>",
    unsafe_allow_html=True
)