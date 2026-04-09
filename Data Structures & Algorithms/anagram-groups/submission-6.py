class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        rep = {}
        i = 0
        
        res = []
        for word in strs:

            idx = [0]*26

            for letter in word:
                idx[ord(letter)-97]+=1
            
            id = "#".join(map(str,idx))

            if id not in rep.keys():
                rep[id] = i
                res.append([])
                i += 1
            
            res[rep[id]].append(word)
        
        return(res)


