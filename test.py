import unittest
from hellowolrd import myclass
class TestStringMethods(unittest.TestCase):

    def test_myHelloWorld1(self):
        self.assertEqual(myclass.my_hello_world_1(), "Hello world 1")
    
    def test_myHelloWorld2(self):
        self.assertEqual(myclass.my_hello_world_2(), 'Hello world 2')

    def test_myHelloWorld3(self):
        self.assertEqual(myclass.my_hello_world_3(), 'Hello world 3')

    def test_myHelloWorld4(self):
        self.assertEqual(myclass.my_hello_world_4(), 'Hello world 4')

    def test_myHelloWorld5(self):
        self.assertEqual(myclass.my_hello_world_5(), 'Hello world 5')

    def test_myHelloWorld6(self):
        self.assertEqual(myclass.my_hello_world_6(), 'Hello world 6')
 

if __name__ == '__main__':
    unittest.main()

 