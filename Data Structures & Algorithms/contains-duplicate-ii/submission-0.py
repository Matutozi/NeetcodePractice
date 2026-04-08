class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()

        left =0

        for R in range(len(nums)):
            if R-left > k:
                hash_set.remove(nums[left])
                left += 1
            if nums[R] in hash_set:
                return True
            else:
                hash_set.add(nums[R])

        return False