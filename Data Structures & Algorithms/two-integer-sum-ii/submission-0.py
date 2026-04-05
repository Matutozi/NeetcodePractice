class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right= len(numbers) -1

        while left < right:
            tar_sum = numbers[left] + numbers[right]
            if tar_sum == target:
                return [left+1, right+1]
            
            elif tar_sum < target:
                left+= 1
            elif tar_sum > target:
                right -= 1
