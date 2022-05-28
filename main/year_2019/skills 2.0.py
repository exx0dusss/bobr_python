import random

list_name = []
list_skill = []
print('Привет!')

n= input('Как много вас пришло?')
for i in range(int(n)):
    list_name.append(input('Как вас зовут?'))
    list_skill = (input('Чем вы увлекаетесь?business skills/soft skills/financial skills'))
    if list_skill == "soft skills":
        print (40 * "=")
        print ("Не забудьте прокачать свои навыки по программе business skills и уделите немного времени financial skills")
        print (40 * "=")
    elif list_skill == "business skills":
        print (40 * "=")
        print("Не забудьте прокачать свои навыки по программе soft skills и уделите немного времени financial skills")
        print (40 * "=")
    elif list_skill == "financial skills":
        print (40 * "=")
        print("Не забудьте прокачать свои навыки по программе soft skills и уделите немного времени business skills")
        print (40 * "=")
        

print('Удачи в развитии ваших навыков!')
print (40 * "=")
