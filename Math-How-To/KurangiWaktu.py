# SOAL : 
# 18 jam 18 menit 17 detik - 5 jam 43 menit 21 detik = ... jam ... menit ... detik

def kurangiWaktu(jam1, menit1, detik1, jam2, menit2, detik2):
    if detik1 < detik2:
        detik1 += 60
        menit1 -= 1
    
    selisihDetik = detik1 - detik2
    
    if menit1 < menit2:
        menit1 += 60
        jam1 -= 1
    
    selisihMenit = menit1 - menit2
    selisihJam = jam1 - jam2
    
    return selisihJam, selisihMenit, selisihDetik

def main():
    jam1 = int(input("Jam pertama : "))
    menit1 = int(input("Menit pertama : "))
    detik1 = int(input("Detik pertama : "))

    print("-" * 35)

    jam2 = int(input("Jam kedua : "))
    menit2 = int(input("Menit kedua : "))
    detik2 = int(input("Detik kedua : "))

    print("=" * 35)

    jam, menit, detik = kurangiWaktu(jam1, menit1, detik1, jam2, menit2, detik2)
    print(f"Hasilnya adalah {jam} jam {menit} menit {detik} detik")

main()