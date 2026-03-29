class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head

        while cur and i < index:
            cur = cur.next
            i += 1

        if cur:
            return cur.val
        return -1


    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head

        if index == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return True

        while cur and i < index - 1:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        cur = self.head
        values = []

        while cur:
            values.append(cur.val)
            cur = cur.next

        return values