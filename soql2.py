def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def display_series(n):
    for i in range(n, 0, -1):
        fact = factorial(i)
        print(f"{fact}", end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Input dari pengguna
n = int(input("Masukkan nilai n: "))

# Tampilkan deret
display_series(n)