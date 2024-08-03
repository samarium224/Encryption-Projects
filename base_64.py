import base64
import gzip
import lzma
import bz2
import os
import random


def get_base64_characters():
    # Base64 character set
    base64_characters = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "+/"
    )
    return list(base64_characters)

def EncodeText(plainText):
    byte_text = plainText.encode('ascii')
    base_64_text = base64.b64encode(byte_text)
    encoded_text = base_64_text.decode('ascii')
    return encoded_text

def EncodeWithCompressImage(ImgPath):
    with open(ImgPath, "rb") as f:
        data = f.read()

    compressed_data = lzma.compress(data)
    compressed_data = base64.b64encode(compressed_data)
    print(compressed_data)
    return compressed_data

def WriteEncodedFileAsText(encoded_data, output_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "wb") as f:
        f.write(encoded_data)


key = get_base64_characters()
print(key)

ENCRYPTION_KEY = 112
random.seed(ENCRYPTION_KEY)
random.shuffle(key)

print(key)
# # Example usage
# img_path = r"E:\Friends\Encryption\Assets\3.jpg"
# encoded_data = EncodeWithCompressImage(img_path)

# output_path = r"E:\Friends\Encryption\Encoded\3.bin"
# WriteEncodedFileAsText(encoded_data, output_path)

# print(f"Encoded data written to {output_path}")
