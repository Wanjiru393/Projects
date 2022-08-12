from run_test import *
#import contact class
from contact import Contact
#Functions to implement what we want
#Creation of contacts.
def create_contact(firstname,lastname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(firstname,lastname,phone,email)
    return new_contact

#save contact

def save_contact():
    '''
    Function to save contact
    '''
    contact.save_contact()

    #delete 

