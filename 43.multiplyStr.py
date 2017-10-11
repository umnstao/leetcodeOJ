class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        pos = [0]*(m+n)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mult = (ord(num1[i]) - ord('0')) *  (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sums = mult + pos[p2]
                pos[p1] += sums / 10
                pos[p2] = sums % 10
        sb = ""
        for p in pos:
            if p == 0 and len(sb) == 0:
                continue
            else:
                sb += str(p)
        return "0" if len(sb) == 0 else sb

