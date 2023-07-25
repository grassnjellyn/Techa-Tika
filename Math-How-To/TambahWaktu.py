def tambah_waktu(waktu1, waktu2):
    jam1, menit1, detik1 = waktu1
    jam2, menit2, detik2 = waktu2

    total_detik = detik1 + detik2
    sisa_detik = total_detik % 60
    menit_tambahan = total_detik // 60

    total_menit = menit1 + menit2 + menit_tambahan
    sisa_menit = total_menit % 60
    jam_tambahan = total_menit // 60

    total_jam = jam1 + jam2 + jam_tambahan

    return total_jam, sisa_menit, sisa_detik

def main():
    # Waktu pertama
    jam1 = 13
    menit1 = 45
    detik1 = 59

    # Waktu kedua
    jam2 = 2
    menit2 = 51
    detik2 = 6

    # Menggabungkan waktu dalam bentuk tuple
    waktu1 = (jam1, menit1, detik1)
    waktu2 = (jam2, menit2, detik2)

    # Memanggil fungsi tambah_waktu dan mencetak hasilnya
    hasil_penjumlahan = tambah_waktu(waktu1, waktu2)
    print("Hasil penjumlahan waktu:", hasil_penjumlahan[0], "jam", hasil_penjumlahan[1], "menit", hasil_penjumlahan[2], "detik")

if __name__ == '__main__':
    main()