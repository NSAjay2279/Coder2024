from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Enter your favorite: ")

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

for row in rows:
    print(row['n'])
