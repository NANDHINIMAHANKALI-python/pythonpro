from cryptography.fernet import Fernet

def generate_key(password):

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    password_encrypted = cipher_suite.encrypt(password.encode())
    return key, password_encrypted

def encrypt_file(filename, key):
    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):

    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    decrypted_data = cipher_suite.decrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def main():
    while True:
        print("\nChoose an action:")
        print("1 - Encrypt file")
        print("2 - Decrypt file")
        print("3 - Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the name of the file to encrypt: ")
            password = input("Enter a password: ")
            key, password_encrypted = generate_key(password)
            with open("key.key", 'wb') as key_file:
                key_file.write(key)
            encrypt_file(filename, key)
            print(f"File '{filename}' encrypted successfully.")
        elif choice == "2":
            filename = input("Enter the name of the file to decrypt: ")
            password = input("Enter the password: ")
            with open("key.key", 'rb') as key_file:
                key = key_file.read()
            decrypt_file(filename, key)
            print(f"File '{filename}' decrypted successfully.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
