# SOAL : 
# Hitung luas permukaan balok dengan panjang 4 cm, lebar 3 cm, dan tinggi 2 cm

def main():
    p = int(input("Panjang: "))
    l = int(input("Lebar: "))
    t = int(input("Tinggi: "))
    satuan = input("Masukkan satuan (cm/m/dll): ")

    lp = 2 * (p*l + p*t + l*t)

    print("Lp = 2 * (pl + pt + lt)")
    print("   = 2 * (", p, "*", l, " + ", p, "*", t, " + ", l, "*", t, ")", sep="")
    print("   = 2 * (", p*l, " + ", p*t, " + ", l*t, ")", sep="")
    print("   = 2 * (", p*l + p*t + l*t, ")", sep="")
    print("Lp =", 2 * (p*l + p*t + l*t))

    print("Jadi, luas permukaan balok adalah ", lp, " ", satuan, "^2", sep="")

main()