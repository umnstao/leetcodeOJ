class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        seq = [""]*n
        seq[0] = '1'
        seq[1] = '11'
        for i in range(2,n):
            count = 1
            p = seq[i-1][0]
            for c in seq[i-1][1:]:
                if c == p:
                    count += 1
                else:
                    seq[i] += str(count)
                    seq[i] += p
                    p = c
                    count = 1
            seq[i] += str(count)
            seq[i] += c
        return seq[n-1]

