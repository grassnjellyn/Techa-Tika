# SOAL : 
# 12 jam 34 menit 56 detik + 5 jam 43 menit 21 detik = ... jam ... menit ... detik

def jumlahkanWaktu(jam1, menit1, detik1, jam2, menit2, detik2):
    jumlahDetik = detik1 + detik2
    menitTambahan = jumlahDetik // 60
    sisaDetik = jumlahDetik % 60

    jumlahMenit = menit1 + menit2 + menitTambahan
    jamTambahan = jumlahMenit // 60
    sisaMenit = jumlahMenit % 60

    jumlahJam = jam1 + jam2 + jamTambahan

    return jumlahJam, sisaMenit, sisaDetik

def main():
    jam1 = int(input("Jam pertama : "))
    menit1 = int(input("Menit pertama : "))
    detik1 = int(input("Detik pertama : "))

    print("-" * 35)

    jam2 = int(input("Jam kedua : "))
    menit2 = int(input("Menit kedua : "))
    detik2 = int(input("Detik kedua : "))

    print("=" * 35)

    jam, menit, detik = jumlahkanWaktu(jam1, menit1, detik1, jam2, menit2, detik2)
    print(f"Hasilnya adalah {jam} jam {menit} menit {detik} detik")

if __name__ == '__main__':
    main()