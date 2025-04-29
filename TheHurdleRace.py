
def hurdle_race(heights,k):
    pot_cnt=0
    
    for max_h in heights:
        if max_h >k:
            temp = max_h-k
            pot_cnt = max(pot_cnt,temp)
    
    return pot_cnt



a,b = map(int,input().split())
nums = list(map(int,input().split()))
print(hurdle_race(nums,b))