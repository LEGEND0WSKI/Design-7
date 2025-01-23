# T: O(n) for sorting O(nlogn)
# S: O(n)//
# Leetcode: Yes
# Issues: No

# usign sort + binary search// O(nlogn)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)       # sort
        n = len(citations)
        low =0
        high = n-1


        while low <= high:                  # binsearch
            mid = low + (high-low)//2
            diff = n - (mid)

            if diff == citations[mid]:
                return diff
            elif diff <= citations[mid]:
                high = mid-1
            else:
                low = mid+1

        return n-low
    
# t: O(n); s:O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        arr = [0]* (n+1)

        for i in citations:
            if i >= n:
                arr[-1] += 1            # directly inmcrement indexes
            else:
                arr[i]  += 1

        rsum = 0
        for i in range(n,-1,-1):        # start counting in reverse
            rsum += arr[i]
            if rsum >= i:
                return i