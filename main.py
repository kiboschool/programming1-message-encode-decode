import sys

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
    return "TODO: encode_morse"

def decode_morse(encoded):
    """
    :param: encoded: string Morse code message using . and - 
    :return: decoded message string
    """
    return "TODO: decode_morse"

# Base64
def encode_base64(message):
    """
    :param: message: string value to be encoded
    :return: base64 encoded value
    """
    return "TODO: encode_base64"

def decode_base64(encoded):
    """
    :param: encoded: base64 string value that needs to be decoded
    :return: base64 decoded value 
    """
    return "TODO: decode_base64"

# Fernet library encrypt / decrypt
def encrypt(plaintext):
    return "TODO: encrypt with Fernet"

def decrypt(ciphertext):
    return "TODO: decrypt with Fernet"


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

