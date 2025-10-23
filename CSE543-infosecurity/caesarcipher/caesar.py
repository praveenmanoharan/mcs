#!/usr/bin/env python3

import argparse
import os
import time
import sys
import string

# Handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt", help='Decrypt a file', required=False)
parser.add_argument("-e", "--encrypt", help='Encrypt a file', required=False)
parser.add_argument("-o", "--outfile", help='Output file', required=False)

args = parser.parse_args()

encrypting = True
ciphertext = bytes

try:
    ciphertext = open(args.decrypt, "rb").read()
    print("ciphertext to be decrypted: " + str(ciphertext))
    try:
        plaintext = open(args.encrypt, "rb").read()
        print("You can't specify both -e and -d")
        exit(1)
    except Exception:
        encrypting = False
except Exception:
    try:
        plaintext = open(args.encrypt, "rb").read()
        print("text to be encrypted: " + str(plaintext))
    except Exception:
        print("Input file error (did you specify -e or -d?)")
        exit(1)


if encrypting:
    keybytes = bytes(os.urandom(1))
    keyrotate = int(keybytes[0] % 25) + 1
    print("Key is " + string.ascii_uppercase[keyrotate])

    with open("caesarkey.txt", "wb") as output:
        output.write(("Key is " + string.ascii_uppercase[keyrotate]).encode("ascii"))
        output.close()
    ciphertext = ""

    for i in range(0, len(plaintext)):
        if chr(plaintext[i]) in string.ascii_uppercase:
            p = plaintext[i] - ord('A')
            c = chr(ord('A') + ((p + keyrotate) % 26))
            ciphertext = ciphertext + c
        else:
            print("Incorrect input character %s." % plaintext[i])

    with open(args.outfile, "wb") as output:
        output.write(ciphertext.encode("ascii"))
        output.close()
else:
    keychar = open("caesarkey.txt", "rb").read()
    keyrotate = string.ascii_uppercase.index(chr(keychar[7]))
    print("Key is " + string.ascii_uppercase[keyrotate])
    plaintext = ""
    
    for i in range(0, len(ciphertext)):
        if chr(ciphertext[i]) in string.ascii_uppercase:
            c = ciphertext[i] - ord('A')
            p = chr(ord('A') + ((c - keyrotate) % 26))
            plaintext = plaintext + p
        else:
            print("Incorrect input character %s." % ciphertext[i])

    print("Decrypted text: " + plaintext)
    with open(args.outfile, "wb") as output:
        output.write(plaintext.encode("ascii"))
        output.close()
    exit(1)
