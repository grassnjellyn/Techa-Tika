# Modus adalah salah satu ukuran statistik, 
# yang digunakan untuk mengetahui nilai yang paling sering muncul dalam suatu kumpulan data
# Cara mencari modus adalah dengan melihat nilai data yang memiliki frekuensi kemunculan 
# (jumlah kejadian) terbanyak di antara seluruh nilai data yang ada. 

# Misal kita memiliki data sebagai berikut : 
# 3, 1, 5, 7, 2, 3, 4, 8
# Modusnya adalah 3 karena muncul sebanyak 2 kali sementara yang lain hanya 1 kali

# Pengecekan data pertama (nilai = 3) -> [0, 0, 0, 1, 0, 0, 0, 0, 0]
# Pengecekan data kedua (nilai = 1) -> [0, 1, 0, 1, 0, 0, 0, 0, 0]
# Pengecekan data ketiga (nilai = 5) -> [0, 1, 0, 1, 0, 1, 0, 0, 0]

# frek = [0, 1, 1, 2, 1, 1, 0, 1, 1]

def hitungModus(data):
    # Hitung frekuensi setiap angka dalam data
    frek = [0] * (max(data) + 1)  # Buat list dengan ukuran maksimum angka dalam data + 1

    for angka in data:
        frek[angka] += 1

    # Menampilkan isi array frek
    print(frek)

    # Cari frekuensi tertinggi
    frekTertinggi = max(frek)

    # Cari angka-angka dengan frekuensi tertinggi (modus)
    modus = []
    for angka in data:
        if frek[angka] == frekTertinggi and angka not in modus:
            modus.append(angka)

    return modus

def main():
    # Contoh data
    data = [1, 2, 2, 3, 4, 4, 5, 5]

    # Panggil fungsi untuk mencari modus
    modus = hitungModus(data)

    if len(modus) == 1:
        print("Modus:", modus[0])
    else:
        print("Data memiliki beberapa modus:", modus)

main()