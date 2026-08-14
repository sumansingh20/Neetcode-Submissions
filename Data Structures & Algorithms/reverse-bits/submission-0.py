class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            ans = ans * 2 + n % 2
            n //= 2

        return ans