# Faktorial adalah hasil perkalian semua bilangan asli 
# yang kurang dari atau sama dengan bilangan yang akan dicari faktorialnya

# Misal, untuk mengetahui faktorial dari 6, caranya adalah dengan mengalikan angka 1 - 6 
# 1 * 2 * 3 * 4 * 5 * 6 = 720

# Program
def hitung_faktorial(n):
    # Var utk menampung hasil, akan dikalikan terus menerus 
    hasil = 1
    # Mengalikan var hasil dengan 1, 2, hingga n
    for i in range (1, n+1, 1):
        hasil = hasil * i
    # Mengembalikan hasil
    return hasil

def main():
    # Meminta input dari pengguna
    n = int(input("Angka yang akan dicari faktorialnya: "))
    # Memanggil fungsi hitung_faktorial
    hasil = hitung_faktorial(n)
    # Mencetak hasil dari faktorial
    print("Hasil dari {}! adalah {}".format(n, hasil))

if __name__ == '__main__':
    main()

# n = 3
# hasil = 1
# i = 1 -> hasil = 1 * 1 = 1
# i = 2 -> hasil = 1 * 2 = 2
# i = 3 -> hasil = 2 * 3 = 6
# fungsi akan mengembalikan hasil