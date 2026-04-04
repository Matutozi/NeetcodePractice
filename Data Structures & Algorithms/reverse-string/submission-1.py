class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        u can use the two pointer approach also
        """
        left= 0
        right = len(s) - 1

        while left < right:
            if left != right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        