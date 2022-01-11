from caesar_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def casesar(start_text,shift_amount,cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            shift_change = alphabet.index(char) + shift_amount
            if shift_change > 25:
                shift_change %= 26
            final_text += alphabet[shift_change]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}")
should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    casesar(start_text=text,shift_amount=shift, cipher_direction=direction)
    result = input('Type "yes" to go again. Otherwise type "no".')
    if result == "no":
        should_continue = False
        print("Good Bye!")
