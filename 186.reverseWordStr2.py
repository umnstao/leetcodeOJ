class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.

        """
        self.reverse(str, 0, len(str) - 1)
        self.reverseWords2(str, len(str))
        #self.cleanSpaces(str, len(str))

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

    def reverse(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1
        return str

    def reverseWords2(self, a, n):
        i, j = 0, 0
        while i < n:
            while i < n and a[i] == ' ':
                i += 1
            j = i
            while j < n and a[j] != ' ':
                j += 1
            self.reverse(a, i, j - 1)
            i = j