
        
def main_menu():
    exit_main = False
    while not exit_main:
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
            print()
        elif choice_main == '2':
            print()
        elif choice_main == '3':
            print()
        elif choice_main == '4':
            print()
        elif choice_main == '5':
            print()
        elif choice_main == '6':
            print('\nGoodbye.')
            exit_main = True
        else:
            print('\nInvalid option, try again.')

# Run 
if __name__ == '__main__':
    main_menu()
    