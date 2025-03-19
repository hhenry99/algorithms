Problem Statement
![alt text](image.png)

Pseudocode
![alt text](image-1.png)

TC : 2^(m\*n)
SC : (m-1) + (n-1)

Recursion -> DP
-Memoization
-Apply when overlapping subproblems

With memo implementation
![alt text](image-2.png)

TC : O(m*n)
SC : O((n-1) + (m-1)) + O(n*m)

---

Tabulation
![alt text](image-3.png)

TC : O(n _ m)
SC : O(n _ m)

--

Space Optimization

- If there is a previous row & previous column, we can space optimize

Space optimize; 1D
