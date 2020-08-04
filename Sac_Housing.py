import pandas as pd 

#open and read spreadsheet (update file path to wherever you saved the sample dataset)
#note the 'price' column is designated as intergers in order to correctly filter 

sac_housing = pd.read_csv (r'C:\Users\Desktop\Sacramentorealestatetransactions.csv', dtype={'price':'int'})

#set query conditions

query = sac_housing[(sac_housing['price'] > 500000) & (sac_housing['city'] == 'SACRAMENTO')]

#save results to a new/seperate spreadsheet

def new_spread(): 

    """
    This function will transport the queried data to a new spreadsheet 
    """

    writer = pd.ExcelWriter('Exported from Python.xlsx')

    query.to_excel(writer)

    writer.save()

    print('DataFrame is written successfully to Excel File.')

new_spread()