class Solution:
    def replaceElements(self, arr):
        right = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = right
            right = max(right, temp)
        return arr