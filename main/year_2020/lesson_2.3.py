def user_database(main_dict,key,values):
    if values != 0:
        main_dict[key] = values
    else:
        main_dict[key] = None
    print(main_dict)
my_dict = {}
my_list = ["Ann", "Alex", "Helen", "Danil"]
that_list = []
user_database(my_dict,1,my_list)
user_database(my_dict,1,that_list)