# Mencetak panjang, lebar, keliling, dan luas dari persegi panjang 
# walaupun hanya ada 2 data yang diketahui 
# dengan syarat salah satunya merupakan panjang atau lebar

# Keliling = 2 * (panjang + lebar) -> K = 2 * (p + l)
# Luas = panjang * lebar -> L = p * l

# Contoh data : 
# panjang = 4
# lebar = 3
# keliling = 14
# luas = 12

def hitungKeliling():
    # memeriksa apakah data sudah ada
    if (k != 0):
        return k
    # menghitung menggunakan rumus
    else:
        return 2 * (p + l)
    
def hitungLuas():
    # memeriksa apakah data sudah ada
    if (L != 0):
        return L
    # menghitung menggunakan rumus
    else:
        return p * l

def hitungPanjang():
    global p, l
    
    # jika yang diketahui lebar dan keliling
    if (l != 0 and k != 0):
        # 2 * (p + l) = k
        # p + l = k / 2
        p = k / 2 - l
    # jika yang diketahui lebar dan luas
    elif (l != 0 and L != 0):
        # L = p * l
        # p * l = L
        p = L / l

    return p

def hitungLebar():
    global p, l

    # jika yang diketahui panjang dan keliling
    if (p != 0 and k != 0):
        l = k / 2 - p
    # jika yang diketahui lebar dan luas
    elif (p != 0 and L != 0):
        l = L / p
    
    return l

def main():
    # variabel global
    global p, l, k, L

    # meminta input dari pengguna 
    # masukkan 0 jika nilai tidak diketahui (nilai yang akan dicari)
    p = int(input("Panjang (masukkan 0 jika tidak diketahui): "))
    l = int(input("Lebar (masukkan 0 jika tidak diketahui): "))
    k = int(input("Keliling (masukkan 0 jika tidak diketahui): "))
    L = int(input("Luas (masukkan 0 jika tidak diketahui): "))

    # mencetak hasil
    print("Panjang:", hitungPanjang())
    print("Lebar:", hitungLebar())
    print("Keliling:", hitungKeliling())
    print("Luas:", hitungLuas())

main()