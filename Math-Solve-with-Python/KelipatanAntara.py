# SOAL : 
# Jumlah semua bilangan kelipatan 3 dan 4 antara 200 dan 450 adalah ...

def hitung(x1, x2, awal, akhir):
    x = x1 * x2
    for i in range (awal+1, akhir, 1):
        if (i % x == 0):
            a = i
            break;
    for j in range (akhir-1, awal, -1):
        if (j % x == 0):
            Un = j
            break;

    return [x, a, Un]

def main():
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    awal= int(input("Bilangan awal: "))
    akhir = int(input("Bilangan akhir: "))

    x = hitung(x1, x2, awal, akhir)[0]
    a = hitung(x1, x2, awal, akhir)[1]
    Un = hitung(x1, x2, awal, akhir)[2]

    print()
    print("Bilangan yang merupakan kelipatan {} dan {} adalah bilangan kelipatan {}"
    .format(x1, x2, x))
    print()

    print("Di antara {} dan {}".format(awal, akhir))
    print("Bilangan pertama yang merupakan kelipatan {} adalah {}"
    .format(x, a))
    print("Bilangan terakhir yang merupakan kelipatan {} adalah {}"
    .format(x, Un))
    print()

    print("a = {}".format(a))
    print("Un = {}".format(Un))
    print()

    print("Un = a + (n - 1) * b")
    print("{} = {} + (n - 1) * {}".format(Un, a, x))
    print("{} = {} + {}n - {}".format(Un, a, x, x))
    print("{} - {} + {} = {}n".format(Un, a, x, x))
    print("{}n = {}".format(x, Un - a + x))
    print("n = {} / {}".format(Un - a + x, x))
    print("n = {}".format((Un - a + x) // x))
    print()

    n = (Un - a + x) // x
    Sn = (n / 2) * (2 * a + (n - 1) * x)

    print("Sn = (n / 2) * (2 * a + (n - 1) * x)")
    print("Sn = ({} / 2) * (2 * {} + ({} - 1) * {})"
    .format(n, a, n, x))
    print("Sn = ({} / 2) * ({} + ({} * {}))"
    .format(n, 2 * a, n - 1, x))
    print("Sn = ({} / 2) * ({} + {})"
    .format(n, 2 * a, (n - 1) * x))
    print("Sn = ({} / 2) * {}"
    .format(n, 2 * a + (n - 1) * x))
    print("Sn = {}".format(Sn))

    print()

main()