def helpful_maths(numbers):
  numbers.sort() 
  return '+'.join(numbers)
  

s=input().split('+')
print(helpful_maths(s))
