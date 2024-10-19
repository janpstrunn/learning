import pymysql
from tabulate import tabulate

function_input = input("What function are you looking for?: ")

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'softwares'
}

connection = pymysql.connect(**db_config)
cursor = connection.cursor()

cursor.execute("SELECT * FROM Softwares WHERE function = %s", (function_input,))

results = cursor.fetchall()

headers = [i[0] for i in cursor.description]
print(tabulate(results, headers=headers, tablefmt="grid"))

cursor.close()
connection.close()