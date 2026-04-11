class Solution:
    def twoSum(self, numbers, target):
        suman = 0
        temp = len(numbers) - 1

        while suman < temp:
            total = numbers[suman] + numbers[temp]

            if total == target:
                return [suman + 1, temp + 1]

            elif total < target:
                suman += 1
            else:
                temp -= 1