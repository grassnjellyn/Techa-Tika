# SOAL :
# Diketahui sebuah matriks A sebagai berikut:
# 1 2 3
# 4 5 6 
# 7 8 9
# Hitung nilai determinan dari matriks A di atas!

def buatMatriks(d1, d2):
    arr = [None]*d1
    for i in range(0, d1, 1):
        arr[i] = [None]*d2
    return arr

def main():
    print("Masukkan data: ")
    # membuat matriks
    m = buatMatriks(3, 3)
    # input data ke dalam matriks
    for i in range(3):
        for j in range(3):
            m[i][j] = int(input("Baris {} kolom {} : ".format(i+1, j+1)))

    # menampilkan bentuk matriks 
    for i in range(3):
        print("|", end=" ")
        for j in range (3):
            print(m[i][j], end=" ")
        print("|", end=" ")
        for k in range (2):
            print(m[i][k], end=" ")
        print("|", end=" ")
        print()

    # menghitung determinan
    determinan = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] - m[2][0] * m[1][1] * m[0][2] - m[2][1] * m[1][2] * m[0][0] - m[2][2] * m[1][0] * m[0][1]

    print("det(A) = (({}*{}*{}) + ({}*{}*{}) + ({}*{}*{})) - (({}*{}*{}) + ({}*{}*{}) + ({}*{}*{}))"
    .format(m[0][0], m[1][1], m[2][2], m[0][1], m[1][2], m[2][0], m[0][2], m[1][0], m[2][1],
    m[2][0], m[1][1], m[0][2], m[2][1], m[1][2], m[0][0], m[2][2], m[1][0], m[0][1]))

    print("det(A) = ({} + {} + {}) - ({} + {} + {})"
    .format(m[0][0] * m[1][1] * m[2][2], m[0][1] * m[1][2] * m[2][0], m[0][2] * m[1][0] * m[2][1],
    m[2][0] * m[1][1] * m[0][2], m[2][1] * m[1][2] * m[0][0], m[2][2] * m[1][0] * m[0][1]))

    print("det(A) = {} - {}"
    .format(m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1], 
    m[2][0] * m[1][1] * m[0][2] + m[2][1] * m[1][2] * m[0][0] + m[2][2] * m[1][0] * m[0][1]))

    print("det(A) = {}".format(determinan))

    print("Jadi, determinan dari matriks A adalah", determinan)

main()