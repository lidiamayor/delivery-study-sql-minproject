import matplotlib.pyplot as plt
import seaborn as sns

def cancel_rate(df_cancel):
    cancel_rate = df_cancel['cancel_rate'].iloc[0]
    plt.figure(figsize=(6, 6))
    plt.pie([cancel_rate, 100 - cancel_rate], labels=['Canceled', 'Not Canceled'], autopct='%1.1f%%', startangle=90)
    plt.title('Cancel rate')
    plt.show()

def cancel_time(df_cancel_time):
    plt.figure(figsize=(10, 6))
    sns.histplot(df_cancel_time['minute_to_cancel'], bins=30, kde=True)
    plt.title('Distribution of Time Until Cancellation')
    plt.xlabel('Minutes Until Cancellation')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def avg_order(df_avg_order): 
    df_avg_order = df_avg_order.dropna().copy()
    df_avg_order['age'] = df_avg_order['age'].astype(int)

    plt.figure(figsize=(10, 4))
    sns.barplot(data=df_avg_order, x='age', y='num_orders', palette='pastel', errorbar=None, hue='age', legend=False)
    plt.title('Average Number of Orders by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Number of Orders')
    plt.xticks(rotation=45)
    plt.show()

def rate_ord(df_rate_ord):
    plt.figure(figsize=(8, 8))
    plt.pie(df_rate_ord['total_orders'], labels=df_rate_ord['sex'], autopct='%1.1f%%', colors=['lightblue', 'lightcoral'], startangle=90)
    plt.title('Percentage of Orders by Gender')
    plt.axis('equal') 
    plt.show()

def couriers(df_couriers):
    df_couriers = df_couriers.dropna().copy()
    df_couriers['age'] = df_couriers['age'].astype(int)-2
    df_couriers = df_couriers[df_couriers['age']>17]

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_couriers, x='age', y='num_couriers', hue='sex')
    plt.title('Number of Couriers by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Number of Couriers')
    plt.legend(title='Gender')
    plt.show()

def avg_deliver(df_avg_deliver):
    df_avg_deliver = df_avg_deliver.dropna().copy()
    df_avg_deliver['age'] = df_avg_deliver['age'].astype(int)
    df_avg_deliver = df_avg_deliver[df_avg_deliver['age']>17]

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_avg_deliver, x='age', y='avg_minutes_to_delivery', hue='sex', estimator='mean', errorbar=None)
    plt.title('Average Delivery Time by Age and Gender of the courier')
    plt.xlabel('Age')
    plt.ylabel('Average Minutes to Delivery')
    plt.legend(title='Gender')
    plt.show()

def users_vs_couriers(df_vs):
    category = ['total_users', 'total_couriers']
    counts = [df_vs['total_users'][0], df_vs['total_couriers'][0]]
    plt.figure(figsize=(8, 6))
    plt.bar(category, counts, color=['skyblue', 'salmon'])
    plt.title('Total Users vs Total Couriers')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.ylim(0, max(counts) * 1.1) 
    plt.grid(axis='y')
    plt.show()

def orders_by_hour(df_order_by_time):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_order_by_time, x='hour_of_day', y='total_orders', palette='pastel',hue = 'hour_of_day', legend = False, errorbar=None)
    plt.title('Total Orders by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Orders')
    plt.xticks(range(0, 24))
    plt.show()

def orders_by_day(df_order_by_time, day_order):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_order_by_time, x='day_of_week', y='total_orders', palette='pastel', order=day_order, errorbar=None, hue='day_of_week')
    plt.title('Total Orders by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Orders')
    plt.show()

def order_by_time(df_order_by_time, day_order):
    heatmap_data = df_order_by_time.pivot_table(index='hour_of_day', columns='day_of_week', values='total_orders', fill_value=0)
    heatmap_data = heatmap_data[day_order]
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g')
    plt.title('Total Orders by Week Number and Hour')
    plt.xlabel('Week Number')
    plt.ylabel('Hour of the Day')
    plt.show()