def isPalindrome(x: int) -> bool:
    number = str(x)
    reverse_number = number[::-1]

    if(number == reverse_number):
        return True
    else:
        return False
    
print(isPalindrome(121))