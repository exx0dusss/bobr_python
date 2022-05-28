from random import randint

import time
igrok1= input("Как вас зовут?")
igrok2= input("Как вас зовут?")

while True:
    print("Подбросьте монетку", igrok1)   
    igrok1=randint(1,2)
    print("Выпало ",igrok1)   
    print("Подбросьте монетку", igrok2)    
    igrok2=randint(1,2)
    print("Выпало",igrok2)
    if igrok1>igrok2:
        print("Поздравляю с победой" + " " + "igrok1")       
        print(" ")        
    elif igrok1<igrok2:
        print("Поздравляю с победой" + " " + "igrok2")
        print(" ")        
    else:
        print('Каждому по доллару,ничья!' )
    user_input = input("wanna play again? (Y/N)")
    if user_input == "no" or user_input == "N":
        print("Goodbye !")
        break
    else :
        user_input == 'yes' or 'Y'
        print("continue")





    
    
