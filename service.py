"""
set of fucntionality to get the service for e-mail access
"""
import httplib2
from apiclient import discovery


def build_service(credentials):
    """
    given a set of credentials return a service.
    """
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    return service