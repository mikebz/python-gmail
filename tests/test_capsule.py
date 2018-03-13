import unittest
from capsule import CapsuleAPI
from secrets import CAPSULE_TOKEN

# a few test data items that might change if you
# port this code to your account
TEST_PARTY_ID = 163763459


class TestCapsule(unittest.TestCase):
    """
    a set of tests for Capsule interface
    """

    def test_simple_read(self):
        """
        a simple test to read a contact
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.get_party(TEST_PARTY_ID)
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

    def test_create_party(self):
        """
        a simple test 
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.create_party("Tester Testerov", "mikebz@outlook.com")
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

        party_id = party['party']['id']
        capsule.delete_party(party_id)