def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    # Membaca input dari pengguna
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))

    # Memanggil fungsi hitung_fpb dan mencetak hasilnya
    hasil_fpb = hitung_fpb(bilangan1, bilangan2)
    print("FPB dari", bilangan1, "dan", bilangan2, "adalah:", hasil_fpb)

if __name__ == '__main__':
    main()