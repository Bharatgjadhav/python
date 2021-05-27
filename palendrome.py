def isPalendrome(s):
    return s==s[::-1]


s="civic"
checkIsPalendrome=isPalendrome(s)


if checkIsPalendrome:
    print("yes")
else:
    print("no")