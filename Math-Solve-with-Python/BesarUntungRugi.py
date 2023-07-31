# Pak Anto membeli sebuah barang dengan harga Rp560.000,00
# Jika ia menjualnya kembali dengan harga Rp630.000,00
# Berapa besar persentase keuntungan / kerugian yang dialami Pak Anto?

def main():
    hargaBeli = int(input("Harga Beli : "))
    hargaJual = int(input("Harga Jual : "))

    if (hargaJual == hargaBeli):
        print("Harga jual sama dengan harga beli")
        print("Tidak mengalami keuntungan ataupun kerugian")
    elif (hargaJual > hargaBeli):
        hasil = "untung"
    else: 
        hasil = "rugi"

    selisih = abs(hargaJual - hargaBeli)

    persen = selisih / hargaBeli * 100

    print("Mengalami ke{}an sebesar {}%".format(hasil, persen))

main()