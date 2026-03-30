
# Dictionary where data will be saved.
students = []

def student_id():
    while True:
        id_student = input('ID: ')
        if len(id_student) != 10:
            print('\nInvalid document, try again.')
            continue
        else:
            print('ID added successfully.')
            return id_student

def student_name():
    
    while True:
        name = input('Student name: ')
        print('\nWanna correct the name?')
        typo = input('1. Yes --- 2. No\n>>> ').strip().lower()
        if typo in ['yes', 'y', '1']:
            continue
        elif typo in ['no', 'n', '2']:
            print('Name registered.')
            return name
        else:
            print('\nPlease enter yes/no or 1/2.\n')
        return name
    
def student_age():
    while True:
        age = int(input('Age: '))
        if age <= 0:
            print('Invalid value, try again.')
        else:
            print('Age saved.')
            return age

    
def student_program():
    
    while True:
        program = input('Program: ')
        print('\nWanna correct the name?')
        typo = input('1. Yes --- 2. No\n>>> ').strip().lower()
        if typo in ['yes', 'y', '1']:
            continue
        elif typo in ['no', 'n', '2']:
            print('Program registered.')
            return program
        else:
            print('\nPlease enter yes/no or 1/2.\n')

def student_status():

    status = input('Is active?\n1. Yes --- 2. No\n>>> ').strip().lower()
    if status in ['yes', 'y', '1']:
        status = 'Active'
        print('Status set to <Active>')
        
    elif status in ['no', 'n', '2']:    
        status = 'Inactive'
        print('Status set to <Inactive>')
        
    else:
        status = 'Inactive'
        print('\nInvalid option, selected <Inactive> by default.\n')
    
    return status

def add_new():
    add_more = False
    while not add_more:
        print('--< Adding new Student >--')
        id_new = student_id()
        name_new = student_name()
        age_new = student_age()
        program_new = student_program()
        status_new = student_status()        
        new_student = {'id':id_new,'Name':name_new,'Age':age_new,'Program':program_new,'Status':status_new}
        
        students.append(new_student) 
        
        print(f'\nAdded: {new_student['Name']}')

        cont = input('Wanna add more? \n>> ')
        if cont in ['yes', 'y', '1']:
            print('\n---<>---\n')
        elif cont in ['no', 'n', '2']:
            print('Retuning...\n')
            add_more = True  

add_new()
