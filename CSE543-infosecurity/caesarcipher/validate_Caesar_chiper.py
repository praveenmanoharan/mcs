#!/opt/pwn.college/python

import glob
import hashlib

EXPECTED = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"


def validateCaesarchiper():
    # find caesarplaintext.txt
    if 'caesarplaintext.txt' not in glob.glob("*"):
        print('caesarplaintext.txt is not found.')
        return

    # open caesarplaintext.txt
    with open('caesarplaintext.txt', 'rb') as f:
        data = f.read()

    # try to decode it
    try:
        txt = data.decode("ascii")
    except UnicodeDecodeError:
        print('caesarplaintext.txt cannot be decoded as ASCII text.')
        return

    txt = txt.strip("\r\n ")
    print(txt)
    checksum = hashlib.sha256(txt.encode("ascii")).hexdigest()

    print("checksum: " + checksum)

    if checksum == EXPECTED:
        print("Good job!")
        print("Here is your flag:")
        # with open("/flag", "r") as f:
        #     print(f.read())
    else:
        print("Incorrect plaintext.")


if __name__ == "__main__":
    validateCaesarchiper()
