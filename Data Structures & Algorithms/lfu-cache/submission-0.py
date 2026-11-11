class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    def pop_head(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove_node(node)
        return node
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node = {}
        self.freq_list = {}
    def _update_freq(self, node):
        freq = node.freq
        self.freq_list[freq].remove_node(node)
        if freq == self.min_freq and self.freq_list[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_list:
            self.freq_list[node.freq] = DoublyLinkedList()
        self.freq_list[node.freq].add_node(node)
    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update_freq(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_node) >= self.capacity:
                lru_node = self.freq_list[self.min_freq].pop_head()
                del self.key_node[lru_node.key]
            node = Node(key, value)
            self.key_node[key] = node
            self.min_freq = 1
            if 1 not in self.freq_list:
                self.freq_list[1] = DoublyLinkedList()
            self.freq_list[1].add_node(node)