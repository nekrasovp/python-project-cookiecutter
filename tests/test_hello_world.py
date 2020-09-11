from unittest import TestCase

from project.hello_world import hello_world

class NumbersTest(TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

class HelloWorldTest(TestCase):
    
    def test_hello_world(self): 
        self.assertEqual(hello_world() == "Hello World!", True)

