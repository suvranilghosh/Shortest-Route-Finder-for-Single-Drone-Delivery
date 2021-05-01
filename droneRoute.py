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

# distance calculator between two coordinates using haversine formula
def haversine(lat1, long1, lat2, long2):
    R = 6378.1 # radius of earth 
    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    delphi = (lat2-lat1) * math.pi / 180
    dellambda = (long2-long1) * math.pi / 180
    a = math.sin(delphi/2) * math.sin(delphi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(dellambda/2) * math.sin(dellambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c # in kilometers


# convert input (list of lines containing coordinates to adjacency matrix)
def coordToGraph(lines):
    # matrix of coords
    coords = np.zeros((len(lines), 2))
    
    # store coordinates in a list
    for i in range(len(lines)):
        # p,q= lines[i].split()
        coords[i][0], coords[i][1] = lines[i].split()  
    
    # adjacency matrix for the graph
    # calculate distance between each combination of the coordinates
    # put the distances in appropriate position in the adjacency matrix
    # distance calculated using haversine formula
    graph = np.zeros((len(coords), len(coords)) )
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                graph[i][j] = 0
            elif j > i:
                # distance = math.sqrt((coords[i][0]-coords[j][0])**2+(coords[i][1]-coords[j][1])**2)
                distance = haversine(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
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
    print("Shortest Route:", s, end = ' -> ')
    count = 0
    for location in shortest_path:
        if count == len(shortest_path)-1: print(location,'->',s)
        else: print(location,end = ' -> ')
        count += 1

    # print shortest route distance and execution time
    print("Shortest Route Distance:", shortest_dist, 'Km')
    print ("Execution time =", total_time, "seconds")


# Driver Code 
if __name__ == "__main__": 
    main()


# New brunswick, NJ  : lat= 40.486216 long = -74.451819
# range from +- 0.15 for both lat and long 