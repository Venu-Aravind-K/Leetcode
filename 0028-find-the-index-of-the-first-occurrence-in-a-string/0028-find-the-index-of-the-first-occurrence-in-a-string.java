class Solution {
    public int strStr(String haystack, String needle) {
        int len1 = haystack.length();
        int len2 = needle.length();
        if(len1 == 0){
            return 0;
        }
        for(int i = 0; i<= len1-len2; i++){
            String slice = haystack.substring(i,i+len2);
            if(slice.equals(needle)){
                return i;
            }
        }
        return -1;
    }
}