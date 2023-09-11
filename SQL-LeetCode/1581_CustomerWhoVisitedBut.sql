-- Write your MySQL query statement below

-- Memilih baris customer_id dari tabel v, 
-- dan juga menghitung jumlah baris visit_id dari tabel v --> COUNT(), untuk ditampilkan
SELECT v.customer_id, COUNT(v.visit_id)

-- Hasil perhitungan visit_id dari tabel v ditulis sebagai kolom baru,
-- dengan nama 'count_no_trans' atau yang berarti hitung yang tanpa transaksi
AS count_no_trans

-- Diambil dari 2 tabel yang digabungkan
-- Yang pertama adalah tabel visits yang dideklarasikan sebagai tabel v
FROM visits v

-- Yang kedua adalah tabel transactions yang dideklarasikan sebagai tabel t
-- Jenis join nya adalah LEFT JOIN dikarenakan untuk tabel kiri atau tabel pertama 
-- (yaitu tabel v), data dari semua barisnya ditampilkan
LEFT JOIN transactions t

-- Digabungkan berdasarkan kesamaan antara visit_id di tabel v dan tabel t
ON v.visit_id = t.visit_id

-- Baris yang ditampilkan hanyalah yang visit_id pada tabel t nya NULL
WHERE t.visit_id IS NULL

-- Data dikelompokkan atau disatukan berdasarkan kolom customer_id pada tabel v
GROUP BY v.customer_id;