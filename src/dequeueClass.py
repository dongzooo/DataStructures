from collections import  deque

def check_palindrome(s):
    dq = deque(s)
    palindrome =True
    while len(dq) >1 :
        if dq.popleft()!=dq.pop():
            palindrome = False
    return palindrome

s= input()
print(check_palindrome(s))
