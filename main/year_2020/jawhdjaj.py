'''
import os

my_dir = "D:\\Games"
json_list = [f for f in os.listdir(my_dir) if f.endswith('.json')]
os.chdir(my_dir)

for file in json_list:
    with open(file, 'r') as f_read:
        lines = f_read.readlines()
        
    with open(file, 'a') as f_write:
        for i in range(100):
            f_write.write('\n{str(i)} - {lines[0]}')
            
'''
'''
import collections
import random
gifts = ['4','3','2','1','5','7','6']
weights = [0.5, 0.8, 2,7 ,15 , 40, 70]
print(random.choices(gifts, weights=weights))
print(collections.Counter(list(random.choices(gifts, weights=weights, k = 100))))
'''

import faker
fake = faker.Faker('uk_UA')
for i in range(10):
    print(dir((fake.address())))
print(dir(Faker))