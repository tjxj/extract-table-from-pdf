import streamlit as st
import base64

def build_pdf(file_uploader):
    # byte object into a PDF file 
    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(file_uploader.read()).decode('utf-8')
        f.write(base64.b64decode(base64_pdf))
    f.close()

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)   
