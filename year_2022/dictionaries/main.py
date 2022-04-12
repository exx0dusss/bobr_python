'''
my_dict = {'aboba': "amogus"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
'''

#BEBRABOCHONOK
print("\n           Laba 5          \n")
print("\n#2\n")
import random
my_dict = {}
brand_list = ["hator", "razer", "bloody", "hyperx", "logitech",
 "cougar", "asus", "corsair", "nzxt", "xp-pen"]
goods_list = ["mouse", "keyboard", "mousepad", "headset",
 "bungee", "keycaps", "graphic tablet"]


for i in range(10):
    brand = brand_list[random.randint(0, len(brand_list))-1]
    good = goods_list[random.randint(0, len(goods_list))-1]
    item_q = random.randint(0, 500)
    while True:
        item_r_q = random.randint(0,500)
        if item_r_q > item_q:
            continue
        else:
            break
    item_r_value = random.randint(0,5000)
    my_dict.setdefault(i+1 ,[brand + " " + good, item_q, item_r_q, item_r_value])

for key, value in my_dict.items():
    print(f'{key}: {value} uah')

print("\n#2.1\n")
tax = 20/100

for i in my_dict.values():
    item_whole_price = i[1] * i[3]
    item_r_whole_price = i[2] * i[3]
    lost_revenue = item_whole_price - item_r_whole_price
    i.append(item_whole_price)
    i.append(item_r_whole_price)
    i.append(lost_revenue)

# Название товара
# Количество товара
# Количество сделанного товара
# цена за один
# общая стоимость ?????
# стоимость сделанного товара
# неполученная выручка
for key, value in my_dict.items():
    print(f'{key}:\n\
        Name: {value[0]}\n\
        Quantity: {value[1]}\n\
        Produced quantity: {value[2]}\n\
        Price for one: {value[3]}\n\
        Total price: {value[4]}\n\
        Total produced price: {value[5]}\n\
        Lost revenue: {value[6]}')

print("\n#2.3\n")
produced_list = []
for i in my_dict.values():
    produced_list.append(i[2])

print(produced_list)

max_produced = max(produced_list)
print(max_produced)
max_index = produced_list.index(max_produced)
print(max_index)
key_list_max = my_dict[max_index+1]

print("\n#2.4\n")
min_produced = min(produced_list)
print(min_produced)
min_index = produced_list.index(min_produced)
print(min_index)
key_list_min = my_dict[min_index+1]

print("\n#2.5\n")

print("\n#2.6\n")
print(f'The least quantity of produced items: {key_list_min[0]}, {min_produced} units')
print(f'The biggest quantity of produced items: {key_list_max[0]}, {max_produced} units')
