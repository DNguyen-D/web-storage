import utils.client_request as client_request

SERVER_URL = "http://127.0.0.1:5000/api"


def signup():
    print("\n=== SIGN UP ===")
    user = input("Username: ")
    password = input("Password: ")

    payload = {
        "action": "signup",
        "user": user,
        "password": password
    }

    result = client_request.post(SERVER_URL, payload)
    print("Server response:", result)


def login():
    print("\n=== LOGIN ===")
    user = input("Username: ")
    password = input("Password: ")

    payload = {
        "action": "login",
        "user": user,
        "password": password
    }

    result = client_request.post(SERVER_URL, payload)
    print("Server response:", result)


def main():
    while True:
        print("\n==== USER MENU ====")
        print("1) Sign Up")
        print("2) Login")
        print("3) Exit")

        choice = input("Select option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()