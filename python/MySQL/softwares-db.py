import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'softwares'
}

connection = pymysql.connect(**db_config)
cursor = connection.cursor()

insert_query = """
INSERT INTO Softwares (name, function, alt_function, paid, open_source)
VALUES (%s, %s, %s, %s, %s)
"""

data = []

while True:
    name = input("Enter software name: ")
    if name.lower() == 'done':
        break
    function = input("Enter function: ")
    alt_function = input("Enter alternative function: ")
    paid = int(input("Enter paid status (0 for FALSE, 1 for TRUE): "))
    open_source = int(input("Enter open source status (0 for FALSE, 1 for TRUE): "))

    data.append((name, function, alt_function, paid, open_source))

cursor.executemany(insert_query, data)

connection.commit()

cursor.close()
connection.close()

print("Rows inserted successfully!")

