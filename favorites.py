from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = db.execute("SELECT * FROM favorites WHERE problem = 'Mario'")

print(favorite)
