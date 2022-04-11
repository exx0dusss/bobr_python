
while True:
    while True:
        n = int(input("Enter the number quantity "))
        if n%2 == 0:
            break
        elif n%2 != 0:
            print("Enter valid number!")
        else:
            print("Enter valid NUMBER!")
       
    numb_list = []
    numb_list = list(range(1, n+1))
    print(numb_list)

    noncouple_list = []
    couple_list = []

    for i in numb_list:
        if i%2 != 0:
            noncouple_list.append(i)
        elif i%2 == 0:
            couple_list.append(i)

    print(noncouple_list)
    print(couple_list)


    final_list = []

    for i in range(len(couple_list)):
        final_list.append(couple_list[i])
        final_list.append(noncouple_list[i])

    print(final_list)
    
    question = input("Wanna continue? Yes/No ")
    if question == "No" or question == "-" or question == "n"\
       or question == "no":
        break
    elif question == "Yes" or question == "+" or question == "y"\
         or question == "yes":
        continue
    else:
        continue
        

    
        
