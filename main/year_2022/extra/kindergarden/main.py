print("\n           Exercise 1              \n")
print("\n#1\n")
a = ("Slava Ukraine! ")
b = ("Heroyam Slava! ")
print(f'{a}\n{b}')

print("\n#2\n")
ab = a + b
print(ab)

print("\n#3\n")
word_list = ab.split()
print(word_list)
for i in range(len(word_list)):
    print(word_list[i])

print("\n#4\n")
for i in range(len(word_list)):
    print(f'    {word_list[i]}')

print("\n#5\n")
import time
abx3 = ab*3
print(abx3)


print("\n#6\n")
for i in range(len(word_list)):
    time.sleep(0.01)
    print(f'{word_list[i]}')

print("\n#7\n")
print(ab[::-1])
print("or")
print(' '.join(word_list[::-1]))

print("\n#8\n")
#print(' '.join(word_list1),"!")
#print("or")
word_list.append("!")
print(' '.join(word_list))

print("\n#9\n")
for i in range(len(word_list)):
    if word_list[i] == "Ukraine!":
        word_list.insert(i+1, "!")
print(' '.join(word_list))

print("\n#10\n")
print(f'Lenth: {len(word_list)} units')

print("\n#11\n")
print(ab.split('!'))

print("\n#12\n")
print(word_list[3], word_list[4], word_list[0], word_list[1])

print("\n#13\n")
if "Dnipro" in word_list: print('Yes')
else:
    print('No')

print("\n#14\n")
for i in range(len(ab)):
    if 'o' == ab[i]:
        print(f'{ab[i]} position: {i}')

print("\n#15\n")
ab_r = ab.swapcase()
print(ab_r)
print(ab_r.swapcase())

print("\n           Exercise 2              \n")
print("\n#1\n")
import random
import string
def generate_random_string(length):
    letters = string.digits
    global rand_string
    rand_string = ''.join(random.choice(letters) + " " for i in range(length))
    print("Random string of length", length, "is:", rand_string)

generate_random_string(random.randint(10, 20))

print("\n#2\n")
rand_list = rand_string.split()
print(rand_list)

print("\n#3\n")
rand_max = max(rand_list)
rand_min = min(rand_list)
print(f'Max element: {rand_max}\nMin element: {rand_min}')

print("\n#4\n")
rand_sort = sorted(rand_list)
print(f'Random list sorted: {rand_sort}')

print("\n#5\n")
rand_sort_rev = sorted(rand_list, reverse=True)
print(f'Random list reversed: {rand_sort_rev}')
print("\n")
