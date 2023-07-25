def hitung_median(data):
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

# Contoh data
data = [6, 3, 2, 4, 1, 5]

# Memanggil fungsi hitung_median dan mencetak hasilnya
hasil_median = hitung_median(data)
print("Median dari data adalah:", hasil_median)
