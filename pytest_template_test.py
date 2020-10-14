'''
https://coderlessons.com/tutorials/python-technologies/uznaite-pytest/pytest-kratkoe-rukovodstvo

import unittest

class TestUtilDate(unittest.TestCase):
    def setUp(self):
        #init_something()
        pass
        
    def tearDown(self):
        #teardown_something()
        pass
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        
    def test_failed_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilDate)
    unittest.TextTestRunner(verbosity=2).run(suite)

'''

# То же самое в PyTest:

import os
import pytest

def setup_module(module):
    #init_something()
    pass

def teardown_module(module):
    #teardown_something()
    pass

def test_upper():
    assert 'foo'.upper() == 'FOO'
    
def test_isupper():
    assert 'FOO'.isupper()
    
def test_failed_upper():
    assert 'foo'.upper() == 'FOo'

if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " --tb=line ")
    #os.system ("pytest -v " + os.path.basename(__file__) + " --tb=line ")
