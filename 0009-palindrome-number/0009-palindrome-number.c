bool isPalindrome(int x) {
    long result = 0;
    int dummy = x;
    int digit;
    while(x > 0){
        digit = x % 10;
        result = result*10 + digit;
        x = x / 10;
    }
    if (result == dummy){
        return true;
    }
    else{
        return false;
    }
}

