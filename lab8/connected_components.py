# Implementation of the count-and-label 
# connected component counting algorithm.
#
# Author: John Bowers
# Version: Mar 17, 2021

# March 2022 -- molloykp
#  Changed code to label components starting a 0 (instead of 1)
# October 2023 -- molloykp
#  Change code to accept new adj list/hash map structure

# Version of the iterative dfs that takes as input
# a list of labels, one per vertex, and a starting 
# vertex v and uses iterative depth-first-search
# to label each vertex with a given currentLabel
# 
# Parameters: 
#   * graph is an adjaceny list where vertices name/keys are stored
#     in a dictionary.  Each vertex has its own dictionary
#     where the key is the edge endpoint and the value is the
#     weight of the edge.
#   * v is the vertex to DFS from
#   * labels is an array of length V which is -1 if the vertex is unvisited
#   * currentLabel is the label to set on every visited vertex
#
# labels is an out-parameter and will be modified destructively during the 
# run of this operation. 
#

def dfs_label(graph, v, labels, currentLabel):
    bag = [v]
    while bag: # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = currentLabel
            for w in graph[u]:
                bag.append(w)

# Counts the number of connected components in the graph
# and labels each vertex with its connected component index
#
# Parameters:
#   * graph given as an adjaceny list/set structure with vertices 0..(n-1)
#
# Returns: 
#   count, labels
#   where count is the number of connected components in the graph
#   and labels is the labeling of each vertex's connected component
#   starting from index 0 
def count_and_label(graph):
    labels = [-1 for _ in range(len(graph))] # Initially all labels are -1
    count = -1
    for v in range(len(graph)): # for each vertex
        if labels[v] == -1: # if v is not visited
            count += 1
            dfs_label(graph, v, labels, count)
    return count+1, labels

if __name__ == "__main__":
    graph = {
        0: {1:2},           # 0's neighbors
        1: {0:2, 2:4, 3:1}, # 1's neighbors
        2: {1:4, 3:5},      # 2's neighbors
        3: {1:1, 2:5},      # 3's neighbors
        4: {5:8},           # 4's neighbors
        5: {4:8}            # 5's neighbors
    }

    count, labels = count_and_label(graph)
    print(f"Number of connected components: {count}")
    print(f"Vertex labels: {labels}")
