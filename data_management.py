import pandas as pd
from datetime import datetime


def add_transaction(datas):

    def transaction_date():
        while True:  # Loop until a valid date is entered
            t_date_str = input('\033[94m' + "Please enter the transaction date (YYYY-MM-DD): "+'\x1b[0m')
            # Validate the input of the user. If there is an error, request another input.
            try:
                # Validate the user input.
                t_date = datetime.strptime(t_date_str, "%Y-%m-%d")
                # Format the time before returning
                return t_date.strftime("%Y-%m-%d")
            except ValueError:
                print('\033[94m' + "Invalid date format. Please use YYYY-MM-DD"+'\x1b[0m')
    t_date = transaction_date()

    def transaction_category():
        print('\033[94m' + "Set the category. Chose one, please:"+'\x1b[0m')
        print(" (1) Food")
        print(" (2) Rent")
        print(" (3) Utilities")
        print(" (4) Transport")
        print(" (5) Income")
        while True:
            p_choice = input('\033[94m' + "Enter your choice: "+'\x1b[0m')
            if p_choice == "1":
                return "Food"
            elif p_choice == "2":
                return "Rent"
            elif p_choice == "3":
                return "Utilities"
            elif p_choice == "4":
                return "Transport"
            elif p_choice == "5":
                return "Income"
            else:
                print('\033[94m' + "Sorry, please enter a valid option"+'\x1b[0m')
    t_category = transaction_category()

    def transaction_description():
        while True:
            descript = input('\033[94m' + "Please enter a description: "+'\x1b[0m')
            if descript == "":
                print('\033[94m' + "Please enter a valid description."+'\x1b[0m')
            # Check the first character of the descript. It must be a letter!
            elif not descript[0].isalpha():
                print('\033[94m' + "Please enter a valid description. Must start with a letter"+'\x1b[0m')
            elif len(descript) > 50:
                print('\033[94m' + "Please enter a valid description. 50 characters maximum"+'\x1b[0m')
            else:
                # Capitalize the input
                descript = descript.title()
                return descript
    t_description = transaction_description()

    def transaction_amount():
        while True:
            amount = input('\033[94m' + "Please enter the amount: "+'\x1b[0m')
            if amount == "":
                print('\033[94m' + "Please enter a valid amount."+'\x1b[0m')
            # validate the user input
            elif not amount.isdigit():
                print('\033[94m' + "Please enter a valid amount. Only numbers"+'\x1b[0m')
            else:
                amount = float(amount)
                return amount
    t_amount = transaction_amount()

    def transaction_type():
        print('\033[94m' + "Set the priority. Please, chose one of the following options:"+'\x1b[0m')
        print(" (1) Expense")
        print(" (2) Income")
        while True:
            p_choice = input('\033[94m' + "Enter your choice: "+'\x1b[0m')
            if p_choice == "1":
                return "Expense"
            elif p_choice == "2":
                return "Income"
            else:
                print('\033[94m' + "Sorry, please enter a valid option"+'\x1b[0m')
    t_type = transaction_type()

    transaction = {"Date": t_date, "Category": t_category, "Description": t_description, "Amount": t_amount, "Type": t_type}
    # Convert the new data to a DataFrame
    transaction_df = pd.DataFrame([transaction])
    # Append the new data to the existing DataFrame using pd.concat
    datas = pd.concat([datas, transaction_df], ignore_index=True)
    print("\n")
    print('\033[94m' + f"The transaction '{t_date}', '{t_category}', '{t_description}' '{t_amount}' and '{t_type} was added."+'\x1b[0m')
    print("\n")
    return datas


def view_by_date_range(datas):
    start_date = input("Please enter start date (YYYY-MM-DD): ")
    end_date = input("Please enter end date (YYYY-MM-DD): ")

    # Convert the 'Date' column to datetime format
    datas['Date'] = pd.to_datetime(datas['Date'])
    # Convert user input to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_trans = datas[(datas['Date'] >= start_date) & (datas['Date'] <= end_date)]

    # Check if the filtered DataFrame is empty
    if filtered_trans.empty:
        print("No transactions in the specified date range.")
    else:
        print("Transactions within the range:")
        print(filtered_trans)


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