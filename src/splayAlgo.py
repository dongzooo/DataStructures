# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
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

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            elif v.key < key:
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
        v = None
        p = self.find_loc(key)
        if p == None:
            v = self.root= Node(key)
        elif p.key != key:
            v = Node(key)
            v.parent = p
            if p.key > key:
                p.left = v
            else:
                p.right = v
        if v != None:
            self.size = self.size + 1
        return v


class SplayTree(Tree):
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
        if z == self.root:
            self.root = x

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



    def splay(self, x):
        if x == None :
            return None
        while x != self.root:
            if x.parent == self.root :
                if x.parent.left == x:
                    self.rotateRight(x.parent)
                elif x.parent.right == x:
                    self.rotateLeft(x.parent)
            elif (x.parent.left ==x and x.parent.parent.left == x.parent):
                self.rotateRight(x.parent)
                self.rotateRight(x.parent)
            elif (x.parent.right ==x and x.parent.parent.right == x.parent):
                self.rotateLeft(x.parent)
                self.rotateLeft(x.parent)
            elif (x.parent.right ==x and x.parent.parent.left == x.parent):
                self.rotateLeft(x.parent)
                self.rotateRight(x.parent)
            elif (x.parent.left ==x and x.parent.parent.right == x.parent):
                self.rotateRight(x.parent)
                self.rotateLeft(x.parent)
        return x

    def search(self, key):
        v = super(SplayTree,self).search(key)
        if v :
            self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        self.root = self.splay(v)
        return v

    def delete(self, x):
        self.splay(x)
        L ,R = x.left, x.right
        if L != None:
            m=L
            while m.right:
                m = m.right
            self.splay(m)
            m.right , R.parent = R, m
        else :
            R.parent , self.root = None, R



    def preorder(self, v):
        super(SplayTree, self).preorder(v)

    def postorder(self, v):
        super(SplayTree, self).postorder(v)

    def inorder(self, v):
        super(SplayTree, self).inorder(v)

T = SplayTree()

while True:
    cmd = input().split()
    if cmd[0] == 'in':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'del':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'find':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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
