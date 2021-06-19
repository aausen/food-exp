"""Test suite for testing server."""

import server
import unittest
from flask_login import current_user
import crud

class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration tests: testing Flask server."""

    def setUp(self):
        print("(setUp ran)")
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def tearDown(self):
        print("(tearDown ran)")
        return 

    # def test_homepage(self):
    #     result = self.client.get('/')
    #     current_user.is_authenticated = True
    #     self.assertIn(b'<h2>Food list here</h2>', result.data)

    ## Throwing an error because I'm not sure how fake that a user is logged in

    def test_login_get(self):
        result = self.client.get('/login')
        self.assertIn(b'<h2>Log In</h2>', result.data)

    def test_register(self):
        result = self.client.get('/register')
        self.assertIn(b'<h2>Create an account</h2>', result.data)

    # def test_register_form(self):
    #     result = self.client.get('register', data={'email' : 'test@test.test', 'password' : 'test', 'pref_contact' : 'email'})

    # def test_search(self):
    #     result = self.client.get('/search')
    #     self.assertIn(b'<h1>Food search results</h1>', result.data)

    # def test_add_item(self):
    #     result = self.client.get('/add-item')
    #     self.assertIn(b'<p>Select a place to store your food</p>', result.data)

    ## Test_search and test_add_item are throwing errors because of the new_url. It says 
    ## the list index is out of range since it's not actually doing a get request

    # def test_profile(self):
    #     result = self.client.get('/profile')
    #     self.assertIn(b'<h2>This is your profile</h2>', result.data)

if __name__ == '__main__':
    unittest.main()