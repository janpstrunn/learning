import sqlite3
from tabulate import tabulate

db_config = {
    'database': '/path/to/sql.db'
}

connection = sqlite3.connect(**db_config)
limit = connection.cursor()

limit.execute("SELECT function, COUNT(*) AS F FROM softwares GROUP BY function ORDER BY F DESC LIMIT 20;")

result = limit.fetchall()

headers = [i[0] for i in limit.description]
print(tabulate(result, headers=headers, tablefmt="grid"))

limit.close()

function_input = input("What function are you looking for?\n")

cursor = connection.cursor()

cursor.execute("SELECT * FROM softwares WHERE FUNCTION = ?", (function_input,))

results = cursor.fetchall()

headers = [i[0] for i in cursor.description]
print(tabulate(results, headers=headers, tablefmt="grid"))

cursor.close()
connection.close()
