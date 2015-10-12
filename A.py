f1=open('input.txt','r')
Q=''
N=f1.read(1)
Q=f1.read()
f1.close()
S=0
T=True
for i in range (int(N)-1):
    k=i+1
    while k<=(int(N)-1):
        if int(Q[i])==int(Q[k]):
            S=Q[i]
            T=False
        k+=1
    if T==False:
        break
f2=open('output.txt','w')
f2.write(S)
f2.close()
