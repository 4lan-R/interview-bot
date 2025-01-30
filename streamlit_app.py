import streamlit as st
import requests

st.title('PDF Uploader')
uploaded_file = st.file_uploader("Choose a PDF File", type=["pdf"])

if uploaded_file is not None:
    st.write(f'Uploaded file: {uploaded_file.name}')
    if st.button('Upload PDF'):
        upload_url = 'http://127.0.0.1:5000/upload_pdf'
        response = requests.post(upload_url, files={'file': uploaded_file})
        st.write(response.json().get('message'))
