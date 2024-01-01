from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = "SELECT * FROM favorites WHERE problem = 'Mario'"

print(favorite)
