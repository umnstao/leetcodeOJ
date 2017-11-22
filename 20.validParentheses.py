class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack = []
        for x in s:
            if x in "({[":
                myStack.append(x)
            if x == ')':
                if len(myStack) == 0:
                    return False
                if myStack[-1] == '(':
                    myStack.pop()
                else:
                    return False
            elif x == ']':
                if len(myStack) == 0:
                    return False
                if myStack[-1] == '[':
                    myStack.pop()
                else:
                    return False
            elif x == '}':
                if len(myStack) == 0:
                    return False
                if myStack[-1] == '{':
                    myStack.pop()
                else:
                    return False
        return len(myStack) == 0