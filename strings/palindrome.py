string = "nayan"

def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right :
        if string[left] != string[right] :
            return False
        else :
            left += 1
            right -= 1
        
    return True


if isPalindrome(string) :
    print("String is palindrome")
else :
    print("Not palindrome")