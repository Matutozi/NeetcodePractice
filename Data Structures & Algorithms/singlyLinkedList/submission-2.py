class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val       

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size+= 1

    def insertTail(self, val: int) -> None:
        #create new node
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        #to remove node at an index
        if index < 0 or index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next

        else:
            current = self.head

            for _ in range(index -1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
                
        return True
            

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current:
            values.append(current.val)
            current = current.next
        return values
        
        
