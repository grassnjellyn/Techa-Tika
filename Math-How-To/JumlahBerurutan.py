# 3 bilangan berurutan jika dijumlahkan hasilnya adalah 54. 
# Tentukan bilangan-bilangan yang dimaksud!

def cariTerkecil(n, jumlah):
    tengah = jumlah / n
    if (n % 2 == 1):
        jarak = (n-1) / 2
    else:
        jarak = (n/2)-0.5
    kecil = tengah - jarak
    return round(kecil)

def main():
    n = int(input("Banyak bilangan: "))
    jumlah = int(input("Jumlah: "))

    isi = []
    kecil = cariTerkecil(n, jumlah)
    for i in range (n):
        isi.append(kecil+i)

    print("Berikut bilangannya:", isi)

main()