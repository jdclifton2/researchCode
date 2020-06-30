import unittest
import bounds


class TestBounds(unittest.TestCase):
   
   #Note that this bound only works for 3 uniform graphs. Any uniformity over 3 is purely for test
   def test_order_3(self):
      self.assertEqual(bounds.collection_of_trees_upper(3, 3, 3), 2)
   
   def test_order_3_5_7(self):
      self.assertEqual(bounds.collection_of_trees_upper(3, 3, 5, 7), 7)

   def test_order_5_5_5(self):
      self.assertEqual(bounds.collection_of_trees_upper(3, 5, 5, 5), 6)

   def test_order_7_7_7(self):
      self.assertEqual(bounds.collection_of_trees_upper(3, 7, 7, 7), 10)


class TestOrders(unittest.TestCase):
   
   def test_3_uniform_size_2(self):
      self.assertEqual(bounds.possible_orders(3, 2), [3, 5])

   def test_3_uniform_size_5(self):
      self.assertEqual(bounds.possible_orders(3, 5), [3, 5, 7, 9, 11])

   def test_4_uniform_size_2(self):
      self.assertEqual(bounds.possible_orders(4, 2), [4, 7])

   def test_4_uniform_size_4(self):
      self.assertEqual(bounds.possible_orders(4, 4), [4, 7, 10, 13])

   def test_5_uniform_size_3(self):
      self.assertEqual(bounds.possible_orders(5, 3), [5, 9, 13])


if __name__ == '__main__':
   unittest.main()

