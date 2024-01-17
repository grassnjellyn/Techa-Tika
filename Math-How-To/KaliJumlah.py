def cari_bilangan(hasil_kali, hasil_jumlah):
    # Mencari pasangan hasil kali
    pairs = []
    for i in range(1, int(abs(hasil_kali)**0.5) + 1):
        if hasil_kali % i == 0:
            pair1 = (i, hasil_kali // i)
            pair2 = (-pair1[0], -pair1[1])
            pairs.extend([pair1, pair2])

    # 12 = {(1, 12), (-1, -12), (2, 6), (-2, -6), (3, 4), (-3, -4)}
    # -12 = {(1, -12), (-1, 12), (2, -6), (-2, 6), (3, -4), (-3, 4)}

    # Mencocokkan jumlahnya dengan variabel hasil_jumlah
    for pair in pairs:
        if (sum(pair) == hasil_jumlah):
            # Mengembalikan dua angka tersebut jika ditemukan
            return pair

    # Mengembalikan None jika tidak ditemukan
    return None

def main():
    # Menginputkan hasil_kali dan hasil_jumlah
    hasil_kali = int(input("Hasil jika dikalikan: "))
    hasil_jumlah = int(input("Hasil jika dijumlahkan: "))

    # Menyimpan hasilnya di variabel
    hasil = cari_bilangan(hasil_kali, hasil_jumlah)

    # Menampilkan dua bilangan tersebut sesuai dengan kondisi
    if (hasil != None):
        print(f"Kedua bilangan tersebut adalah {hasil[0]} dan {hasil[1]}")
    else:
        print("Tidak ada dua bilangan yang memenuhi")

main()