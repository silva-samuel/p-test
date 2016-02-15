"""Unit tests for the hour_manipulation module."""

import unittest
from unittest import TestCase  
import hour_manipulation as hour_man

class AllTests(TestCase):
    """Test the stand-alone module functions."""
    def setUp(self):
    	pass

    def test_zero_hour(self):
        """Test the login function."""
        self.assertEqual( hour_man.hhmmss2sec(0,0,0), 0 )
        
        
if __name__ == '__main__':
	unittest.main()        