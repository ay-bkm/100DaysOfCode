import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
iscontinue = True


def caesar(plain_text, shift_amount, direct):
        result= ""
        for letter in plain_text:
            if letter not in alphabet:
                result += letter
            else:
                indexL = alphabet.index(letter)
                
                if direct == "encode":
                    if indexL + shift_amount > 25:
                            indexL = -1
                    f_letter = alphabet[indexL + shift_amount]
                elif direct == "decode":
                    if indexL - shift_amount < 0:
                            indexL = 26
                    f_letter = alphabet[indexL - shift_amount]
                result += f_letter
        print(result)
while iscontinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
        

    shift = shift%26
    caesar(text, shift, direction)
    answer = input("Do you want to continue \"yes\" or \"no\" ?").lower()
    if answer == "no":
        iscontinue = False
        print("Goodbye!")

