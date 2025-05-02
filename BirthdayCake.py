
def birthdayCake(n,candles):
    count = 0
    tallest = float('-inf')

    for i in range(n):
        if candles[i]> tallest:
            tallest= candles[i]
            count = 1
        elif candles[i]  == tallest:
            count +=1 

    return count


n = int(input())
candles = list(map(int,input().split()))
print(birthdayCake(n,candles))