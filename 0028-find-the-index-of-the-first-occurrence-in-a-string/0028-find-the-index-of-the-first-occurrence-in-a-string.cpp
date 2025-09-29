class Solution {
public:
    int strStr(string haystack, string needle) {
        if( haystack == ""){
            return 0;
        }
        int pos = haystack.find(needle, 0);
        if(pos >= 0){
            return pos;
        }
        return -1;
    }
};