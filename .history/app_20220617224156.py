from os import set_inheritable
import camelot
import pandas as pd 


tables = camelot.read_pdf('/Users/huhaiyang/Archives/2020.pdf',pages='1-3')

result = pd.ExcelWriter('result.xlsx') 
for i in range(0,len(tables)):
    table = tables[i].df
    sheetname = str(i)
    table.to_excel(result, sheetname,index=False) 

result.save() 