class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = 0
        for x in s:
            if x == "(":
                left += 1
                right += 1
            elif x == ")":
                left -= 1
                right -= 1
            else:
                left -= 1
                right += 1
            if right < 0:
                return False
            if left < 0:
                left = 0
        if left == 0:
            return True
        return False