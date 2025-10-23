class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        count = 1
        a, b = 0, 1
        while count != n: 
            c = a + b
            a = b
            b = c
            count += 1
        return c