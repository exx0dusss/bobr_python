import time

###########GENERATOR###########
#1. Generate Integers
#2. Generate String
# i => Integers(3000000 = > 10 000 000)
#
#sf => Strings(Names Females)
#sm => Strings(Names Males)





male_dict = {'male':'Noah','male1':'Oliver','male2':'William','male3':'Elijah','male4':'James','male5':'Benjamin'}             
female_dict = {'female':'Isabella','female1':'Sophia','female2':'Ava','female3':'Emma','female4':'Olivia'}


print("Welcome to the generator,\nit can generate different numbers or names")
time.sleep(1)
print()
user_input = int(input("What would you like to generate\nnumbers or names?(1/2)"))
if user_input == 1:
    def num_gen():
        num = 0
        while True:
            yield num
            num += 1
    gen = num_gen()
    print(next(gen))
    
        
elif user_input == 2:
    user2_input = input('Male or Female names?(1/2)')
    if user2_input == 1:
        def male_gen():
            for key,value in male_dict:
                yield print(key,value)
        mgen = male_gen()
        print(next(mgen))
    elif user2_input == 2:
        def female_gen():
            for key1,value1 in female_dict:
                yield (key1,value1)
                print(key1, value1)
        fgen = female_gen()
        print(next(fgen))
        
        
        
        
    
