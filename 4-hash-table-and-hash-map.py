# Hash Table and HashMap

# there are 2 ways to create dictionary
# 1. by {} brackets
# 2. by using dict() function

employees = {'Dave': '001', 'Ava': '002', 'Joe': '003'}

# print(employees)
# print(type(employees))

# newEmployees = dict()
# print(newEmployees)
# print(type(newEmployees))

newEmployees = dict(Arman='004',Arif='005')
# print(newEmployees)

# nested dictionary
emp_details={
    'Employee': {
        'Dave': {
            'Id': '001',
            'Salary': '2000',
            'Designation': 'Team Leader'
        },
        'Ava': {
            'Id': '002',
            'Salary': '1500',
            'Designation': 'Executive'
        }
    }
}
print(emp_details)

# Hash table operations
# * Accessing Items

# print(employees['Dave'])
# print(employees.keys())
# print(employees.values())
# print(employees.get('Ava'))

# for x in employees:
#     print(x)
#
# for x in employees.values():
#     print(x)

for x, y in employees.items():
    print(y, x)

# * updating entries in dict
employees['Dave'] = '007'
employees['Vicky'] = '008'

print(employees)


