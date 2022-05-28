from random import *

while True:
    while True:
        try:
            n = int(input("How many elements should your list have? "))
        except ValueError as e:
            print("Enter the number!")
        else:
            break

    a_list = []
    for i in range(n):
        while True:
            try:
                el = input(f'Enter {i+1} element ')
                el = float(el)
                a_list.append(el)
            except ValueError as e:
                print("Enter the number!")
            else:
                break


    print(a_list)

    a1_list = [0] * n
    for i in range(n):
        if i == (n-1):
            a1_list[0] = a_list[i]
        else:
            a1_list[i + 1] = a_list[i]
                   
    a_list = a1_list.copy()
    print(a_list)
            

    question = input("Wanna continue? Yes/No ")
    
    if question == "No" or question == "-" or question == "n"\
       or question == "no":
        print("Done")
        break
    elif question == "Yes" or question == "+" or question == "y"\
         or question == "yes":
        continue
    else:
        continue
