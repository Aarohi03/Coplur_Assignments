import sqlite3
import hashlib

def change_password():
    username = input("Enter Username: ")

    conn = sqlite3.connect("user_register.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password, logged_in FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user is None:
        print("User not found.")
    elif user[1] == 0:
        print("You are not logged in. Login first to change password.")
    else:
        current_password = input("Enter Current Password: ")
        hashed_current = hashlib.sha256(current_password.encode()).hexdigest()

        if hashed_current != user[0]:
            print("Current password is incorrect.")
        else:
            new_password = input("Enter New Password: ")
            confirm_password = input("Confirm New Password: ")

            if new_password != confirm_password:
                print("Passwords do not match.")
            else:
                hashed_new = hashlib.sha256(new_password.encode()).hexdigest()
                cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new, username))
                conn.commit()
                print("Password changed successfully.")

    conn.close()

if __name__ == "__main__":
    change_password()
