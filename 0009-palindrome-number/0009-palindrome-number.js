function isPalindrome(x) {
  let result = 0;
  let dummy = x;
  
  while (x > 0) {
    let digit = x % 10;
    result = result * 10 + digit;
    x = Math.floor(x / 10); // Use Math.floor for integer division
  }

  return result === dummy;
}
