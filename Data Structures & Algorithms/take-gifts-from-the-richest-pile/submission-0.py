class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            m = max(gifts)
            idx = gifts.index(m)
            gifts[idx] = int(m ** 0.5)
            
        ans = 0
        for x in gifts:
            ans = ans + x
        return ans