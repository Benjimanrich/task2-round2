import caesar
x="heydontleakthisguysthisissecretpleasebekindtomebecauseidontknowwhattodobuthereitisandnowijustwanttomakethislonger"
print(caesar.cae_enc(x,1),caesar.cae_enc(caesar.cae_enc(x,1),25))
dec_alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p_i=[8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,0.2,0.8,4.0,2.4,6.7,1.5,1.9,0.1,6.0,6.3,9.1,2.8,1.0,2.4,0.2,2.0,0.1]#vals from textbook
for i in range(len(p_i)):
    p_i[i]/=100
def key_freqguess(x):
    x=x.upper()
    keylist=[]
    q_i=[]
    

    freqsum=0.0
    for key in range(26):
        for i in range(26):
            q_i.append(0.0)
        enc_alph=caesar.cae_enc(dec_alph,key)
        for i in range(26):
            q_i[(i+key)%26]=x.count(dec_alph[(i+key)%26])/len(x)
            #print(x.count(enc_alph[i])/len(x))
        for i in range(26):
            freqsum+=(p_i[i]*q_i[(i+key)%26])
        #print("\n\n\n\n",freqsum)
        if -0.01<(freqsum-0.065)<0.01:
            keylist.append(key)
        #print(q_i)
        q_i=[]
        freqsum=0.0
    return keylist
for i in range(26):
    x2=caesar.cae_enc(x,i)
    print(f"key:{i}")
    print(f"key guess:{key_freqguess(x2)}")