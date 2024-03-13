def apakah_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

def bilangan_prima_terdekat(n):
    # Mulai cek dari n-1 turun ke 2
    for i in range(n-1, 1, -1):
        if apakah_prima(i):
            return i

# Input dari pengguna
n = int(input("Masukkan bilangan: "))

# Cari bilangan prima terdekat yang kurang dari n
bilangan_prima_terdekat = bilangan_prima_terdekat(n)

# Tampilkan hasil
print(f"Bilangan prima terdekat yang kurang dari {n} adalah {bilangan_prima_terdekat}")