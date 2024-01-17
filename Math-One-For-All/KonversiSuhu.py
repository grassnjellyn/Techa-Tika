def ubahCelcius(C, satuan):
    if (satuan == "R"):
        hasil = 4 / 5 * C
    elif (satuan == "F"):
        hasil = 9 / 5 * C + 32
    elif (satuan == "K"):
        hasil = C + 273.15
    return round(hasil, 2)

def ubahReamur(R, satuan):
    if (satuan == "C"):
        hasil = 5 / 4 * R
    elif (satuan == "F"):
        hasil = 9 / 4 * R + 32
    elif (satuan == "K"):
        hasil = 5 / 4 * R + 273.15
    return round(hasil, 2)

def ubahFahrenheit(F, satuan):
    if (satuan == "C"):
        hasil = (5/9) * (F-32)
    elif (satuan == "R"):
        hasil = (4/9) * (F-32)
    elif (satuan == "K"):
        hasil = (5/9) * (F-32) + 273.15
    return round(hasil, 2)

def ubahKelvin(K, satuan):
    if (satuan == "C"):
        hasil = K - 273.15
    elif (satuan == "R"):
        hasil = (4/5) * (K-273.15)
    elif (satuan == "F"):
        hasil = (9/5) * (K-273.15) + 32
    return round(hasil, 2)

def main():
    print("="*40)
    print("Masukkan satuan yang akan diubah")
    satuan1 = input("C / R / F / K: ")
    nilai = int(input("Berapa nilainya? "))
    print("="*40)
    print("Masukkan satuan tujuan akhir")
    satuan2 = input("C / R / F / K: ")
    print("="*40)

    if (satuan1 == "C"):
        hasil = ubahCelcius(nilai, satuan2)
    elif (satuan1 == "R"):
        hasil = ubahReamur(nilai, satuan2)
    elif (satuan1 == "F"):
        hasil = ubahFahrenheit(nilai, satuan2)
    elif (satuan1 == "K"):
        hasil = ubahKelvin(nilai, satuan2)

    print(nilai, satuan1, " setara dengan ",
    hasil, satuan2, sep="")

main()