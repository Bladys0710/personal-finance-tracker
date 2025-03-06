
def analysis_data(data,option):
    import datetime
    import pandas as pd
    #Functions
    def spending_category(data):

        #Spending by Category
        spending_category= data[(data.Type=='Expense')].pivot_table(values="Amount", index="Category", aggfunc='sum')
        print('\033[94m'+"Spending by Category:"+'\x1b[0m')
        print(spending_category)

    def average_monthly(data):
        #Average monthly
        data['month_date'] = pd.DatetimeIndex(data['Date']).month
        print(data)
        spending_month= data[(data.Type=='Expense')].pivot_table(values="Amount", index="month_date", aggfunc='mean')
        print('\033[94m'+" Average Monthly Spending:"+'\x1b[0m')
        print(spending_month)

    def top_spending(data):
        #Top average spending category
        spending_top= data[(data.Type=='Expense')].pivot_table(values="Amount", index="Category", aggfunc='mean').sort_values(by='Amount' , ascending=False)
        top_spending = spending_top["Amount"].idxmax()
        Top=spending_top.iloc[:1]
        print('\033[94m'+"Top Average Spending Category and Value:"+'\x1b[0m')
        print(Top)

    #options
    if len(data)==0:
        print("Nothing to see here. Try adding some transactions first")
        return
    if option==6:
        spending_category(data)
    if option==7:
        average_monthly(data)
    if option==8:
        top_spending(data)

