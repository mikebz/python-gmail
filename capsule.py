"""
Helper functionality working with Capsule API.
"""
import requests
import pprint
from nameparser import HumanName

class CapsuleAPI:
    """
    a simple utility class for dealing with Capsule API
    """

    def __init__(self, token):
        """
        class constructor
        for now we are just taking in the authorization token
        """
        self._token = token

    def _headers(self):
        """
        a private function for header generations
        """
        headers = {'Authorization': f"Bearer {self._token}"}
        return headers

    def file_contact(self, name, email, replied, note):
        """
        method to file the contact record in Capsule API
        """
        pass
    
    def create_party(self, name, email):
        """
        create a contact and return the contact ID
        """
        hn = HumanName(name)
        party = {
                "party": {
                    "type": "person",
                    "firstName": hn.first,
                    "lastName": hn.last,
                    "emailAddresses": [{
                        "type": "Home",
                        "address": email
                    }],
                    "tags": [ {"name": "loader"}],
                }
            }
        url = "https://api.capsulecrm.com/api/v2/parties"
        r = requests.post(url, headers=self._headers(), json=party)
        if not r.status_code == requests.codes.ok:
            r.raise_for_status()        
        result = r.json()
        return result


    def delete_party(self, id):
        """
        a way to delete a party, mostly used in tests.
        """
        url = f"https://api.capsulecrm.com/api/v2/parties/{id}"
        r = requests.delete(url, headers=self._headers())
        if not r.status_code == requests.codes.ok:
            r.raise_for_status()

    def get_party(self, id):
        """
        get the party based on ID
        """
        url = f"https://api.capsulecrm.com/api/v2/parties/{id}"
        r = requests.get(url, headers=self._headers())
        if not r.status_code == requests.codes.ok:
            r.raise_for_status()
        result = r.json()
        return result
