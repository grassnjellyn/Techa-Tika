def cari_modus(data):
    # Hitung frekuensi setiap angka dalam data
    frekuensi = [0] * (max(data) + 1)  # Buat list dengan ukuran maksimum angka dalam data + 1

    for angka in data:
        frekuensi[angka] += 1

    # Cari frekuensi tertinggi
    frekuensi_tertinggi = max(frekuensi)

    # Cari angka-angka dengan frekuensi tertinggi (modus)
    modus = []
    for angka in data:
        if frekuensi[angka] == frekuensi_tertinggi and angka not in modus:
            modus.append(angka)

    return modus

def main():
    # Contoh data
    data = [1, 2, 2, 3, 4, 4, 5, 5]

    # Panggil fungsi untuk mencari modus
    hasil_modus = cari_modus(data)

    if len(hasil_modus) == 1:
        print("Modus:", hasil_modus[0])
    else:
        print("Data memiliki beberapa modus:", hasil_modus)

main()