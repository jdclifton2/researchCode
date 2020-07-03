"""
This program is used to generate lower bounds for a collection of stars.
Author: Justin Clifton
Version 07/03/20
"""

import bounds
import itertools
from sys import argv,exit

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
      for comb in combs:
         if 0 not in comb:
            factorials = []
            for num in comb:
               
               fact = bounds.binomial((num - 1), (uniformity - 1))
 
               factorials.append(fact)
            if sum(list(factorials)) - len(factorials) >= one_facs:
               yield comb

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


def main():
   order = int(argv[2])
   uniformity = int(argv[1])

   if order % uniformity == 0:
      ramsey_stars_string(uniformity, order, theorem_6_stars(uniformity, order))
   else:
      print("Order must be divisible by uniformity.")
      exit(1)

if __name__ == '__main__':
   main()
