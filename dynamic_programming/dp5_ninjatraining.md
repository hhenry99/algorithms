# 🥷 Ninja Training Problem

## **Problem Description**

- Maximize the ninja's score.
- The ninja cannot perform the same task on consecutive days.

### **Resource**

- [YouTube Explanation](https://www.youtube.com/watch?v=AE39gJYuRog)

---

## **Recursive Approach (Brute Force)**

We define a recursive function `f(day, last)` that returns the maximum points achievable when the ninja is on `day` and the last performed task was `last`.

### **Python Implementation**

```python
def ninja_training_recursive(day, last, tasks):
    if day == 0:
        # Base case: On day 0, pick the maximum valid task
        return max(tasks[0][i] for i in range(3) if i != last)

    maxi = 0
    for i in range(3):
        if i != last:
            points = tasks[day][i] + ninja_training_recursive(day - 1, i, tasks)
            maxi = max(maxi, points)

    return maxi

# Example Usage
tasks = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
n = len(tasks)
print(ninja_training_recursive(n - 1, 3, tasks))  # Output: Maximum score


TC: O(3^N)
SC: O(N)

//Draw an example recursion tree
//Notice overlapping problem
//Can use memoization


def ninja_training_memo(day, last, tasks, dp):
    if day == 0:
        return max(tasks[0][i] for i in range(3) if i != last)

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for i in range(3):
        if i != last:
            points = tasks[day][i] + ninja_training_memo(day - 1, i, tasks, dp)
            maxi = max(maxi, points)

    dp[day][last] = maxi
    return dp[day][last]

# Example Usage
n = len(tasks)
dp = [[-1] * 4 for _ in range(n)]
print(ninja_training_memo(n - 1, 3, tasks, dp))  # Output: Maximum score




//Tabulation method

def ninja_training_tabulation(tasks):
    n = len(tasks)
    dp = [[0] * 4 for _ in range(n)]

    # Base Case
    dp[0][0] = max(tasks[0][1], tasks[0][2])
    dp[0][1] = max(tasks[0][0], tasks[0][2])
    dp[0][2] = max(tasks[0][0], tasks[0][1])
    dp[0][3] = max(tasks[0])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    points = tasks[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], points)

    return dp[n - 1][3]

# Example Usage
print(ninja_training_tabulation(tasks))  # Output: Maximum score


///Space optimation



def ninja_training_space_optimized(tasks):
    n = len(tasks)
    prev = [0] * 4

    # Base Case
    prev[0] = max(tasks[0][1], tasks[0][2])
    prev[1] = max(tasks[0][0], tasks[0][2])
    prev[2] = max(tasks[0][0], tasks[0][1])
    prev[3] = max(tasks[0])

    for day in range(1, n):
        curr = [0] * 4
        for last in range(4):
            curr[last] = 0
            for task in range(3):
                if task != last:
                    points = tasks[day][task] + prev[task]
                    curr[last] = max(curr[last], points)
        prev = curr  # Move current results to previous

    return prev[3]

# Example Usage
print(ninja_training_space_optimized(tasks))  # Output: Maximum score
```
