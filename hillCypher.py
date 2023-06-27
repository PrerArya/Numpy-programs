# -*- coding: utf-8 -*-
'''
Hill Cipher is a polygraphic substitution cipher based on linear algebra.
Here the plain text is converted into encrypted form.
Each letter of plain text is represented by a number modulo 26.
Often the simple scheme A=0, B=1,....Z=25 is used
To encrypt a message, each block of n letters is multiplied by an invertible n × n matrix, against modulus 26
The matrix used for encryption is the cipher key, and it should be chosen randomly
Lets us take plain text = edureka and cipher key = [11 9
                                                     8 17]
Plain text is converted into 2×1 matrix format i.e. [e d] [u r] [e k]
Again plain text is converted into numbers i.e. [4 3] [20 11] [4 10]
So, encryption of hill cipher = (each column of plain text)*(key)*mod 26
'''
"""

import numpy as np

def alpha_to_num(text):
    message = []
    for i in text:
        if i.isupper():
            number = ord(i) - 65
            message.append(number)
        elif i.islower():
            number = ord(i) - 97
            message.append(number)
    return message

def array_div(message):
    message = np.array(message)
    new_message = message.reshape(-1, 2).T
    return new_message

def cipher_text(new_message, key):
    c = np.dot(key, new_message) % 26
    return c

if __name__ == "__main__":
    key_input = input("Enter the Key (4 integers separated by spaces): ")
    key = np.array(key_input.split(), dtype=int).reshape(2, 2)

    plaintext = input("Enter the text to be encrypted: ")

    a = alpha_to_num(plaintext)
    b = array_div(a)
    c = cipher_text(b, key)

    print("Cipher Text:", c.T)



m= np.array([[1,3],[5,6]])
new_message = m.reshape(-1,2).T
new_message

