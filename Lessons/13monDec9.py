names = ['kanye', 'yee', 'skeeYee']

for i in names:
	print(i)

#Lists are mutable, those we've learned so far don't

new_names = names
print(new_names)
print(names)

#---------------------------------------------------

names[0] = "bdf"

print(new_names)
print(names)

#---------------------------------------------------

new_names = names[:]
names[0] = "hawk"

print(new_names)
print(names)

#---------------------------------------------------

f = -4096
g = -4096

print(id(f))
print(id(g))

#---------------------------------------------------

def lcgr(li):
	li[0] = 100

nums = [1, 2, 3]

print(nums)
lcgr(nums)
print(nums)

#---------------------------------------------------

"""
Methods are funcs driven by an object
"""

def APPEND(list, value):
    list += [value]

nums = []
APPEND(nums, 1)
APPEND(nums, 2)
APPEND(nums, 3)
print(nums)

#---------------------------------------------------

# Methods are forms of procedural abstraction where self is passed

nums.append(1)
nums.append(2)
nums.append(3)
