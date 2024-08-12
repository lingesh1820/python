def revers (s):
    return s[::-1]
def ispalindrom (s):
    if s ==s[::-1]:
        return True
    else :
        return False
print(ispalindrom("dad"))
def anagram (a,b):
    a=sorted(a)
    b=sorted(b)
    if a==b:
        return True
    else:
        return False
    
