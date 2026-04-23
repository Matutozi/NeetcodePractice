class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = 0
        hash_map = {}

        for n in range(len(nums)):
            remainder = target - nums[n]
            if remainder in hash_map:
                return [hash_map[remainder], n]
            else:
                hash_map[nums[n]] = n

        return []