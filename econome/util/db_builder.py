import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from hashlib import sha256
f="data/db.db"



def create_db():
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users( username TEXT, password TEXT)"
    c.execute(command)

def add_user(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT username FROM users WHERE username = \'" + username + "\'" #checks if username already exists
    result = c.execute(command)
    if result.fetchone() == None:
        encrypt = sha256(password).hexdigest() #encrypt password

        command = "INSERT INTO users VALUES('" + username + "','" + encrypt + "')"
        c.execute(command)

        db.commit()
        db.close()
        return True
    else:
        db.close()
        return False

def auth_user(username, password): #note: this does not differentiate between wrong password and non-existing username
    db = sqlite3.connect(f)
    c = db.cursor()
    entered_password = sha256(password).hexdigest()
    command = "SELECT password FROM users WHERE username = \'" + username + "\'"
    actual_password = c.execute(command).fetchone()[0]
    return (entered_password == actual_password)


def create_lobbies():
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS games(id INTEGER, round TEXT, drawing TEXT)"
    c.execute(command)

def add_lobby(code, creator):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "INSERT INTO games VALUES(" + str(code) + ", \'Waiting\', NULL)"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS lobby_" + str(code) + "(username TEXT, points INTEGER, drawing TEXT, word TEXT, state INTEGER)"
    c.execute(command)
    command = "INSERT INTO lobby_" + str(code) + " VALUES(\'" + creator + "\', 0, NULL, NULL, 0)"
    c.execute(command)

def add_player(lobby, username):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "INSERT INTO lobby_" + lobby + " VALUES(\'" + username + "\', 0, NULL, NULL, 0)"
    c.execute(command)

def auth_id(id_num):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT id FROM games WHERE id = " + str(id_num)
    return c.execute(command).fetchone() != None

if __name__ == "__main__":

    f = "../data/db.db"
    create_db()
    create_lobbies()
    print add_user("leo", "wat")
    print auth_user("leo", "wat")
