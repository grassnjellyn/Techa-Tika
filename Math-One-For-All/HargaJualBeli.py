# Menentukan harga jual atau beli jika diketahui besarnya keuntungan atau kerugian

def cariHargaJualUntung(hargaBeli, persen):
    hargaJual = hargaBeli + persen / 100 * hargaBeli
    return round(hargaJual)

def cariHargaBeliUntung(hargaJual, persen):
    # j = b + (p/100) * b
    # j = (100/100) * b + (p/100) * b
    # j = (100+p) / 100 * b
    # b = j * 100 / (100+p)
    hargaBeli = hargaJual * 100 / (100 + persen)
    return round(hargaBeli)

def cariHargaBeliRugi(hargaJual, persen):
    hargaBeli = hargaJual + persen / 100 * hargaJual
    return round(hargaBeli)

def cariHargaJualRugi(hargaBeli, persen):
    # b = j + (p/100) * j
    # b = (100/100) * j + (p/100) * j
    # b = (100+p) / 100 * j
    # j = b * 100 / (100+p)
    hargaJual = hargaBeli * 100 / (100 + persen)
    return round(hargaJual)

def main():
    # Untuk harga jual dan harga beli, jika tidak diketahui diisi dengan -1
    hargaBeli = int(input("Harga Beli : "))
    hargaJual = int(input("Harga Jual : "))

    print("="*35)
    print("Mengalami keuntungan atau kerugian?")
    print("1. Untung")
    print("2. Rugi")
    kode = int(input("Silakan pilih 1 / 2 : "))

    while (kode != 1 and kode != 2):
        print("Tolong masukkan antara 1 atau 2 saja")
        kode = int(input("Silakan pilih 1 / 2 : "))

    print("="*35)
    print("Berapa persentasenya?", end=" ")
    persen = float(input())

    if (hargaBeli == -1):
        if (kode == 1):
            hargaBeli = cariHargaBeliUntung(hargaJual, persen)
        elif (kode == 2):
            hargaBeli = cariHargaBeliRugi(hargaJual, persen)
        print("Harga belinya adalah Rp{},-".format(hargaBeli))
    elif (hargaJual == -1):
        if (kode == 1):
            hargaJual = cariHargaJualUntung(hargaBeli, persen)
        elif (kode == 2):
            hargaJual = cariHargaJualRugi(hargaBeli, persen)
        print("Harga jualnya adalah Rp{},-".format(hargaJual))

main()