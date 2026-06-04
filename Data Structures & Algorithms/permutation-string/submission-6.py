class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt1 = {}
        cnt2 = {}

        for i in range(len(s1)):
            cnt1[s1[i]] = cnt1.get(s1[i], 0) + 1
            cnt2[s2[i]] = cnt2.get(s2[i], 0) + 1

        if cnt1 == cnt2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            cnt2[s2[right]] = cnt2.get(s2[right], 0) + 1
            cnt2[s2[left]] -= 1

            if cnt2[s2[left]] == 0:
                del cnt2[s2[left]]

            left += 1

            if cnt1 == cnt2:
                return True
        return False