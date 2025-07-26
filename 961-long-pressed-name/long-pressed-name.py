class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_i = 0
        typed_i = 0

        while name_i < len(name) and typed_i < len(typed):
            
            nameCount = 1
            while name_i + 1 < len(name) and name[name_i] == name[name_i + 1]:
                nameCount += 1
                name_i += 1

            typedCount = 1
            while typed_i + 1 < len(typed) and typed[typed_i] == typed[typed_i + 1]:
                typedCount += 1
                typed_i += 1
            
            if name[name_i] != typed[typed_i] or nameCount > typedCount:
                return False
            
            name_i += 1
            typed_i += 1
        
        return name_i == len(name) and typed_i == len(typed)
