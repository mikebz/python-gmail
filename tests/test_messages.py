import unittest
from credentials import get_credentials
from service import build_service
from messages import list_messages, list_message_with_labels
from messages import download_message, download_mime_message

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self._creds = get_credentials()
        self._service = build_service(self._creds)


    def test_list_messages(self):
        """
        basic test to make sure we get some messages
        """
        messages = list_messages(self._service, 'me', 'submissions@formspree.io')
        self.assertIsNotNone(messages)
        self.assertTrue(messages)

    def test_messages_with_label(self):
        """
        test finding messages in Inbox
        """
        messages = list_message_with_labels(self._service, 'me', ['INBOX'])
        self.assertIsNotNone(messages)
        self.assertTrue(messages)

    def test_download_message(self):
        """
        test downloading a message,
        we are going to pick the first message in the inbox.
        """
        messages = list_message_with_labels(self._service, 'me', ['INBOX'])
        self.assertIsNotNone(messages)
        self.assertTrue(messages)

        message_id = messages[0]['id']
        message = download_message(self._service, 'me', message_id)
        self.assertIsNotNone(message)
        self.assertIsNotNone(message['snippet'])

    def test_download_mime_message(self):
        """
        test downloading a message,
        we are going to pick the first message in the inbox.
        """
        messages = list_messages(self._service, 'me', 'submissions@formspree.io')
        self.assertIsNotNone(messages)
        self.assertTrue(messages)

        message_id = messages[0]['id']
        message = download_mime_message(self._service, 'me', message_id)
        self.assertIsNotNone(message)
