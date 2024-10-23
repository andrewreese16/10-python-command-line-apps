from cryptography.fernet import Fernet
import os
import json


def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)


def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}


def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)


def store_password(service, password, cipher):
    passwords = load_passwords()
    encrypted_password = cipher.encrypt(password.encode()).decode()
    passwords[service] = encrypted_password
    save_passwords(passwords)
    print(f"Password for {service} stored.")


def retrieve_password(service, cipher):
    passwords = load_passwords()
    if service in passwords:
        decrypted_password = cipher.decrypt(passwords[service].encode()).decode()
        print(f"Password for {service}: {decrypted_password}")
    else:
        print("Service not found.")


def delete_password(service):
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for {service} deleted.")
    else:
        print("Service not found.")


def menu():
    cipher = load_key()
    while True:
        print("\n=== Password Manager ===")
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            store_password(service, password, cipher)
        elif choice == "2":
            service = input("Enter the service name: ")
            retrieve_password(service, cipher)
        elif choice == "3":
            service = input("Enter the service name: ")
            delete_password(service)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()
