
def my_func(datatype):
    sentence1 = str(datatype[1]).strip('[]')
    sentence2 = str(datatype[2]).strip('[]')
    sentence3 = str(datatype[3]).strip('[]')
    global immutable_list
    immutable_list = []
    global mutable_list
    mutable_list = []
    
    if datatype[0] is list or datatype[0] is set or datatype[0] is dict:
        mutable_list.append(datatype[0])
    else:
        immutable_list.append(datatype[0])
    if sentence1 is list or sentence1 is set or sentence1 is dict:
        mutable_list.append(sentence1)
    else:
        immutable_list.append(sentence1)
    if sentence2 is list or sentence2 is set or sentence2 is dict:
        mutable_list.append(sentence2)
    else:
        immutable_list.append(sentence2)
    if sentence3 is list or sentence3 is set or sentence3 is dict:
        mutable_list.append(sentence3)
    else:
        immutable_list.append(sentence3)
      
this_list = [['This','is','List'],[1,2,3], [set('hello')], [{"Age":15, "Name":"Peter"}]]
my_func(this_list)
print(mutable_list)
print(immutable_list)

        