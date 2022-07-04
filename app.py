#-*- coding : utf-8-*-
import base64
from subprocess import STDOUT 
import streamlit as st
import pandas as pd 
import camelot as cam # extracting tables from PDFs 

st.title("PDF Table Extractor")
input_pdf = st.file_uploader(label = "", type = 'pdf')
background = st.selectbox("表格线条是否透明",(False,True))
page_number = st.text_input("请填写表格所在PDF页码，eg: 3, 1-3, 2-end, all", value = 1)

if input_pdf is not None:
    # byte object into a PDF file 
    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(input_pdf.read()).decode('utf-8')
        f.write(base64.b64decode(base64_pdf))
    f.close()
    tables_all= cam.read_pdf("input.pdf", pages=page_number, process_background=background)
    result_all = pd.ExcelWriter("result.xlsx", engine='xlsxwriter') 
    for i in range(0,len(tables_all)):
        table = tables_all[i].df
        sheetname = str(i)
        table.to_excel(result_all, sheetname,index=False) 
    result_all.save()
    with open(result_all,'rb') as f:
       st.download_button('抽取完成, 点击下载！', f,file_name="result.xlsx",mime="application/vnd.ms-excel")