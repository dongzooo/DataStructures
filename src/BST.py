class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')



    def find_loc(self, key): # if key is in T,
        if self.size == 0:
            return None
        p = None    # p = parent node of v
        v = self.root
        while v:    # while v != None
            if v.key == key: return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key: # p is parent of v
                if p.key < key: p.right = v
                else: p.left = v
                v.parent = p
        self.size += 1
        return v


    def deleteByMerging(self, x):
   # assume that x is not None
        a, b, pt = x.left, x.right, x.parent
        if a == None: c = b
        else: # a != None
            c = m = a
   # find the largest leaf m in the subtree of a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m

        if self.root == x: # c becomes a new root
            if c: c.parent = None
            self.root = c
        else:      # c becomes a child of pt of x
            if pt.left == x: pt.left = c
            else: pt.right = c
            if c: c.parent = pt
        self.size -= 1

    def deleteByCopying(self, x):
        if x == None:
            return
        a,b,pt = x.left, x.right, x.parent

        #case 1 : delete Node is terminal node
        if (a == None) and (b == None):
            if x == self.root:
                self.root = None
            elif pt.right == x:
                pt.right = None
                x= None
            elif pt.left == x:
                pt.left = None
                x = None

        elif a == None:
            if x == self.root:
                self.root = b
            elif b.left:
                m=b
                while m.left:
                    m=m.left
                x.key = m.key
                m.parent.left = m.right
            else:
                pt.right = b # or pt.right = x.right
                b.parent = pt # or b.parent = x.parent



        elif a == None:
            print("0_0")
            if x == self.root:
                self.root = b
                  #m = b
            #while m.left:
            #    m = m.left
            #x.key = m.key
            #if m==b:
            #    x.right = None
            #else:
            #    m.parent.left = m.right
            #    if m.right:
            #        m.right.parent = m.parent
            else:
                pt.right = b # or pt.right = x.right
                b.parent = pt # or b.parent = x.parent



        else:

            m = a
            if m.right:
                while m.right : m = m.right
                m.parent.right=m.left
            else :
                m.parent.left = m.left
            #if x==self.root :
            #    print("x is root!")
            #else : print(" x is not root!")
            x.key = m.key
            t=self.root
            #print("Now root is ", t)
            #print("now root.left is ",t.left,"and right is ", t.right)
        #print(x)
        self.size=-1zzz




    def height(self, x):
        if x == None: return -1
        else :
            l = self.height(x.left)
            r = self.height(x.right)
            v_height = 0
            if (l>r):
                return l+1
            return r+1


    def number(self, x):
        if x == None:
            return 0
        if x != None:
            n=1
            a=self.number(x.left)
            b=self.number(x.right)
            return n+a+b


    def rotateRight(self, z):    # rotateLeft도 유사하게 정의
        if z==None:
            return
        x = z.left                # assume that z != None
        if x == None: return     # if x == None: nothing changed
        b = x.right              # b == None 인 경우도 가능
        x.parent = z.parent
        if z.parent != None:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.right = z
        z.parent = x
        z.left = b
        if b: b.parent = z
       # z == self.root라면 x가 새로운 루트가 되어야 함!
        if z == self.root:
            self.root = x #이거를 z가 아니라 x로 해야함
       # [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요

    def rotateLeft(self, z):    # rotateLeft도 유사하게 정의
        if z==None :
            return
        x = z.right                # assume that z != None
        if x == None: return     # if x == None: nothing changed
        b = x.left              # b == None 인 경우도 가능
        x.parent = z.parent
        if z.parent:
            if z.parent.right == z:
                z.parent.right = x
            else:
                z.parent.left = x
        x.left = z
        z.parent = x
        z.right = b
        if b: b.parent = z
       # z == self.root라면 x가 새로운 루트가 되어야 함!
        if z == self.root:
            self.root = x


T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'number':
        num = T.number(T.search(int(cmd[1])))
        if num == 0:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has {1} descendants".format(cmd[1], num))
    elif cmd[0] == 'Rleft':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(z)
            print(" * Rotated left at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
    elif cmd[0] == 'Rright':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(z)
            print(" * Rotated right at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
