import operator
my_fruit_list = [
    {'type': 'banana', 'color': 'yellow', 'country': 'Zimbabwe', 'price': 32, 'taste': 'sweat', 'scores': 0},
    {'type': 'apple', 'color': 'red', 'country': 'Ukraine', 'price': 24, 'taste': 'sour', 'scores': 0},
    {'type': 'mango', 'color': 'green', 'country': 'Spain', 'price': 300, 'taste': 'sweat', 'scores': 0},
    {'type': 'grape', 'color': 'purple', 'country': 'France', 'price': 50, 'taste': 'sour', 'scores': 0},
    ]

my_options = ['red', 'Ukraine', 50]

def guess_the_fruit(my_fruit_list, my_options):
    my_fruit_list_final = []
    for fruit in my_fruit_list:
        print(f"Fruit to analyze is {fruit['type']}")
        
        for option in my_options:
            if option in fruit.values():
                fruit['scores'] += 25
        
    for fruit in my_fruit_list:
        all_values = fruit.values()
        max_value = max(all_values)
        print(max_value)
            
    print(f"Final List: {my_fruit_list_final}")

guess_the_fruit(my_fruit_list, my_options)