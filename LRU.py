class Node:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRU:
    def __init__(self, mx_len):
        self.mx_len = mx_len
        self.dummy = Node()
        self.length = 0
        self.last = None
    
    def insert(self, val):
        head = self.dummy.nxt
        while head:
            if head.val == val:
                break
            head = head.nxt
        if head:
            # remove head
            # then re-insert head at top of cache
            head.prev.nxt = head.nxt
            self.length -= 1
        self.add_to_top(val)
    
    def add_to_top(self, val):
        self.dummy.nxt = Node(val, self.dummy.nxt, self.dummy)
        if self.dummy.nxt.nxt:
            self.dummy.nxt.nxt.prev = self.dummy.nxt
        self.length += 1

        if self.last is None:
            self.last = self.dummy.nxt
        
        if self.length > self.mx_len:
            # delete last node
            self.last = self.last.prev
            self.last.nxt = None
            self.length -= 1
        
        

    def __repr__(self):
        rep = []
        head = self.dummy.nxt
        while head:
            rep.append(str(head.val))
            head = head.nxt
        return "->".join(rep)


lru = LRU(3)
lru.insert(1)
print(lru)
lru.insert(2)
print(lru)
lru.insert(3)
print(lru)
lru.insert(4)
print(lru)
lru.insert(3)
print(lru)


