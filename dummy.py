
import streamlit as st
import urllib.parse

st.title("📱 Dummy Notifikasi Satker")

# Data dummy seolah-olah berasal dari dashboard
data_satker = {
    "kode_satker": "SATKER001",
    "nama": "Satker Contoh 1",
    "no_wa": "6281273737212",
    "sisa_hari": 2
}

st.write("### Data Satker")
st.write("**Kode Satker:**", data_satker["kode_satker"])
st.write("**Nama Satker:**", data_satker["nama"])
st.write("**Sisa hari:**", data_satker["sisa_hari"])

# Trigger dari data
if data_satker["sisa_hari"] <= 2:

    st.warning("⚠️ Satker memenuhi kondisi untuk reminder.")

    pesan = """*REMINDER*

Sehubungan dengan batas revolving UP yang sudah mendekati,
izin mengingatkan agar Bapak/Ibu dapat segera mengajukan
revolving UP.

Atas kerja samanya diucapkan terima kasih 🙏"""

    st.text_area(
        "Pesan Notifikasi",
        value=pesan,
        disabled=True
    )

    # Membuat link WhatsApp
    nomor = data_satker["no_wa"]
    pesan_encoded = urllib.parse.quote(pesan)

    link_wa = f"https://wa.me/{nomor}?text={pesan_encoded}"

    st.markdown(
        f"[📱 Buka WhatsApp dan Kirim Reminder]({link_wa})"
    )

else:

    st.success("✅ Satker belum perlu menerima reminder.")
```
