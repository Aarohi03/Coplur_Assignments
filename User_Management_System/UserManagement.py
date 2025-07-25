import os

def main():
    while True:
        print('''
        \n--- User Management System ---
        1. Register
        2. Login
        3. Logout
        4. Change Password
        5. Exit
        ''')
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            os.system("python register.py")
        elif choice == '2':
            os.system("python login.py")
        elif choice == '3':
            os.system("python logout.py")
        elif choice == '4':
            os.system("python change_password.py")
        elif choice == '5':
            print("Exiting...Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
