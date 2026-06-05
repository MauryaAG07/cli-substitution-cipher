import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters #imports symbols, digits, and letters, lower and upper.
    #instead of using string.whitespace, to avoid extraneous symbols we simply use " "
chars = list(chars)
key = chars.copy()
random.shuffle(key) #randomly shuffles the order of characters in the sequence
#print(chars)
#print(key)         #test for randomization, keep commented for practicality of program.
#ENCRYPTING
def main():
    def encrypt():
        plain_text = input("Enter the text to be encrypted: ")
        cipher_text = ""
        for char in plain_text:
            index = chars.index(char) #chars.index creates a list of index to include every value of chars
            cipher_text += key[index] #key is a different assort of same values. key[index] makes a new string using the list sequence of keys
        print(f"Original text: {plain_text}")
        print(f"Encrypted text:{cipher_text}")
    encrypt()

    #DECRYPTING
    def decrypt():
        plain_text = ""
        cipher_text = input("Enter the text to be decrypted: ")
        for char in cipher_text:
            index = key.index(char) #key.index because we are converting from key to chars
            plain_text += chars[index] #creating the sequence string of chars
        print(f"Encrypted text:{cipher_text}")
        print(f"Deciphered text: {plain_text}")
    decrypt()

if __name__ == "__main__":
    main()
