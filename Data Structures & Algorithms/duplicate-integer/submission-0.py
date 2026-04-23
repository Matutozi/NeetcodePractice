class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_m = []
        for i in nums:
            if i in hash_m:
                return True
            else:
                hash_m.append(i)
        return False        