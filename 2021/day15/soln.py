from collections import deque

class Graph():
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
        self.heur = {el:1 for el in adjac_lis}
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = self.heur
   
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()

                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
        
    
def add_nodes_and_edges(coords):
        
    xlength = len(coords)**0.5
    nodes_and_edges = {}
    node_values = {}
    for n, node_value in coords.items():
    
        for m in [[0,1], [0,-1],[1,0],[-1,0]]:
            nbr = (n[0]+m[0], n[1]+m[1])
            list_pos_n = n[0] + n[1]*xlength
            list_pos_nbr = nbr[0] + nbr[1]*xlength
            
            if nbr in coords.keys():
                node_values[list_pos_n] = node_value
                nodes_and_edges[list_pos_n] = nodes_and_edges.get(list_pos_n, []) + [(list_pos_nbr, node_value)]

    return nodes_and_edges, node_values
    

    
f = open('input.txt')
raw = f.readlines()
f.close()

lines = list(raw)

part1_coords = {}
for y_coord, line in enumerate(lines):
    line_length = len(line.strip())
    x_values = [int(num) for num in line.strip()]
    for x_coord, x in enumerate(x_values):
        part1_coords[(x_coord, y_coord)] = x
        
     
part2_coords = {}
for i in range(5):
    for j in range(5):
        for k, v in part1_coords.items():
            if v+i+j> 9:
                val = (v+i+j) % 10 +1
            else:
                val = v+i+j
            part2_coords[k[0]+line_length*i, k[1]+line_length*j] = val
        
for coords in [part1_coords, part2_coords]:
    nodes_and_edges, node_values = add_nodes_and_edges(coords)
    graph = Graph(nodes_and_edges)
    shortest_path = graph.a_star_algorithm(0, max(nodes_and_edges.keys()))
    print(sum([node_values[node] for node in shortest_path])-1)