-- Write your MySQL query statement below

-- Memilih kolom id dari tabel w1 untuk ditampilkan
SELECT w1.id

-- Kolom tersebut diambil dari tabel Weather yang dideklarasikan sebagai w1
FROM Weather w1

-- Yang digabungkan dengan tabel Weather yang dideklarasikan sebagai w2
JOIN Weather w2 

-- Digabungkan berdasarkan kesamaan kolom recordDate di tabel w1
ON w1.recordDate = 

-- Dan juga recordDate di w2, yang tanggalnya sudah ditambahkan
DATE_ADD(w2.recordDate, INTERVAL 1 DAY)

-- Baris yang diambil hanyalah pada saat suhu di w1 lebih besar dari w2
WHERE w1.temperature > w2.temperature;