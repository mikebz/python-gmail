import unittest
from credentials import get_credentials
from service import build_service
from messages import list_messages, list_message_with_labels

class TestCredentials(unittest.TestCase):

    def test_list_messages(self):
        """
        basic test to make sure we get some messages
        """
        creds = get_credentials()
        service = build_service(creds)
        messages = list_messages(service, 'me', 'submissions@formspree.io')
        self.assertIsNotNone(messages)
        self.assertTrue(messages)
    
    def test_messages_with_label(self):
        """
        test finding messages in Inbox
        """
        creds = get_credentials()
        service = build_service(creds)
        messages = list_message_with_labels(service, 'me', ['INBOX'])
        self.assertIsNotNone(messages)
        self.assertTrue(messages)
