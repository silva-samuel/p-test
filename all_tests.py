"""Unit tests for the hour_manipulation module."""

import unittest
from unittest import TestCase  
import hour_manipulation as hour_man

class AllTests(TestCase):
    """Test the stand-alone module functions."""
    def setUp(self):
        pass

    def test_zero_hour(self):
        """Test if function return correct value for 00:00:00."""
        self.assertEqual( hour_man.hhmmss2sec(0,0,0), 0 )
        
    def test_max_hour(self):
        """Test if function return correct value for 23:59:59."""
        self.assertEqual( hour_man.hhmmss2sec(23,59,59), 86399 )
        
    def test_hour_range_pos(self):
        """Test if function returns True for hour value between 0 and 23."""
        self.assertTrue( hour_man.checkHourRange(0) )

    def test_hour_range_neg(self):
        """Test if function returns False for hour value out of 0 and 23 range."""
        self.assertFalse( hour_man.checkHourRange(24) )
        
    def test_minutes_seconds_range_pos(self):
        """Test if function returns True for minutes/seconds value between 0 and 59."""        
        self.assertTrue( hour_man.checkMinutesSecondsRange(37) )
        
    def test_minutes_seconds_range_neg(self):
        """Test if function returns True for minutes/seconds value out of 0 and 59 range."""        
        self.assertFalse( hour_man.checkMinutesSecondsRange(60) )
        
if __name__ == '__main__':
    unittest.main()        