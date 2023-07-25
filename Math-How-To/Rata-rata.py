def hitung_mean(data):
    total = sum(data)
    jumlah_data = len(data)
    mean = total / jumlah_data
    return mean

def main():
    # Contoh data
    data = [2, 4, 6, 8, 10]

    # Memanggil fungsi hitung_mean dan mencetak hasilnya
    hasil_mean = hitung_mean(data)
    print("Mean dari data adalah:", hasil_mean)

if __name__ == '__main__':
    main()