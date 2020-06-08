"""
Python program to return unique permutations. 
Author: Justin Clifton
Version: 06/08/2020 
"""
from itertools import permutations

def unique_permutations(numbers,size = None):
   """
   The user will input a list of numbers and the size of the permutation.
   This function takes in the list and returns all unique permutations of given
   size. 
   :param original The original list of items.
   :param size The size of the permutations. 

   """
   perms = permutations(numbers,size)

   unique_perms = []

   for perm in perms:
      if sorted(perm) not in unique_perms:
         unique_perms.append(sorted(perm))
   return unique_perms

print(unique_permutations([1,2,3,4,5],3))
   
