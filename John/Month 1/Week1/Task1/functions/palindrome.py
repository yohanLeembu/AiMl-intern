def ispalindrome(n):
    og = n
    reverse = 0
    while n>0:
        digit = n%10
        reverse = reverse * 10 + digit
        n = n//10

    if reverse == og:
        return True
    else:
        return False
    
print(ispalindrome(121))