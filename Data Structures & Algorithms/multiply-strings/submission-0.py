class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                x = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                x += ans[i + j + 1]

                ans[i + j + 1] = x % 10
                ans[i + j] += x // 10

        return ''.join(map(str, ans)).lstrip('0')