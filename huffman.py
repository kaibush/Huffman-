decode_code = {'00':'A',
               '01':'E',
               '100':'L',
               '110':'O',
               '111':'R',
               '1010':'B',
               '1011':'D'}

encode_code = dict([(y, x) for x,y in decode_code.items()])
print encode_code

init_str = 'DOORBELL'

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
enstr = encode_it(init_str)
print enstr
print decode_it(enstr)










    
