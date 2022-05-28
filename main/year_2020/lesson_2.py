my_list = ["sad","aad","dsa","asd"]
print(dir(my_list))

list_from_log = "[Error] [23456] [MainKernel] Alarm001"
print(list_from_log.split(' '))
if "[Error]" in list_from_log:
    output_list = list_from_log[1:]
    print(output_list)
