from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
message = "Hello, Symmetric Encryption!"
encrypted_message = cipher.encrypt(message.encode())

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Secret Key:", key.decode())
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
