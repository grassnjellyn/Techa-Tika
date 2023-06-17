# Bilangan Kuadrat atau bilangan pangkat dua adalah suatu bilangan yang diperoleh dari 
# hasil dua bilangan bulat yang sama yang dikalikan

# Misal, 9 merupakan bilangan kuadrat karena 3 kali 3 hasilnya adalah 9
# Sedangkan 10 bukan bilangan kuadrat karena tidak ada bilangan bulat yang jika dikalikan
# dengan dirinya sendiri hasilnya adalah 10

# Untuk mengetahui apakah suatu bilangan merupakan bilangan kuadrat atau bukan,
# dapat dengan cara memeriksa hasil akarnya merupakan bilangan bulat atau bukan

def cek_kuadrat(n):
    # Mencari nilai akar dari bilangan n
    akar = n ** (0.5)
    # Memeriksa apakah hasil akar merupakan bilangan bulat
    # Jika akar n merupakan bilangan bulat, maka n adalah bilangan kuadrat
    if (akar == int(akar)):
        kuadrat = True
    else:
        kuadrat = False

    # Mengembalikan status kuadrat (True / False)
    return kuadrat

def main():
    # Meminta input dari pengguna
    bilangan = int(input("Masukkan bilangan: "))

    # Memeriksa dan mencetak apakah bilangan tersebut kuadrat atau bukan
    if cek_kuadrat(bilangan):
        print(bilangan, "adalah bilangan kuadrat.")
    else:
        print(bilangan, "bukan bilangan kuadrat.")

if __name__ == '__main__':
    main()

# n = 5
# akar = 2,236
# int(akar) = 2
# 5 bukan bilangan kuadrat

# n = 9
# akar = 3
# int(akar) = 3
# 9 merupakan bilangan kuadrat