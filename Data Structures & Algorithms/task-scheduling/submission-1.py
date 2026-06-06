class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        dict_ = Counter(tasks)

        max_freq =  max(dict_.values())

        

        max_counter = sum(1 for f in dict_.values() if f == max_freq)

        completion = (max_freq-1) * (n+1) + max_counter

        return max(len(tasks), completion)