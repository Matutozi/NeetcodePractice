class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed: Compare s1 against s2, not itself
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        # Fixed: Initialize with 0 instead of an empty list
        bucket_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            bucket_count[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if s1_count == bucket_count:
            return True
            
        # Slide the window across the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window on the right
            bucket_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove the character falling out of the window on the left
            left_char_index = i - len(s1)
            bucket_count[ord(s2[left_char_index]) - ord('a')] -= 1
            
            # If the frequency arrays match, we found a permutation
            if s1_count == bucket_count:
                return True
                
        return False