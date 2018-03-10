import unittest
from credentials import get_credentials

class TestCredentials(unittest.TestCase):

    def test_get_creds(self):
        """
        Test the basic presence of creds.  This will be a good flag
        if tests start failing all over the place.
        """
        creds = get_credentials()
        self.assertIsNotNone(creds)