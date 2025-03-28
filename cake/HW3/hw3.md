## Problem 1

- I affirm that I have not given or received any unauthorized help
  on this assignment, and that this work is my own.

## Problem 2

- Problem: Given a set of boxes, output an order in which to stack the boxes such that no box gets crushed, or outputs that no such order exists.

- Intuition: Greedy does not approach because the values are not not uniform.
- Approach: Recursion with memoization

  - Try all different possible way
  - If there is a success, return true

- Base Case:
  1. The current_box_weight > previous_box_max_weight: return False #The current box crushes the previous stacked box
  2. The base_box_weight is execeeded: return False #All boxes are crushed because the maximum weight is exceeded
  3. Able to stack all boxes: return True

```py

# boxes is a list of tuples: (weight of box, max weight the box can tolerate on top)

def can_stack(prev_box, base_weight, visited, boxes, memo):
    if base_weight < 0:
        return False  # Base box is overloaded

    if len(visited) == len(boxes):
        return True  # All boxes stacked successfully

    if(visited in memo):    #Assume that this will work
        return False

    for box in boxes:
        if box not in visited:
            curr_weight, curr_limit = box

            # Base case 1: current box would crush the previous box
            if prev_box:
                prev_weight, prev_limit = prev_box
                if curr_weight > prev_limit:
                    continue  # Try next box

            visited.add(box)
            if can_stack(box, base_weight - curr_weight, visited, boxes):
                return True
            visited.remove(box)  # Backtrack

    memo[visited] = False
    return False

def main(boxes):
    memo = {}

    for box in boxes:  # Try every box as the base box
        weight, limit = box
        visited = set()
        visited.add(box)
        if can_stack(prev_box=box, base_weight=limit, visited=visited, boxes=boxes):
            return True  # Found a valid stacking order

    return False  # No valid stacking order exists

```

#### Run time Analysis: O(n!) //Trying all different combinations of n boxes. Optimize with memoization to make it polynomial O(n^3) The loop in the main function n \* the nested loop within the stacked function n^2.

### Proof of correctness

- Proof By Induction

Base Case:

1. If all boses are used return true.
2. If the accumulated weights of the stack box, exceeds the base weight capacity return false.
3. If the current box weight exceeds the previous box weight capacity return false.

All Base cases held and is true.

Inductive Hypothesis:

- Assume that for any k boxes, the algorithm correctly determines whether those k boxes can be stacked

Inductive Step:

- Prove that k+1 boxes, the algorithm correctly determines it can be stacked.
- The algorithm will first iterate through through each box marking it as the base of the stack. Calling the recursion function stacked().
  - This stacked() function will then continue to try out all possible combinations, stacking the box at each iteration and checks the base case.
  - Once all the boxes are stacked, return True ... the answer has been found, else continue recursing and uses one less boxes each time.
- Since this recursion uses fewer boxes the inductive hypothesis holds true, therefore the algorithm will correctly determine whether k+1 boxes can be stacked.

## Problem 3

- Problem Statement: Give a polynomial time algorithm for finding the sest of meetings with the highest total important scores.

- Intuition:

  - Greedy would not work because the values are not uniformed. E.g. if I was to choose only the meetings with the highest possible score, this would not work because this approach would not always give us the highest total score.
  - Approach: Recursion with memoization.

    1. First sort the meeting times based on start and end time, for easier computation later on. (n log n)
       - We want to sort it like this (9am, 10am), (9:30am, 10pm)
    2. At each meeting we have 2 options
       - Take: Take the meeting and add the value of the current meeting
       - Not take: Do not take the meeting
       - Return the maximum of both choices
    3. Use memoize to avoid recomputation
    4. Base Case: if there are no more meeting return 0.

- ## Approach: Recursion

```py

    def helper(i, meetings, arr, result, memo):
        if(i >= len(meetings)): return 0

        if((i, arr[-1]) in memo): #Memo storing the current meeting and the previous meeting
            return memo[(i, arr[-1])]

        current_meeting = meetings[i]

        curr_score = calculate_score(current_meeting) #Assume this this function is O(1) and calcuates the score of a meeting

        #Option 1: Take the meeting if its not overlapping with the last one
        op1 = 0
        if(arr not empty or current_meeting.startTime >= arr[-1].endTime){
            arr.append(curr)
            op1 = helper(i+1, meetings, arr, result) + curr.importance
            arr.pop() #Backtrack
        }

        #Option 2: Not take or skip the current meeting
        op2 = (helper(i+1, meetings, arr, result))

        if(op1 > op2):
            result.append(meetings[i])

        memo[i, arr[-1]] = max(op1, op2)
        return memo[i]

    def algo(meetings):
        meetings.sort() #Sort meetings in increasing order O(nlogn)
        memo = {}
        arr = [] # Temporary array
        result = [] #Store the meetings with the maximum result

        helper(i, meetings, arr, result, memo)

        return result
```

### RunTime Analysis: O(n^2) //Time is calculate from filling the memo table\*

### Proof of Correctness

- Proof by Induction
- Base Case: i >= meetings.length

  - There are no more meetings to consider
  - The function returns 0, which is correct because no meetings remain, therefore there is no score.
  - Base case holds

- Inductive Hypothesis:

  - Assume that for any subset of k remaining meetings (from i to n), the algorithm computes the max score by selecting non-overlapping subset of meetings.

- Inductive Step:
  - Proof that the algorithm works for k+1 meeting
  - The algorithm sorts the meetings in increasing order based on the start, end times.
  - The algortihm contains a helper function which recursively decides whether to take the meeting or skip the meeting with respect to the base cases.
  - Both cases the recursive calls are made on smaller subproblem with fewer than k+1 meetings.
  - By Inductive Hypothesis, the reduced meetings will be correct
  - The algorithm selects the maximum of the two choice, thus for k+1 meetings, the algo algorithm works for k+1 meeting.

## Problem 4

- Problem Statement: Give a polynomial time algorithm for deciding which flavor to swap from the front to the back when needed that minimizes the number of times you have to run to the back fridge.

- Approach: Greedy

  - Swap function: Search and swap the furthest occurence flavor or the flavor that is never used again. O(n)
  - Iterate and store all of the occurences of flavor into a dictionary O(n)
    - "Chocolate: [0,3,5,7]" Chocolate is ordered at timeslot 0, 3, 5, 7

- This is how the swap will work:
  - We have 2 flavors on display--Chocolate & Vanilla, & here are their associated mapping
    - Chocolate: [3,5,6]
    - Vanilla: [4,7]
    - The swapping of the flavor will be vanilla because it is the next furthest occurrence.
    - If one of the k flavor is empty, it will be swapped automatically.
    - O(k) to search through the displayed flavors

```py
def algo(time, k):
    dic = map_flavor(time) #Assume this function maps the occurence of flavors

    display = []
    step = 0

    for i in range(n): #Have up to K flavors to display
        if time[i] not in display:
            display.append(time[i])
            step += 1

        if step == k:
            break

    step = 0
    for i in range n, start=k: #start at k and iterate to n:
        flavor = time[i]
        dic[flavor].pop(0)  # remove the current occurrence O(1)

        if flavor not in display:
            swap(display) #assumes the swap function will swap out the further occurence flavor, and removing it from the dictionary
            step+=1

    return step
```

- Time complexity: O(n x k) #Nested loop

### Proof of correctness

- Exchange Argument

  - We want to prove that our greedy algorithm will result in the minimum number of swap / steps.

  - Let G be the solution produce by the greedy algorithm
  - Let O be the solution produce by any other algorithm that is not greedy
  - Want to show that O can't be better than G

  - Say G and O agree on the first i steps and i' is the step they differ.

  - G swaps flavor f & O swaps flavor f'

  - The number of swaps will not increase because f is needed later than f'
  - We can say that the other algorithm will only get better swapping each values with G
  - Thus this algorthim is optimal.

## Problem 5

### A.

- Problem: Give an O(n) time algorithm for constructing the rest of the pairing
- Given: Some vertex r1 from T1 could be paired to vertex r2 from T2

- Approach: BFS

  - Implementation with queue
  - Base Case: If the r1 and r2 color does not match, return false

- Algorithm:

```py
def aglo(T1, T2, r1, r2):
    stack_t1 = []
    stack_t2 = []

    queue = [r1, r2]

    while(queue):
        node_r1, node_r2 = queue.pop(0)

        #Base Case; the color don't match
        if node_r1 != node_r2:
            return False

        neighbors_r1 = nei(node_r1) #Assume the function nei return a list of all the neighbors of node_r1
        neighbors_r2 = nei(node_r2)

        #This nested loop will iterate through all the nodes of r1 and compares it with r2, if it does not found a match, return a False becasue the tree is not the same.

        for i in neighbors_r1:
            found = False
            for j in neighbors_r2:
                if i == j:
                    queue.append((i,j)) #Adds the item to the queue
                    found = True
                    break

            if found == False:
                return False

    return True
```

#### Time Analysis: O(n^3)

- nei(): O(n)
- nested loop : O(n^2)
- while loop : O(n)

#### Proof of Correctness

The algorithm works because its a BFS, just keep expanding the nodes, checking the base case each time.

### B.

- Problem Statement: Find two vertics that are far apart as possible.

- Approach DFS

```pseudo

    #The usual DFS
    def dfs(node, diameter):
        if node is null: return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left+right) # At this step can store the nodes if it is greater than the diameter
        return max(left,right) + 1

    def algo(root);
        diameter = 0
        return dfs(root, diameter)
```

#### Time Complexity Analysis: O(n)

- DFS: O(n) //the height of the tree, at the worst case the height would be n

#### Proof of correctness

### C.

- Proof by contradiction

- P = the midpoint of the path between the two node is the same.
- Assume ~P is true = the midpoint of the path between the two node is not the same.

- There is contradiction because if the midpoint is not the same, the diameter between the node is not equal because it can be less than or greater than with a different midpoint.

## Problem 6

### A. Give an algorithm assuming that G is strongly connected

- **Strongly Connected Graph**: A Graph that is connected such that starting at each vertex you can get to another node. There must be a cycle.

- Approach: USE DFS or BFS traversal
- Since all nodes are reachable by definition, we just do a simple DFS or BFS to count all the nodes, while keeping track of the visited nodes

- Time O(m + n); We are at most visiting each node once and each edge once.

```py

def dfs(graph, node, visited):
    if node in visited:
        return 0  #already visited

    visited.add(node)
    score = graph[node]['score']

    for neighbor in graph[node]['neighbors']:
        score += dfs(graph, neighbor, visited)

    return score

```

### B. Give an algorithm assuming that G is a DAG

- **DAG (Directed AAcyclic Graph)**: A directed graph with no cycles.

  - It can be weakly connected: Its connected(if ignoring the directions)
  - It can be disconnected (isolated components)

- Approach: since the graph is a DAG, we can use topological sorting
  - For every directed edge u -> v, vertex u comes before vertex v in the ordering.
- Store all edges in an **Adjacency list**, so we know which vertices are reachable from each vertex
- Have a DP table where dp[i] is the the best score you can collect by reaching vertex i
  - For each vertex u in topological order:
    - For each neighbor v of u:
      - dp[v] = max(dp[v], dp[u] + score[v])
- The answer would be the maximum value in the dp table.

```py

def max_score(G, score, start):
    n = len(score) #num of vertices
    adj = adj_list(G) #assume adj_list returns an adjacency list from graph G

    order = top_sort(G) # Get the vertices in topological order. Assume that the function top_sort, sorts the vertices in topological order

    dp = [0] * n #initialize dp of size n
    dp[start] = score[start]

    for u in order:
        for v in adj[u]: # For each neighbor of u
            dp[v] = max(dp[v], dp[u] + score[v])


    return max(dp)
```

- Time Complexity: O(V + E)
  - Building adj list: O(E)
  - Topological Sort: O(V + E)
  - DP: O(V + E)
  - max(dp) : O(V)

### C. General Digraphs

- **General Graph**: A graph with directed edges and can have any strucures, including cycles, disconnected parts, and complex connectivity.

- Approach use recursion + memoization, similiar to DAG approach.

```python
def dfs(node, visited):
    if(not node):
        return 0

    if(node in visited):
        return vistied[node]

    score = node.score

    for nei in node:
        curr_score = score + dfs(nei visited)
        score = max(score, curr_score)

    return score


```

1. Start off at one node
2. Use DFS and keep exploring node neighbors
3. Once there is no node left, return score of that path
4. Backtrack and explore the next possible path
