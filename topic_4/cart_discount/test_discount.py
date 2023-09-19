import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    # 3 items, discount
    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # Test for 2 items.  Since that's less than the 3 required it won't apply
    def test_list_of_two_prices_no_discount(self):
        prices = [20,1] # arrange
        expected_discount = 0 #arrange
        actual_discount = discount(prices) #action
        self.assertEqual(expected_discount, actual_discount) #assert


    # Test with 1 item, expected discount should be 0, so it should also not apply
    def test_returns_0_when_called_with_1_item(self):
        prices = [11]
        
        expected_discount = 0 #arrange
        
        actual_discount = discount(prices)
        self.assertEqual(expected_discount,actual_discount)


    # Test with 4 items.
    def test_four_items(self):
        prices = [11,4,5,7]
        
        expected_discount = 4
        
        self.assertEqual(expected_discount, discount(prices))


    # Test with more than 4 item
    def test_more_than_4_items_in_cart(self):
        self.assertEqual(discount([5,10,15,20,25]), 5)
        
        
    # Empty list test.
    def test_if_list_is_empty(self):
        prices = []
        
        expected_discount = 0
        
        self.assertEqual(expected_discount, discount(prices))
        
        
    # Same prices
    def test_if_same_prices(self):
        prices = [11,11,11]
        
        expected_discount = 11
        
        self.assertEqual(expected_discount, discount(prices))


if __name__ == '__main__':
    unittest.main()
    
    # Tests
    # Same prices, empty list, 4 items, more than 4 items, 1 tests, 2 items, 3 items
    
    # Other Tests That Are Not Written Yet
    # Strings
    # Negatives
    # Other iterative beside a lists
    # Emojis
    # Other type of characters 
    # Floats