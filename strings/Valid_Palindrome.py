s = "?A man, a plan, a canal: Panama"

def isPalindrome():
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalpha():
            left += 1

        while left < right and not s[right].isalpha():
            right -= 1

        if s[left].lower() != s[right].lower():
            return "Not Palindrome..."

        left += 1
        right -= 1

    return "Is Palindrome..."


print(isPalindrome())
