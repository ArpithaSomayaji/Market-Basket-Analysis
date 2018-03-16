import pandas as pd
import csv

#Read CSV file from location to marketBasket_data
marketBasket_data = pd.read_csv("C:/Users/Arpitha Somayaji/Desktop/Fall 2017/DATA SCIENCE/Homework/MarketBasket/marketbasketData.csv")
#Store the product names in Columnnames
columnnames = list(marketBasket_data)

#iterate through each row in marketBasket_data . Append it to csv file if  row[column] equals to true 
for index, row in marketBasket_data.iterrows():
    column = []
    for names in columnnames:
        if row[names].strip() == 'true':
            column.append(names)

    with open('C:/Users/Arpitha Somayaji/Desktop/Fall 2017/DATA SCIENCE/Homework/MarketBasket/Modified_marketbasketData.csv','a') as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(column)
