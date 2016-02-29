class dqNode:  
    def __init__(self, key, val):  
        self.val = val  
        self.key = key  
        self.pre = None  
        self.next = None  
  
class LRUCache:  
  
    # @param capacity, an integer  
    def __init__( self, capacity ):  
        self.capacity = capacity  
        self.curSize = 0      
        self.keys2valNode = { }   # mapping key to the node that has the value info  
        # dqlist to store <key, value> pairs  
        self.head = dqNode(-1, -1)  
        self.tail = dqNode(-1, -1)  
        self.head.next = self.tail  
        self.tail.pre = self.head  
          
    # util functions      
    def moveToFirst( self, pnode ):  
        # link pnode.pre and pnode.next  
        if pnode.pre:  
            pnode.pre.next = pnode.next  
        if pnode.next:  
            pnode.next.pre = pnode.pre  
        # move pnode to first  
        pnode.next = self.head.next  
        if self.head.next:  
            self.head.next.pre = pnode  
        self.head.next = pnode  
        pnode.pre = self.head  
          
    def removeLRU( self ):  
        pdel = self.tail.pre  
        pdel.pre.next = self.tail  
        self.tail.pre = pdel.pre  
        del self.keys2valNode[ pdel.key ]  
        del pdel  
  
    def Insert( self, key, value ):  
        newNode = dqNode(key, value)  
        # add to dict  
        self.keys2valNode[ key ] = newNode  
        # insert to first of dqueue  
        self.moveToFirst(newNode)  
    # @return an integer  
    def get(self, key):  
        if self.keys2valNode.has_key(key):  
            # get the node that has value info.  
            pvalue = self.keys2valNode[ key ]  
            value =  pvalue.val  
            # change pvalue to be recently visited one  
            self.moveToFirst( pvalue )  
            return value  
        else:   
            return -1  
          
    # @param key, an integer  
    # @param value, an integer  
    # @return nothing  
    def set( self, key, value ):  
        # if has key, just have to change the value  
        if self.keys2valNode.has_key( key ):  
            self.keys2valNode[ key ].val = value  
            self.moveToFirst( self.keys2valNode[ key ] )  
        # insert a new key  
        # 1) curSize < capacity, just insert  
        # 2) curSize == capacity, remove LRU and insert  
        else:  
            self.Insert(key, value)  
            if self.curSize < self.capacity:  
                self.curSize += 1  
            else:  
                self.removeLRU()  
      