class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            new_perm = []
            for subset in permutations:
                for i in range(len(subset) + 1):
                    subset_copy = subset.copy()
                    subset_copy.insert(i, n)
                    new_perm.append(subset_copy)
            permutations = new_perm
        
        return permutations
        