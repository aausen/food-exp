"""Test suite for testing server."""

import server
import unittest

class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration tests: testing Flask server."""

    def setUp(self):
        print("(setUp ran)")
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def tearDown(self):
        print("(tearDown ran)")
        return 

if __name__ == '__main__':
    unittest.main()