# CryptoMessenger v1.0.0
# Powered by Karthik
# Encrypt Messages
from cryptography.fernet import Fernet

def generate_key(password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    with open('encryption_key.txt', 'wb') as f:
        f.write(key)
    with open('password.txt', 'wb') as f:
        f.write(encrypted_password)

def encrypt_message(message, password):
    key, cipher_suite = load_key_and_cipher_suite(password)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, password):
    key, cipher_suite = load_key_and_cipher_suite(password)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

def load_key_and_cipher_suite(password):
    with open('encryption_key.txt', 'rb') as f:
        key = f.read()
    with open('password.txt', 'rb') as f:
        encrypted_password = f.read()
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    if decrypted_password.decode() != password:
        raise ValueError("Incorrect password!")
    return key, cipher_suite

def main():
    choice = int(input("Enter '1' to encrypt or '2' to decrypt: "))
    password = input("Enter your password: ")

    if choice == 1:
        message = input("Enter the message you want to encrypt: ")
        generate_key(password)
        encrypted_message = encrypt_message(message, password)
        print("Encrypted message:", encrypted_message.decode())
    elif choice == 2:
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_message(encrypted_message.encode(), password)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
