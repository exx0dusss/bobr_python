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
            
    a_list = []
    
    for i in range(n):
        while True:
            try:
                el = int(input(f'Enter {i+1} element '))
                a_list.append(el)
            except ValueError as e:
                print("Enter the number!")
            else:
                break
    while True:
        try:
            a = int(input("1. Which element range do you want to remove? "))
            b = int(input("2. Which element range do you want to remove? "))
        except ValueError as e:
            print("Enter integer!")
            continue
        else:
            if b < a:
                print("Error")
                continue
            elif a > len(a_list) or b > len(a_list):
                print("Error")
                continue
            else:
                break
    

    for i in range(a, b+1):
        try:
            a_list.remove(i)
        except ValueError as e:
            continue


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

