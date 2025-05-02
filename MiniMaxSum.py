
def miniMaxSum(nums):
    nums.sort()

    a_sum = sum(nums[0:4])
    b_sum = sum(nums[1:5])

    minimum = min(a_sum,b_sum)
    maximum = max(a_sum,b_sum)

    print(minimum, maximum)



array = list(map(int,input().split()))
miniMaxSum(array)