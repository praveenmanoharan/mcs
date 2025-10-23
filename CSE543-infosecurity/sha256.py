import hashlib

# Example 1: Hashing a string
input_string = "2XS4E8UBINPR421E"
# Encode the string to bytes, as hash functions operate on bytes
hashed_string = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
print(f"SHA-256 hash of '{input_string}': {hashed_string}")

