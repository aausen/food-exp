"""Test suite for testing server."""

from flask import Flask
import server
import unittest
import crud
import model
from test_data import example_data



class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration tests: testing Flask server."""

    def setUp(self):
        print("(setUp ran)")
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                

        model.connect_to_db(server.app, "postgresql:///test_fooddb")

        model.User.query.delete()
        model.Food.query.delete()
        model.Location.query.delete()
        model.User_food.query.delete()

        model.db.create_all()
        example_data()

    def tearDown(self):
        print("(tearDown ran)")
        return 

    def test_homepage(self):
        with self.client:
            result = self.client.post('/login', data={
                'email': 'liz@test.com', 'password' : 'test'
            })
            
            self.assertEqual(302, result.status_code)


    def test_login_get(self):
        result = self.client.get('/login')
        self.assertIn(b'<h2>Log In</h2>', result.data)
        

    def test_register(self):
        result = self.client.get('/register')
        self.assertIn(b'<h1>Create an account</h1>', result.data)
       

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
    #     result = self.client.get('/profile', data={email : "test@test.test"})
    #     self.assertIn(b'<h2>This is your profile</h2>', result.data)
    #     print("*"*30)
    #     print("test_profile", result.data)
    #     print("*"*30)

if __name__ == '__main__':
    unittest.main()