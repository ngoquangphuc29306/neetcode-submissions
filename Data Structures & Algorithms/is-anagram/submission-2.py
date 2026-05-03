class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = {}

        for char in s:
            cnt[char] = cnt.get(char, 0) + 1

        for char in t:
            if char not in cnt or cnt[char] == 0:
                return False
            cnt[char] -= 1
        return True