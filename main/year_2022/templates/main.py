while True:

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
