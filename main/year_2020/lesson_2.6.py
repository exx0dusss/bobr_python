'''
my_list = [1, 2 , 33 , 56, 78, 990]

a = [el for el in my_list if el > 33]
print(a)

a = []
b = []
c = []


for el in my_list:
    if el > 33:
        a.append(el)
    elif el < 33:
        b.append(el)
    elif el == 33:
        c.append(el)
print(a)
print(b)
print(c)
'''
  
my_fruit_list = [
    {'type': 'banana', 'color': 'yellow', 'country': 'Africa', 'price': 32, 'taste': 'sweat'},
    {'type': 'apple', 'color': 'red', 'country': 'Spain', 'price': 34, 'taste': 'sweat'},
    {'type': 'mango', 'color': 'green', 'country': 'Italy', 'price': 25, 'taste': 'sweat'},
    {'type': 'grape', 'color': 'purple', 'country': 'Ukraine', 'price': 67, 'taste': 'sweat'}
    ]
my_options = ['red', 'Ukraine', 50]
def guess_the_fruit(my_fruit_list, my_options):
    my_fruit_list_final = []
    for fruit in my_fruit_list:
        print(f"Fruit to analyze is {fruit['type']}")
        for option in my_options:
            if option in fruit.values():
                fruit['scores'] += 25
        if fruit['scores'] == 0:
            continue
        else:
            my_fruit_list_final.append(fruit)
        
    print(f"Final List: {my_fruit_list_final}")
    print(max(my_fruit_list_final))    
guess_the_fruit(my_fruit_list, my_options)



        
        
