# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 02:10:10 2018

@author: Toshiba
"""
import vigenere
"""
# ge the message
user_input = ""
user_input = input("[keyword] [message]> ")

# separete keyword and message
keyword = ""
message = ""
for char in user_input:
    if (char != " "):
        keyword += char
    else:
        break

key_len = len(keyword)
message = user_input[(key_len+1):]     

#print(vigenere.encrpyt(keyword, message))
"""
"""
print(vigenere.encrypt('bond', 'theredfoxtrotsquietlyatmidnight'))
print(vigenere.encrypt('train', 'murderontheorientexpress'))
print(vigenere.encrypt('garden', 'themolessnuckintothegardenlastnight'))    
"""

print(vigenere.decrypt('cloak','klatrgafedvtssdwywcyty'))
print(vigenere.decrypt('python', 'pjphmfamhrcaifxifvvfmzwqtmyswst'))
print(vigenere.decrypt('moore', 'rcfpsgfspiecbcc'))