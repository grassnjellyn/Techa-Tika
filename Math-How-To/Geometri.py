# Barisan geometri adalah pola yang memiliki pengali atau rasio yang tetap 
# untuk setiap 2 suku yang berdekatan
# Rasio pada barisan geometri biasa disimbolkan dengan r

# Misal, ada suatu barisan, 1, 2, 4, 8, dan seterusnya 
# Barisan ini dikategorikan sebagai barisan geometri dikarenakan 
# pengali antar sukunya sama, yaitu 2
# Pengali atau rasio ini dapat diketahui dengan membagi nilai dari suatu suku 
# dengan suku sebelumnya, seperti 2/1, 4/2, ataupun 8/4
# Suku manapun yang dibagi dengan suku sebelumnya pasti memberikan hasil yang sama

# Dalam suatu barisan, Un merupakan bilangan pada suku ke-n 
# Sementara Sn merupakan jumlah seluruh barisan hingga suku ke-n
# Jadi, pada barisan 1, 2, 4, 8, ...
# U4 atau bilangan pada suku ke-4 adalah 8
# Sementara S4 atau jumlah seluruh barisan hingga suku ke-4 adalah 
# 1 + 2 + 4 + 8 = 15

def geometri(n, a, r):
    un = a * (r ** (n - 1))

    if (r == 1):
        sn = n * a
    else:
        sn = a * ((r ** n) - 1) / (r - 1)

    print("Suku ke-{} (Un): {}".format(n, un))
    print("Jumlah {} suku pertama (Sn): {}".format(n, sn))
    return 

def main():
    n = int(input("Suku yang hendak dicari: "))
    a = int(input("Dimulai dari: "))
    r = int(input("Rasio antar suku: "))

    geometri(n, a, r)

main()