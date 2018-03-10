
from __future__ import print_function
import httplib2
import argparse

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from credentials import get_credentials

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials(flags)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
      print('Labels:')
      for label in labels:
        print(label['name'])


if __name__ == '__main__':
    main()