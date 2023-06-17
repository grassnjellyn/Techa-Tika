# Bilangan prima adalah bilangan bulat yang lebih besar dari 1 dan
# hanya memiliki dua faktor pembagi yang berbeda, yaitu 1 dan bilangan itu sendiri

# Misal, 5 adalah bilangan prima karena selain 1 dan 5, 5 tidak dapat dibagi habis
# oleh bilangan lainnya
# Sementara, 12 bukan bilangan prima karena selain 1 dan 12, 12 juga
# dapat dibagi habis oleh 2, 3, 4, dan 6

# Cara memeriksa apakah suatu bilangan prima atau bukan adalah dengan mencoba
# membaginya dengan 2, 3, 4, hingga akar dari bilangan tersebut

def cek_prima(n):
    # Di awal, anggap n merupakan bilangan prima
    prima = True
    # Tidak ada bilangan prima yang lebih kecil dari 2
    if n < 2:
        prima = False
    
    # Memeriksa apakah n habis dibagi 2, 3, hingga akar dari n
    # Jika n habis dibagi bilangan yang lebih besar dari akar n, 
    # hasil baginya sudah pasti lebih kecil dari akar n yang berarti sudah diperiksa,
    # sehingga tidak perlu memeriksa angka di atas akar n

    # Jika ditemukan bahwa n habis dibagi sesuatu, maka n bukanlah prima
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prima = False
    # Mengembalikan variabel prima (True / False)
    return prima

def main():
    # Meminta input dari pengguna
    bilangan = int(input("Masukkan bilangan: "))

    # Memeriksa apakah bilangan tersebut prima atau bukan
    if cek_prima(bilangan):
        print(bilangan, "adalah bilangan prima.")
    else:
        print(bilangan, "bukan bilangan prima.")

if __name__ == '__main__':
    main()

# n = 9
# prima = True
# i = 2 -> 9 % 2 = 1 -> prima = True
# i = 3 -> 9 % 3 = 0 -> prima = False
# prima = False 