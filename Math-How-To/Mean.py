# Rata-rata atau mean merupakan suatu bilangan yang mewakili sekumpulan data
# Cara menghitungnya adalah jumlah data dibagi banyaknya data

# Misal kita memiliki data sebagai berikut 
# 2, 4, 6, 8, 10
# Jumlah data = 2 + 4 + 6 + 8 + 10 = 30
# Banyak data = 5 (dikarenakan terdapat 5 bilangan)
# Mean = jumlah data / banyak data = 30 / 5 = 6

def hitung_mean(data):
    jumlahData = sum(data)
    banyakData = len(data)
    mean = jumlahData / banyakData
    return mean

def main():
    # Contoh data
    data = [2, 4, 6, 8, 10]

    # Memanggil fungsi hitung_mean dan mencetak hasilnya
    mean = hitung_mean(data)
    print("Mean dari data adalah:", mean)

if __name__ == '__main__':
    main()