import pandas as pd
from sqlalchemy import create_engine, text
import pymysql

# Your connection parameters
bd = "delivery"
password = ""  # Replace this with your actual password
connection_string = 'mysql+pymysql://root:' + password + '@localhost/' + bd
engine = create_engine(connection_string)

# Sample DataFrame
'''url = 'Database/users.csv'
df = pd.read_csv(url)
df['birth_date'] = pd.to_datetime(df['birth_date'], format = '%d/%m/%y')'''

'''url = 'Database/couriers.csv'
df = pd.read_csv(url)
df['birth_date'] = pd.to_datetime(df['birth_date'], format = '%d/%m/%y')'''

'''url = 'Database/orders.xlsx'
df = pd.read_excel(url)'''

'''url = 'Database/user_actions.csv'
df = pd.read_csv(url)
users = pd.read_csv('Database/users.csv')
valid_user_ids = users['user_id'].unique()
df = df[df['user_id'].isin(valid_user_ids)]
df['time'] = pd.to_datetime(df['time'], format='%d/%m/%y %H:%M')'''

url = 'Database/courier_actions.csv'
df = pd.read_csv(url)
courier = pd.read_csv('Database/couriers.csv')
valid_courier_ids = courier['courier_id'].unique()
df = df[df['courier_id'].isin(valid_courier_ids)]
df['time'] = pd.to_datetime(df['time'], format='%d/%m/%y %H:%M')

# Send DataFrame a MySQL
table_name = 'courier_actions' # change this with the correct name of the table
df.to_sql(table_name, con=engine, if_exists='append', index=False)