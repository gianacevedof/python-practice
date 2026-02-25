import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key  : {key}")

plain_text = input("Enter your message: ")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]
print(f"Cipher text: {cipher_text}")

while True:
    decryption = input("Enter the key of your message: ")
    if decryption == cipher_text:
        print(f"Your message is: {plain_text}")
        break
    else:
        print("Invalid key.")