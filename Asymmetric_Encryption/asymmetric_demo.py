from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate private & public keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message
message = b"Hello, Asymmetric Encryption!"

# Encrypt with public key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None)
)

# Decrypt with private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None)
)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message.decode())
