import pickle # untuk meload dot  sav
import streamlit as st # untuk membut kodingan streamlit

# membaca model
DataGizi_model = pickle.load(open('StatusGizi_model.sav', 'rb'))

# judul web
st.title('Data Mining Prediksi Status Gizi')

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Jenis_Kelamin = st.text_input ('Input Nilai Jenis Kelamin')

with col1 :
    Usia_Saat_Ukur = st.text_input ('Input Nilai Usia Saat Ukur')

with col2 :
    Berat_Badan = st.text_input ('Input Nilai Berat Badan')

with col2 :
    Tinggi_Badan = st.text_input ('Input Nilai Tinggi Badan')

# code untuk prediksi
status_gizi_gizi = ''

# membuat tombol untuk prediksi
if st.button('Status Gizi Anak') :
    datagizi_prediction = DataGizi_model.predict([[Jenis_Kelamin,Usia_Saat_Ukur,Berat_Badan,Tinggi_Badan]])


    if(datagizi_prediction[0] ==1):
        status_gizi = 'Gizi Normal'
    else :
        status_gizi = 'Gizi kurang'

    st.success(status_gizi)