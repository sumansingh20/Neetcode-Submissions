class Solution:
    def mergeTriplets(self, triplets, target):
        x = False
        y = False
        z = False
        for arr in triplets:
            if arr[0] > target[0]:
                continue
            if arr[1] > target[1]:
                continue
            if arr[2] > target[2]:
                continue
            if arr[0] == target[0]:
                x = True
            if arr[1] == target[1]:
                y = True
            if arr[2] == target[2]:
                z = True
        if x and y and z:
            return True
        return False