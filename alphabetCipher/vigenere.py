# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 03:23:51 2018

@author: Toshiba
"""

def encrypt(keyword, message):
    key_len = len(keyword)
    long_key = ""
    
    for i in  range(len(message)):
        long_key += keyword[i%key_len]  
        
    chart = []
    # get the substitution chart as a list       
    with open('substitution_chart.txt', 'r') as fp:
        while True:
            chart.append(fp.readline())
            if chart[-1] == "":
                break    
    
    encrypted_message = ""
    for i in range(len(message)):
        column_letter = message[i]
        row_letter = long_key[i]
        target_row = ""
        target_index = 0
        for row in chart:
            #print(row)
            if row[0] == row_letter.upper():
                target_row = row
                break
        
        for j in range(len(chart[0])):
            if chart[0][j] == column_letter.upper():
                target_index = j
                break
                
        encrypted_message += target_row[target_index]
    
    return encrypted_message

def decrypt(keyword, encrypted_message):
    key_len = len(keyword)
    long_key = ""
    
    for i in  range(len(encrypted_message)):
        long_key += keyword[i%key_len]  
        
    chart = []
    # get the substitution chart as a list       
    with open('substitution_chart.txt', 'r') as fp:
        while True:
            chart.append(fp.readline())
            if chart[-1] == "":
                break    
    
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        column_letter = encrypted_message[i]
        row_letter = long_key[i]
        target_row = ""
        target_index = 0
        for row in chart:
            #print(row)
            if row[0] == row_letter.upper():
                target_row = row
                break
        
        for j in range(len(target_row)):
            if target_row[j] == column_letter.lower():
                target_index = j
                break
                
        decrypted_message += chart[0][target_index]
    
    return decrypted_message
    