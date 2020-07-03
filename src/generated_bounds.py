"""
This code will be used to produce direct computations of bounds for Ramsey numbers.
Author: Justin Clifton
Version 06/30/2020
"""

import bounds
import itertools

"""
This function will find the upper bound for all possible combinations of 3 uniform trees from a
single edge to a max size. 
param: max_size_of_tree The maximum size of the tree.
"""
def generate_3_uniform_upper(max_size_of_tree):
   
   #get every possible valid order
   orders = bounds.possible_orders(3, max_size_of_tree)

   for i in range(2,len(orders)):
      #We want all possible combinations of the orders.
      combs = itertools.combinations(orders,i)
      for comb in combs:
         #Creating an array for the string of Tree.
         tree_str = []
         for num in comb:
            tree_str.append("T^3_{}".format(num))

         print("R({}) <= {}".format(', '.join(tree_str),bounds.collection_of_trees_upper(3, comb)))
   #For repeating numbers.
   for order in orders:
      for j in range(1, 10):
         copies_of_order = [order] * j

         print("R({}) <= {}".format(str(copies_of_order), bounds.collection_of_trees_upper(3, copies_of_order)))

"""
This function is used to generate the size of all stars that have a lower order than our 
complete graph.
param: uniformity The uniformity of the complete graph.
param: order The order of the graph.
"""
def generate_stars(uniformity, order):
   
   #All possible one factors
   one_facs = bounds.complete_one_factors(uniformity, order)
   print("K^{}_{} # of 1 factors: {}".format(uniformity, order, one_facs))

   #Get all possible stars by their size.
   possible_stars = []
   for i in range(order):
      possible_stars.append(bounds.number_star_edges(uniformity, i))
   
   for j,star in enumerate(possible_stars):
      print("S^{}_1,{} # of edges {}".format(uniformity, j , star))

   possible_stars = list(filter(lambda num: num != 0, possible_stars)) #Remove size 0 enteries.
   #print(possible_stars) 
   
   #iterate through possible stars
   for k in range(len(possible_stars)):
      #get combinations of the stars of various sizes
      combs = itertools.combinations(possible_stars, k)
      for comb in combs:
         #make a list so its mutable
         l_comb = list(comb)
         #subtract 1 from each entry
         for l in range(len(comb)):
            l_comb[l] = comb[l] - 1
         if not 0 in l_comb:
            if one_facs - sum(l_comb) == 0:

               print(l_comb)

"""
Finds all combinations up to the size of the iterable.
param: iterable The iterable object. 
param: start_index The size of the smallest combinations. Will start here and go up to the size
of the iterable.
return: yields the next item in the combinations. if you want the full list, do 
list(generate_combinations_upto(iterable, start_index))
"""
def generate_combinations_upto(iterable, start_index = 2):
   
   #Iterate through the iterable.
   if  start_index >= 0:
      for k in range(start_index, len(iterable)):
     
         combs = itertools.combinations(iterable,k)
         #get combinations of size k up to len(iterable).
         for comb in combs:
            yield comb

   
print("Debug generate_combinations_upto(1, 2, 3, 4)) {}".format(list(generate_combinations_upto([1,2,3,4]))))

"""
This came from theorem 6. Only works if uniformity divides the order. order must be >= 2. 
This takes the uniformity and order of a complete graph. It then finds the number of one factors
of the complete graph. After this, it gets the possible sizes for any star below the order of the
complete graph. Next, it looks at all combinations of stars of order less than the order of the 
complete graph.
param: uniformity The uniformity of the graph.
param: The order of the graph.  
"""
def theorem_6_stars(uniformity, order):
   #All possible one factors
   one_facs = bounds.complete_one_factors(uniformity, order)
   print("K^{}_{} # of 1 factors: {}".format(uniformity, order, one_facs))

   #Get all possible stars by their size.
   possible_stars = []
   for i in range(order):
      possible_stars.append(bounds.number_star_edges(uniformity, i))
   
   for j,star in enumerate(possible_stars):
      print("S^{}_1,{} # of edges {}".format(uniformity, j , star))

   possible_stars = list(filter(lambda num: num != 0 and num > uniformity, possible_stars)) #Remove size 0 enteries.
   
   #iterate through possible stars
   for k in range(2, len(possible_stars)):
      #get combination of the stars of various sizes
      combs = itertools.combinations(list(range(uniformity, order)), k)
      #print("Combs {}".format(list(combs)))
      for comb in combs:
         if 0 not in comb:
            factorials = []
            #print("Comb {}".format(comb))
            for num in comb:
               #print("Num {}".format(num))
               fact = bounds.binomial((num - 1), (uniformity - 1))
               #print("Fac {}".format(fact))
               factorials.append(fact)

         #print("Factorials {}".format(factorials))
            if sum(list(factorials)) - len(factorials) >= one_facs:

               #print("Sum {} >= {}".format(sum(list(factorials)) - len(factorials), one_facs))
               #consider making this a yield statement?
               yield comb


         #make a list so its mutable
         #l_comb = list(comb)
         #subtract 1 from each entry
         #for l in range(len(comb)):
          #  l_comb[l] = comb[l] - 1
         #if not 0 in l_comb:
            #if one_facs - sum(l_comb) == 0:

#generate_stars(3,9)
"""
This function prints the equality corresponding with a collection of star orders. 
Example: If you pass in (3,9,[(1,2), (3,4)]),
output will be
R(S^3_1,1 S^3_1,2) >= 10
R(S^3_1,3 S^3_1,4) >= 10
param: uniformity The uniformity of a graph.
param: order The order of a graph.
param: star_orders A collection of orders corresponding with stars that produced a desired result.
"""
def ramsey_stars_string(uniformity, order, star_orders):
   for comb in star_orders:
      star_string =  ['R','(']
      for num in comb:
         star_string.append("S^{}_1,{} ".format(uniformity,num))
      star_string.append(')')
      print(''.join(star_string) + " >= {}".format(order + 1))


#print("T^3_1,".join(list(theorem_6_stars(3,12))))
ramsey_stars_string(4,12,theorem_6_stars(4,12))
