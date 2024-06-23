import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      
      self.assertEqual(getDataPoint(quote), (quote['stock'], expected_bid_price, expected_ask_price, expected_price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      
      self.assertEqual(getDataPoint(quote), (quote['stock'], expected_bid_price, expected_ask_price, expected_price))
      
  def test_getDataPoint_handleNegativeValues(self):
    quotes = [
      {'top_ask': {'price': -110, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': -120, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -110, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      
      self.assertEqual(getDataPoint(quote), (quote['stock'], expected_bid_price, expected_ask_price, expected_price))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_normal(self):
    
    dummyData = [
      {'arg1': 10, 'arg2': 2, 'ratio': 5},
      {'arg1': 1, 'arg2': 1, 'ratio': 1},
      {'arg1': 0, 'arg2': 1, 'ratio': 0},
    ]
    
    for dummyPoint in dummyData:
      self.assertEqual(getRatio(dummyPoint['arg1'], dummyPoint['arg2']), dummyPoint['ratio']);
      
  def test_getRatio_float(self):
    
    dummyData = [
      {'arg1': 10.5, 'arg2': 2, 'ratio': 5.25},
      {'arg1': 10, 'arg2': 2.5, 'ratio': 4},
      {'arg1': 0.0, 'arg2': 1.0, 'ratio': 0.0},
    ]
    
    for dummyPoint in dummyData:
      self.assertEqual(getRatio(dummyPoint['arg1'], dummyPoint['arg2']), dummyPoint['ratio']);

  def test_getRatio_zeroDivision(self):
    
    dummyData = [
      {'arg1': 10, 'arg2': 0},
      {'arg1': 0, 'arg2': 0},
    ]
    
    for dummyPoint in dummyData:
      self.assertIsNone(getRatio(dummyPoint['arg1'], dummyPoint['arg2']));
      
  def test_getRatio_float(self):
    
    dummyData = [
      {'arg1': -10, 'arg2': 2, 'ratio': -5},
      {'arg1': 10, 'arg2': -2, 'ratio': -5},
      {'arg1': -10, 'arg2': -2, 'ratio': 5},
    ]
    
    for dummyPoint in dummyData:
      self.assertEqual(getRatio(dummyPoint['arg1'], dummyPoint['arg2']), dummyPoint['ratio']);

if __name__ == '__main__':
    unittest.main()
