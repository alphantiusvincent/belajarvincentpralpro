n=int(input("Masukkan n = "))
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(j," ",end='')
    else:
        for j in range(n,0,-1):
            print(j," ",end='')
    print()