
def calledPm(s):
    hour = int(s[:2])
    if hour == 12:
        new_hour = "12"

    else:
        new_hour = str(hour+12)
    
    return new_hour + s[2:-2]
     
         

def calledAm(s):
    hour = int(s[:2])
   
    if hour == 12:
        new_hour = "00"
    
    else:
        new_hour = "0" + str(hour) if hour <10 else str(hour)

    return new_hour +s[2:-2]


def timeConversion(s):

   
    if s[-2:] =='PM':
        return calledPm(s)
    else:
        return calledAm(s)

s = input()
print(timeConversion(s))