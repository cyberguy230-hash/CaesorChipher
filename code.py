alphabet = input("enter text:")
shift = int(input("how much shift you need:"))
def cipher():
    cipher_txt = alphabet[shift:] + alphabet[0:shift]
    return cipher_txt

print(cipher())

