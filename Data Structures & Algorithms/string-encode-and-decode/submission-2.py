class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result+= str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        i=0
        res = []

        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])

            res.append(s[j+1:j+length+1])

            i = j+1+length
        
        return res
