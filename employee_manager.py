import employee
import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employees.dat'

def main():
    
    emp = load_contacts()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(emp)
        elif choice == ADD:
            add(emp)
        elif choice == CHANGE:
            change(emp)
        elif choice == DELETE:
            delete(emp)

   
    save_contacts(emp)

def load_contacts():
    try:
       
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        emp_dict = pickle.load(input_file)

    
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        emp_dict = {}

    # Return the dictionary.
    return emp_dict


def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

def look_up(emp):
   
    ID_number = int(input('Enter an ID number: '))

    # Look it up in the dictionary.
    print(emp.get(ID_number, 'That employee was not found.'))


def add(emp):
    
    name = input('Name: ')
    ID_number = int(input('ID Number: '))
    dept = input('Department: ')
    job_title = input('Job Title: ')


    
    entry = employee.Employee(name, ID_number, dept, job_title)

   
    if name not in emp:
        emp[ID_number] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

# The change function changes an existing
# entry in the specified dictionary.
def change(emp):
    
    
    ID_number = int(input('ID Number: '))

    if ID_number in emp:
       
        name = input('Name: ')
        dept = input('Department: ')
        job_title = input('Job Title: ')
       
       
        entry = employee.Employee(name, ID_number, dept, job_title)

       
        emp[ID_number] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# specified dictionary.
def delete(emp):
   
    ID_number = int(input('Enter a ID Number: '))

  
    if ID_number in emp:
        del emp[ID_number]
        print('Entry deleted.')
    else:
        print('That employee is not found.')

# The save_contacts funtion pickles the specified
# object and saves it to the contacts file.
def save_contacts(emp):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(emp, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()

    

