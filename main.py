import pandas as pd
# import functions

from data_management import delete_transaction,edit_transaction
from data_analysis import analysis_data

print("""
 _                          __                     ___                  
|_) _  __ _  _ __  _  |    |_  o __  _ __  _  _     |  __ _  _  |  _  __
|  (/_ | _> (_)| |(_| |    |   | | |(_|| |(_ (/_    |  | (_|(_  |<(/_ | 

""")

value = 0
datas = []
while value == 0:
    while True:
        print("""
        Main Menu:
        0. Import a CSV File
        1. View All Transactions
        2. View Transactions by Date Range
        3. Add a Transaction
        4. Edit a Transaction
        5. Delete a Transaction
        6. Analyze Spending by Category
        7. Calculate Average Monthly Spending
        8. Show Top Spending Category
        9. Visualize Monthly Spending Trend
        10. Save Transactions to CSV
        11. Exit""")
        option = input('\033[94m' + "please choose an option (1-11):" + '\x1b[0m')
        try:
            if (int(option) >= 0 and int(option) <= 11):
                break
        except:
            print("Invalid entry. Please try again")  # Invalid = loop
    opt = int(option)
    if int(option) == 0:
        datas = pd.read_csv('sampledata.cvs')
        print("Data was imported")
    if int(option) == 1:
        if len(datas) == 0:
            print("Nothing to see here. Try adding some transactions first")
        else:
            print("All Transactions:")
            print(datas)
    if int(option) == 2:
        print("")
    if int(option) == 3:
        print("")
    if int(option) == 4:
        edit_transaction(datas)
    if int(option) == 5:
        delete_transaction(datas)
    if int(option) == 6:
        analysis_data(datas, opt)
    if int(option) == 7:
        analysis_data(datas, opt)
    if int(option) == 8:
        analysis_data(datas, opt)
    if int(option) == 9:
        print("")
    if int(option) == 10:
        datas.to_csv("sampledata.csv")
        print("transactions saved successfully")
    if int(option) == 11:
        print("Have a good day")
        value = 1



