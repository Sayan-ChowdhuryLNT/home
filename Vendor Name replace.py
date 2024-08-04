import os, os.path
 
import win32com.client
 
import pythoncom
 
from math import *
 
xl=win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())

 
# xl.Visible = True
# change the folder folder path accordingly
wb = xl.Workbooks.Open(r'C:\Users\20323801\Downloads\Detailed_PR_Status_2024_03_18_06-08-33.xlsx')
 
# ws1 = wb.worksheets("Detailed_PR_Status")
ws1=wb.Worksheets("Detailed_PR_Status")
# for i in range (2,2425):
# # i=4
#     if ws1.Cells(i,6).Value != None:
#         value=ws1.Cells(i,6).Value
#         # print(value)
#         value1=""
#         if value[0] == " ":
#             for j in range(1,len(value)):
#                 value1+=value[j]
#             print("row",i,value1)
#             ws1.Cells(i,6).Value=value1
for i in range (2,2425):
# i=2
    status=["MFC issued","Post-order pending with EDRC","Post-order technically cleared","Post-order comments issued","Awaiting post-offer from vendor"]
    value=ws1.Cells(i,7).Value
    if value in status:
        ws1.Cells(i,29).Value=ws1.Cells(i,6).Value           
