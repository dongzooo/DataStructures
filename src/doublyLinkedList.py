class Node:
    def __init__(self, key=None):
        self.key = key  # 노드에 저장되는 key값
        self.next = self.prev = self  # 자기로 향하는 링크

    def __str__(self):  # print(node)인 경우 출력할 문자열
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # 빈 리스트는 dummy 노드만으로 표현
        self.size = 0

    def printList(self): # 변경없이 사용할 것!
        v = self.head
        v.key = 'h'
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
            if v.key == 'h':
                return print('h')
        print("None")

    def first(self):
        if self.head != None:
            return True
        else:
            return None

    def last(self):
        v = self.head
        if self.head != None:
            return v.prev
        else :
            return None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False



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
        self.size += 1
        self.insertAfter(self.head,key)
    def pushBack(self,key):
        self.size += 1
        self.insertBefore(self.head,key)
    def deleteNode(self, x):
        if x == None or x == self.head:
            return
		# 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key



L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
