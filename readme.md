# Python Client for GMail

This project is based on Google's walkthrough on how to use Python with GMail API.

For full documentation on how to use Python with GMail API look here:
https://developers.google.com/gmail/api/quickstart/python

## Setup
1. create virtual environment using these steps: https://docs.python.org/3/library/venv.html
1. activate it `$ source <venv>/bin/activate`
1. install the required libraries `pip3 install -r requirements.txt`
1. run the quickstart to get your credentials stored on the system (this will require a browser session) `python3 quickstart.py`


# the general algorithm for finding e-mails and classifying them
1. get a list of e-mails that fit the search criteria
1. get the headers such as "reply-to" to figure out where the reply would go
1. find in the body of the e-mail the part of the message we care about.
1. find the e-mail that was sent to that address, if it's nothing then this has not been responded to.
1. find the response.