class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permMap = {}
        for s in s1:
            permMap[s] = permMap.get(s, 0) + 1
        
        window = {}
        have, need = 0, len(permMap)

        left = 0
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if s2[right] in permMap and window[s2[right]] == permMap[s2[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 == len(s1):
                    return True

                # shrink
                window[s2[left]] -= 1
                if s2[left] in permMap and window[s2[left]] < permMap[s2[left]]:
                    have -= 1
                left += 1
            
        return False

        
