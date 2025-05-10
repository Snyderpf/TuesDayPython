
def reverseNum(number):
      
      x = 0 
      while(number !=0):
         
         last =  number %10
         x = x*10 + last 
         number = number// 10 
      return x


def beautifulDays(start,end,k):
     
     days = 0 
     for x in range(start,end+1):
            
            new_num = reverseNum(x)
            total = abs(x -new_num)
            if total %k ==0:     
                    
                    days +=1
     return days
 

start,end,k = map(int,input().split())

print(beautifulDays(start,end,k))




