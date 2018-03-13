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

    def file_contact(self, name, email, responded, note):
        """
        method to file the contact record in Capsule API
        """
        party = self.create_party(name, email, responded)
        party_id = party['party']['id']
        self.create_note(party_id, note)
        return party
    
    def create_party(self, name, email, responded=False):
        """
        create a contact and return the contact ID
        """
        hn = HumanName(name)
        tags = [ {"name": "loader"}]
        if responded:
            tags.append({"name": "responded"})

        party = {
                "party": {
                    "type": "person",
                    "firstName": hn.first,
                    "lastName": hn.last,
                    "emailAddresses": [{
                        "type": "Home",
                        "address": email
                    }],
                    "tags": tags,
                }
            }
        url = "https://api.capsulecrm.com/api/v2/parties"
        r = requests.post(url, headers=self._headers(), json=party)
        if not r.status_code == requests.codes.ok:
            r.raise_for_status()        
        result = r.json()
        return result

    def create_note(self, id, note):
        """
        create a note and attach it to a party.
        manual is here: https://developer.capsulecrm.com/v2/operations/Entries#createEntry
        """
        url = "https://api.capsulecrm.com/api/v2/entries"
        entry = {
                "entry" : {
                    "party" : {
                        "id" : id
                    },
                    "type" : "note",
                    "content" : note
                }
            }
        r = requests.post(url, headers=self._headers(), json=entry)
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
