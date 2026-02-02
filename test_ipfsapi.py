# test_ipfsapi.py
"""
Tests for IPFSApi module.
"""

import unittest
from ipfsapi import IPFSApi

class TestIPFSApi(unittest.TestCase):
    """Test cases for IPFSApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IPFSApi()
        self.assertIsInstance(instance, IPFSApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IPFSApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
