import unittest
import sys
import os

# Add the parent directory to the Python path to import the hello module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hello import say_hello


class TestSayHello(unittest.TestCase):
    """Test cases for the say_hello function"""

    def test_say_hello_with_name(self):
        """Test say_hello with a regular name"""
        result = say_hello("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_say_hello_with_empty_string(self):
        """Test say_hello with an empty string"""
        result = say_hello("")
        self.assertEqual(result, "Hello, !")

    def test_say_hello_with_special_characters(self):
        """Test say_hello with special characters in name"""
        result = say_hello("José")
        self.assertEqual(result, "Hello, José!")

    def test_say_hello_with_numbers(self):
        """Test say_hello with numbers in name"""
        result = say_hello("John123")
        self.assertEqual(result, "Hello, John123!")

    def test_say_hello_with_spaces(self):
        """Test say_hello with spaces in name"""
        result = say_hello("John Doe")
        self.assertEqual(result, "Hello, John Doe!")

    def test_say_hello_with_long_name(self):
        """Test say_hello with a very long name"""
        long_name = "A" * 100
        result = say_hello(long_name)
        self.assertEqual(result, f"Hello, {long_name}!")

    def test_say_hello_return_type(self):
        """Test that say_hello returns a string"""
        result = say_hello("Test")
        self.assertIsInstance(result, str)

    def test_say_hello_format(self):
        """Test that say_hello returns the correct format"""
        result = say_hello("World")
        self.assertTrue(result.startswith("Hello, "))
        self.assertTrue(result.endswith("!"))
        self.assertIn("World", result)


if __name__ == "__main__":
    unittest.main()
