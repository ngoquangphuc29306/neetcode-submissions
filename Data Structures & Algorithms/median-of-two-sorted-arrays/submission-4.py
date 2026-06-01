class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = 0
        r = n

        while l <= r:
            p1 = (l + r) // 2
            p2 = (m + n + 1) // 2 - p1

            maxL1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            minR1 = float('inf') if p1 == n else nums1[p1]

            maxL2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            minR2 = float('inf') if p2 == m else nums2[p2]

            if maxL1 <= minR2 and maxL2 <= minR1:
                if (m + n) % 2 == 0:
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2.0
                else:
                    return max(maxL1, maxL2)
            elif maxL1 > minR2:
                r = p1 - 1
            else:
                l = p1 + 1
        return 0.0