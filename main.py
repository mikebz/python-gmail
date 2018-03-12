import argparse
import pprint
from oauth2client import tools
from credentials import get_credentials
from service import build_service
from messages import download_mime_message, list_messages, get_message_html
from html_parsing import get_message_content

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()


def main():
    """
    GMail API retrieval
    """
    credentials = get_credentials(flags)
    service = build_service(credentials)

    messages = list_messages(service, 'me', 'from:submissions@formspree.io')
    if not messages:
        print("No messages, exiting")
        return
    
    for message in messages: 
        message_id = message['id']
        mime_message = download_mime_message(service, 'me', message_id)

        reply_header = mime_message.get('Reply-To')
        # if this is a message that was not well formed we might as well skip it.
        # from formspree the well formed messages have a Reply-To header.
        if not reply_header:
            continue

        html = get_message_html(mime_message)
        content = get_message_content(html)
        pprint.pprint(content)
        

if __name__ == '__main__':
    main()