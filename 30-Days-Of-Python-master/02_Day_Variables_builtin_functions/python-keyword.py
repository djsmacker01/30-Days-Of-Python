# Getting User input

# first_name = input('What is your first name?')
# age = input('How old are you?')

# print(first_name, age)
# Casting: converting one data type to another

# int to float
# num_int = 10
# # print('num_int:', num_int)
# num_float = float(num_int)
# print('num_float:', num_float)


# # float to int
# gravity = 9.81
# print('gravity:', int(gravity))

# # int to str
# num_int = 10
# num_string = str(num_int)
# print('num_string:', (num_string))

# str to int or float
# num_str = '19.8'
# print('num_float:', float(num_str))
# print('num_int:', int(num_str))


num_str = '10.6'
print('num_float:', float(num_str))      # Convert to float first
print('num_int:', int(float(num_str)))