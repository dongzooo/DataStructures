class Node:
    def __init__(self,key= None, value = None):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self) :
        return str(self.key)


class SinglyLinkedList :
    def __init__(self) :
        self.head = None
        self.size = 0

    def __iter__(self) :
        v = self.head
        while v != None :
            yield  v
            v= v.next

    def __str__(self) :
        return print("->".join(str(v) for v in self))
    def __len__(self):		# len(L): 리스트 L의 size 리턴
        return self.size

    def printList(self): # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key, value = None) :
        new_node = Node(key,value)
        new_node.next = self. head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:  # empty list --> new_node becomes a head!
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:	# follow links until tail
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        key = value = None
        if len(self) > 0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        return key, value

    def popBack(self):
        if self.size == 0: 	# empty list (nothing to pop)
            return None, None
        else:
            # tail 노드와 그 전 노드인 previous를 찾는다
            previous, current = None, self.head
            while current.next != None:
                previous, current = current, current.next 	# 한 노드씩 진행
            # 만약 리스트에 노드가 하나라면 그 노드가 head이면서 동시에 tail임
            # 그런 경우라면 tail을 지우면 빈 리스트가 되어 head = None으로 수정해야함!
            tail = current
            key, value = tail.key, tail.value
            if self.head == tail:	# 또는 if previous == None:
                self.head = None
            else:
                previous.next = tail.next	# previous가 새로운 tail이 됨!
            self.size -= 1
            return key

    def search(self, key):
        v = self.head
        while v:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(self, x) :
        if self.head == None :
            return None
        prev, v  = None, self.head
        if x == self.head :
            self.popFront
        else:
            while v.next != None :
                if x == v:
                    prev.next = v.next
                    del v
            prev = v
            v = v.next
    def size(self):
        return self.size






L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")
