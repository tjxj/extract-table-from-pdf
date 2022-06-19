import gradio as gr
import camelot
import pandas as pd
imort base64
def table_extracter(file):   

    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(input_pdf.read()).decode('utf-8')
        f.write(base64.b64decode(base64_pdf))
    f.close()

    # read the pdf and parse it using stream
    table = cam.read_pdf("input.pdf", pages = page_number, flavor = 'stream')


    tables = camelot.read_pdf(file,pages='1-4')
    result = pd.ExcelWriter('result.xlsx') 
    for i in range(0,len(tables)):
        table = tables[i].df
        sheetname = str(i)
        table.to_excel(result, sheetname,index=False) 
    return 'result.xlsx'

demo =  gr.Interface(fn=table_extracter, inputs="file", 
        outputs="file",title = 'PDF into table Application',
        description = 'Simple application in python to try the Gradio package components')
demo.launch()