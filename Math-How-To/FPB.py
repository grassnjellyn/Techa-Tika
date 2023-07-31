# Faktor persekutuan terbesar atau FPB adalah bilangan bulat positif terbesar 
# yang dapat membagi dua bilangan atau lebih
# Atau bisa juga disebut sebagai bilangan bulat positif terbesar
# yang merupakan faktor dari dua bilangan atau lebih

# Misal kita memiliki angka 24 dan 36
# Faktor dari 24 adalah 1, 2, 3, 4, 6, 8, 12, 24
# Faktor dari 36 adalah 1, 2, 3, 4, 6, 9, 12, 18, 36
# Faktor yang sama : 1, 2, 3, 4, 6, 12
# Faktor terbesar yang sama adalah 12, maka FPB dari 24 dan 36 adalah 12

def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    # Membaca input dari pengguna
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))

    # Memanggil fungsi hitung_fpb dan mencetak hasilnya
    hasil_fpb = hitung_fpb(bilangan1, bilangan2)
    print("FPB dari", bilangan1, "dan", bilangan2, "adalah:", hasil_fpb)

main()

# Cara Kerja Program

# Misal a = 24 dan b = 36
# 1 -> 36 != 0 -> a = 36, b = 24 % 36 = 24
# 2 -> 24 != 0 -> a = 24, b = 36 % 24 = 12
# 3 -> 12 != 0 -> a = 12, b = 24 % 12 = 0
# 4 -> 0 == 0 -> program terhenti
# FPB = nilai a terakhir = 12

# Misal a = 56 dan b = 75
# 1 -> 75 != 0 -> a = 75, b = 56 % 75 = 56
# 2 -> 56 != 0 -> a = 56, b = 75 % 56 = 19
# 3 -> 19 != 0 -> a = 19, b = 56 % 19 = 18
# 4 -> 18 != 0 -> a = 18, b = 19 % 18 = 1
# 5 -> 1 != 0 -> a = 1, b = 18 % 1 = 0
# 6 -> 0 == 0 -> program terhenti
# FPB = nilai a terakhir = 1