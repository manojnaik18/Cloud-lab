def calculate_key(base, exponent, modulus):
    return pow(base, exponent, modulus)

prime = int(input("Enter a large prime number: "))
base = int(input("Enter the base: "))

# Alice's keys
alice_private = int(input("Enter Alice's private key: "))
alice_public = calculate_key(base, alice_private, prime)
print("Alice's public key:", alice_public)

# Bob's keys
bob_private = int(input("Enter Bob's private key: "))
bob_public = calculate_key(base, bob_private, prime)
print("Bob's public key:", bob_public)

# Shared secrets
alice_shared = calculate_key(bob_public, alice_private, prime)
bob_shared = calculate_key(alice_public, bob_private, prime)

if alice_shared == bob_shared:
    print("Success! The shared secret is:", alice_shared)
else:
    print("Error! Shared keys do not match.")
