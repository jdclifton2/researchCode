"""
Python program to return combinations. 
Author: Justin Clifton
Version: 06/08/2020 
"""
from itertools import permutations
import sys

def unique_permutations(numbers,size = None):
   """
   The user will input a list of numbers and the size of the combinations.
   This function takes in the list and returns all combinations of given
   size. 
   :param original The original list of items.
   :param size The size of the combinations. 

   """
   perms = permutations(numbers,size)

   unique_perms = []

   for perm in perms:
      if sorted(perm) not in unique_perms:
         unique_perms.append(sorted(perm))
   return unique_perms


   
if __name__ == '__main__':

   print("List Should Be Inputted As Such:\n 1 2 3 4 5")

   numbers = input("Input the list you would like combinations of: ")

   #this would be an incorrect format
   if("," in numbers):
      sys.exit("No commas allowed.")
   
   numbers_split = numbers.split()

   #further checks for incorrect format
   try:
      size = int(input("Enter the size of the permutations: "))
      #convert items in list to ints
      map_object = map(int, numbers_split)
   except ValueError:
      sys.exit("Both parameters must contain only numbers.")
   
   numbers_list = list(map_object)
   print(unique_permutations(numbers_list,size))
