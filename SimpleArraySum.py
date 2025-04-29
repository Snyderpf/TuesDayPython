def simpleArraySum(array):
    total_sum = 0
    n= len(array)
    for i in range(n):
        total_sum +=array[i]

    return total_sum


n= int(input())
input_array = list(map(int, input().split()))
print(simpleArraySum(input_array))
