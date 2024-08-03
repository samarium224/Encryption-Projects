import base64
import gzip
import lzma
import bz2
import os
import random
import string

def get_base64_characters():
    # Base64 character set
    base64_characters = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "+/"
    )
    return list(base64_characters)

# Encryption Function
def Encrypt_msg(text, char_, key_):
    plain_text = text
    cipher_text = ""
    for letter in plain_text:
        index = char_.index(letter)
        cipher_text += key_[index]

    return cipher_text

# Decryption Function
def Decrypt_msg(encrypted_text_, char_, key_):
    # Decrypt
    text_to_decode = encrypted_text_
    final_message = ""

    for letter in text_to_decode:
        if letter == '':
            continue
        index = key_.index(letter)
        final_message += char_[index]

    return final_message

def EncryptWithB64Text(plainText, char_, key_):
    encrypted_text = Encrypt_msg(plainText, char_, key_)
    byte_text = encrypted_text.encode('ascii')
    base_64_text = base64.b64encode(byte_text)
    encoded_text = base_64_text.decode('ascii')
    return encoded_text

def DecryptWithB64Text(plainText, char_, key_):
    decoded_text = plainText.encode('ascii')
    base64_decode = base64.b64decode(decoded_text)
    decoded_text = base64_decode.decode('ascii')
    decrypted_text = Decrypt_msg(decoded_text, char_, key_)
    return decrypted_text

def EncryptImage(ImgPath, char_, key_, OutputPath = None, filename = "Test.txt"):
    with open(ImgPath, "rb") as f:
        data = f.read()
    encoded_data = base64.b64encode(data).decode('ascii')
    encoded_data = EncryptWithB64Text(encoded_data, char_, key_)
    encoded_data = encoded_data.encode('ascii')

    output_path = r"E:\Friends\Encryption\Encrypted"
    os.makedirs(os.path.dirname(os.path.join(output_path, filename)), exist_ok=True)
    output_img_path = os.path.join(output_path, filename)

    with open(output_img_path, "wb") as f:
        f.write(encoded_data)

    return output_img_path

def DecryptImage(ImgPath, char_, key_, OutputPath = None, filename = "Test.png"):
    with open(ImgPath, "rb") as f:
        data = f.read()

    decoded_data = data.decode('ascii')
    decoded_data = DecryptWithB64Text(decoded_data, char_, key_)
    decoded_data = base64.b64decode(decoded_data)

    output_path = r"E:\Friends\Encryption\Decrypted"
    os.makedirs(os.path.dirname(os.path.join(output_path, filename)), exist_ok=True)

    with open(os.path.join(output_path, filename), "wb") as f:
        f.write(decoded_data)

    return True


def WriteEncodedFileAsText(encoded_data, output_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "wb") as f:
        f.write(encoded_data)


char = list(" " + string.punctuation + string.digits + string.ascii_letters)
# print(char)

key = char.copy()

ENCRYPTION_KEY = 518
random.seed(ENCRYPTION_KEY)
random.shuffle(key)

data = EncryptImage(r"E:\Friends\Encryption\Assets\0.png", char, key)
# data = r"E:\Friends\Encryption\Encrypted\Test.txt"
output = DecryptImage(data,char, key)