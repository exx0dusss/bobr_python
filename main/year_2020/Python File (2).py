'''#LIST 1...n
my_list = []
n = 0
for i in range(10):
    n = n + 1
    my_list.append(n)
    
print(my_list)
'''




'''#SORTERS
def findDuplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
        
print(findDuplicate([3,1,3,4,2]))
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
        
    return ptr1

print(findDuplicate([3,1,3,4,2]))
'''




'''#FIND COMMON ELEMENTS
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a.sort()
b.sort()
ab = []
for el in a:
    for ell in b:
        if el == ell:
            ab.append(el)
        else:
            continue
print(ab)
result = [elem for elem in a if elem in b]
print(result)
'''




'''SORTER FROM > to <
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)
'''




'''MIX ALL THE DICTIONARIES
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
result = {}
for el in (dict_a, dict_b, dict_c):
    result.update(el)
print(result)
'''




''' THREE HIGHEST ELEMENTS
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)
'''

