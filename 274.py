"""274. H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times."
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        freq = [0] * (n+1)
        for i in citations:
            if i >= n:
                freq[n] += 1
            else:
                freq[i] += 1
        sum = 0
        for i in range(len(freq)-1, -1, -1):
            if freq[i] + sum >= i:
                return i
            sum += freq[i]
        else:
            return 0
