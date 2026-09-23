```python
import streamlit as st
import urllib.parse

st.title("📱 Dummy Notifikasi Satker")

# Data dummy
dummy_kontak = {
    "SATKER001": {
        "nama": "Satker Contoh 1",
        "no_wa": "6281273737212"
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

# Ambil data Satker
data_satker = dummy_kontak[kode_satker]

st.write("**Nama Satker:**", data_satker["nama"])
st.write("**Nomor WhatsApp:**", data_satker["no_wa"])

# Pesan
pesan = st.text_area(
    "Pesan Notifikasi",
    value="""*REMINDER*

Sehubungan dengan batas revolving UP yang sudah mendekati,
izin mengingatkan agar Bapak/Ibu dapat segera mengajukan
revolving UP.

Atas kerja samanya diucapkan terima kasih 🙏"""
)

# Tombol buka WhatsApp
if st.button("📱 Buka WhatsApp"):

    nomor = data_satker["no_wa"]
    pesan_encoded = urllib.parse.quote(pesan)

    link_wa = f"https://wa.me/{nomor}?text={pesan_encoded}"

    st.success("✅ Nomor dan pesan berhasil disiapkan!")

    st.markdown(
        f"[➡️ Klik di sini untuk membuka WhatsApp]({link_wa})"
    )

    st.write("**Nomor tujuan:**", nomor)
    st.write("**Status:** Siap dikirim melalui WhatsApp")
```
