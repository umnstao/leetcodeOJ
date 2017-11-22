class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        children = {}
        for i in range(len(pid)):
            if ppid[i] in children:
                children[ppid[i]].append(pid[i])
            else:
                children[ppid[i]] = [pid[i]]

        res = []
        queue = [kill]
        while len(queue) > 0:
            n = queue.pop()
            res.append(n)
            if n in children:
                for x in children[n]:
                    queue.append(x)
        return res
