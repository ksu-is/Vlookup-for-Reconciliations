import pandas as pd
input("Press Enter when templates are filled out")


smartreport_data = pd.read_excel('smartreport.xlsx')
tmf_data = pd.read_excel('tmf.xlsx')


outer_join = pd.merge(smartreport_data, 
                     tmf_data,
                     on ='mvsid', 
                     how ='outer')
outer_join
print(outer_join)
print('Vlookup Complete if records = NaN Please take the correct action')
