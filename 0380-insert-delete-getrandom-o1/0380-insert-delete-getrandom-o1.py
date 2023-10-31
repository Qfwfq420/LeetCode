class RandomizedSet(object):

    def __init__(self):
        self.set = {}
        self.data = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set[val] = len(self.data)
        self.data.append(val)
        return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.set:
            return False
        last = self.data[-1]
        remove_index =  self.set[val]
        self.set[last] = remove_index
        self.data[remove_index] = last
        self.data.pop()
        self.set.pop(val)
        return True

        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()