import gradio as gr
import camelot
import pandas as pd

def table_extracter(file):   
    tables = camelot.read_pdf(file,pages='1-4')
    result = pd.ExcelWriter('result.xlsx') 
    for i in range(0,len(tables)):
        table = tables[i].df
        sheetname = str(i)
        table.to_excel(result, sheetname,index=False) 
    

demo =  gr.Interface(fn=table_extracter, inputs="file", outputs="file")
demo.launch()