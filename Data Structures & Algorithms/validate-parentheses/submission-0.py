class Solution:
    def isValid(self, s):
        suman = []
        for ch in s:
            if ch in "([{":
                suman.append(ch)
            else:
                if not suman:
                    return False
                top = suman.pop()
                if ch == ")" and top != "(":
                    return False
                if ch == "}" and top != "{":
                    return False
                if ch == "]" and top != "[":
                    return False
        return len(suman) == 0