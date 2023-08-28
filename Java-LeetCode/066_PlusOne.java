class Solution {
    public int[] plusOne(int[] digits) {
        // Mengetahui panjang digits
        int n = digits.length;

        // Menambahkan 1
        // Looping dimulai dari belakang karena sistemnya seperti penjumlahan simpan
        for (int i = n - 1; i >= 0; i--) {
            // Jika digit bukan 9, ditambahkan 1, selesai
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // Jika digit 9, yang ditulis hanya 0, kemudian dilanjutkan ke posisi selanjutnya
            digits[i] = 0;
        }

        // Kondisi jika semua digitnya adalah 9, misal agar 999 -> 1000
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1;
        return newDigits;
    }
}