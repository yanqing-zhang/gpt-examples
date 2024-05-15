import unittest
class ListDicTestCase(unittest.TestCase):

    def test_diclist(self):
        a = [
            {'name': 'John', 'age': 25},
            {'name': 'Jane', 'age': 30},
        ]
        print(a[0]['name'])


