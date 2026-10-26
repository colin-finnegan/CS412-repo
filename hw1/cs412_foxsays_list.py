"""
    name: Colin Finnegan

"""

def read():
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    sounds = []
    animals = []
    total = [sounds, animals]
    for line in lines:
        sounds.append(line[2])
        animals.append(line[0])
    last = input()
    return total

def translate(list, message):
    fox = []
    animals = []
    for l in message:
        if l not in list[0]:
            fox.append(l)
        else:
            i = list[0].index(l)
            a_name = list[1][i]
            if a_name not in animals:
                animals.append(a_name)
    print("what the fox says:", " ".join(fox))
    print("also heard:", " ".join(animals))
    
    

def main():
    message = input().split(" ")
    total = read()
    translate(total, message)


if __name__ == "__main__":
    # main must be called when the script is executed.
    main()