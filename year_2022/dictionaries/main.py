print("\n           Laba 5          \n")
print("\            n#2\            n")
print("\n#2.1\n")
import random

my_dict = {}

brand_list = ["hator", "razer", "bloody", "hyperx", "logitech",
 "cougar", "asus", "corsair", "nzxt", "xp-pen"]

goods_list = ["mouse", "keyboard", "mousepad", "headset",
 "bungee", "keycaps", "graphic tablet"]

item_list = [] #0 Item name
quantity_list = [] #1 Expected quantity
produced_quantity_list = [] #2 Produced quantity
price_list = [] #3 Price for one
total_price_list = [] #4 Price for all
total_produced_price_list = [] #5 Price for all produced
lost_revenue_list = [] #6 Lost revenue
lost_revenue_quantity_list = [] #7 Quantity of lost revenue items
for i in range(10):
    brand = brand_list[random.randint(0, len(brand_list))-1]
    good = goods_list[random.randint(0, len(goods_list))-1]
    item_q = random.randint(0, 500)
    while True:
        item_r_q = random.randint(0, 500)
        if item_r_q > item_q:
            continue
        else:
            break
    item_r_value = random.randint(500, 5000)
    my_dict.setdefault(i+1 ,[brand + " " + good, item_q, item_r_q, item_r_value])


for key, value in my_dict.items():
    print(f'{key}: {value} uah')

print("\n#2.2\n")
tax = 20/100

for i in my_dict.values():
    item_whole_price = i[1] * i[3]
    item_r_whole_price = i[2] * i[3]
    lost_revenue = item_whole_price - item_r_whole_price
    i.append(item_whole_price)
    i.append(item_r_whole_price)
    i.append(lost_revenue)

print(my_dict)
print("\n#2.3\n")
for i in my_dict.values():
    item_list.append(i[0])
    quantity_list.append(i[1])
    produced_quantity_list.append(i[2])
    price_list.append(i[3])
    total_price_list.append(i[4])
    total_produced_price_list.append(i[5])
    lost_revenue_list.append(i[6])
    lost_revenue_quantity_list.append(i[1]-i[2])


max_produced_quantity = max(produced_quantity_list)
#print(max_produced)
max_produced_quantity_index = produced_quantity_list.index(max_produced_quantity)
#print(max_produced_index)
key_max_produced_quantity = my_dict[max_produced_quantity_index+1]

print("\n#2.4\n")
min_produced_quantity = min(produced_quantity_list)
#print(min_produced)
min_produced_quantity_index = produced_quantity_list.index(min_produced_quantity)
#print(min_produced_index)
key_min_produced_quantity = my_dict[min_produced_quantity_index+1]

print("\n#2.5\n")

max_income = max(total_produced_price_list)
#print(max_income)
max_income_index = total_produced_price_list.index(max_income)
#print(max_income_index)
key_list_income_max = my_dict[max_income_index+1]

print("\n#2.6\n")
min_income = min(total_produced_price_list)
#print(min_income)
min_income_index = total_produced_price_list.index(min_income)
#print(min_income_index)
key_list_income_min = my_dict[min_income_index+1]

print(f'The lowest quantity of produced items: {key_min_produced_quantity[0]}, {min_produced_quantity} units')
print(f'The biggest quantity of produced items: {key_max_produced_quantity[0]}, {max_produced_quantity} units')
print(f'The biggest amount of income: {key_list_income_max[0]}, {max_income} uah')
print(f'The lowest amount of income: {key_list_income_min[0]}, {min_income} uah')

print("\n#2.7\n")
for key, value in my_dict.items():
    print(f'\n\
    #{key}:\n\
    Name: {value[0]}\n\
    Total produced price: {value[5]}')

print("\n#2.8\n")
print(f'Total produced sum: {sum(total_produced_price_list)} uah\n\
Total produced quantity: {sum(produced_quantity_list)}')

print("\n#2.9\n")
print(f'Total lost revenue: {sum(lost_revenue_list)} uah\n\
Total unproduced quantity: {sum(lost_revenue_quantity_list)}')
print("\n#2.10\n")
print(f'Total produced: {sum(produced_quantity_list)  * 100//sum(quantity_list)}%')
print(f'Total produced price: {sum(total_produced_price_list)  * 100//sum(total_price_list)}%')
print("\n       Dictionary     \n")
for key, value in my_dict.items():
    print(f'{key}:\n\
        Name: {value[0]}\n\
        Quantity: {value[1]}\n\
        Produced quantity: {value[2]}\n\
        Price for one: {value[3]} uah\n\
        Total price: {value[4]} uah\n\
        Total produced price: {value[5]} uah\n\
        Lost revenue: {value[6]} uah')
