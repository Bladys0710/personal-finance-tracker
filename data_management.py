

def delete_transaction(data):
    import datetime
    import pandas as pd
    #function:
    def delete_entry(data,value):
        for x in data.index:
            if int(x) == int(value):
                data.drop(x, inplace=True)
        print('\033[94m'+"Transaction deleted successfully"+'\x1b[0m')
        print('\033[94m'+"Current Data:"+'\x1b[0m')
        data.index= range(0, len(data))
        print(data)
    #Data validation
    if len(data)==0:
        print("Nothing to see here. Try adding some transactions first")
        return
    #index
    while True:
        value = input('\033[94m'+"please Enter the index of the transaction to delete:"+'\x1b[0m')
        try:
            if (int(value) >=0  and int(data.iloc[[value]].size) > 0):
                print("Current transaction details:")
                print(data.iloc[[value]])
                break  # valid choice
        except:
            print("Invalid entry. Please try again") # Invalid = loop

    while True:
        sure = input("Are you sure you want to delete the transaction? (Y/N)").strip().upper()
        if sure in ["Y", "N"]:
            break # Valid Choice
        print("Invalid choice! Please, try again.") # Invalid = loop

    if sure=="y" or sure=="Y":
        delete_entry(data,value)
    else:
        return



def edit_transaction(data):
    import datetime
    import pandas as pd
    # Function
    def edit_entry(data,date_new,value):
        if date_new !="":
            for x in data.index:
                if int(x) == int(value):
                    data.loc[x, "Date"]= date_new
        if category_new != "":
            for x in data.index:
                if int(x) == int(value):
                    data.loc[x, "Category"]= category_new
        if description_new != "":
            for x in data.index:
                if int(x) == int(value):
                    data.loc[x, "Description"]= description_new
        if amount_new !="":
            for x in data.index:
                if int(x) == int(value):
                    data.loc[x, "Amount"]= int(amount_new)
        if type_new != "":
            for x in data.index:
                if int(x) == int(value):
                    data.loc[x, "Type"]= type_new
        print('\033[94m'+"Transaction updated successfully"+'\x1b[0m')
        print(data.iloc[[value]])
    #Data validation
    if len(data)==0:
        print("Nothing to see here. Try adding some transactions first")
        return
    #index
    while True:
        value = input('\033[94m'+"please Enter the index of the transaction to edit:"+'\x1b[0m')
        try:
            if (int(value) >=0  and int(data.iloc[[value]].size) > 0):
                print("Current transaction details:")
                print(data.iloc[[value]])
                break  # valid choice
        except:
            print("Invalid entry. Please try again") # Invalid = loop

    #date
    while True:
        date_new = input('\033[94m'+"Enter new date (YYYY-MM-DD) or press Enter to keep current:"+'\x1b[0m').strip()
        try:
            if date_new=="":
                break
            DateTransaction = datetime.datetime.strptime(date_new, "%Y-%m-%d").date()
            today = datetime.date.today()
            if DateTransaction < today:
                print('\033[94m'+"The Date of transaction can't be past date."+'\x1b[0m')
                continue
            if len(date_new) != 10 :
                print('\033[94m'+"Invalid Date of transaction.)"+'\x1b[0m')
                continue
            else:
                break
        except ValueError:
            print('\033[94m'+"Invalid Date of transaction. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)"+'\x1b[0m')
            continue

    #category
    category_new = input('\033[94m'+"Enter new category or press Enter to keep current:"+'\x1b[0m')
    #Description
    description_new = input('\033[94m'+"Enter new description or press Enter to keep current:"+'\x1b[0m')
    #Amount
    while True:
        amount_new = input('\033[94m'+"Enter new amount or press Enter to keep current:"+'\x1b[0m')
        if amount_new=="":
            break # No updates
        try:
            if int(amount_new):
                break  # valid choice
        except:
            print("Invalid entry. Please try again")
    #Type
    while True:
        type_new = input('\033[94m'+"Enter new Type or press Enter to keep current:"+'\x1b[0m')
        if type_new =="":
            break
        if type_new =='Expense'or type_new =='Income':
            break
        else:
            print('\033[94m' + "Invalid Type please enter Expense or Income" + '\x1b[0m')

    edit_entry(data,date_new,value)