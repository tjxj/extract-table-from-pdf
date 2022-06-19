import gradio as gr

def image_classifier(inp):
    pass  # image classifier model defined here
def table_extracter(file):   
    tables = camelot.read_pdf(file,pages='1-4')
    result = pd.ExcelWriter('result.xlsx') 
    for i in range(0,len(tables)):
        table = tables[i].df
        sheetname = str(i)
        table.to_excel(result, sheetname,index=False) 
    
    
gr.Interface(fn=image_classifier, inputs="image", outputs="label")