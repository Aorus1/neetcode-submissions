class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    
    def get(self, index: int) -> int:
        print(index, self.count, len(self.getValues()))
        if index >= self.count:
            return -1
        else:
            curr = self.head
            for i in range(0, index):
                curr = curr.next
            return curr.val

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val=val, next=self.head)
        if self.count == 0:
            self.head = self.tail = newHead
            self.count += 1
        else:
            self.head = newHead
            self.count += 1

        


    def insertTail(self, val: int) -> None:
        newTail = ListNode(val=val, next=None)
        if self.count == 0:
            self.head = self.tail = newTail
            self.count += 1
            return
        else:
            self.tail.next = newTail
            self.tail = newTail
            self.count += 1


    def remove(self, index: int) -> bool:
        if index >= self.count or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if prev.next is None:
                self.tail = prev

        self.count -= 1
        return True
     



        

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head
        for i in range(0, self.count):
            ans.append(curr.val)
            curr = curr.next
        return ans

        
