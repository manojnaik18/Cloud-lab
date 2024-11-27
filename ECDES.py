from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate private and public keys
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Display public key in PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Public Key (PEM format):\n", public_pem.decode())

# Sign the message
message = input("Enter a message to sign: ").encode()
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
print("Signature:", signature)

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid.")
except:
    print("Signature verification failed.")
