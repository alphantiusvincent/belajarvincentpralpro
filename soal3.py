def tampilkan_deret(tinggi, lebar):
    angka = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(angka, end=" ")
            angka += 1
        print()

# Input dari pengguna
tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

# Tampilkan deret
tampilkan_deret(tinggi, lebar)