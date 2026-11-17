class Solution:
        def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
                return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))
                