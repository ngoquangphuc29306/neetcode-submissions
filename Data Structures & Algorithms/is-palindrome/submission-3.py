class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for x in s:
            if x.isalpha() or x.isdigit():
                if x.isalpha():
                    res += x.lower()
                else:
                    res += x
        l = 0
        r = len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True