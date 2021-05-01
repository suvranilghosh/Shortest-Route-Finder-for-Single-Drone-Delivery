# shortest drone delivery finder
# takes coordinates of a set of delivery locations as input
# starts from location 0 by default [starting point]
# calculates distance of shortest hamiltonian cycle
# yet to implement storage of path

import time
import math
import numpy as np
from sys import maxsize, argv
from itertools import permutations

# V=4

# convert input
def coordToGraph(lines):
    # matrix of coords
    coords = np.zeros((len(lines), 2))
    
    for i in range(len(lines)):
        # p,q= lines[i].split()
        coords[i][0], coords[i][1] = lines[i].split()  
    
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
    return graph

# implementation of traveling Salesman Problem 
def shortestPath(graph, s, V): 
    # store all vertex apart from source vertex
    vertex = [i for i in range(V) if i != s]
 
    # initialize minimum path length to infinity 
    # (later used for returning the weight of the shortest Hamiltonian Cycle)
    min_path_distance = float('inf')
    # returns permutations of entire list of vertices [0 to V-1] as immutatble tuples
    next_permutation = permutations(vertex)
    
    # print(min_path_distance)
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
        if current_pathweight <= min_path_distance:
            min_path_distance = current_pathweight
            min_path = i
        
    return min_path_distance, min_path
 
def main():
    if len(argv)<2:
        print ("***ERROR : Please input file name along in cmd line***")
        exit()
    file = open("./data/"+argv[1], 'r')
    lines = file.readlines()
    V = len(lines)

    print("Number of delivery locations: ", V)

    start_time = time.time()
    graph = coordToGraph(lines)  
    
    # drone starts from 0
    s = 0
    shortest_dist, shortest_path = shortestPath(graph, s, V)
    end_time = time.time()
    total_time = end_time - start_time
    
    # print shortest route
    print("Shortest Route: ", s, end = '->')
    count = 0
    for location in shortest_path:
        if count == len(shortest_path)-1:
            print(location)
        else:
            print(location,end = '->')
        count += 1

    # print shortest route distance and execution time
    print("Shortest Route Distance: ", shortest_dist)
    print ("Execution time = ", total_time)


# Driver Code 
if __name__ == "__main__": 
    main()


# New brunswick, NJ  : lat= 40.486216 long = -74.451819
# range from +- 0.10 for both lat and long 