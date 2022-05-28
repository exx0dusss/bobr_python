import random

ing_=['tomato', 'pum','chiken','meat','cucumber']
rec_=['boil','fry','cook','freeze']
cal_=['200g','400g','600g','100g','50g']
#ingr=[rec_ + rec_ +cal_ ]
print("Recipe of yammy")
print(40 * "-")
ing_to_recipe = []
num_ing = random.randint(1, len(ing_))

for _ in range(num_ing):
     raw_index = random.randint(0, len(ing_)-1)
     
     if ing_[raw_index] not in ing_to_recipe:
         ing_to_recipe.append(ing_[raw_index])
ing_ = input(" What ingridiends do you wanna use?")
cal_ = input(" What quantity do you wanna use?")
print(ing_ + (20 * " ") + cal_ )
print(40 * "-")
rec_ = input("How do you wanna cook it?")
print (rec_)
