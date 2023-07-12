import math

def main():
    huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    k = [
        [0,0,0],
        [1,0,0],
        [1,0,1],
        [0,0,1],
        [0,1,0],
        [1,1,0],
        [1,1,1],
        [0,1,1]        
    ]
    cari1 = input("Masukkan titik 1 : ")
    cari2 = input("Masukkan titik 2 : ")

    for i in range (8):
        if (cari1.lower() == huruf[i]):
            c1 = i
        if (cari2.lower() == huruf[i]):
            c2 = i

    jarak = ((k[c1][0]-k[c2][0]) * (k[c1][0]-k[c2][0]) +
    (k[c1][1]-k[c2][1]) * (k[c1][1]-k[c2][1]) + 
    (k[c1][2]-k[c2][2]) * (k[c1][2]-k[c2][2]))

    if (math.sqrt(jarak) % 1 == 0):
        print(round(math.sqrt(jarak)))
    else:
        print("√{}".format(jarak))

    return

main()