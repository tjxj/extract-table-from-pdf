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


def show_pdf(file):
    with open(file,"wb") as f:
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
            tables = camelot.read_pdf(file,pages='1')
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

#writer()

#uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
# if uploaded_file is not None:
#     with pdfplumber.open(uploaded_file) as pdf:
#         tables = camelot.read_pdf(pdf,pages='1-4')

import streamlit as st # data app development
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
st.subheader("with `Camelot` Python library")

#st.image("https://raw.githubusercontent.com/camelot-dev/camelot/master/docs/_static/camelot.png", width=200)


# file uploader on streamlit 

input_pdf = st.file_uploader(label = "upload your pdf here", type = 'pdf')

#st.markdown("### Page Number")

#page_number = st.text_input("Enter the page # from where you want to extract the PDF eg: 3", value = 1)

# run this only when a PDF is uploaded

if input_pdf is not None:
    # byte object into a PDF file 
    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(input_pdf.read()).decode('utf-8')
        f.write(base64.b64decode(base64_pdf))
    f.close()

    # read the pdf and parse it using stream
    tables = cam.read_pdf("input.pdf", pages='1')
    result = pd.ExcelWriter('result.xlsx', engine='xlsxwriter') 
    tables[0].to_excel(result,index=False) 
    # for i in range(0,len(tables)):
    #     table = tables[i].df
    #     sheetname = str(i)
    #     table.to_excel(result, sheetname,index=False) 

    with open('result.xlsx') as f:
       st.download_button('表格抽取完成，点此下载！', f,file_name='result.xlsx',mime="application/vnd.ms-excel")  # Defaults to 'text/plain'
       
# result = pd.ExcelWriter('result.xlsx') 
# for i in range(0,len(tables)):
#     table = tables[i].df
#     sheetname = str(i)
#     table.to_excel(result, sheetname,index=False) 

## https://www.adobe.com/acrobat/online/compress-pdf.html?mv=search&sdid=DZTGZX2P&ef_id=CjwKCAiAjoeRBhAJEiwAYY3nDARHYPn2H7Cs1ZrGfMDx01ikownQ-DYhp0EX_mKnwWtC6TyrWP3tjBoCG_QQAvD_BwE:G:s&s_kwcid=AL!3085!3!559402382057!e!!g!!pdf%20compress!12981897010!121481297003&cmpn=mobile-search&gclid=CjwKCAiAjoeRBhAJEiwAYY3nDARHYPn2H7Cs1ZrGfMDx01ikownQ-DYhp0EX_mKnwWtC6TyrWP3tjBoCG_QQAvD_BwE
## https://github.com/insightsbees/Personal_Website/blob/main/website_app.py

## https://choodesmond42.medium.com/pdf-manipulation-how-to-remove-unwanted-pages-using-pdfminer-56ba93bdd7d1