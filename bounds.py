"""
These functions will serve to help me in calculating the upper and lower bounds
for R(H_1,H_2,...H_t;r). 
"""


from math import floor, ceil

"""Function to compute the weak chromatic number of a hypergraph.
   param: order The order of the graph, the number of vertices.
   param: uniformity The uniformity of the graph, how many vertices each hyperedge
   contains.  
"""
def weak_chromatic(order,uniformity):

   return ceil(order/(uniformity - 1))


"""Function to compute the chromatic surplus of a hypergraph.
   param: order The order of the graph,the number of vertices.
   param: uniformity The uniformity of the graph, how many vertices each hyperedge
   contains.  
"""
def chromatic_surplus(order, uniformity):
   surplus = order % (uniformity -1)

   if surplus == 0:
      surplus = uniformity - 1

   return surplus

"""
The formula for R(P_m, P_n; 3).
param: path1_size The size of the first path. The number of edges of the first path.
param: path2_size The size of the second path. The number of edges of the second path. 
"""
def path_bound(path1_size, path2_size):
   return 2 * path1_size + floor(path2_size/2)

"""
TODO: Finish programming the lower bound. Need a formula for determining the number of edges in
a tree. 
"""
def lower_bound(tree_order,tree2_order, uniformity, *args):
   #Since this upper bound works for comparing up to t hypergraphs, this list will hold their orders.
   orders = []
   for num in args:
      orders.append(num)
   


print(path_bound(2,2)) 



