import matplotlib.pyplot as plt

def visualization_analysis(df):
    # Figure 1: Total Spending Amount Over Time by Type
    plt.figure(1)
    # Aggregate the data on `Date` and `Type`
    df_agg = df.groupby(['Date', 'Type'])['Amount'].sum().reset_index()
    # Filter the DataFrame to only include rows where `Type` is 'Expense'
    df_filtered = df_agg[df_agg['Type'] == 'Expense'].copy()
    # Plot a line for the filtered data
    plt.plot(df_filtered['Date'], df_filtered['Amount'], label='Expense')
    # Rotate the x-axis labels to be more readable
    plt.gcf().autofmt_xdate(rotation=45)
    # Set the title of the plot
    plt.title('Total Spending Amount Over Time for Expenses')
    # Label the x-axis and y-axis
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    # Add a legend to the plot
    plt.legend()
    # Add gridlines to the plot
    plt.grid(True)


    # Figure 2: Total Spending Amount Over Time for Expenses
    plt.figure(2)
    # Aggregate the data on `Category` and sum the `Amount`
    df_category_agg = df.groupby('Category')['Amount'].sum().reset_index()
    # Create a bar chart using `Category` on the x-axis and `Amount` on the y-axis.
    plt.bar(df_category_agg['Category'], df_category_agg['Amount'])
    # Set the title of the chart
    plt.title('Total Spending Amount by Category')
    # Label the x-axis and y-axis
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    # Rotate the x-axis labels to be more readable
    plt.gcf().autofmt_xdate(rotation=45)


    # Figure 3: Total Spending Amount by Category
    plt.figure(3)
    # Create a pie chart using `Amount` for the size of each slice and `Category` for the labels.
    plt.pie(df_category_agg['Amount'], labels=df_category_agg['Category'], autopct='%1.1f%%')
    # Set the title of the chart
    plt.title('Distribution of Spending Across Categories')

    # Show the plot
    plt.show()

