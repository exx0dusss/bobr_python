import faker
import os
file = 'data.txt'
faker = faker.Faker('en_US')

print(os.getcwd())
while True:
    try:
        dirct = input('Enter your directory to save the file in ')
        os.chdir(dirct)
        break
    except FileNotFoundError as e:
        print('Try again!')
def fakedata():
    counter = int(input("Enter the number of contacts you want to get "))
    n = 0
    with open(file, 'w', encoding='utf-8') as my_file:
        my_file.write('')
    while True:
        n = n + 1
        aa = faker.name()
        bb = faker.date()
        cc = faker.phone_number()
        with open(file, 'a', encoding='utf-8') as my_file:
            my_file.write(f'\nName: {aa}; Date: {bb}; Phone: {cc}')
        if n == counter:
            break
    print("")
    print("Your data contains in the directory with the way: {dirct} ")
fakedata()







