from random import randint

def generate_phone_number():
    phone_number = ''
    for _ in range(10):
        phone_number += str(randint(0, 9))
    return phone_number

def generate_contacts(num_contacts):
    contacts = {}
    for i in range(1, num_contacts+1):
        contact_name = 'Contact_' + str(i)
        phone_number = generate_phone_number()
        contacts[contact_name] = phone_number
    return contacts


if __name__ == "__main__":
    num_contacts = 10
    contacts = generate_contacts(num_contacts)
    print(contacts)