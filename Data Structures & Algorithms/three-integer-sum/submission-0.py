class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i -1]:
                continue

            lo, hi = i + 1, n-1

            while lo < hi:
                sumn = nums[i] + nums[lo] + nums[hi]
                if sumn == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo+=1
                    hi -=1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo+=1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi-=1
                    
                elif sumn < 0:
                    lo+=1
                else:
                    hi-=1

        return answer


            