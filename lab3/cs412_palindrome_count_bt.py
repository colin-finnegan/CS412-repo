"""
    name: Colin Finnegan

"""


def is_palindrome(s, start, end):
    if start >= end:
        return True
    
    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)


def partitions(s):
    if s == "":
        return 1
    
    total = 0
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if is_palindrome(prefix, 0, len(prefix) - 1):
            total += partitions(s[i:])
    return total


def main():
    num = int(input())
    for _ in range(num):
        s = input().strip()
        print(partitions(s))
    

if __name__ == "__main__":
    main()

