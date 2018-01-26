# -*- coding: utf-8 -*-

alpha= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

default_freq = ["e","a","t","i","o","s","n","r","h","l","d","c","u","m","p","f","g","y","w","b","v","k","j","x","q","z"]

freq = {}
freq_sorted = []

f = open('encryptedText.txt')
word = f.read()
f.close()

u = 0
for i in range (26):
    freq[alpha[u]] = word.count(alpha[u])
    u = u + 1

for k, v in sorted(freq.items(), key=lambda x: -x[1]):
    freq_sorted.append(k)


word_list = list(word)

word_mod = word_list[:]

print freq_sorted


v = 0
for n in range(len(word)):
    w = 0
    for i in range(26):
        if word_list[v] == freq_sorted[w]:
            word_mod[v] = default_freq[w]
        
        w = w + 1        
    v = v + 1

print "\n"
print "[" + "".join(word_mod) + "]" 

f = open('decryptedText.txt', 'w')
f.write("".join(word_mod))
f.close()
