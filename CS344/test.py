
# Assume we have a function SCORE(b) available
def SCORE(b):
    # Replace this with the actual scoring function
    return len(b)  # Example scoring function (length of substring)

def max_partition_score(s):
    n = len(s)

    @lru_cache(None)
    def dp(i):
        if i == n:
            return 0  # Base case: empty string has score 0
        
        max_score = float('-inf')
        
        # Try all partitions starting at i
        for j in range(i + 1, n + 1):
            substring = s[i:j]  # Possible split
            max_score = max(max_score, SCORE(substring) + dp(j))
        
        return max_score

    return dp(0)
