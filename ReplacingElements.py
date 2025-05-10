
def replaceElement(n,d,nums):

    if all(x<=d for x in nums):
        return "YES"
        
    nums.sort()
    if nums[0]+nums[1]<d:
        return "YES"
    else:
        return "NO"

t = int(input())
while t:
    n,d=map(int,input().split())
    array = list(map(int,input().split()))
    print(replaceElement(n,d,array))
    t-=1