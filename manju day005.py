#! ----> common function for list
'''''

l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))


l1=[6,8,9, "p","u"]
print(max(l1))   # ---> error
print(min(l1))   #--->error
''
#l1=[6,7,8,9,0,8.89,-5,0.78]
#print(min(l1))  #-5


#l1=[6,7,8,9,0,8.89,-5,0.78]
# index() ---> to get index value of specific element
#print(l1.index(9))

#l1=[6,7,8,9,0,8.89,-5,0.78]


# count()--->how many num of times an element is repeated
# * remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)
# * clear() --> to complete delete all element in list
li.clear()# * remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)

# * clear() --> to complete delete all element in list
li.clear()
print(l1)
print

# M:-2 --> descending order
l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)
'''

# ? list constructor
# * list()--> to conver other collection datatype to list
# 13 = ((8, 9, 0))
# print(list(l3))

# 14 =(8, 9)
# print(list(l4))

# ! ---> nested list


# ? sort ---> arrange elements in list in ascending or descending order
#l1 = [9, 7, 45, 0,-6, 5, 12]
# l1.sort() # to arrange in ascending order
# print(l1)

# l1.sort(reverse=True) # to sort in ascending order
# print(l1)

# l1 = ['z','i', 'o', 'p', 9]
# l1.sort()
# print(l1) # ---> error

# list constructor
# list() --> to conver other collection datatype to list
# l3 = ((8, 9, 0))
# print(list(l3))

# l4 = (8, 9)
# print(list(l4))

# ! ---> nested list

l1 = [8, 9, [0, 8, 7]],['p', 'o', 'y'],

l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
# ! ----> nested list
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
# ! ----> nested list

# M:-1

l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[3][1])

# M:-2

l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:5])

# M:-3

l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:-1])



# ------. commmon function

# len()' min(),max(),index(),count()
s1 = "hello world"
# print(len(s1))
#


# ! function of string
s1 = "hello world"

# ? to convert all character to upper case
# print(s1.upper())






#ord()--->used to find the ASCII value of a character
s1='u'
print(ord(s1))

#strip()--->to eliminate the space in beginning and end of string
s1=" where are you"
print(s1.lstrip())


# --> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space


s1 = "   where are you.?"
print(s1.lstrip())


# M:-2
# --> to eliminate right space

s1 = "where are you.?  "
print(s1.rstrip())


# M:-3
# --> to eliminate right and left space


s1 = "   where are you.?    "
print(s1.strip())


# ---> split()-->
# --> to split the words in string based on a character
s1= "where are you.?"
print(s1.split(" "))



# replace() --> to replace a specific char in the string

s1= "where are you.?"
print(s1.replace('r','&&'))


# swapace() --> to convert capital to small and small to capital at a time


s1 = "HEY there"
print(s1.swapcase())


# * title()---> to write the string in format of title
# s1 = 'never givenup'
# print(s1.capitalize())

# * join the strings
 # s1 = "hello"
 # s2 = "world"
 # print(s1+s2)



 
# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)



#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))


s1 = "hello world"
print(s1.index('h'))



# join() -->
l1 = ["hey","there"]
pr

# M:-1# join() -->
l1 = ["hey","there"]
print


#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))



# * join() -->
#l1 = ["hey" ,"there"]
#print(" ".join(l1))
#print("$".join(l1))


s1 = "Welcome to all"
# * print(s1.endswitch('l'))
# * print(s1.startswitch('W'))


# s1 = "67"
# print(t




# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswitch('1'))
print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1.endswith('L'))


s1 = "Welcome to all"
print(s1[::-1])


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1.endswith('L'))


 # ! ----> Eg:1
 # wap to find the number of lower case letters
# s1 =" Hey there you are"
# count = 0
# for i in s1:
# if i.is lower():
#  count+=1
 # print("the total num of lower case letters:",count)       



characters =len(s1)
#print(characters)


words = s1.split(" ")
print(words)


words = s1.split(" ")
print(len(words))


#sentences = s1.split('.')
#print(len(sentences))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))
''

 
 # 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

