# shortest drone delivery finder
# takes coordinates of a set of delivery locations as input

import time
import math
import numpy as np
from sys import maxsize, argv
from itertools import permutations

# V=4

def coordToGraph(file, V):
    lines = file.readlines()
    # matrix of coords
    coords = np.zeros((len(lines), 2))
    
    for i in range(len(lines)):
        # p,q= lines[i].split()
        coords[i][0], coords[i][1] = lines[i].split()  
    # print (len(coords))
    V=len(coords)
    
    # adjacency matrix for the graph
    # calculate distance between each combination of the coordinates
    # put the distances in appropriate position in the adjacency matrix
    graph = np.zeros((len(coords), len(coords)) )
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                graph[i][j] = 0
            elif j > i:
                distance = math.sqrt((coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2)
                graph[i][j] = (distance)
                graph[j][i] = (distance)
    # print(graph)
    return graph, V

# implementation of traveling Salesman Problem 
def shortestPath(graph, s, V): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    print(V)
    for i in range(V): 
        if i != s: 
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize
    next_permutation=permutations(vertex)
    
    # print(min_path)
    # print(permutations(range(V)))
    for i in next_permutation:
        # print(i)
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
        # min_path = current_pathweight
    return min_path 
 
def main():
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    f = open("./data/"+argv[1], 'r')
    V = 0
    start_time = time.time()
    graph, V = coordToGraph(f, V)
        
    # matrix representation of graph 
    # graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
    print(shortestPath(graph, s, V))
    end_time = time.time()
    total_time = end_time - start_time
    print ("Execution time = ", total_time)

# Driver Code 
if __name__ == "__main__": 
    main()