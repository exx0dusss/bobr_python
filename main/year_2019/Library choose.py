import random

list_name = []
list_skill = []
print('Привет!')

n= input('Как много вас пришло?')
for i in range(int(n)):
    list_name.append(input('Как вас зовут?'))
j= input('Сколько программ вы изучаете?')
for i in range(int(j)):
    list_skill.append(input('Чем вы увлекаетесь?Buisness skills/soft skills/financial skills'))

#for i in range(len(list_name)):
#    for i in range(len(list_name)):
#        print(list_name[i], list_skill[random.randint (0,1)]) 
 

user_input = input("Правильно ли работает наша программа? Y yes/N no)")
if user_input == "no" or user_input == "N":
    print("Мы улучшим свои рекомендации,извините =) !")
else :
    user_input == 'yes' or 'Y'
    print("Большое спасибо!")
print('Спасибо что пришли!')    
