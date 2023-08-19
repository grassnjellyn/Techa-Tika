class Solution {
    public int lengthOfLastWord(String s) {
        // Mendeklarasikan variabel kata bertipe array of string
        // untuk menyimpan daftar kata dari suatu kalimat
        String[] kata = s.split(" ");

        // Mengembalikan panjang dari elemen terakhir pada array kata
        // atau dengan kata lain panjang dari kata terakhir
        return kata[kata.length - 1].length();
    }
}