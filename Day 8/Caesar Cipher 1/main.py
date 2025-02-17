alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            # Find the current position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position with wrap-around using modular arithmetic
            new_position = (position + shift_amount) % 26
            # Get the new character from the alphabet
            new_char = alphabet[new_position]
            encrypted_text += new_char
        else:
            # If the character is not in the alphabet (e.g., space, punctuation), keep it unchanged
            encrypted_text += char

    print(f"The encoded text is: {encrypted_text}")


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            # Find the current position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position with wrap-around using modular arithmetic
            new_position = (position - shift_amount) % 26
            # Get the new character from the alphabet
            new_char = alphabet[new_position]
            decrypted_text += new_char
        else:
            # If the character is not in the alphabet (e.g., space, punctuation), keep it unchanged
            decrypted_text += char

    print(f"The decoded text is: {decrypted_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)