class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for j in t:
            if j in hash_map and hash_map[j] > 0:
                hash_map[j] -= 1
            else:
                return False
        return True