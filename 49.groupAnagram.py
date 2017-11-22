class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        """
        myHash = {}
        for word in strs:
            sw = ''.join(sorted(word))
            if sw not in myHash:
                myHash[sw] = [word]
            else:
                myHash[sw].append(word)
        return myHash.values()

        """

        myMap = {}
        strs.sort()
        for i in range(len(strs)):
            word = sorted(strs[i])
            word = ''.join(word)
            if word not in myMap:
                myMap[word] = [strs[i]]
            else:
                myMap[word].append(strs[i])
        return myMap.values()

        """
