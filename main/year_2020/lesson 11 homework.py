from shutil import copyfile, os

folder = input('Type your disk name ')
folder_path = input('Type your folder path ')
folder_name = input('Type your folder name ')
full_path = os.path.join(folder, folder_path, folder_name)

os.makedirs(full_path, exist_ok=False)
os.chdir(full_path)
print(os.getcwd())

f = open('text.txt','w')
username = input("Type your username ")
source = (f"C:\\Users\\{username}\\Desktop\\text.txt")
target = (full_path + "\\" + "textcopy.txt")
try:
    copyfile(source, target)
except IOError as e:
    print(f"Unable to copy file: {e}" )