class Node:
    def __init__(self, key=None):
        self.key = key  # 노드에 저장되는 key값
        self.next = self.prev = self  # 자기로 향하는 링크

    def __str__(self):  # print(node)인 경우 출력할 문자열
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # 빈 리스트는 dummy 노드만으로 표현

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        ap = a.prev  # ap is previous node of a
        bn = b.next  # bn is next node of b

        # cut [a..b]
        ap.next = bn
        bn.prev = ap

        xn = x.next

        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    def __str__(self):
        n = self.head.next
        print(n.key)
        while (n != self.head):
            n = n.next
            print(n.key)

        #return self.head.key

    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return v


    def moveAfter(self, a,x):
        self.splice(a,a,x)
    def moveBefore(self,a,x):
        self.splice(a,a,x.prev)
    def insertAfter(self,x,key):
        self.moveAfter(Node(key),x)
    def insertBefore(self,x,key):
        self.moveBefore(Node(key),x)
    def pushFront(self,key):
        self.insertAfter(self.head,key)
    def pushBack(self,key):
        self.insertBefore(self.head,key)
    def remove(self,x):
        if x == None: return
        x.prev.next, x.next.prev = x.next, x.prev


def josephus(n,k):
    L = DoublyLinkedList()
    for i in range(1,n+1):
        L.pushBack(i)
    count = n
    num = k
    for i in L :
        if i.key == None :
            continue
        if count == 1:
            return i.key
        num-= 1
        if num == 0 :
            #print(L.__str__())
            L.remove(L.search(i.key))
            #L.remove(i)
            num = k
            count-= 1







a, b = input().split()
a = int(a)
b = int(b)
result = josephus(a,b)
print(result)
