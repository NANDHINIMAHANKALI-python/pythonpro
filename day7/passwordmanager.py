import json
from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)


def load_passwords(filename):
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            return json.loads(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_passwords(filename, passwords):
    data = json.dumps(passwords)
    encrypted_data = cipher_suite.encrypt(data.encode())
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def main():
    password_file = "passwords.json"  

    passwords = load_passwords(password_file)

    while True:
        print("Choose an action:")
        print("1 - Add password")
        print("2 - Retrieve password")
        print("3 - Update password")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            passwords[account] = password
            save_passwords(password_file, passwords)
            print("Password added.")
        elif choice == '2':
            account = input("Enter the account name: ")
            if account in passwords:
                print(f"Password for {account}: {passwords[account]}")
            else:
                print("Account not found.")
        elif choice == '3':
            account = input("Enter the account name: ")
            if account in passwords:
                new_password = input("Enter the new password: ")
                passwords[account] = new_password
                save_passwords(password_file, passwords)
                print("Password updated.")
            else:
                print("Account not found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
