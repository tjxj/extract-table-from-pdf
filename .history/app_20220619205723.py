#-*- coding : utf-8-*-
#coding: unicode_escape

import pandas as pd 
import streamlit as st
from pdfminer.high_level import extract_pages
import base64,tempfile
from pathlib import Path
import pdfplumber
import subprocess # process in the os
from subprocess import STDOUT, check_call #os process manipuation
import os #os process manipuation
import base64 # byte object into a pdf file 
import camelot as cam # extracting tables from PDFs 

# to run this only once and it's cached
@st.cache
def gh():
    """install ghostscript on the linux machine"""
    proc = subprocess.Popen('apt-get install -y ghostscript', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
    proc.wait()

gh()



st.title("PDF Table Extractor")

input_pdf = st.file_uploader(label = "upload your pdf here", type = 'pdf')

page_number = st.text_input("Enter the page # from where you want to extract the PDF eg: 3", value = 1)

if input_pdf is not None:
    # byte object into a PDF file 
    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(input_pdf.read()).decode('utf-8')
        f.write(base64.b64decode(base64_pdf))
    f.close()

    # read the pdf and parse it using stream
    tables = cam.read_pdf("input.pdf", pages=page_number)
    result = pd.ExcelWriter('result.xlsx', engine='xlsxwriter') 
    tables[0].to_excel(result,index=False) 
    # for i in range(0,len(tables)):
    #     table = tables[i].df
    #     sheetname = str(i)
    #     table.to_excel(result, sheetname,index=False) 

    st.download_button('download', f,file_name='result.xlsx',mime="application/vnd.ms-excel")
       

## https://www.adobe.com/acrobat/online/compress-pdf.html?mv=search&sdid=DZTGZX2P&ef_id=CjwKCAiAjoeRBhAJEiwAYY3nDARHYPn2H7Cs1ZrGfMDx01ikownQ-DYhp0EX_mKnwWtC6TyrWP3tjBoCG_QQAvD_BwE:G:s&s_kwcid=AL!3085!3!559402382057!e!!g!!pdf%20compress!12981897010!121481297003&cmpn=mobile-search&gclid=CjwKCAiAjoeRBhAJEiwAYY3nDARHYPn2H7Cs1ZrGfMDx01ikownQ-DYhp0EX_mKnwWtC6TyrWP3tjBoCG_QQAvD_BwE
## https://github.com/insightsbees/Personal_Website/blob/main/website_app.py

## https://choodesmond42.medium.com/pdf-manipulation-how-to-remove-unwanted-pages-using-pdfminer-56ba93bdd7d1