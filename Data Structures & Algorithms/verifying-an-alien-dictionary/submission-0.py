class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: [order.index(c) for c in w])
