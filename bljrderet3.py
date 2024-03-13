n=int(input("Masukkan n = "))
for i in range(0,n+1):
    for j in range(1,n-i+1):
        print("X",end='') if j%2==1 else print("O",end='')
    print()
