class Solution {
    public int missingNumber(int[] nums) {
        // Menghitung panjang array nums
        int n = nums.length;

        // Menghitung jumlah seharusnya menggunakan rumus Gauss
        int jumlahSeharusnya = n * (n + 1) / 2;
        // Mendeklarasikan variabel untuk menyimpan jumlah sebenarnya
        int jumlahSebenarnya = 0;

        // Menghitung jumlah sebenarnya
        for (int i = 0; i < nums.length; i++) {
            jumlahSebenarnya += nums[i];
        }

        // Mengembalikan selisih antara jumlah seharusnya dan jumlah sebenarnya
        return jumlahSeharusnya - jumlahSebenarnya;
    }
}