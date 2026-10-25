class Solution:
    def calPoints(self, operations):
        a = []

        for x in operations:
            if x == "C":
                a.pop()
            elif x == "D":
                a.append(2 * a[-1])
            elif x == "+":
                a.append(a[-1] + a[-2])
            else:
                a.append(int(x))
        return sum(a)