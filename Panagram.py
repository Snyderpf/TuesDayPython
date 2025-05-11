
def panGram(n,s):
    
    s = s.lower()
    new_s = set(s)
    if len(new_s) < 26 or n<26:
        return "NO"
    else:
        return "YES"
    


n = int(input())
s = input()
print(panGram(n,s))