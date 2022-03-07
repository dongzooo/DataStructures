    def remove(self, key):
        i = self.find_slot(key)
        if i==None or self.keys[i] == None :
            return None
        j = i
        while True :
            self.keys[i] = None
            while True :
                j=(j+1)%self.size
                if self.keys[j] == None:
                    return key
                k = self.hash_function(self.keys[j])
                if not (i<k<=j or j<i<k or k<=j<i):
                    break
                self.keys[i] = self.keys[j]
                i=j

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:
            key_value = self.keys[i]
            self.keys[i]= None
            return key_value
        else :
            return None
