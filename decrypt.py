import csv

read_fp=csv.reader(open("key.csv", "r"))
alpha = next(read_fp)
beta = next(read_fp)

message_mod = raw_input('Enter Encrypted Word >>>>')

message_list_mod = list(message_mod)

message_list_ans = message_list_mod[:]

u = 0
for n in range(len(message_mod)):
    v = 0
    for i in range(26):
        if message_list_mod[u] == beta[v]:
            message_list_ans[u] = alpha[v]
        
        v = v + 1        
    u = u + 1


ans = "".join(message_list_ans)

print "The message is" + "[" + ans + "]"