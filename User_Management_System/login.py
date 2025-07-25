import sqlite3
import hashlib

# User login
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    conn = sqlite3.connect("user_register.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password, logged_in FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user is None:
        print("User not found.")
    elif user[1] == 1:
        print("User is already logged in.")
    else:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        if hashed_input == user[0]:
            cursor.execute("UPDATE users SET logged_in = 1 WHERE username = ?", (username,))
            conn.commit()
            print("Login successful!")
        else:
            print("Incorrect password.")

    conn.close()

if __name__ == "__main__":
    login()

