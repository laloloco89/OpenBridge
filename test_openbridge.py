# test_openbridge.py
"""
Tests for OpenBridge module.
"""

import unittest
from openbridge import OpenBridge

class TestOpenBridge(unittest.TestCase):
    """Test cases for OpenBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenBridge()
        self.assertIsInstance(instance, OpenBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
