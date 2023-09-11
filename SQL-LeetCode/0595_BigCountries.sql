-- Write your MySQL query statement below

-- Memilih kolom name, population, dan area untuk ditampilkan
SELECT name, population, area

-- Kolom tersebut diambil dari tabel world
FROM world

-- Baris yang ditampilkan hanyalah yang areanya lebih besar dari 3000000
WHERE area >= 3000000

-- atau populasinya lebih besar dari 25000000
OR population >= 25000000;