# ASCII demo

print("The ASCII characters between 65 and 123")
for character in bytes(range(65, 123)).decode("ascii"):
    print(character, end=" ")

print("\nByte values for the string 'hello world'")
for byte in b"hello world":
    print(byte, end=" ")


