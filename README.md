# Symmetric Cipher Algorithms

This repository contains Python implementations of several symmetric cipher algorithms, including the Ceaser Cipher, Double Transition Cipher, and Vigenere Cipher. Symmetric ciphers use the same key for both encryption and decryption, and are commonly used to protect the confidentiality of data.

## Ciphering Algorithms

### Ceaser Cipher

The Ceaser Cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions down the alphabet. This algorithm has been used since ancient times and can be easily implemented by hand. The code in this repository provides a Python implementation of the Ceaser Cipher.

### Double Transition Cipher

The Double Transition Cipher is a more complex substitution cipher that rearranges the letters in the plaintext based on a series of transpositions. This algorithm provides a higher level of security than the Ceaser Cipher, but is also more computationally expensive. The code in this repository provides a Python implementation of the Double Transition Cipher.

### Vigenere Cipher

The Vigenere Cipher is a polyalphabetic substitution cipher that uses a series of different Ceaser ciphers based on a keyword. This algorithm provides a higher level of security than the Ceaser Cipher, and is relatively easy to implement. The code in this repository provides a Python implementation of the Vigenere Cipher.

## Usage

To use any of these algorithms, simply import the desired ciphering algorithm and use the provided functions to encrypt and decrypt your data. The specific usage will vary depending on the algorithm, but most will require you to provide a key and plaintext to encrypt, and a key and ciphertext to decrypt.
