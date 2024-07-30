import random
import string

# Define the character set
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
# word library

word_library = {
    '00000': "Hi.",
    '00001': "What are you doing?",
    '00010': "You forgot?",
    '00011': "Feeling good?",
    '00100': "Be happy.",
    '00101': "Call me.",
    '00110': "Check this.",
    '00111': "Do that.",
    '01000': "Email me.",
    '01001': "Forget it.",
    '01010': "Get ready.",
    '01011': "Have fun.",
    '01100': "Help me.",
    '01101': "Join us.",
    '01110': "Keep calm.",
    '01111': "Let me know.",
    '10000': "Love you.",
    '10001': "Meet me.",
    '10010': "Never mind.",
    '10011': "Okay, sure.",
    '10100': "Perfect day.",
    '10101': "Quick check.",
    '10110': "Relax now.",
    '10111': "See you.",
    '11000': "Take care.",
    '11001': "Try again.",
    '11010': "Update me.",
    '11011': "Very good.",
    '11100': "Well done.",
    '11101': "Yes, please.",
    '11110': "Zoom in.",
    '11111': "Absolutely.",
    # Add more entries as needed until all binary strings up to '11111'
}

# Generate a random key
ENCRYPTION_KEY = random.randint(2024, 12024)
ENCRYPTION_KEY = 224
random.seed(ENCRYPTION_KEY)
random.shuffle(key)

# Encryption Function
def Encrypt_msg(text, encryption_key = 224):
    plain_text = text
    cipher_text = ""
    meaningful_sentence = ""

    for letter in plain_text:
        index = char.index(letter)
        cipher_text += key[index]

    for encodedLetter in cipher_text:
        keyIndex = key.index(encodedLetter)
        meaningful_sentence += word_library[keyIndex]

    return meaningful_sentence

# Decryption Function
def Decrypt_msg(encrypted_text_, encryption_key = 224):

    # Decrypt
    encrypted_wordbox = encrypted_text_.split('.')
    decrypted_text = []

    for sentense in encrypted_wordbox: 
        value = {i for i in word_library if word_library[i] == sentense}
        print(value)

    final_message = encrypted_wordbox

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
