# Segitiga adalah bangun datar yang dibatasi dengan adanya tiga buah sisi 
# serta memiliki tiga buah titik sudut.

# Berdasarkan panjang sisinya : 
# Segitiga sama sisi -> ketiga sisinya sama panjang
# Segitiga sama kaki -> dua di antara tiga sisinya sama panjang 
# Segitiga sembarang -> ketiga sisinya memiliki panjang yang berbeda-beda, tidak ada yang sama

# Berdasarkan sudutnya : 
# Segitiga lancip -> mempunyai tiga sudut yang lancip
# Segitiga tumpul -> salah satu sudutnya adalah sudut tumpul
# Segitiga siku-siku -> salah satu sudutnya merupakan sudut siku-siku atau besarnya 90 derajat. 

def main():
    # Input sisi segitiga
    a = int(input("Panjang sisi 1: "))
    b = int(input("Panjang sisi 2: "))
    c = int(input("Panjang sisi 3: "))

    # Mengurutkan sisi a, b, c dari terpendek ke terpanjang
    if (a > c):
        a, c = c, a
    if (b > c):
        b, c = c, b

    # Menentukan apakah segitiga atau bukan
    if (c >= a + b):
        print("Ketiga sisi ini tidak dapat membentuk segitiga")
    # Memeriksa apakah sisi merupakan triple pythagoras
    elif (c * c == (a * a + b * b)):
        print("Ketiga sisi merupakan triple pythagoras dan membentuk segitiga siku-siku")
    else:
        # Menentukan jenis segitiga berdasarkan sisinya
        if (a == b == c):
            jenisSisi = "sama sisi"
        elif (a == b or b == c or a == c):
            jenisSisi = "sama kaki"
        else:
            jenisSisi = "sembarang"
        print("Berdasarkan sisinya, segitiga ini merupakan segitiga", jenisSisi)

        # Menentukan jenis segitiga berdasarkan sudutnya
        if (c * c > (a * a + b * b)):
            jenisSudut = "tumpul"
        else:
            jenisSudut = "lancip"
        print("Berdasarkan sudutnya, segitiga ini merupakan segitiga", jenisSudut)

main()