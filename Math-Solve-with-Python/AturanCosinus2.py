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
# Diketahui sebuah segitiga ABC yang ketiga sisinya memiliki panjang yang sama,
# yaitu 3 cm. Tentukan besar sudut B!

import math
import numpy as np

def main():
    titik1 = input("Masukkan nama titik 1: ")
    titik2 = input("Masukkan nama titik 2: ")
    titik3 = input("Masukkan nama titik 3: ")

    sisi1 = int(input("Masukkan panjang sisi {} atau sisi {}{}: "
    .format(titik1.lower(), titik2.upper(), titik3.upper())))
    sisi2 = int(input("Masukkan panjang sisi {} atau sisi {}{}: "
    .format(titik2.lower(), titik1.upper(), titik3.upper())))
    sisi3 = int(input("Masukkan panjang sisi {} atau sisi {}{}: "
    .format(titik3.lower(), titik1.upper(), titik2.upper())))

    print("{}^2 = {}^2 + {}^2 - 2{}{} * cos {}".
    format(titik3.lower(), titik1.lower(), titik2.lower(), 
    titik1.lower(), titik2.lower(), titik3.upper()))

    print("{}^2 = {}^2 + {}^2 - 2 * {} * {} * cos {}".
    format(sisi3, sisi1, sisi2, sisi1, sisi2, titik3.upper()))

    print("{} = {} + {} - {} * cos {}".
    format(sisi3 * sisi3, sisi1 * sisi1, sisi2 * sisi2, 
    2 * sisi1 * sisi2, titik3.upper()))

    print("{} * cos {} = {} + {} - {}".
    format(2 * sisi1 * sisi2, titik3.upper(),
    sisi3 * sisi3, sisi1 * sisi1, sisi2 * sisi2))

    print("{} * cos {} = {}".
    format(2 * sisi1 * sisi2, titik3.upper(),
    sisi3 * sisi3 + sisi1 * sisi1 - sisi2 * sisi2))

    print("cos {} = {} / {}".
    format(titik3.upper(), sisi3 * sisi3 + sisi1 * sisi1 - sisi2 * sisi2, 2 * sisi1 * sisi2))

    print("cos {} = {}".
    format(titik3.upper(), 
    round((sisi3 * sisi3 + sisi1 * sisi1 - sisi2 * sisi2) / (2 * sisi1 * sisi2), 4)))

    print("{} = {}°".
    format(titik3.upper(), 
    round(np.degrees(np.arccos((sisi3 * sisi3 + sisi1 * sisi1 - sisi2 * sisi2) / (2 * sisi1 * sisi2))))))

main()