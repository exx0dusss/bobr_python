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
        el = input(f'Enter {i+1} element ')
        a_list.append(el)

    b_list = a_list.copy()
    b_list.pop(0)
    print(f'a_list = {a_list}')
    print(f'b_list = {b_list}')
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

