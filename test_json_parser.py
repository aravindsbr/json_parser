import unittest
import json 
from json_parser import json_data, extracting_values_from_json
from unittest.mock import patch

class JSONParserTest(unittest.TestCase):
    def test_extracting_values_from_json(self):
        """
        Unit test case to test the json_extract function
        """

        # expected
        expected = ['System', 'videoMode', 'windowMode', 'verticalSync', 
        'textureMode', 'anisotropy', 'multisample', 'supersample', 
        'rate', 'apply']

        # actual
        print("TESTING")
        actual = extracting_values_from_json(json_data, "identifier")

        # test
        self.assertIsNotNone(actual)
        self.assertEqual(actual, expected)
        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
