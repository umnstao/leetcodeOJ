class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                stack.append(-stack.pop() + stack.pop())
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(float(n2)/ n1))
            else:
                stack.append(int(tokens[i]))
            #print stack
        return stack.pop()