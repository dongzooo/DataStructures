class Stack :
    def __init__(self) :
        self.item= []

    def push(self, val) :
        self.item.append(val)

    def pop(self) :
        try :
            return self.item.pop()
        except IndexError():
            print("Stack is empty")

    def __len__(self) :
        return len(self.item)

    def isEmpty(self):
        return self.__len__() == 0

S = Stack()
#S.push(10)
#S.push(2)
#print(S.pop())
#print(S.pop())
#print(len(S))
#print(S.isEmpty())
