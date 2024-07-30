import random
import string

# Define the character set
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
# word library

# Generate a random key
ENCRYPTION_KEY = random.randint(2024, 12024)
ENCRYPTION_KEY = 518
random.seed(ENCRYPTION_KEY)
random.shuffle(key)

# Encryption Function
def Encrypt_msg(text):
    plain_text = text
    cipher_text = ""

    for letter in plain_text:
        index = char.index(letter)
        cipher_text += key[index]

    return cipher_text

# Decryption Function
def Decrypt_msg(encrypted_text_):

    # Decrypt
    text_to_decode = encrypted_text_
    final_message = ""

    for letter in text_to_decode:
        index = key.index(letter)
        final_message += char[index]

    return final_message

while True:
    print("1. Encode")
    print("2. Decode")
    option = input("Enter your choice: ")

    if option == "1":
        plain_text = input("Enter your text: ")
        encoded_text = Encrypt_msg(plain_text)
        print(encoded_text)

    if option == "2":
        encoded_text = input("Enter text to decode: ")
        decoded_text = Decrypt_msg(encoded_text)
        print(decoded_text)
