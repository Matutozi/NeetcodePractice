class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #to return the k most frequent elemet
        dict_map = {}

        for num in nums:
            if num in dict_map:
                dict_map[num] += 1
            else:
                dict_map[num] = 1

        bucket = [[] for _ in range(len(nums)+ 1)]

        for num, freq in dict_map.items():
            bucket[freq].append(num)
        
        result = []

        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result