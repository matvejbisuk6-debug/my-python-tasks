#Задача 1
def caesar_cipher(text, shift):

    result = ""
    for letter in text:
        result += chr(ord(letter) + shift)

    return result
text = "abc z"
shift = 1

print(caesar_cipher(text, shift))

#Задача 2
