#multiple recursion calls


#Example 1: Fibonaci

# Fib(n) = Fib(n-1) + Fib(n-2)

# O(2^n) without DP





#Example 2: Recursion on Subsequences -- Printing the number of subsequences

# Subsequence: A sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

def printSubsequences(arr, index, n, values):
    if index == n:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        
        print()
        return 
    
    arr.append(values[index])
    printSubsequences(arr, index+1, n, values)

    arr.pop()
    printSubsequences(arr, index+1, n, values)



def main():
    values = [1, 2, 3]
    n = len(values)
    printSubsequences([], 0, n, values)


if __name__ == "__main__":
    main()






