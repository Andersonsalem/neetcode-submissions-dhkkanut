class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter

        res = []

        seen = {}

        i = 0

        for elem in strs:
            constituants = Counter(elem)
            constituants = frozenset(constituants.items())
            
            if constituants in seen.keys():
                res[seen[constituants]].append(elem)
            else:
                res.append([elem])
                seen[constituants] = i
                i += 1
        
        return res

