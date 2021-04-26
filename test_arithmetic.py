import crud
import unittest
import doctest


class AdderTestCase(unittest.TestCase):
    """Examples of unit tests: discrete code testing."""

    def test_crud(self):
        assert crud.get_users == 

    def test_crud(self):
        self.assertEqual(crud.get_users(2, 2), 4)


def load_tests(loader, tests, ignore):
    """Also run our doctests and file-based doctests.

    This function name, ``load_tests``, is required.
    """

    tests.addTests(doctest.DocTestSuite(crud))
    tests.addTests(doctest.DocFileSuite("tests.txt"))
    return tests


if __name__ == "__main__":
    # If called like a script, run our tests
    unittest.main()
