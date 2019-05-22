#Namrata Sivakumar, nxs8168, 1001508168
#Python Homework 2, Question 2
#Python Version 3.7.x
import os


def add():
    ans='' 
    
    while ans!='n':

        print("Enter the following contact info:")
        name = input("Name: ")
        email = input("email: ")
        phone = input("phone: ")

        myfile = open('contact.txt','a')

        
        myfile.write(name + '\n')
        myfile.write(email + '\n')
        myfile.write(phone + '\n')
        
        
        myfile.close()
        ans = input('Do you want to add another record? \n y = yes, n = no: ')

def show():
    num = 1
    myfile = open('contact.txt', 'r')

    name = myfile.readline()

    while name!='':
        email = myfile.readline()
        phone = myfile.readline()

        name = name.rstrip('\n')

        print("Contact # ",num)
        num+=1
    
        print('\tName: ',name )
        print('\temail: ',email)
        print('\tPhone: ', phone)
        print('----------------\n')
        
        name = myfile.readline()




    myfile.close()
    

def search():
    found = False
    search = input('Enter a name to search for: ')

    myfile = open('contact.txt', 'r')
    name = myfile.readline()

    while name!='':

        email = myfile.readline()
        phone = myfile.readline()
        name = name.rstrip('\n')
        if name == search:

            print('Name: ', name)
            print('email: ', email)
            print('Phone: ', phone)
            found  = True

        name = myfile.readline()
        myfile.close()
        if not found:
            print('That item was not found in the file!, Try again')

def modify():
    found = False

    search = input('Enter a name to search for: ')
    new_email = input('Enter the new email: ')
    new_phone = input ('Enter the new phone: ')
    
    # Open the original file.
    myfile = open('contact.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    name = myfile.readline()
    while name != '':
        # Read the email field.
        email = myfile.readline()
        phone = myfile.readline()

        # Strip the \n from the description.
        name= name.rstrip('\n')

        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.
        if name == search:
            # Write the modified record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(new_email + '\n')
            temp_file.write(new_phone + '\n')
            
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')


        # Read the next description.
        name = myfile.readline()

    
    myfile.close()
    temp_file.close()

    
    os.remove('contact.txt')

    
    os.rename('temp.txt', 'contact.txt')

    
    if found==True:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')


def delete():
    found = False

    
    search = input('Which name do you want to delete? ')
    
    
    myfile = open('contact.txt', 'r')

   
    temp_file = open('temp.txt', 'w')

    
    name = myfile.readline()

   
    while name != '':
       
        email = myfile.readline()
        phone = myfile.readline()

       
        name = name.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if name != search:
            # Write the record to the temp file.
            temp_file.write(name + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next description.
        name = myfile.readline()

    
    myfile.close()
    temp_file.close()

    # Delete the original  file.
    os.remove('contact.txt')
    # Rename the temporary file.
    os.rename('temp.txt', 'contact.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')



def main():
    choice = 0


    while choice!=6:


        print("CHOICE MENU")
        print("1) Add a Contact")
        print("2) Show the list of contacts")
        print("3) Search for a name in the list")
        print("4) Modify a contact")
        print("5) Delete a contact form the list")
        print("6) Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            search()
        elif choice == 4:
            modify()
        elif choice == 5:
            delete()
        else:
            print("End of Program, Thanks!")

    

main()