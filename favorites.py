from cs50 import SQL

db = SQL("sqlite:///favorites.db")

rows = db.execute("SELECT COUNT(*) FROM favorites WHERE problem = 'Mario'")

for row in rows:
    print(row[])
