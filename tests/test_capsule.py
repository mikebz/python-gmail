import unittest
from faker import Faker
from capsule import CapsuleAPI
from secrets import CAPSULE_TOKEN

# a few test data items that might change if you
# port this code to your account
TEST_PARTY_ID = 163763459
fake = Faker()

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
        a simple test to create a party and then delete it.
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.create_party("Tester Testerov", fake.email())
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

        party_id = party['party']['id']
        capsule.delete_party(party_id)

    def test_create_responded_party(self):
        """
        a simple test 
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.create_party("Tester Testerovich", fake.email(), True)
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

        party_id = party['party']['id']
        capsule.delete_party(party_id)

    def test_create_party_add_note(self):
        """
        a simple test to create a party and add a note.
        the test will delete the party at the end.
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.create_party("Tester Testerko", fake.email())
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

        party_id = party['party']['id']
        capsule.create_note(party_id, "Smokey Bear")

        capsule.delete_party(party_id)

    def test_file_contact(self):
        """
        a simple test to create a party and add a note.
        the test will delete the party at the end.
        """
        capsule = CapsuleAPI(CAPSULE_TOKEN)
        party = capsule.file_contact("Tester Testerson", fake.email(), True, "Snowflake")
        self.assertIsNotNone(party)
        self.assertIsNotNone(party['party'])
        self.assertIsNotNone(party['party']['id'])

        party_id = party['party']['id']
        capsule.create_note(party_id, "Smokey Bear")

        capsule.delete_party(party_id)
