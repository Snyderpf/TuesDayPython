
def berlandishTranslation(s,t):
    new_word = s[::-1]

    if new_word == t:
        return "YES"
    else:
        return "NO"


s = input()
t = input()
print(berlandishTranslation(s,t))