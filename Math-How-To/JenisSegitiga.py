def main():
    # Input sisi segitiga
    a = int(input("Panjang sisi 1: "))
    b = int(input("Panjang sisi 2: "))
    c = int(input("Panjang sisi 3: "))

    # Sisi c atau sisi 3 harus merupakan sisi terpanjang
    if (a > c):
        temp = a
        a = c 
        c = temp
    if (b > c):
        temp = b
        b = c
        c = temp

    # Menentukan apakah segitiga atau bukan
    if (c >= a + b):
        print("Ketiga sisi ini tidak dapat membentuk segitiga")
    elif (c * c == (a * a + b * b)):
        print("Ketiga sisi merupakan triple pythagoras dan membentuk segitiga siku-siku")
    else:
        if (a == b == c):
            jenisSisi = "sama sisi"
        elif (a == b or b == c or a == c):
            jenisSisi = "sama kaki"
        else:
            jenisSisi = "sembarang"
        print("Berdasarkan sisinya, segitiga ini merupakan segitiga", jenisSisi)

        if (c * c > (a * a + b * b)):
            jenisSudut = "tumpul"
        else:
            jenisSudut = "lancip"
        print("Berdasarkan sudutnya, segitiga ini merupakan segitiga", jenisSudut)

main()