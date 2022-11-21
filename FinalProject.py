import pandas as pd

excel_report = pd.read_excel("Vlookup sample data.xlsx")
print(excel_report[excel_report["usrMVS_ID"].str.contains("A{2}")])