-- Write your MySQL query statement below

-- Memilih kolom unique_id dari tabel eu, dan name dari tabel e untuk ditampilkan
SELECT eu.unique_id, e.name

-- Mendeklarasikan tabel employees sebagai tabel e
FROM employees e

-- Tabel e digabungkan dengan tabel employeeuni yang dideklarasikan sebagai tabel eu
-- Jenis JOIN yang digunakan adalah LEFT JOIN karena semua baris di tabel e dimasukkan
LEFT JOIN employeeuni eu
ON e.id = eu.id;