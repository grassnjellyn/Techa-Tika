-- Write your MySQL query statement below

-- Memilih kolom name untuk ditampilkan
SELECT name

-- Kolom tersebut diambil dari tabel customer
FROM customer

-- Baris yang ditampilkan hanyalah yang referee_id nya tidak sama dengan 2
WHERE referee_id != 2

-- atau referee_id nya adalah NULL
OR referee_id IS NULL;