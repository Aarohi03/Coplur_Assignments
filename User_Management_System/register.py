import getpass
import sqlite3
import hashlib

# User registration
def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    conn = sqlite3.connect("user_register.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        logged_in INTEGER DEFAULT 0
    )
    ''')

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists. Try a different one.")
    else:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        print("You are registered successfully!")

    conn.close()

if __name__ == "__main__":
    register()

