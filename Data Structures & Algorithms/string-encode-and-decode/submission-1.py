class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for word in strs:
            l = str(len(word))
            x = x + l + "#" + word + "#"
        return x



    def decode(self, s: str) -> List[str]:
        i = 0
        num = ""
        digits = "0123456789"
        res = []
        word = ""
        while i < len(s):
            curr = s[i]

            if curr in digits:
                num += curr
                i += 1
            
            if curr == "#":
                num = int(num) if len(num) > 0 else 0
                i += 1
                word = s[i:i+num]
                res.append(word)
                i += num+1
                num = ""
        
        return res

