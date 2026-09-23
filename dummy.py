import streamlit as st

st.title("📱 Dummy Notifikasi Satker")

# Data dummy untuk testing
dummy_kontak = {
    "SATKER001": {
        "nama": "Satker Contoh 1",
        "no_wa": "6281234567890"
    },
    "SATKER002": {
        "nama": "Satker Contoh 2",
        "no_wa": "6289876543210"
    }
}

# Pilih Satker
kode_satker = st.selectbox(
    "Pilih Kode Satker",
    options=list(dummy_kontak.keys())
)

# Ambil data kontak berdasarkan kode Satker
data_satker = dummy_kontak[kode_satker]

st.write("**Nama Satker:**", data_satker["nama"])
st.write("**Nomor WhatsApp:**", data_satker["no_wa"])

# Template pesan
pesan = st.text_area(
    "Pesan Notifikasi",
    value="""*REMINDER*

Sehubungan dengan batas revolving UP yang sudah mendekati,
izin mengingatkan agar Bapak/Ibu dapat segera mengajukan
revolving UP.

Atas kerja samanya diucapkan terima kasih 🙏"""
)

# Tombol simulasi
if st.button("📤 Simulasi Kirim Notifikasi"):

    st.info("Mengirim ke dummy broker...")

    st.success("✅ Dummy notifikasi berhasil diproses")

    st.write("**Kode Satker:**", kode_satker)
    st.write("**Nomor tujuan:**", data_satker["no_wa"])
    st.write("**Status:** Simulasi berhasil")
