
def plusMinus(n,array):
    positive = 0
    negative = 0 
    zeros = 0
    
    for num in array:
        if num <0:
            negative +=1
        elif num>0 :
            positive +=1 
        
        else:
            zeros +=1 
    total = [positive,negative,zeros]
    for i in range(3):
        to_print =total[i]/n
        print(f"{to_print:.6f}")


n = int(input())
array = list(map(int,input()))
plusMinus(n,array)