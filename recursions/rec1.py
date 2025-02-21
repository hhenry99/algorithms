#Print from 1 To N using BackTracking
def printToN(i, n):
    if i < 1:
        return
    
    printToN(i-1, n)
    print(str(i) + " iteration: " + str(i))

#Print from N to 1 using BackTracking
def printFromNTo1(i, n):

    if(i > n):
        return
    
    printFromNTo1(i+1, n)
    print(str(i) + " iteration: " + str(i))


def main():
    n = 10
    printToN(n, n)
    printFromNTo1(1, n)


if __name__ == "__main__":
    main()

