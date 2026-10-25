class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            x = str1[:i]

            if str1 == x * (len(str1) // i) and str2 == x * (len(str2) // i):
                return x

        return ""