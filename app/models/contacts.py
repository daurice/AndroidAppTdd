class Contacts:
    def __int__(self):
        self.contact = {}
        self.id = id

    def add_contact(self, number, name, address, email):
        self.contact[number] = name
        self.contact[number] = address
        self.contact[number] = email
        return{"message": "saved"}

    def remove_contact(self, contact):
        self.contact.pop(contact.name)
        self.contact.pop(contact.address)
        self.contact.pop(contact.email)
        self.contact.pop(contact.number)
        return {"message": "deleted"}






