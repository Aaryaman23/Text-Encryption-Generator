#Create a text encryption generator. This would take text as input, replaces each letter with another letter, and outputs the “encoded” message.
import string

def text_input():
        while True:
         text = input("Enter the text: ")
         if text.isdigit() :
            print("Oops! Its a number, please enter the text.")

         else:
           print(f"The following {text} text is entered")
           return text

def encryption_of_input(text, shift = 3):
    alphabet = string.ascii_lowercase         #abcdefghijklmnopqrstuvwxyz
    encrypted_text = ""

    for char in text.lower():                  #char = h
        if char in alphabet:                   #h in alphabet ;T
            new_index = (alphabet.index(char) + shift) % 26   # h is at 7th posi, so index is 7 + 3 = 10% 26 = 10 as remainder 
            encrypted_text += alphabet[new_index]    #encrypted text = encrypted_text + alphabet[10] = " " = " " + alphabet[10] //k
        else:                                        #encrypted text = k
            encrypted_text += char                      #keeps thing unchanged
    return encrypted_text                

def main():
    text = text_input()
    if text :
        encode = encryption_of_input(text)
        print(f"The encoded message is: {encode}")

if __name__ == "__main__":
    main()
