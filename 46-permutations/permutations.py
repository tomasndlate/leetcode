class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [] -> [1] -> [1,2] -> [1,2,3]
        #                    -> [1,3,2]
        #                    -> [3,1,2]
        #           -> [2,1] -> [2,1,3]
        #                    -> [2,3,1]
        #                    -> [3,2,1]
        permutations = [[]]

        for n in nums:
            newPerms = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    permCopy = perm[:]
                    permCopy.insert(i, n)
                    newPerms.append(permCopy)
            permutations = newPerms
        
        return permutations