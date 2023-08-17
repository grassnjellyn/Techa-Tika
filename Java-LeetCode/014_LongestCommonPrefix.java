class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Mengembalikan string kosong jika strs null atau kosong
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Menyimpan nilai index ke 0 strs ke var hasil
        String hasil = strs[0]; 

        // Untuk memeriksa apakah elemen ke i dari strs diawali dengan hasil
        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(hasil)) {
                // Jika tidak, karakter terakhir dari hasil akan dibuang
                hasil = hasil.substring(0, hasil.length() - 1);

                // Jika hasil kosong, mengembalikan string kosong
                if (hasil.isEmpty()) {
                    return "";
                }
            }
        }

        return hasil;
    }
}

// hasil = "flower"
// i = 1 -> strs[1] = "flow"
// "flow" tidak diawali "flower"
// hasil berubah dari "flower" menjadi "flowe"
// "flow" tidak diawali dengan "flowe"
// hasil berubah dari "flowe" menjadi "flow"
// "flow" diawali dengan "flow"

// i = 2 -> strs[2] = "flight"
// "flight" tidak diawali dengan "flow"
// hasil berubah dari "flow" menjadi "flo"
// "flight" tidak diawali dengan "flo"
// hasil berubah dari "flo" menjadi "fl"
// "flight" diawali dengan "fl"

// karena sudah memeriksa semua elemen, 
// maka fungsi akan mengembalikan hasil
// sehingga outputnya adalah hasil = "fl"