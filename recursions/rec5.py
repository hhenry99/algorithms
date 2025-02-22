#Printing whose subsequence whos sum is K


def subsequenceSum(index, arr, sum, k, values):
    if(index == len(values)):
        if (sum == k):
            print(arr)
        return
    
    arr.append(values[index])
    subsequenceSum(index+1, arr, sum+values[index], k, values)



    arr.pop()
    subsequenceSum(index+1, arr, sum, k, values)
  

def main():
    values = [1, 2, 3]
    k = 3
    subsequenceSum(0, [], 0, k, values)


if __name__ == "__main__":
    main()


#example 2
#Print only one answer, use bools --> Ret T/F




#example 3
#counting the number of subsequences whose sum is K

#left = funct()
#right = funct()
#return left + right

