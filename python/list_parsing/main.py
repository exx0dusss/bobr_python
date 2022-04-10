while True:
    while True:
        try:
            n = int(input("How many elements should your list have? "))
        except ValueError as e:
            print("Enter the integer!")
        else:
            if n < 0:
                print("The number should be positive!")
                continue
            else:
                break
    
    def extend():
        global el
        while True:
            try:
                el = input(f'Enter {i+1} element ')
                el = float(el)
            except ValueError as e:
                print("Enter the number!")
            else:
                break
    a_list = []
    b_list = []#pos
    c_list = []#neg
    for i in range(n):
        extend()
        a_list.append(el)
        if el > 0:
            b_list.append(el)
        elif el < 0:
            c_list.append(el)


            
    print(f'list A: {a_list}')
    print(f'list B: {b_list}')
    print(f'list C: {c_list}')
    print(f'list A sum is {sum(a_list)}')
    print(f'list B sum is {sum(b_list)}')
    print(f'list C sum is {sum(c_list)}')
    print(f'list A has {len(a_list)} element(s)')
    print(f'list B has {len(b_list)} element(s)')
    print(f'list C has {len(c_list)} element(s)')
    
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

