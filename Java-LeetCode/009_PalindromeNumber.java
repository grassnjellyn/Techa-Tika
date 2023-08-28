class Solution {
    public boolean isPalindrome(int x) {
        // Bilangan negatif sudah pasti bukan palindrome
        if (x < 0) {
            return false;
        }

        // Mendeklarasikan variabel : 
        // number untuk menyimpan nilai x awal
        int number = x;
        // reverse untuk menyimpan nilai yang sudah dibalik, misal dari 123 ke 321
        int reverse = 0;

        // Mengubah reverse menjadi yang seharusnya (membalikkan angka)
        while (x != 0) {
            int sisa = x % 10;
            reverse = reverse * 10 + sisa;
            x /= 10;
        }

        // Memeriksa dan mengembalikan apakah number sama dengan reverse
        return number == reverse;
    }
}