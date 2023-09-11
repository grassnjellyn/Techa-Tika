-- Write your MySQL query statement below

-- Memilih kolom product_id untuk ditampilkan
SELECT product_id

-- Kolom tersebut diambil dari tabel products
FROM products

-- Baris yang ditampilkan hanyalah baris yang low_fats nya adalah 'Y'
WHERE low_fats = 'Y'

-- dan recyclable nya juga adalah 'Y'
AND recyclable = 'Y';