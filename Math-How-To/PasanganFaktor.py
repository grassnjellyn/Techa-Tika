# Pasangan faktor adalah kumpulan dua bilangan asli apapun yang dapat dikalikan 
# untuk memperoleh hasil kali tertentu

# Contoh : 
# Pasangan faktor dari 12 adalah 
# 1 dan 12 
# 2 dan 6
# 3 dan 4

def cari(n):
    # Membuat array untuk menyimpan pasangan faktor
    pasangan = []
    # Mendeteksi faktor yang merupakan pasangan
    # Memasukkannya ke dalam array
    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            pasang = (i, n // i)
            pasangan.append(pasang)
    # Mengembalikan array pasangan
    return pasangan

def main():
    # Input bilangan yang akan dicari pasangan faktornya
    bilangan = int(input("Bilangan: "))

    # Panggil fungsi cari()
    pasangan = cari(bilangan)

    # Menampilkan pasangan faktor
    print("Pasangan faktor dari", bilangan, "adalah:")
    for pair in pasangan:
        print(pair)

main()