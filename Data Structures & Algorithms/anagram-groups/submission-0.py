class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for char in strs:
            key = [0] * 26
            for c in char:
                key[ord(c)- ord("a")] += 1
            
            key = tuple(key)
                
            groups.setdefault(key, []).append(char)


        return list(groups.values())