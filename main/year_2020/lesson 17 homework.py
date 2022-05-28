import os

def echecker():
    global folder
    folder = 'C:\\IT'
    assert(os.path.isdir(folder) ),'there is no such foler in that directory'
try:
    echecker()
except AssertionError as e:
    full_path = os.path.join(folder)
    os.makedirs(full_path, exist_ok=True)
    print(e)