import unittest

from app.models.contacts import Contacts


class ContactTestCase(unittest.TestCase):

    def test_add_contact(self):
        contacts = Contacts()
        resp = contacts.add_contact("doris", "0734672489", "loak", "doris@hsj.com")
        print("checking response" + resp)
        self.assertEqual(resp["message"], "saved")

    def test_remove_contact(self):
        self.assertEqual(1, len(self.contacts.contact))
        self.contacts.remove_contacts(self.contact)
        self.assertEqual(0, len(self.contacts.contact))

    def test_update_contact(self, contact):
        self.contacts.update({contact.id: contact})















if __name__== '__main__':
    unittest.main()







