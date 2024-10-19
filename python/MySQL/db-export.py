import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="softwares"
)

query = "SELECT * FROM Softwares"
df = pd.read_sql(query, conn)
df.to_csv('/home/$USER/tmp/backup.csv', index=False)
print("Done!"