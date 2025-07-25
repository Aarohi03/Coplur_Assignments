import sqlite3

def logout():
    username = input("Enter Username to logout: ")

    conn = sqlite3.connect("user_register.db")
    cursor = conn.cursor()

    cursor.execute("SELECT logged_in FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user is None:
        print("User not found.")
    elif user[0] == 0:
        print("You are already logged out.")
    else:
        cursor.execute("UPDATE users SET logged_in = 0 WHERE username = ?", (username,))
        conn.commit()
        print("Logout successful.")

    conn.close()

if __name__ == "__main__":
    logout()
