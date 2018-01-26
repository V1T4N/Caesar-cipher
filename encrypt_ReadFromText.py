# -*- coding: utf-8 -*-

import random
import csv
import string


f = open('text.txt')
message = f.read()
f.close()

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

beta = alpha[:]
random.shuffle(beta)

write_fp=csv.writer(open("key.csv", "w"))

write_fp.writerow(alpha)
write_fp.writerow(beta)



message_list = list(message)
message_list_mod = list(message)

x = 0
for n in range(len(message)):
    y = 0
    for i in range(26):
        if message_list[x] == alpha[y]:
            message_list_mod[x] = beta[y]
        
        y = y + 1        
    x = x + 1


message_mod = "".join(message_list_mod)

print("Encrypted message is" + "[" + message_mod + "]" )

f = open('encryptedText.txt', 'w')
f.write(message_mod)
f.close()
