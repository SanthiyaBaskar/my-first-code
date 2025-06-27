msg = "SANDHIYA"
encoded = ''.join(chr(ord(c) + 2) for c in msg)
print("Secret code 🔐:", encoded)
