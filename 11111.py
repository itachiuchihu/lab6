A=input()
k=int(A[0])
n=int(A[1])
B=[]
for i in range(k):
    Q=''
    Q=Q+input()
    for t in range(n):
        B=B+[int(Q[t])]
Q=''
for i in range(n):
    u=i
    C=[]
    for t in range(k):
        C=C+[B[u]]
        u=u+n
    f=min(C)
    Q=Q+str(f)
print(Q)

