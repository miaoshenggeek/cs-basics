from typing import List

#1561. Maximum Number of Coins You Can Get
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3::2])
        #S S S S S S M L M L M L M L M L