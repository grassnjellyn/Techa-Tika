def hitungMean(data):
    total = sum(data)
    jumlah_data = len(data)
    mean = total / jumlah_data
    return mean

def hitungMedian(data):
    data_urut = sorted(data)
    jumlah_data = len(data_urut)
    
    # Jika jumlah data ganjil, ambil nilai tengah
    if jumlah_data % 2 == 1:
        median = data_urut[jumlah_data // 2]
    # Jika jumlah data genap, ambil rata-rata dua nilai tengah
    else:
        tengah_kiri = data_urut[(jumlah_data // 2) - 1]
        tengah_kanan = data_urut[jumlah_data // 2]
        median = (tengah_kiri + tengah_kanan) / 2
    
    return median

def hitungModus(data):
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
    data = [8,7,6,8,9,9,8,7,6,9,7,8,8,7,9,8,8,6,8,7] 

    mean = hitungMean(data)
    median = hitungMedian(data)
    modus = hitungModus(data)

    print("Mean dari data adalah:", mean)
    print("Median dari data adalah:", median)

    if len(modus) == 1:
        print("Modus:", modus[0])
    else:
        print("Data memiliki beberapa modus:", modus)

main()