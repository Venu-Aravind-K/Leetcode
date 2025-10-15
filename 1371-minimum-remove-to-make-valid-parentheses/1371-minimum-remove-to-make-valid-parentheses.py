class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_count = 0
        result = ""
        for ch in s:
            if ch == "(":
                open_count += 1
                result += ch
            elif ch == ")":
                if open_count > 0:
                    result += ch
                    open_count -= 1
            else:
                result += ch
        print(result,open_count)
        final = ""
        if open_count > 0:
            for ch in result[::-1]:
                if (ch == "(") and (open_count > 0):
                    open_count -= 1
                    print(final, open_count)
                    continue
                else:
                    final += ch   
        else: 
            return result
        return final[::-1]