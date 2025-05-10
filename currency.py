def currencySystem(n,array):

    for i in range(n):
       if array[i] ==1:
            
            return 1
    return -1

n = int(input())
array = list(map(int,input().split()))
print(currencySystem(n,array))

