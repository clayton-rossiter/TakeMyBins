import unittest

from main import main


class TestMain(unittest.TestCase):
    
    def test_main_function_works(self):
        """tests operation of main function works as intended"""
        main()
