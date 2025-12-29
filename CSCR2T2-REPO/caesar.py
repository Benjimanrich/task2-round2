def cae_enc(text,ckey):
    text=text.upper()
    encstr=""
    for i in text:
        encasc=65+(((ord(i)+ckey-65)%26))
        encstr+=chr(encasc)
    return encstr

def cae_dec(text,ckey):
    decstr=""
    text=text.upper()
    for i in text:
        decasc=65+(((ord(i)-ckey+65)%26))
        decstr+=chr(decasc)
    return decstr
#for i in range(-30,31):
    #y=cae_dec(x,i)
    #print(x)
    #print(y)
