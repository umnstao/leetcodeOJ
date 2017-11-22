class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        self.reverse(a, 0, len(a) - 1)
        self.reverseWords2(a, len(a))
        return self.cleanSpaces(a, len(a))

    def reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def cleanSpaces(self, a, n):
        i, j = 0, 0
        while i < n:
            while i < n and a[i] == ' ':
                i += 1
            while i < n and a[i] != ' ':
                a[j] = a[i]
                j += 1
                i += 1
            while i < n and a[i] == ' ':
                i += 1
            if i < n:
                a[j] = ' '
                j += 1
        return ''.join(a[:j])


    def reverseWords2(self, a, n):
        i, j = 0, 0
        while i < n:
            # skip space
            while i < n and a[i] == ' ':
                i += 1
            j = i
            while j < n and a[j] != ' ':
                j += 1
            self.reverse(a, i, j-1)
            i = j


