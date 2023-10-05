print("第4题")

class Node():                
    def __init__ (self, value = None, next = None):
        self._value = value
        self._next = next
 
    def getValue(self):
        return self._value
 
    def getNext(self):
        return self._next
 
    def setValue(self,new_value):
        self._value = new_value
 
    def setNext(self,new_next):
        self._next = new_next
 

class LinkedList():
    def __init__(self):     
        self._head = None
        self._tail = None
        self._length = 0
 
    def isEmpty(self):
        return self._head == None  
    
    def append(self,value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode   #若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()   #遍历链表
            current.setNext(newnode)   #此时current为链表最后的元素
            
    def remove(self,value):
        current = self._head
        pre = None
        while current!=None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())                
            else:
                pre = current
            current = current.getNext()
 
    #索引元素在链表中的位置
    def index(self,value):
        current = self._head
        count = 0
        found = None
        index=[]
        while current != None:
            count += 1
            if current.getValue()==value:
                found = True
                index.append(count)
            current=current.getNext()
                
        if found:
            return index
        else:
            return -1
    
    #遍历
    def walkthrough(self):
        cur = self._head
        while cur is not None:
            print(cur._value,end=" ")
            cur = cur._next
 
linklist=LinkedList()
linklist.append(1)
linklist.append(2)
linklist.append(3)
linklist.append(4)
linklist.append(3)
print("原链表:",end="")
linklist.walkthrough()
print("")

print("查找元素3的位置:",end="")
print(linklist.index(3))

linklist.remove(3)
print("删除元素3后的链表:",end="")
linklist.walkthrough()
 
    
