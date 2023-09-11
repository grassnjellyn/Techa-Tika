-- Write your MySQL query statement below

-- Memilih kolom unique_id dari tabel eu, dan name dari tabel e untuk ditampilkan
SELECT eu.unique_id, e.name

-- Mendeklarasikan tabel employees sebagai tabel e
FROM employees e

-- Tabel e digabungkan dengan tabel employeeuni yang dideklarasikan sebagai tabel eu
-- Jenis JOIN yang digunakan adalah LEFT JOIN karena semua baris di tabel e ditampilkan
LEFT JOIN employeeuni eu

-- Barisan dengan id yang sama di tabel e dan tabel eu, ditampilkan di satu baris yang sama
ON e.id = eu.id;