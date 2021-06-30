# Sequential

print("hello world")
print("my name is Eko \n" * 10)

# If Else

is_login = True
if is_login:
    print('You`re login')
else:
    print('Please login first')

# more than 2 condition
is_authorized = False
if is_login and is_authorized:
    print('Meet two conditions')
elif is_login or is_authorized:
    print('Meet one of conditions \n')
else:
    print('Not meet any conditions')

# Looping
numbers = 5

for index in range(1, numbers):
    print(f'number {numbers} in  index {index}')

# List data type

# for add new data in list using append
foods = ['Burger', 'Egg', 'Fried Rice']
print(f'\n{foods}')
foods.append('Ketoprak')
print(f'foods after append {foods}')

# check length of data list
print(len(foods))

# Dict data type

math_score = {'eko': 90, 'budi': 80, 'toni': 30}

print('\nmath score :')
print(math_score['eko'])

response_data_drivers = {
    "created_at": '20-06-2021',
    "drivers": [
        {'name': 'Eko', 'distance': 100, 'rating': 5, 'is_available': True},
        {'name': 'Eki', 'distance': 10, 'rating': 1, 'is_available': True},
        {'name': 'Eka', 'distance': 1000, 'rating': 2, 'is_available': True},
        {'name': 'Eku', 'distance': 20, 'rating': 4.5, 'is_available': True},
        {'name': 'Eke', 'distance': 3000, 'rating': 5, 'is_available': True}
    ]
}

print('\ndata driver')
print(f"first driver data : {response_data_drivers['drivers'][0]}")
print(f"first driver data rating: {response_data_drivers['drivers'][0]['rating']}")
