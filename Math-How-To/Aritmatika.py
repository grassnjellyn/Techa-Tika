# Barisan Aritmatika adalah barisan bilangan yang memiliki pola yang tetap
# Polanya dapat terbentuk berdasarkan operasi penjumlahan atau pengurangan
# Jadi, setiap urutan suku memiliki selisih atau beda yang nilainya sama
# Selisih inilah yang dinamakan beda, yang biasa disimbolkan dengan b

# Misal, ada suatu barisan, 2, 5, 8, 11, dan seterusnya
# Barisan ini dikategorikan sebagai barisan aritmatika dikarenakan 
# selisih antar sukunya sama, yaitu 3
# Selisih atau beda ini dapat diketahui dengan mengurangkan nilai dari suatu suku 
# dengan suku sebelumnya, seperti 5-2, 8-5, ataupun 11-8
# Suku manapun yang dikurangkan dengan suku sebelumnya pasti memberikan hasil yang sama

# Dalam suatu barisan, Un merupakan bilangan pada suku ke-n 
# Sementara Sn merupakan jumlah seluruh barisan hingga suku ke-n
# Jadi, pada barisan 2, 5, 8, 11, ...
# U4 atau bilangan pada suku ke-4 adalah 11
# Sementara S4 atau jumlah seluruh barisan hingga suku ke-4 adalah 
# 2 + 5 + 8 + 11 = 26

def aritmatika(n, a, b):
    un = a + (n - 1) * b;
    sn = (n / 2) * (2 * a + (n - 1) * b);

    print("Suku ke-{} (Un): {}".format(n, un));
    print("Jumlah {} suku pertama (Sn): {}".format(n, sn));

    return

def main():
    n = int(input("Suku yang hendak dicari: "));
    a = int(input("Dimulai dari: "));
    b = int(input("Beda antar suku: "));

    aritmatika(n, a, b);

main()