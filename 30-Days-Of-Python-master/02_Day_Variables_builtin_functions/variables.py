
# Variables in Python
first_name = 'Nurudeen'
last_name = 'Adedeji'
country = 'United Kingdom'
city = 'London'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python','JavaScript']
person_info = {
    'firstname':'Nurudeen', 
    'lastname':'Adedeji', 
    'country':'United Kingdom',
    'city':'London'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
# print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Nurudeen', 'Adedeji', 'London', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)