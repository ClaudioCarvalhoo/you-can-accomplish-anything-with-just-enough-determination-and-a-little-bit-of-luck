# O(n)
# n = len(pid)


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parentToChildren = {}
        for i in range(len(pid)):
            if pid[i] not in parentToChildren:
                parentToChildren[pid[i]] = []
            if ppid[i] not in parentToChildren:
                parentToChildren[ppid[i]] = []
            parentToChildren[ppid[i]].append(pid[i])

        res = [kill]
        p = 0
        while p < len(res):
            res += parentToChildren[res[p]]
            p += 1
        return res