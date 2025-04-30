
def untopian_tree(n):
    height = 1 
    for i in range(1,n+1):
        if i%2 ==0:
            height+=1
        else:
            height *=2
    
    return height
    


cycle = int(input())
while cycle>0:
    n = int(input())
    print(untopian_tree(n))
    cycle-=1

