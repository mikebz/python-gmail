"""Get a list of Messages from the user's mailbox.
"""

import email
import pprint
import base64
from apiclient import errors


def list_messages(service, user_id, query=''):
    """List all Messages of the user's mailbox matching the query.
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
    """
    response = service.users().messages().list(userId=user_id,
                                                q=query).execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id, q=query,
                                            pageToken=page_token).execute()
        messages.extend(response['messages'])

    return messages


def list_message_with_labels(service, user_id, label_ids=[]):
    """List all Messages of the user's mailbox with label_ids applied.
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

    Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
    """
    response = service.users().messages().list(userId=user_id,
                                                labelIds=label_ids).execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id,
                                                    labelIds=label_ids,
                                                    pageToken=page_token).execute()
        messages.extend(response['messages'])

    return messages

def download_message(service, user_id, message_id ):
    """Get a Message with given ID.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

    Returns:
    A Message.
    """
    message = service.users().messages().get(userId=user_id, id=message_id).execute()
    return message


def download_mime_message(service, user_id, message_id):
    """Get a Message and use it to create a MIME Message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

    Returns:
    A MIME Message, consisting of data from Message.
    """
    message = service.users().messages().get(userId=user_id, id=message_id,
                                             format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw']).decode('ASCII')
    mime_msg = email.message_from_string(msg_str)
    return mime_msg


def get_message_html(mime_message):
    """
    Given a mime message extract the HTML content of it
    """
    if not mime_message.is_multipart():
        return None

    html = None
    for part in mime_message.get_payload():
        if part.get_content_charset() is None:
            continue

        #charset = part.get_content_charset()
        if part.get_content_type() == 'text/html':
            html = part.get_payload(decode=True)

    return html