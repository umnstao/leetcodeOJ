class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlist = str.split(" ")
        if len(pattern) != len(strlist):
            return False
        myMap = {}
        for i in range(len(pattern)):
            if pattern[i] not in myMap:
                if strlist[i] in myMap.values():
                    return False
                myMap[pattern[i]] = strlist[i]
            else:
                if myMap[pattern[i]] != strlist[i]:
                    return False

        return True
