class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        windowLen = 0
        most_repeated = 0

        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            most_repeated = max(most_repeated, window[s[right]])

            # shrink until valid (length - most repeated <= k)
            while right - left + 1 - most_repeated > k:
                window[s[left]] -= 1
                left += 1
                # don't need most repeated update - to be longer most repeated need to be same or higher
            
            windowLen = max(windowLen, right - left + 1)

        return windowLen
            

        