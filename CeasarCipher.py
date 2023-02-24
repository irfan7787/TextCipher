# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:45:04 2023

@author: irfan kösesoy
"""

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt the given text using the Caesar cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The number of positions to shift the letters in the alphabet.
        mode (str): 'encrypt' or 'decrypt'. Defaults to 'encrypt'.

    Returns:
        str: The encrypted or decrypted text.
    """

    # Create a list to hold the result
    result = []

    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Loop over the text
    for char in text:
        # Get the index of the current character in the alphabet
        char_index = alphabet.find(char.upper())

        # If the character is not in the alphabet, leave it as is
        if char_index == -1:
            result.append(char)
        else:
            # Encrypt or decrypt the current character
            if mode == 'encrypt':
                new_index = (char_index + shift) % 26
            else:
                new_index = (char_index - shift) % 26

            # Add the encrypted or decrypted character to the result list
            result.append(alphabet[new_index])

    # Convert the result list to a string and return it
    return ''.join(result)



##  

text = 'selam'
shift = 3
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(encrypted_text)
print(decrypted_text)
