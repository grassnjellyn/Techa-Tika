import math

def translasi(titik_awal, translasi):
    return (titik_awal[0] + translasi[0], titik_awal[1] + translasi[1])

def refleksi(titik_awal, jenis):
    titik_hasil = (0,0)
    if (jenis == 1):
        titik_hasil = (titik_awal[0], -titik_awal[1])
    elif (jenis == 2):
        titik_hasil = (-titik_awal[0], titik_awal[1])
    elif (jenis == 3):
        titik_hasil = (-titik_awal[0], -titik_awal[1])
    elif (jenis == 4):
        titik_hasil = (titik_awal[1], titik_awal[0])
    elif (jenis == 5):
        titik_hasil = (-titik_awal[1], -titik_awal[0])
    elif (jenis == 6):
        garis_y = int(input("Terhadap garis y = "))
        titik_hasil = (titik_awal[0], 2 * garis_y - titik_awal[1])
    elif (jenis == 7):
        garis_x = int(input("Terhadap garis x = "))
        titik_hasil= (2 * garis_x - titik_awal[0], titik_awal[1])
    return titik_hasil

def rotasi(titik_awal, sudut, pusat_rotasi):
    x_relatif = titik_awal[0] - pusat_rotasi[0]
    y_relatif = titik_awal[1] - pusat_rotasi[1]
    
    radian = math.radians(sudut)
    x_rotasi = math.cos(radian) * x_relatif - math.sin(radian) * y_relatif
    y_rotasi = math.sin(radian) * x_relatif + math.cos(radian) * y_relatif
    
    x_rotasi += pusat_rotasi[0]
    y_rotasi += pusat_rotasi[1]
    
    return (round(x_rotasi), round(y_rotasi))

def dilatasi(titik_awal, faktor_skala, pusat_dilatasi):
    x_relatif = titik_awal[0] - pusat_dilatasi[0]
    y_relatif = titik_awal[1] - pusat_dilatasi[1]
    
    x_dilatasi = x_relatif * faktor_skala
    y_dilatasi = y_relatif * faktor_skala
    
    x_dilatasi += pusat_dilatasi[0]
    y_dilatasi += pusat_dilatasi[1]
    
    return (round(x_dilatasi), round(y_dilatasi))

def main():
    print("=" * 50)
    print("Bagian 1 : Input titik yang akan ditransformasi")
    x = int(input("Masukkan x : "))
    y = int(input("Masukkan y : "))
    titik_awal = (x,y)
    print(f"Titik Awal = {titik_awal}")

    print("=" * 50)
    print("Bagian 2 : Menentukan jenis transformasi")
    print("""Berikut ini merupakan kode dari jenis transformasi
1. Translasi (Pergeseran)
2. Refleksi (Pencerminan)
3. Rotasi (Perputaran)
4. Dilatasi (Perbesaran)""")
    print("=" * 50)
    jenis = int(input("Kode transformasi yang ingin dilakukan : "))

    if(jenis == 1):
        print("=" * 50)
        print("Bagian 3 : Input titik translasi")
        x = int(input("Masukkan x : "))
        y = int(input("Masukkan y : "))
        titik_translasi = (x,y)

        print("=" * 50)
        hasil_translasi = translasi(titik_awal, titik_translasi)
        print(f"Titik setelah ditranslasi = {hasil_translasi}")

    elif (jenis == 2):
        print("=" * 50)
        print("Bagian 3 : Menentukan jenis refleksi")
        print("""Berikut ini merupakan kode dari jenis refleksi terhadap : 
1. Sumbu x
2. Sumbu y
3. Titik asal  (0,0)
4. Garis y = x
5. Garis y = -x
6. Garis y = h
7. Garis x = h""")
        print("=" * 50)
        jenisR = int(input("Kode jenis refleksi yang ingin dilakukan : "))

        print("=" * 50)
        hasil_refleksi = refleksi(titik_awal, jenisR)
        print(f"Titik setelah direfleksi = {hasil_refleksi}")

    elif (jenis == 3):
        print("=" * 50)
        print("Bagian 3 : Input sudut rotasi (derajat)")
        sudut_rotasi = float(input("Masukkan sudut rotasi : "))
        
        print("=" * 50)
        pusat_rotasi = (int(input("Masukkan x pusat rotasi : ")), int(input("Masukkan y pusat rotasi : ")))
        hasil_rotasi = rotasi(titik_awal, sudut_rotasi, pusat_rotasi)
        print(f"Titik setelah dirotasi = {hasil_rotasi}")

    elif (jenis == 4):
        print("=" * 50)
        print("Bagian 3 : Input faktor skala dilatasi")
        faktor_dilatasi = float(input("Masukkan faktor skala dilatasi : "))
        
        print("=" * 50)
        pusat_dilatasi = (int(input("Masukkan x pusat dilatasi : ")), int(input("Masukkan y pusat dilatasi : ")))
        hasil_dilatasi = dilatasi(titik_awal, faktor_dilatasi, pusat_dilatasi)
        print(f"Titik setelah dilatasi = {hasil_dilatasi}")

if __name__ == '__main__':
    main()