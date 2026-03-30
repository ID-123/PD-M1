import os

# Dictionary where data will be saved.
students = []

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_student():

    clear_screen()
    keep_add = False
    print('--< Adding new Students >--')    
    while not keep_add:
            
        id_student = input('ID: ')
        if len(id_student) > 10  or len(id_student) < 9:
            print('\nInvalid document, try again.')
            continue
        else:
            print('ID added successfully.')
            
        name = input('\nStudent name: ')
        typo = input('Wanna correct the name?\n1. Yes --- 2. No\n>>> ').strip().lower()
        if typo in ['yes', 'y', '1']:
            continue
        elif typo in ['no', 'n', '2']:
            print('Name registered.')       
        
        try:
            age = int(input('Age: '))
            break
        except ValueError:
            print('\nInvalid value, try again.')

        status = input('Is active?\n1. Yes --- 2. No\n>>> ').strip().lower()
        if status in ['yes', 'y', '1']:
            status = 'Active'
        elif status in ['no', 'n', '2']:
            status = 'Inactive'
        
        program = input('Program: ')
                
        new_student = {'id':id_student,'Name':name,'Age':age,'Program':program,'Status':status}
        students.append(new_student)

        while True:
            add_more = input('\nAdd another product?\n1. Yes --- 2. No\n>>> ').strip().lower()
            if add_more in ['yes', 'y', '1']:
                break
            elif add_more in ['no', 'n', '2']:
                keep_add = True
                break
            else:
                print('\nPlease enter yes/no or 1/2.\n')          
        
    
    clear_screen()
    return students

add_student()