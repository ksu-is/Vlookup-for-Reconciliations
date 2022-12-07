import pandas as pd
input("Press Enter when templates are filled out")
def main():
    
    smartreport_data = pd.read_excel('smartreport.xlsx')
    tmf_data = pd.read_excel('tmf.xlsx')


    outer_join = pd.merge(smartreport_data, 
                        tmf_data,
                        on ='mvsid', 
                        how ='outer')
    outer_join
    print(outer_join)
    print('If records = NaN Please take the correct action and run report again')

while True:
    answer = input("Run again once the actions are taken (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Reconciliation complete!")
        break
