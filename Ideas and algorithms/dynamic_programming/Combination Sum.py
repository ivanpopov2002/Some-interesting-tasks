'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Test case: 
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
'''

candidates = list(map(int, input().split()))
target = int(input())

dp = [[] for i in range(target + 1)]
for c in candidates:
    comb = [c]
    for i in range(target + 1):
        if sum(comb) > i:
            continue
        elif sum(comb) == i:
            dp[i].append(comb.copy())
        else:
            current = i - sum(comb)
            if dp[current] != []:
                for lst in dp[current]:
                    cur = comb + lst
                    dp[i].append(cur.copy())
print(dp[target])
