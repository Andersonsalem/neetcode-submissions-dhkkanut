class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elems = defaultdict(int)

        for i in s:
            elems[i] += 1
        for i in t:
            elems[i] -= 1

        return len(set(elems.values())) == 1
