def is_palindrome(palindrome, front, rear):
    while front < rear:
        if palindrome[front] != palindrome[rear]:
            return False
        front += 1
        rear -= 1
    return True
    
def checkPalindrome3(palindrome):
    front, rear = 0, len(palindrome) - 1
    
    while front < rear:
        if palindrome[front] != palindrome[rear]:
            if is_palindrome(palindrome, front + 1, rear) or is_palindrome(palindrome, front, rear - 1):
                return 1
            else:
                return 2
        front += 1
        rear -= 1
    return 0

T = int(input())

for i in range(T):
    palindrome = input()
    print(checkPalindrome3(palindrome))