
from __future__ import print_function
import httplib2
import argparse

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from credentials import get_credentials
from messages import list_messages

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

def main():
    """
    GMail API retrieval
    """
    credentials = get_credentials(flags)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    messages = list_messages(service, 'me', 'submissions@formspree.io')
    if not messages:
        print('No messages')
    else:
        print('Messages:')
        for msg in messages:
            print(msg)

if __name__ == '__main__':
    main()