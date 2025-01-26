# T: O(1) for put and get
# S: O(n) for hmap, LL and Freqmap
# Leetcode: Yes
# Issues:update function spellcheck and put funtion indentation

class LFUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.next = None
            self.prev = None

    class DLList:
        def __init__(self):
            self.head = LFUCache.Node(-1, -1)
            self.tail = LFUCache.Node(-1, -1)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0

        def addNodeToHead(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1

        def removeNode(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            self.size -= 1

    def __init__(self, capacity: int):
        self.hmap = {}  # Key-to-Node mapping
        self.freqMap = {}  # Freq-to-DLList mapping
        self.capacity = capacity
        self.minFreq = 0

    def update(self, node):
        oldF = node.freq
        oldFList = self.freqMap[oldF]
        oldFList.removeNode(node)

        if oldF == self.minFreq and oldFList.size == 0:
            self.minFreq += 1

        node.freq += 1                                  # used freq +1
        newF = node.freq
        if newF not in self.freqMap:
            self.freqMap[newF] = self.DLList()
        self.freqMap[newF].addNodeToHead(node)

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.hmap:
            node = self.hmap[key]
            node.value = value
            self.update(node)                               # update freq
        else:
            if len(self.hmap) == self.capacity:
                minFreqList = self.freqMap[self.minFreq]    # remove lfu
                toRemove = minFreqList.tail.prev
                minFreqList.removeNode(toRemove)
                self.hmap.pop(toRemove.key)

            
            newNode = self.Node(key, value)                 # add new nodw
            self.minFreq = 1
            if self.minFreq not in self.freqMap:
                self.freqMap[self.minFreq] = self.DLList()
            self.freqMap[self.minFreq].addNodeToHead(newNode)
            self.hmap[key] = newNode

