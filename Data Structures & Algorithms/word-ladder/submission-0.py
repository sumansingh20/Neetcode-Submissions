class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nums = set(wordList)
        q = []
        q.append([beginWord, 1])
        while len(q) > 0:
            data = q.pop(0)
            word = data[0]
            step = data[1]
            if word == endWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    new = word[:i] + ch + word[i + 1:]
                    if new in nums:
                        nums.remove(new)
                        q.append([new, step + 1])
        return 0