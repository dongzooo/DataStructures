class Queue :
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self) :
        if len(self.items) == 0 or self.front_index == len(self.items) :
            print("Queue is empty")

        else :
            x = self.items[self.front_index]
            self.front_index +=1
            return x

Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
print(Q.items)
print(Q.dequeue())
print(Q.dequeue())
print(Q.items)

#S.push(10)
#S.push(2)
#print(S.pop())
#print(S.pop())
#print(len(S))
#print(S.isEmpty())
