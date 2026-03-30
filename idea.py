students = []
new_student = {}

def f():    
    id_student = input('ID: ')
    name = input('Student name: ')
    age = int(input('Age: '))
    program = input('Program: ')
    status = input('Is active?\n1. Yes --- 2. No\n>>> ').strip().lower()
    if status in ['yes', 'y', '1']:
        status = 'Active'
    elif status in ['no', 'n', '2']:
        status = 'Inactive'


    new_student = {'id':id_student,'Name':name,'Age':age,'Program':program,'Status':status}
            
    students.append(new_student) 

    print(f'\nAdded: {new_student['Name']}')
f()

# add
more = input('wanna add more? \n-- ')
if more in ['yes', 'y', '1']:
    f()
elif more in ['no', 'n', '2']:
    print('bye')        
print(students)

# Delete
n = input('Wanna delete someone? \n-- ')
if n in ['yes', 'y', '1']:
    x = input('which one?: ')
    if x == new_student['Name']:
        students.pop(x)
        print('deleted')
elif n in ['no', 'n', '2']:
    print('a')        

print(students)

# search
srch = input('name?: ')
for i in range (l):
    for j in range (k):
        if srch == new_student['Name']:
            print('Founded')
        else:
            print('Not found.')

# update