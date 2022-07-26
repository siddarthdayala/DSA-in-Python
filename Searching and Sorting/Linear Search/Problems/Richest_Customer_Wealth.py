# Leetcode link: https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            add = 0
            for j in range(len(accounts[i])):
                add+=accounts[i][j]
            if add>wealth:
                wealth = add
            
        return wealth
