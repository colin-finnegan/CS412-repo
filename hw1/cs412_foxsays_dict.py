"""
    name: Colin Finnegan

"""

def read():
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    thisdict = {}
    for line in lines:
        thisdict[line[2]] = line[0]
    last = input()
    return thisdict

def translate(dictionary, message):
    fox = []
    animals = []
    a_set = set()
    for l in message:
        if l not in dictionary:
            fox.append(l)
        else:
            if dictionary[l] not in a_set:
                animals.append(dictionary[l])
                a_set.add(dictionary[l])
    print("what the fox says:", " ".join(fox))
    print("also heard:", " ".join(animals))
    
    

def main():
    message = input().split(" ")
    dictionary = read()
    translate(dictionary, message)


if __name__ == "__main__":
    # main must be called when the script is executed.
    main()