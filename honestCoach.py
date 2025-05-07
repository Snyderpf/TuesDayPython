
def honestCoach(n,players):
   ans = 10^9
   players.sort()
   
   for i in range(n-1):
       a= max(players[:i+1])
       b = min(players[i+1:])
       ans = min(ans,abs(a-b))
  
   return ans


t= int(input())
while(t):
   n= int(input())
   players = list(map(int,input().split()))
   print(honestCoach(n,players))
   t-=1

