"""Palindrome Lab B
Version: 2025
Author: Colin Finnegan
"""

def isPalindrome(s, left, right):
    return s[left:right] == s[left:right][::-1]


def count_palindrome_parts(input_string):
    n = len(input_string)
    
    memo = [-1] * (n + 1)

    def countPP(i):
        if i == n:
            return 1
        
        if memo[i] != -1:
            return memo[i]

        total = 0
        for j in range(i + 1, n + 1):
            if isPalindrome(input_string, i, j):
                total += countPP(j)
        memo[i] = total
        return total
    
    return countPP(0)


def main():
    number = int(input())
    for _ in range(number):
        word = input().strip()
        print(count_palindrome_parts(word))


if __name__ == "__main__":
    main()
