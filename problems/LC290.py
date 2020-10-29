# O(n)
# n = len(s)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = []

        tmp = ""
        for i in s:
            if i == " " and len(tmp) > 0:
                words.append(tmp)
                tmp = ""
            else:
                tmp += i
        if len(tmp) > 0:
            words.append(tmp)

        if len(words) != len(pattern):
            return False

        table = {}
        used = {}
        for i in range(len(pattern)):
            if not pattern[i] in table:
                if not words[i] in used:
                    table[pattern[i]] = words[i]
                    used[words[i]] = True
                else:
                    return False
            elif table[pattern[i]] != words[i]:
                return False

        return True
