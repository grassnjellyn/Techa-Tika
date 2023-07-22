# -------- KASUS --------
# Dik : nilai dari 2 suku pada barisan aritmatika
# Dit : Suku ke-n (Un) atau jumlah n barisan pertama (Sn)

def hitungUn(n, a, b):
    Un = a + (n - 1) * b
    print("Suku ke-{} (U{}): {}".format(n, n, Un))


def hitungSn(n, a, b):
    Sn = (n / 2) * (2 * a + (n - 1) * b)
    print("Jumlah {} suku pertama (S{}): {}".format(n, n, Sn))


def hitung(suku1, nilai1, suku2, nilai2):
    # U2 = 5 dan U4 = 11
    # suku1 = 2, nilai1 = 5, suku2 = 4, nilai2 = 11
    b = (nilai2 - nilai1) / (suku2 - suku1)

    # Un = a + (n - 1) * b
    # a + (n - 1) * b = Un
    # a = Un - (n - 1) * b
    a = nilai1 - (suku1 - 1) * b

    return [a, b]


def main():
    print("Masukkan data yang diketahui")
    print()

    suku1 = int(input("Suku pertama yang diketahui -> suku ke-"))
    print("Nilai dari suku ke-{} : ".format(suku1), end="")
    nilai1 = int(input())
    print()

    suku2 = int(input("Suku kedua yang diketahui -> suku ke-"))
    print("Nilai dari suku ke-{} : ".format(suku2), end="")
    nilai2 = int(input())
    print()

    a = hitung(suku1, nilai1, suku2, nilai2)[0]
    b = hitung(suku1, nilai1, suku2, nilai2)[1]

    print("Apa yang hendak dicari?")
    print("1. Suku ke-n (Un)")
    print("2. Jumlah n barisan pertama (Sn)")

    pilihan = int(input("Masukkan kode (1 atau 2) : "))
    print()

    if (pilihan == 1):
        n = int(input("Suku keberapa yang ingin dicari? "))
        print()
        hitungUn(n, a, b)
    elif (pilihan == 2):
        n = int(input("Jumlah hingga suku keberapa yang ingin dicari? "))
        print()
        hitungSn(n, a, b)

main()

# KASUS : 
# Diketahui barisan 11, 15, 19, 23, 27, ...
# U2 = 15 dan U4 = 23
# Buktikan U5 = 27 dan S3 = 45 (11 + 15 + 19)