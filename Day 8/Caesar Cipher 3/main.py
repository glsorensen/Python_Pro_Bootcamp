from art import logo

# Print the logo at the start
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    result_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = (position + shift) % 26
            elif direction == 'decode':
                new_position = (position - shift) % 26
            new_char = alphabet[new_position]
            result_text += new_char
        else:
            result_text += char  # Leave non-alphabet characters unchanged

    if direction == 'encode':
        print(f"The encoded text is: {result_text}")
    elif direction == 'decode':
        print(f"The decoded text is: {result_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart != 'yes':
        should_continue = False
        print("Goodbye!")



