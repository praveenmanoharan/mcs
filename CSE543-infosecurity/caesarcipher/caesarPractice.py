#!/usr/bin/env python3

print ("This is a placeholder for the keyTest.py file in the caesarcipher directory.")
print (str(ord('A') ) +  " "  +  str(ord('P')) +  " "  +  str(ord('F')))


cipherText = "PRAVEEN"
keychar ="D"

def caesar_encrypt(plain_text, keychar):
    cipher_text = ""
    key = ord(keychar) %  26
    print("Key: ", key)
    for char in plain_text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            cipher_text += shifted
        else:
            cipher_text += char
    return cipher_text

encrypted = caesar_encrypt(cipherText, keychar)
print("Encrypted Text: ", encrypted)


# The above code is a simple implementation of the Caesar cipher encryption method.
# It takes a plaintext string and a key character, calculates the shift based on the key character,
#and then shifts each letter in the plaintext by that amount to produce the ciphertext.

# decrypt logic => 
# get the ord(keychar)
# get the decrypt chart (ord(char) - ord('A') - key) % 26 + ord('A')

def caesar_decrypt(cipher_text, keychar):
    plain_text = ""
    key = ord(keychar) %  26
    print("Key: ", key)
    for char in cipher_text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            plain_text += shifted
        else:
            plain_text += char
    return plain_text

decrypted = caesar_decrypt(encrypted, keychar)
print("Decrypted Text: ", decrypted)
