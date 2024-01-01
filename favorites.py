from cs50 import SQL

db = SQL("sqlite:///favorites.db")

SELECT * FROM favorites WHERE problem = 'Mario';
