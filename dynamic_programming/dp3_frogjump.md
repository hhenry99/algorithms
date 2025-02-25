# Frog Jump

[Video Explanation](https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4)

## Problem Description:

The goal is to find the minimum energy required for a frog to jump from the first stone to the last stone, given that the frog can either jump to the next stone or skip one stone.

### Key Observations:

- A greedy approach does not work in all cases.
- Recursion tries all possible ways and finds the minimum energy required.

## Recursive Approach:

1. Define the problem recursively:
   - `f(index)`: Minimum energy required to reach `index` from `0`.
   - The frog can jump from `index-1` or `index-2`.

```python
def frog_jump_recursive(index, heights):
    if index == 0:
        return 0

    left = frog_jump_recursive(index - 1, heights) + abs(heights[index] - heights[index - 1])

    right = float('inf')
    if index > 1:
        right = frog_jump_recursive(index - 2, heights) + abs(heights[index] - heights[index - 2])

    return min(left, right)

```

### Memoization(Top-Down DP)

- Store the computed results to avoid redundant calculations

```python
def frog_jump_memoization(index, heights, dp):
    if index == 0:
        return 0

    if dp[index] != -1:
        return dp[index]

    left = frog_jump_memoization(index - 1, heights, dp) + abs(heights[index] - heights[index - 1])

    right = float('inf')
    if index > 1:
        right = frog_jump_memoization(index - 2, heights, dp) + abs(heights[index] - heights[index - 2])

    dp[index] = min(left, right)
    return dp[index]

# Wrapper function
def frog_jump(n, heights):
    dp = [-1] * n
    return frog_jump_memoization(n - 1, heights, dp)
```

Time and Space Complexity

TC: O(N)
SC: O(N) for recursion stack + O(N) for dp array

---

### Tabulation (Bottom-Up DP)

```python
def frog_jump_tabulation(n, heights):
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        left = dp[i - 1] + abs(heights[i] - heights[i - 1])
        right = dp[i - 2] + abs(heights[i] - heights[i - 2]) if
```

TC: O(N)
SC: O(N)

### Space Optimization (O(1) Space Complexity)

```python
def frog_jump_optimized(n, heights):
    prev = 0
    prev2 = 0

    for i in range(1, n):
        left = prev + abs(heights[i] - heights[i - 1])
        right = prev2 + abs(heights[i] - heights[i - 2]) if i > 1 else float('inf')
        curr = min(left, right)
        prev2 = prev
        prev = curr

    return prev
```
