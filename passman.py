import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_pass
    print("Account successfully added")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_pass:
        print("Login Successful")
    else:
        print("Invalid Login please check your username or password.")


def main():
    while True:
        choice = input("1 to add/create account, 2 for login, 0 exit")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()