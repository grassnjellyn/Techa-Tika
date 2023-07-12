# ------ ATURAN COSINUS ------

# Pengertian : 
# Aturan Cosinus merupakan aturan yang menjelaskan hubungan antara kuadrat panjang sisi 
# dengan nilai cosinus dari salah satu sudut pada segitiga.

# Syarat : 
# Ada 2 kasus dimana aturan cosinus dapat digunakan 
# untuk mencari unsur-unsur lain dalam suatu segitiga : 
# 1) Diketahui 2 sisi dan sudut apitnya -> sisi segitiga yang lainnya
# 2) Diketahui ketiga sisinya -> besar dari salah satu sudutnya

# SOAL : 
# Diketahui segitiga dengan panjang sisi AB = 4 cm, sisi BC = 7 cm
# Jika besar sudut B adalah 60°, tentukan panjang sisi AC!

import math

def main():
    # titik yang besar sudutnya tidak diketahui
    titik1 = input("Masukkan nama titik 1: ")
    titik2 = input("Masukkan nama titik 2: ")
    # titik yang besar sudutnya diketahui
    titik3 = input("Masukkan nama titik 3: ")

    sisi1 = int(input("Masukkan panjang sisi {} atau sisi {}{}: "
    .format(titik1.lower(), titik2.upper(), titik3.upper())))
    sisi2 = int(input("Masukkan panjang sisi {} atau sisi {}{}: "
    .format(titik2.lower(), titik1.upper(), titik3.upper())))

    sudut = int(input("Masukkan besar sudut {}: ".format(titik3.upper())))

    print("{}^2 = {}^2 + {}^2 - 2{}{} * cos {}".
    format(titik3.lower(), titik1.lower(), titik2.lower(), 
    titik1.lower(), titik2.lower(), titik3.upper()))

    print("{}^2 = {}^2 + {}^2 - 2 * {} * {} * cos {}°".
    format(titik3.lower(), sisi1, sisi2, sisi1, sisi2, sudut))

    print("{}^2 = {} + {} - {} * {}".
    format(titik3.lower(), sisi1 * sisi1, sisi2 * sisi2, 
    2 * sisi1 * sisi2, round(math.cos(sudut / 180 * math.pi), 1)))

    print("{}^2 = {} - {}".
    format(titik3.lower(), sisi1 * sisi1 + sisi2 * sisi2, 
    round(2 * sisi1 * sisi2 * math.cos(sudut / 180 * math.pi))))

    print("{}^2 = {}".
    format(titik3.lower(), sisi1 * sisi1 + sisi2 * sisi2 -
    round(2 * sisi1 * sisi2 * math.cos(sudut / 180 * math.pi))))

    print("{} = √{}".
    format(titik3.lower(), sisi1 * sisi1 + sisi2 * sisi2 -
    round(2 * sisi1 * sisi2 * math.cos(sudut / 180 * math.pi))))

    print("{} = {}".
    format(titik3.lower(), round(math.sqrt(sisi1 * sisi1 + sisi2 * sisi2 -
    round(2 * sisi1 * sisi2 * math.cos(sudut / 180 * math.pi))), 2)))

main()