# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:58:11 2023

@author: irfan kösesoy
"""


def vigenere_cipher(text, key, mode='encrypt'):
    """
    Encrypt or decrypt the given text using the Vigenère cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        key (str): The encryption key.
        mode (str): 'encrypt' or 'decrypt'. Defaults to 'encrypt'.

    Returns:
        str: The encrypted or decrypted text.
    """

    # Create a list to hold the result
    result = []

    # Convert the text and key to uppercase
    text = text.upper()
    key = key.upper()

    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Loop over the text
    for i in range(len(text)):
        # Get the current character in the text
        char = text[i]

        # Get the corresponding key character
        key_char = key[i % len(key)]

        # Get the index of the current and key characters in the alphabet
        char_index = alphabet.find(char)
        key_char_index = alphabet.find(key_char)
        if char_index == -1:
            result.append(char)
        else:

            # Encrypt or decrypt the current character
            if mode == 'encrypt':
                new_index = (char_index + key_char_index) % 26
            else:
                new_index = (char_index - key_char_index) % 26

            # Add the encrypted or decrypted character to the result list
            result.append(alphabet[new_index])

    # Convert the result list to a string and return it

    return ''.join(result)


text = 'HELLO WORLD'
key = 'password'
encrypted_text = vigenere_cipher(text, key)
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
print(encrypted_text)
print(decrypted_text)
