import hashlib
import sys
import os

def is_valid_filename(filename):
    if not isinstance(filename, str):
        return False

    # Check if the filename is empty
    if len(filename.strip()) == 0:
        return False

    # Check if the filename contains any invalid characters
    invalid_chars = set(r'<>:"/\|?*')
    if any(char in invalid_chars for char in filename):
        return False

    # Check if the file exists
    if os.path.isfile(filename):
        return True

    return False



while True:
    filename = input("file: ")
    if (is_valid_filename(filename)):
        with open(filename,"rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest()
        break
    print("Filename not found, try again.\n")

    
token = input("Authentication: ")

if (token.upper() == readable_hash.upper()):
    print("File verified.")

else:
    print("Cannot verify file!")

