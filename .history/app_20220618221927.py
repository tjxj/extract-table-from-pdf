import camelot
import pandas as pd 
import streamlit as st
from pdfminer.high_level import extract_pages
import base64,tempfile
from pathlib import Path
import pdfplumber

import streamlit as st
import base64
from pathlib import Path
import tempfile

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
def writer():
    file = st.file_uploader("选择待上传的PDF文件", type=['pdf'])
    if st.button("抽取表格"):
        if file is not None:
            tables = camelot.read_pdf(file,pages='1-4')
            result = pd.ExcelWriter('result.xlsx') 
            for i in range(0,len(tables)):
                table = tables[i].df
                sheetname = str(i)
                table.to_excel(result, sheetname,index=False) 
            
            st.download_button(
                 label="Download data as CSV",
                 data=result,
                 file_name='result.csv',
                 mime='text/csv',
             )

writer()
