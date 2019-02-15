##def reverse_num(s):
##    num = []
##    while (s != 0):
##        num.append(s % 10)
##        s /= 10
##    total = len(num) - 1
##    n = 0
##    for i in num:
##        n += i * (10** total)
##        total -= 1
##    return n
##
##reverse_num(12355)
##    
##    
##
##for i in range(10000, 100000):
##    if i<<2 == int(reverse_num(i)):
##        break
##print i



##for i in range(10000, 100000):
##    j = 0
##    t = i
##    if i  == 21978:
##        print
##    while(t != 0):
##        j = j * 10 + t % 10
##        t /= 10
##        if i<<2 == j:
##            print i
##            break
import math
def get_float(num):
     m, n = math.modf(num)
     return n, m

     
##num = 0.75
##
##l = []
##while(1):
##    num_n, num_m = get_float(num)
##    chengfa = num_m * 2.0
##    num_n, num = get_float(chengfa)
##    l.append(num_n)
##    if num == 0:
##        break
##print l


decode_code = {'00':'A',
               '01':'E',
               '100':'L',
               '110':'O',
               '111':'R',
               '1010':'B',
               '1011':'D'}

encode_code = dict([(y, x) for x,y in decode_code.items()])
print encode_code

org_str = 'DOORBELL'

def encode_it(s):
    encode_lst = []
    for i in s:
        encode_lst.append(encode_code[i])
    return ''.join(encode_lst)

def decode_it(encode_str):
    pos = 1
    decode_lst = []
    while 1:
        match = encode_str[:pos]
        if match in decode_code:
            decode_lst.append(decode_code[match])
            encode_str = encode_str[pos:]
            pos = 1
        else:
            pos += 1
        if not match:
            break
    return ''.join(decode_lst)
enstr = encode_it(org_str)
print enstr
print decode_it(enstr)










    
