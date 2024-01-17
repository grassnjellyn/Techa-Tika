def skema_horner(koefisien, x):
    hasil = 0
    for i in koefisien:
        hasil = hasil * x + i
    return hasil


def main():
    koefisien = []
    x = int(input("Nilai x: "))

    derajat = int(input("Derajat Tertinggi: "))
    for i in range (derajat, -1, -1):
        koef = int(input(f"Koefisien x^{i}: "))
        koefisien.append(koef)

    hasil = skema_horner(koefisien, x)
    print(f"Hasil untuk x = {x} adalah: {hasil}")

main()