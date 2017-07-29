import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    car = [
        ('Ford', 'F150', 10),
        ('Ford', 'Crown Victoria', 15),
        ('Ford', 'Explorer', 16),
        ('Honda', 'Accord', 16),
        ('Honda', 'Oydessy', 18)
    ]

    c.executemany('INSERT INTO inventory VALUES(?,?,?)', car)
