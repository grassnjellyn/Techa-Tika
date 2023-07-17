# -------- KASUS --------
# Dik : nilai dari 2 suku pada barisan geometri
# Dit : Suku ke-n (Un) atau jumlah n barisan pertama (Sn) 

def hitungUn(n, a, r):
    Un = a * (r ** (n - 1))
    print("Suku ke-{} (U{}): {}".format(n, n, Un))

def hitungSn(n, a, r):
    if (r == 1):
        Sn = n * a
    else:
        Sn = a * ((r ** n) - 1) / (r - 1)
    print("Jumlah {} suku pertama (S{}): {}".format(n, n, Sn))

def hitung(suku1, nilai1, suku2, nilai2):
    r = (nilai2 / nilai1) ** (1 / (suku2 - suku1))

    # Un = a * r^(n-1)
    # a * r^(n-1) = Un
    # a = Un / r^(n-1) 
    a = nilai1 / (r ** (suku1 - 1))

    return [a, r]

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
    r = hitung(suku1, nilai1, suku2, nilai2)[1]

    print("Apa yang hendak dicari?")
    print("1. Suku ke-n (Un)")
    print("2. Jumlah n barisan pertama (Sn)")

    pilihan = int(input("Masukkan kode (1 atau 2) : "))
    print()

    if (pilihan == 1):
        n = int(input("Suku keberapa yang ingin dicari? "))
        print()
        hitungUn(n, a, r)
    elif (pilihan == 2):
        n = int(input("Jumlah hingga suku keberapa yang ingin dicari? "))
        print()
        hitungSn(n, a, r)

main()
