import sqlite3

db_config = {
    'database': '/path/to/sqlite.db'
}

connection = sqlite3.connect(**db_config)
cursor = connection.cursor()

insert_query = """
INSERT INTO Softwares (software, function, alt_function, paid, desktop, mobile, open_source)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

data = []

while True:
    software = input("Enter software name: ")
    if software.lower() == 'done':
        break
    function = input("Enter function: ")
    alt_function = input("Enter alternative function: ")
    paid = int(input("Enter paid status (0 for FALSE, 1 for TRUE): "))
    desktop = int(input("Is it available for desktop (0 for FALSE, 1 for TRUE): "))
    mobile = int(input("Is it available for mobile (0 for FALSE, 1 for TRUE): "))
    open_source = int(input("Enter open source status (0 for FALSE, 1 for TRUE): "))

    data.append((software, function, alt_function, paid, desktop, mobile, open_source))

cursor.executemany(insert_query, data)

connection.commit()

cursor.close()
connection.close()

print("Rows inserted!")

