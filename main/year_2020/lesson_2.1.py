import random
def parser(sentence, pattern):
    list_log = sentence.split(" ")
    if pattern is '1':
        list_log_end = list_log[1:]
        print(f"ID: {str(random.randint(999,1000))} {''.join(list_log_end)}")
    elif pattern is '2':
        list_log_end = list_log[0]
        print(f"ID: {str(random.randint(999,1000))} {''.join(list_log_end)}")
    else:
        print("Given information was uncorrect, please try again.")
        
while True:
    print("Welcome to Parser")
    s = input("Type your string,please ")
    p = input("Choose pattern 1/2/3 ")
    parser(s,p)
    go = input("Would you like to try again?('-' if not) ")
    if go  is "-":
        break
        