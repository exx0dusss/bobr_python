# tab + spaces
# 79
#if width == 120 and y!= 30 or \
#   color == 'red' and y == 100
'''

func(list[1], {'some': 10})
dict['new_key'] = 100

l
o
'''
import os
'''
print(f'My Current Directory {os.getcwd()}')
print(f'Files in Directory: {os.listdir(".")}')
py_files_my = [] #only*py
for file in os.listdir("."):
    if os.path.isfile(file) and file.endswith('.py'):
        py_files_my.append(file)
    
    full_path_with_name = os.path.realpath(file)
    print(full_path_with_name)
    
    full_path = os.path.dirname(full_path_with_name)
    print(full_path)
    
os.chdir('c:\Windows')
print(f'New directory is: {os.getcwd()}')

my_current_dict = ['C:\\Windows','C:\\Program Files','C:\\Games']
for el in my_current_dict:
    print(f'My current directory is {el}')
#py_files = [f for f in os.listdir(".") if os.pathfile(f) and f.endswith('.py')]
print(f'py_file_my: {py_files_my}')
#print(f'py_file: {py_files}')
'''

#folder_creator
folder_name = "Maxim"
full_path = os.path.join('C:\\Games', folder_name)
os.makedirs(full_path, exist_ok=False)
os.chdir(full_path)
os.getcwd()

print(f'Current directory is {os.getcwd()}')

'''
os.chdir('C:\\Games')
filename = 'my.txt'
with open(filename, 'r') as my_file:
    for string in my_file:
        print(string)
with open(filename, 'a') as my_file:
    my_file.write('\n1000')
'''
