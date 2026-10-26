"""One line summary of program.

Author: Colin Finnegan

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
    (Describe any help you got.)

I may ask you to include some additional reflection or description of
your algorithm in your submission. That information can be placed
here.

1. Dictionary, List
2. split(), get(), dictionary assignment, lsit iteration (for loop)
3. split() runtime is Θ(k), where k is the length of the string, get() is Θ(1),
   dictionary insertion is also Θ(1).  List iteration is Θ(n)
4. The runtime of my algorithm is Θ(n + 2m), where n is the pairs in the dictonary,
   and m is the number of characters in a line being split, and the amount of
   lookups in the dictionary.       
5. It works because it stores each foreign-English pair in a dictionary, with the 
   foreign word as the key and the English word as the value. This allows fast lookups 
   when translating the message, since each word can be found in constant time using the dictionary.
"""


# All submissions will have a function called main. You are certainly
# free to add additional helper functions.

def read():
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    thisdict = {}
    for line in lines:
        thisdict[line[1]] = line[0]
    return thisdict

def translate(dictionary, message):
    for l in message:
        print(dictionary.get(l, "???"), end=" ")

def main():
    dictionary = read()
    message = input().split(" ")
    translate(dictionary, message)
    print("")


if __name__ == "__main__":
    # main must be called when the script is executed.
    main()