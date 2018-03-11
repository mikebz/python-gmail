
from __future__ import print_function
import argparse

from oauth2client import tools
from credentials import get_credentials
from messages import list_messages
from service import build_service

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

def main():
    """
    GMail API retrieval
    """
    credentials = get_credentials(flags)
    service = build_service(credentials)

    messages = list_messages(service, 'me', 'submissions@formspree.io')
    if not messages:
        print('No messages')
    else:
        print('Messages:')
        for msg in messages:
            print(msg)

if __name__ == '__main__':
    main()