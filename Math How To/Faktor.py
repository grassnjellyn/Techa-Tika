# Faktor dari suatu bilangan adalah daftar bilangan yang dapat membagi habis
# bilangan tersebut

# Misal, jika kita memiliki angka 12, yang menjadi faktornya adalah
# 1 2 3 4 6 12 karena jika 12 dibagi oleh keenam bilangan ini, maka hasilnya tidak akan bersisa
# Bandingkan dengan 12 dibagi 5 yang akan menyisakan 2, ini berarti 5 bukanlah faktor dari 12

# Jadi, cara untuk mencari faktor dari suatu bilangan 
# ialah dengan memeriksa satu persatu apakah bilangan tersebut habis dibagi dengan 
# bilangan yang sedang diperiksa atau tidak

def cari_faktor(angka):
    faktor = []

    for i in range (1, angka + 1, 1):
        if (angka % i == 0):
            faktor.append(i)

    return faktor

def main():
    bil = int(input("Masukkan bilangan yang ingin dicari faktornya: "))

    faktor = cari_faktor(bil)

    print("Faktor-faktor dari", bil, "adalah: ")
    print(faktor)

if __name__ == '__main__':
    main()

# angka = 6
# i = 1 -> 6 % 1 == 0 -> [1]
# i = 2 -> 6 % 2 == 0 -> [1, 2]
# i = 3 -> 6 % 3 == 0 -> [1, 2, 3]
# i = 4 -> 6 % 4 == 2 -> 6 % 4 != 0 -> [1, 2, 3]
# i = 5 -> 6 % 5 == 1 -> 6 % 5 != 0 -> [1, 2, 3]
# i = 6 -> 6 % 6 == 0 -> [1, 2, 3, 6]
# Fungsi akan mengembalikan [1, 2, 3, 6]