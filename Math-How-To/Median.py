# Nilai tengah atau median adalah pemusatan data 
# yang membagi data terurut menjadi dua bagian sama banyak
# Sebelum dicari mediannya, data harus diurutkan terlebih dahulu dari terkecil ke terbesar

def hitung_median(data):
    dataUrut = sorted(data)
    banyakData = len(dataUrut)
    
    # Jika jumlah data ganjil, ambil nilai tengah
    # Median = data ke (n / 2) -> dibulatkan ke atas
    # Atau bisa juga data ke (n+1) / 2
    # 17 -> (17/2) = 8.5 dibulatkan ke atas menjadi 9
    # Atau (17+1) / 2 = 18 / 2 = 9
    if banyakData % 2 == 1:
        median = dataUrut[banyakData // 2]
    # Jika jumlah data genap, ambil rata-rata dua nilai tengah
    # Median = (tengah kiri + tengah kanan) / 2
    # Tengah kiri = data ke (n/2)
    # Tengah kanan = data ke (n/2) + 1
    # 18 data -> data ke 9 dan 10
    # 100 data -> data ke 50 dan 51
    else:
        tengahKiri = dataUrut[(banyakData // 2) - 1]
        tengahKanan = dataUrut[banyakData // 2]
        median = (tengahKiri + tengahKanan) / 2
    
    return median

def main():
    # Contoh data
    data = [6, 3, 2, 4, 1, 5]

    # Memanggil fungsi hitung_median dan mencetak hasilnya
    median = hitung_median(data)
    print("Median dari data adalah:", median)

main()