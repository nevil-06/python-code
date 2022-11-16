s1 = "Ault"
s2 = "Kelly"

def strInStr(s1,s2):
    len1 = len(s1)//2
    newStr = s1[:len1]+s2+s1[len1:]
    print(newStr)

strInStr(s1,s2)