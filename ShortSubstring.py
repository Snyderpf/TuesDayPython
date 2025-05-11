def shortSubstring(s):
    n = len(s)
    new_word = s[:2]

    for i in range(3,n,2):
        if i%2 ==1:
            new_word +=s[i]
    return new_word


t = int(input())
while t:
    s = input()
    print(shortSubstring(s))
    t-=1
