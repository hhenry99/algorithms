#Sum of first N numbers

# Parameter -- Printing the final result instead of returning it

def sumOfN(n, sum):

    if n < 1:
        print(sum)
        return

    sumOfN(n-1, sum + n)

# Function -- Returning the final result instead of printing

def sumOfNFunc(n):

    if n == 0:
        return 0

    return n + sumOfNFunc(n-1)


def main():

    n = 10
    print("Parameter")   
    sumOfN(n, 0)

    print("=====================================")

    print("Functional")
    print(sumOfNFunc(n))


if __name__ == "__main__":
    main()

