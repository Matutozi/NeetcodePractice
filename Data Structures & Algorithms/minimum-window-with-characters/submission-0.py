class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        window = {}

        # Build frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")

        l = 0

        # Expand window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Check if current character requirement is satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # Shrink window while valid
            while have == need:

                # Update result if smaller window found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # Remove left character
                window[s[l]] -= 1

                # Check if validity breaks
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move left pointer
                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("infinity") else ""