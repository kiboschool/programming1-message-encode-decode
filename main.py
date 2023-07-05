import base64
import sys
from cryptography.fernet import Fernet

# Mapping of letters and numerals to their Morse code representations
MORSE_TABLE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

# Morse code representations back to letters and numerals
MORSE_INVERSE = {v: k for k, v in MORSE_TABLE.items()}

# Morse
def encode_morse(message):
    """
    :param: message: string value to be encoded in Morse
    :return: Morse encoded value, using . and -
    """
    result = []
    for letter in message.upper():
        if letter in MORSE_TABLE:
            result.append(MORSE_TABLE[letter])
        else:
            return f"ERROR: {letter} cannot be encoded in Morse"
    return " ".join(result)

def decode_morse(encoded):
    """
    :param: encoded: string Morse code message using . and - 
    :return: decoded message string
    """
    result = []
    for code in encoded.split(" "):
        if code in MORSE_INVERSE:
            result.append(MORSE_INVERSE[code])
        else:
            return f"ERROR: {code} cannot be decoded in Morse"
    return "".join(result)

# Base64
def encode_base64(message):
    """
    :param: message: string value to be encoded
    :return: base64 encoded value
    """
    return base64.urlsafe_b64encode(message.encode("ascii")).decode("ascii")


def decode_base64(encoded):
    """
    :param: encoded_text: base64 string value that needs to be decoded
    :return: base64 decoded value 
    """
    return base64.urlsafe_b64decode(encoded.encode("ascii")).decode("ascii")

key = Fernet.generate_key()
f = Fernet(key)

# Fernet library encrypt / decrypt
def encrypt(plaintext):
    return f.encrypt(plaintext.encode("ascii")).decode("ascii")

def decrypt(ciphertext):
    return f.decrypt(ciphertext.encode("ascii")).decode("ascii")


# Demonstrate each of the functions on a message
def main(plaintext):
    # Morse
    morse_encoded = encode_morse(plaintext)
    print("Morse encoded: ")
    print(morse_encoded)
    decoded = decode_morse(morse_encoded)
    print("Morse decoded: ")
    print(decoded)

    # Base64
    base64_encoded = encode_base64(plaintext)
    print("\nBase64 encoded: ")
    print(base64_encoded)
    decoded = decode_base64(base64_encoded)
    print("Base64 decoded: ")
    print(decoded)

    # Encryption (AES-CBC using Fernet)
    ciphertext = encrypt(plaintext)
    print("\nEncrypted (using Fernet):")
    print(ciphertext)
    decrypted = decrypt(ciphertext)
    print("Decrypted:")
    print(decrypted)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage: python3 main.py 'your message'")

