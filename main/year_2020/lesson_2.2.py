'''
dictionary = {"key ": 101,}
print(dictionary['key '])
'''

dictionary = {1: "key1",2:"key2",3:"key3"}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
'''
for key,value in dictionary.items():
    print(f'Key: {key},Value: {value}')

print(dictionary.pop(2))
del dictionary[1]
print(dictionary)
del dictionary
print(dictionary)
id(dictionary)
'''
'''
dictionary = {}
for i in range (1000):
    dictionary[i] = str(i) + "_python"
print(dictionary)
'''

