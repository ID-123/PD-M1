# Dicctionary where all students will be saved.
main_dic = []

# Checks if value is int, if not send error and repeats.
def getInt():
    try:
        return int(input('> '))
    except ValueError:
        print('Invalid value, try again.')
        return getInt()

# Asks status and return Active/Inactive.
def getStatus():
    status = input('Is active?\n1. Yes --- 2. No\n>  ').strip().lower()
    if status in ['yes', '1']:
        status = 'active'
        print('Status set to <Active>')
        
    elif status in ['no', '2']:    
        status = 'inactive'
        print('Status set to <Inactive>')
        
    else:
        status = 'inactive'
        print('\nInvalid option, selected <Inactive> by default.\n')
    return status

# Asks for student data and creates a list.
def addStudent():
    print('ID: ')
    id_student = getInt()
    name = input('Name: ')
    print('Age: ')
    age = getInt()
    program = input('Program: ')
    status = getStatus()

    student = {'id':id_student,'name':name,'age':age,'program':program,'status':status}
    main_dic.append(student)
    print(f'Added: {student["name"]}')

# Show every student registered.
def showList():
    if len(main_dic) == 0:
        print('List is empty.') 
    else:
        for student in main_dic:
            print(student)

# Asks for ID and search if exists.
def searchStudent():
    found = False
    print('Student ID: ')
    search_id = getInt()
    
    for student in main_dic:
        if search_id == student['id']:
            print(f'ID:{student['id']} | Name:{student['name']} | Age:{student['age']} | Program:{student['program']} | Status:{student['status']}')
            found = True
    if not found:
        print('Not registered yet.')

# Asks for ID, then select a value to change and updates it.
def updateStudent():
    found = False
    print('Student ID: ')
    search_id = getInt()
    for update in main_dic:
        if search_id == update['id']:
            found = True
            updateSelect = input('Which value?\n1. ID --- 2. Name\n3. Age --- 4. Program\n5. Status\n>> ')
            if updateSelect == '1':
                print('New ID:')
                new_id = getInt()
                update['id'] = new_id
                print('Updated.')
            elif updateSelect == '2':
                new_name = (input('New Name: '))
                update['name'] = new_name
                print('Updated.')
            elif updateSelect == '3':
                print('New age:')
                new_age = getInt()
                update['age'] = new_age
                print('Updated.')
            elif updateSelect == '4':
                new_program = (input('New Program: '))
                update['program'] = new_program
                print('Updated.')
            elif updateSelect == '5':
                if update['status'] == 'active':
                    update['status'] = 'inactive'
                    print('Status changed to <Inactive>')
                elif update['status'] == 'inactive':
                    update['status'] = 'active'
                    print('Status changed to <Active>')
            
    if not found:
        print('ID not found, try again.')

# Asks for ID, then deletes log if found.
def deleteStudent():
    found = False
    print('Student ID: ')
    search_id = getInt()
    for delete in main_dic:
        if search_id == delete['id']:
            main_dic.remove(delete)
            found = True
            print('Deleted successfully.')
    if not found:
        print('Invalid ID, try again.')

# Shows main options.
def main_menu():
    print('''
        --< Students Management System >--
        
        1. Add new Student
        2. Show registered
        3. Search Student
        4. Update student data
        5. Remove Student
        6. Exit
        ''')
    choice_main = input('Choose an option: ')
    
    if choice_main == '1':
        addStudent()
    elif choice_main == '2':
        showList()
    elif choice_main == '3':
        searchStudent()
    elif choice_main == '4':
        updateStudent()
    elif choice_main == '5':
        deleteStudent()
    elif choice_main == '6':
        print('\nGoodbye.')
        return
    else:
        print('\nInvalid option, try again.')
    if choice_main != '6':
        main_menu()

# Runs the code.
main_menu() 
