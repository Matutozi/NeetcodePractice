class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_f= 0
        result = 0
        f_map = {}

        for r in range(len(s)):
            f_map[s[r]] = f_map.get(s[r], 0) + 1

            max_f = max(f_map[s[r]], max_f)

            while (r-left+1) - max_f > k:
                f_map[s[left]] -= 1
                left += 1
            result = max(result, r -left+1)

        return result
