import pandas as pd
import mysql.connector
from config import MYSQL_PASSWORD

#load csv file
df = pd.read_csv('C:/Users/shiv/Downloads/movie.csv')

#checking shape of data
print(df.shape)
#print some rows
print(df.head(2))

# Create MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=MYSQL_PASSWORD,
    database='sentiment_analysis'
)

cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("INSERT INTO reviews (text, sentiment) VALUES (%s, %s)", (row['text'], row['label']))
conn.commit()
cursor.close()
conn.close()