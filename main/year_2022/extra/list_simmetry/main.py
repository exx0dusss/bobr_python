
while True:
    while True:
        try:
            n = int(input("How many elements should your list have? "))
        except ValueError as e:
            print("Enter the number!")
        else:
            break

    a_list = []
    a1_list = []
    a2_list = []
    
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

    for i in range(len(a_list)):
        if a_list[i] <= n//2:
            a1_list.append(a_list[i])
        elif a_list[i] > n//2:
            a2_list.append(a_list[i])
        
    if n%2 != 0:
        a1_list.append(a_list[n//2])
        

    print(f'List: {a_list}')
    print(f'Left simmetry list: {a1_list + list(reversed(a1_list))}')
    print(f'Right simmetry list: {a2_list + list(reversed(a2_list))}')

    

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
