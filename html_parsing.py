"""
a set of functionality for working with parsing 
the HTML content of messages
"""
from bs4 import BeautifulSoup

def get_message_content(body):
    """
    A function to grab the content of the message.
    will return a dictionary of email, name and note.

    This has a lot of assumptions about how 
    e-mails are laid out specifically from formspree
    """
    soup = BeautifulSoup(body, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        class_attr = table.attrs.get('class')
        # note that the class attribute returns a list.
        # given the particular attribute we are parsing
        # the main class is the first item we got
        if class_attr and ('form-items' in class_attr[0]):
            
            name_element = table.find('td', string='name')
            name_element = name_element.find_next_sibling('td')

            email_element = table.find('td', string='email')
            email_element = email_element.find_next_sibling('td')
            
            message_element = table.find('td', string='message')
            message_element = message_element.find_next_sibling('td')

            return {
                'name': name_element.get_text(),
                'email': email_element.get_text(),
                'note': message_element.get_text()
            }

    return None