class WordDictionary:
    def __init__(self):
        self.trie = {}
    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "#" in node
            ch = word[i]
            if ch == ".":
                for key in node:
                    if key != "#" and dfs(i + 1, node[key]):
                        return True
                return False
            if ch not in node:
                return False
            return dfs(i + 1, node[ch])
        return dfs(0, self.trie)