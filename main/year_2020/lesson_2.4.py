import time
def dictionaryy():
    my_dict = {"id": 20333435, 'Name': "Peter", "Position": "Student"}
    mandatory = [ "id", "Name","Position", "Age", "City"]
    for i in mandatory:
        print(f"Field {i} is {i in my_dict}")
    tt = time.sleep(1)
    for o in range(3):
        tt
        print("-               ")
    
    for el in mandatory:
        if bool(el in my_dict) is False:
            print(f"{el} is Missing")
            time.sleep(2)
            askel = (input(f"Type dictionary {el}  "))
            add = {el: askel}
            my_dict.update(add)
        else:
            None
    time.sleep(2)
    
    time.sleep(2)
    for o in range(3):
        tt
        print("-               ")
    print("Checking the data ")
    for o in range(3):
        tt
        print("-               ")
    for i in mandatory:
        print(f"Field {i} is {i in my_dict}")  
    for o in range(3):
        tt
        print("-               ")
    for key, value in my_dict.items():
        print(f'Key: {key}, Value: {value}')
        
        
dictionaryy()