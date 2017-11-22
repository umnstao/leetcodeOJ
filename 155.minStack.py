class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myStack = []
        self.minStack = []



    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.myStack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if self.minStack[-1] > x:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])
        print 'a',self.myStack
        print 'b',self.minStack


    def pop(self):
        """
        :rtype: nothing
        """
        self.myStack.pop()
        self.minStack.pop()
        print 'a',self.myStack
        print 'b',self.minStack

    def top(self):
        """
        :rtype: int
        """
        return self.myStack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
