class Solution {
    public int searchInsert(int[] nums, int target) {
        // Deklarasi variabel i
        int i = 0;

        // Selama i masih lebih kecil dari panjang nums, dan
        // elemen ke i dari array nums lebih kecil dari target
        while (i < nums.length && nums[i] < target) {
            // i akan terus bertambah
            i++;
        }

        return i;
    }
}