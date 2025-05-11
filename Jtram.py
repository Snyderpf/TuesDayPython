
def Jtram(n,exit,enter):
    max_capacity = 0
    curr_inside = 0
    for i in range(n):
        curr_inside  -= exit[i]
        curr_inside  += enter[i]
        max_capacity = max(max_capacity,curr_inside)

    return max_capacity


n = int(input())
exit = []
enter = []
for _ in range(n):
    getting_out, getting_in = map(int,input().split())
    exit.append(getting_out)
    enter.append(getting_in)

print(Jtram(n,exit,enter))



