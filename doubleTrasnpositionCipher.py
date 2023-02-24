# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:19:42 2023

@author: irfan kösesoy
"""

import math
import copy


def double_transposition_encrypt(text, key1, key2):
    """
    Encrypt or decrypt the given text using the Double Transposition Cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        key1 (int): The first encryption key.
        key2 (int): The second encryption key.


    Returns:
        str: The encrypted  text.
    """

    # Convert the keys to lists of digits
    key1 = [int(digit) for digit in str(key1)]
    key2 = [int(digit) for digit in str(key2)]

    # Calculate the dimensions of the grid based on the length of the text and the keys
    rows = math.ceil(len(text) / len(key1))
    cols = len(key1)

    # Pad the text with x characters to make it fit the grid
    padded_text = text.ljust(rows * cols, '_')

    # Create the grid
    grid = []
    for i in range(rows):
        row = [padded_text[j] for j in range(i * cols, (i + 1) * cols)]
        grid.append(row)

    # transpose of grid
    grid = list(map(list, zip(*grid)))

    grid1 = [grid[i-1] for i in key1]

    # transpose of grid
    grid12 = list(map(list, zip(*grid1)))

    grid2 = [grid12[i-1] for i in key2]

    # Flatten the grid into a string
    result = ''.join([char for row in grid2 for char in row])

    # Return the encrypted or encrypted text
    return result


def double_transposition_decrypt(text, key1, key2):
    """
    Encrypt or decrypt the given text using the Double Transposition Cipher.

    Args:
        text (str): The text to be encrypted or decrypted.
        key1 (int): The first encryption key.
        key2 (int): The second encryption key.


    Returns:
        str: The encrypted  text.
    """
    # Convert the keys to lists of digits
    key1 = [int(digit) for digit in str(key1)]
    key2 = [int(digit) for digit in str(key2)]

    # Calculate the dimensions of the grid based on the length of the text and the keys
    rows = math.ceil(len(text) / len(key1))
    cols = len(key1)

    # Pad the text with x characters to make it fit the grid
    padded_text = text.ljust(rows * cols, '_')

    # Create the grid
    grid = []
    for i in range(rows):
        row = [padded_text[j] for j in range(i * cols, (i + 1) * cols)]
        grid.append(row)


    # reverse text with key2
    gridTemp = copy.deepcopy(grid)
    for i in range(rows):
        gridTemp[key2[i]-1][:] = grid[i]


    # transpose of grid
    gridTemp = list(map(list, zip(*gridTemp)))
    result = copy.deepcopy(gridTemp)
    for i in range(cols):
        result[key1[i]-1][:] = gridTemp[i]

    # transpose of grid
    result = list(map(list, zip(*result)))


    # Flatten the grid into a string
    result = ''.join([char for row in result for char in row])
    # Return the encrypted or encrypted text
    return result


##


text = 'encrypt text'
key1 = 3124
key2 = 213
encrypted_text = double_transposition_encrypt(text, key1, key2)

decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
print(encrypted_text)
print(decrypted_text)
