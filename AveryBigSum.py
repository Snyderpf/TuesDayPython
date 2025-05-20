

def aBigSum(n, array):
    total = 0
    for num in array:
        total +=num

    return total 




n = int(input())
array = list(map(int, input().split()))
print(aBigSum(n,array))