"""
These functions will serve to help me in calculating the upper and lower bounds
for various ramsey numbers. 
"""


from math import floor, ceil,factorial

"""Function to compute the weak chromatic number of a hypergraph.
   param: order The order of the graph, the number of vertices.
   param: uniformity The uniformity of the graph, how many vertices each hyperedge
   contains.  
"""
def weak_chromatic(order, uniformity):
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
Returns the size of a given graph.
param: order The order of the graph.
param: uniformity The uniformity of the graph. 
"""
def size(order, uniformity):
   return (order - 1)/(uniformity - 1)


"""
The formula for a collection of r-uniform trees upper bound. 
R(T^(r)_{m_1},T^(r)_{m_2},...,T^(r)_{m_p}) <= R(L_1 K^(r-1)_{r-1},L_2 K^(r-1)_{r-1},...,
L_p K^(r-1)_{r-1}) = L_1 + 1 + summation from j = 1 to i of L_j - 1.
param: uniformity The uniformity of the trees in the collection.
param *args The order of each tree. m_1,m_2,...,m_p. 
"""
def collection_of_trees_upper(uniformity, orders):
   sizes = []
   for order in orders:
      curr_size = size(order, uniformity)
      sizes.append(curr_size)
  
   max_of_sizes = max(sizes)

   sum_of_sizes = sum(sizes) - len(sizes)

   return max_of_sizes + 1 + sum_of_sizes


"""
This function will generate all possible orders for a given uniformity. These orders are for a 
1-tight hypergraph. 
param: uniformity The uniformity of the hypergraph
size: The size of the hypergraph.
"""
def possible_orders(uniformity, max_size):
   orders = []
   orders.append(uniformity)
   
   for edge in range(1, max_size): 
      vertices = (uniformity - 1) + orders[edge - 1] 
      orders.append(vertices)

   return orders


"""
This function computes the lower bound for the case with two stars with order1,order2 >= r >= 2.
param: uniformity The uniformity of the star.
param: order1 The order of the first star.
param: order2 The order of the second star.
return: The lower bound for two stars.

def star_vs_star_lower_bound(uniformity,order1,order2):
   return order1 + order2 - 2uniformity + 1



This function computes the lower bound for a collection of stars with orders >= r >=2. Order of
complete graph must by divisible by uniformity. 
param: uniformity The uniformity of the graph.
param: *args The orders of the stars.
returns: The lower bound for the collection of stars.

def collection_of_stars_lower(uniformity,*args):
   return 
   
"""  


"""
A function for computing the binomal coefficient. 
param: x The number to choose from.
param: y The number of things being chosen.
return: The binomal coefficient.
"""
def binomial(x,y):
   try:
      binom = factorial(x) // factorial(y) // factorial(x - y)
   except ValueError:
      binom = 0
   return binom 


"""
This function will compute the number of one factors for a complete graph K^r_n where r divides n.
param: uniformity The uniformity of the hypergraph.
param: order The order of the hypergraph. 
returns: The number of possible one factors. 
""" 
def complete_one_factors(uniformity, order):
   one_factors = 0
   if order % uniformity == 0:
      one_factors = binomial(order - 1, uniformity - 1)
   return one_factors
   

def number_star_edges(uniformity, order):
   return binomial(order -1, uniformity - 1)


