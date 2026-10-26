"""Dynamic Programming Lab 7 Palindrome
Version: 2025
Author: Colin Finnegan
"""

def isPalindrome(s, left, right):
    return s[left:right] == s[left:right][::-1]


def count_palindrome_parts(input_string):
    n = len(input_string)
    
    memo = [0] * (n + 1)

    memo[n] = 1

    for i in range(n - 1, -1, -1):
        total = 0
        for j in range(i + 1, n + 1):
            if isPalindrome(input_string, i, j):
                total += memo[j]
        memo[i] = total
    
    return memo[0]


def main():
    number = int(input())
    for _ in range(number):
        word = input().strip()
        print(count_palindrome_parts(word))


if __name__ == "__main__":
    main()
