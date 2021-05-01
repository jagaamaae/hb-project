"""Sample test suite for testing demo."""

import server
import unittest

from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        connect_to_db(app, "postgresql:///covid")


    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Welcome!", result.data)
    
    def test_logout(self):
        result = self.client.post("/logout", 
                                    follow_redirects=True)
        self.assertIn(b'Logget out', result.data)

    def test_get_email(self):
        result = self.client.get

    def test_login(self):
        """Test login page."""

        result = self.client.post("/login-info",
                                  data={"email": "user0@test.com", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Logged in", result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///covid")

        # Create tables and add sample data
        db.create_all()

    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_all_countries(self):
        """Test countries page."""

        result = self.client.get("/countries")
        self.assertIn(b"All countries", result.data)

    def country_details(self):

        result = self.client.get('/countries/<country>.json')
        self.assertIn(b"confirmed", result.data)


class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_important_page(self):
        """Test profile page."""

        result = self.client.get("/users/<email>")
        self.assertIn(b"logged in", result.data)


class FlaskTestsLoggedOut(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_important_page(self):
        """Test that user can't see logged in page when logged out."""

        result = self.client.post("/users/<email>", follow_redirects=True)
        self.assertNotIn(b"logged in", result.data)
        # self.assertIn(b"You must be logged in", result.data)


class FlaskTestsLogInLogOut(TestCase):  # Bonus example. Not in lecture.
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        """Test log in form.

        Unlike login test above, 'with' is necessary here in order to refer to session.
        """

        with self.client as c:
            result = c.post('/login',
                            data={'user_id': '1', 'password': 'test'},
                            follow_redirects=True
                            )
            self.assertEqual(session['user_id'], '1')
            self.assertIn(b"logged in", result.data)

    # def test_logout(self):
    #     """Test logout route."""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess['user_id'] = '1'

    #         result = self.client.get('/logout', follow_redirects=True)

    #         self.assertNotIn(b'user_id', session)
    #         self.assertIn(b'Logged out', result.data)

class MyAppIntegrationTestCase(unittest.TestCase):
    """testing Flask server."""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'Welcome', result.data)

    def test_create_account_form(self):
        client = server.app.test_client()
        result = client.post('/login-info', data={'password': 'test'})
        self.assertIn(b'test', result.data)


class MyAppIntegrationTestCase2(unittest.TestCase):
    """Examples of integration tests: testing Flask server."""

    def setUp(self):
        # print("(setUp ran)")
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def tearDown(self):
        # We don't need to do anything here; we could just
        # not define this method at all, but we have a stub
        # here as an example.
        # 
        return
        print("(tearDown ran)")


if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()
