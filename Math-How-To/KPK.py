# Kelipatan Persekutuan Terkecil atau KPK dari 2 bilangan adalah 
# bilangan bulat positif terkecil yang dapat dibagi habis oleh kedua bilangan tersebut

# Misal kita memiliki angka 12 dan 15
# Jika kita tuliskan 5 kelipatan pertama dari masing-masing bilangan seperti ini
# 12 24 36 48 60
# 15 30 45 60 75
# Kita dapat melihat bahwa 60 merupakan bilangan pertama 
# yang merupakan kelipatan dari kedua bilangan tersebut
# Kita dapat mengetahuinya karena 60 habis dibagi 12, 60 juga habis dibagi 15

# Dengan begini, kita bisa mengetahui KPK dengan cara memeriksa semua bilangan bulat 
# yang lebih besar dari kedua bilangan yang hendak dicari KPK nya hingga didapatkan 
# bilangan yang dapat dibagi habis oleh keduanya

# Program 
def cari_kpk(a, b):
    # Definisikan bilangan yang lebih besar sebagai KPK sementara 
    kpk = max(a, b)
    # Buat variabel yang nilainya akan terus bertambah hingga KPK baru didapatkan
    cari = kpk

    # Selama nilai dari KPK masih sama atau belum berganti
    while (kpk == max(a, b)):
        # Jika variabel cari habis dibagi a dan b
        if (cari % a == 0) and (cari % b == 0):
            # Maka nilai KPK berubah menjadi nilai dari variabel 'cari' saat ini
            kpk = cari
        # Nilai dari variabel cari akan bertambah 1
        cari += 1
    # Karena nilai KPK sudah berubah, maka program akan keluar dari while dan
    # mengembalikan nilai KPK saat ini
    return kpk

def main():
    # Membaca input dari pengguna
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))

    # Memanggil fungsi cari_kpk dan mencetak hasilnya
    hasil_kpk = cari_kpk(bilangan1, bilangan2)
    print("KPK dari", bilangan1, "dan", 
    bilangan2, "adalah", hasil_kpk)

if __name__ == '__main__':
    main()

# a = 2, b = 3
# kpk = 3
# cari = kpk = 3

# selama nilai kpk masih sama dengan 3, maka baris kode pada 22 - 24 akan dijalankan
# cari = 3 -> 3 tidak habis dibagi 2, habis dibagi 3
# cari = 4 -> 4 habis dibagi 2, tidak habis dibagi 3
# cari = 5 -> 5 tidak habis dibagi 2 dan 3
# cari = 6 -> 6 habis dibagi 2, 6 habis dibagi 3
# kpk = 3 -> kpk = 6
# nilai dari kpk akan dikembalikan