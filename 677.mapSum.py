class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dict[key] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sums = 0
        for key in self.dict.keys():
            if self.check(prefix, key):
                sums += self.dict[key]
        return sums

    def check(self, prefix, key):
        if len(key) < len(prefix):
            return False
        for i in range(len(prefix)):
            if prefix[i] != key[i]:
                return False
        return True



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)