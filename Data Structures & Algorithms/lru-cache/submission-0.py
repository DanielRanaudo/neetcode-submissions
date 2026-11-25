class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dictionary = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key] 
            node.next.prev = node.prev
            node.prev.next = node.next

            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail

            
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            node = self.dictionary[key] 
            node.next.prev = node.prev
            node.prev.next = node.next

            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.val = value
            return
        #otherwise, add to the end
        if len(self.dictionary) + 1 > self.capacity:
            nodeToRem = self.head.next
            keyToRem = nodeToRem.key
            self.head.next = self.head.next.next
            nodeToRem.next.prev = self.head
            del self.dictionary[keyToRem]
        node = Node(key, value)

        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        self.dictionary[key] = node
        return
        

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)