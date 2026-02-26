# test_neuralnetboost.py
"""
Tests for NeuralNetBoost module.
"""

import unittest
from neuralnetboost import NeuralNetBoost

class TestNeuralNetBoost(unittest.TestCase):
    """Test cases for NeuralNetBoost class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralNetBoost()
        self.assertIsInstance(instance, NeuralNetBoost)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralNetBoost()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
