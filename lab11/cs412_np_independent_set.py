def main():
    vertices = int(input())
    graph = {i: [] for i in range(vertices)}
    
    for i in range(vertices):
        neighbor = list(map(int, input().split()))
        neighbor = [v for v in neighbor if v != i]        
        graph[i] = neighbor   
    last_line = set(map(int, input().split()))

    print("Dictionary:", graph)
    print("Independent set:", last_line)

    if independent_set_check(graph, last_line):
        print("TRUE")
    else:
        print("FALSE")


def independent_set_check(adjacency_dict, indySet):
    for i in indySet:
        for j in adjacency_dict.keys():
            if i == adjacency_dict.get(j):
                return False
            else:
                return True




if __name__ == "__main__":
    main()