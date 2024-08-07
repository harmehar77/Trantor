contact_book = {}
def add_contact(dict):
    num = int(input("Enter the number of contacts you want to add: "))
    
    for i in range(0,num):
        key = str(input("Enter the name of contact: "))
        value = int(input("Enter the phone number of contact: "))    
        contact_book[key]=value
    print(f"Contact Book after adding user input: {contact_book}")
        
'''def print_contacts(file):
    in_file = open(file,'r')
    print(f"The contacts in file are:\n{in_file.read()}")'''
    
def search_contacts(dict):
    name = str(input("Enter the name of contact you want to search: "))
    if name in contact_book:
        print("Given name exists in the file.")
        print(f"Phone number of {name} is {contact_book[name]}")
    else:
        print("Given name does not exist in the file.")
        print(f"{contact_book}\n")

def delete_contact(dict):
    delete_name = str(input("Enter the name of contact you want to delete: "))

    for delete_name in contact_book:
        for delete_name in contact_book.items():
            if delete_name==contact_book.keys():
                del contact_book[delete_name]
        else:
            print("Entered contact is not in contact list.")
    print(f"{contact_book}")
     
add_contact(contact_book)
search_contacts(contact_book)
delete_contact(contact_book)

in_file = open('contacts.txt','r')
print(f"The contacts file is {len(in_file.read())} bytes long.")
in_file.close()

with open('contacts.txt','a') as data:
            data.write(str(contact_book))
            data.close()
print("Contact Book has been updated in .txt file.")