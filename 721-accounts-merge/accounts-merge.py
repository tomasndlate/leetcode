from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        parent = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] # compression
                x = parent[x]
            return x
        
        def union(x, y):
            rootX = find(x) #1
            rootY = find(y) #0
            if rootX != rootY:
                parent[rootY] = parent[rootX]

        for account in accounts:
            first_email = account[1]
            names[first_email] = account[0]
            
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)

        groupedAccounts = {}

        for email in parent.keys():
            acc = find(email)
            if acc not in groupedAccounts:
                groupedAccounts[acc] = [names[acc]]
            groupedAccounts[acc].append(email)

        return [ [acc[0]] + sorted(acc[1:]) for acc in groupedAccounts.values() ]