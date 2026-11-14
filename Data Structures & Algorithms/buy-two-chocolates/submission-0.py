class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        return money - s if (s := sum(sorted(prices)[:2])) <= money else money
