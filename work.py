#Write a program which takes input from the user and checks whether the number is odd or even


# a=int(input("enter any number- "))
# if a%2==0:
#       print("even number")
# else:
#       print("not even number") 



#Write a program which takes input from the user and checks whether the number is positive or negative.

# a=int (input("enter any number- "))
# if a>=0:
#     print('given number is positive')
# elif a<0:
#     print('given number is negative')

#Write a program which takes input from the user and verifies the condition using ‘and’ & ‘or’ operator.

# maths=int (input("enter student marks- "))
# physics=int (input("enter student marks- "))

# if maths>=25 and physics>=25:
#     print('first class')
# elif maths>=20 or physics>=20:
#     print('second class')
# else:
#     print('last batch')

#Print only the even numbers from the list.[1,2,3,4,5,6,22,46,99,100,33,36]

# a=[1,2,3,4,5,6,22,46,99,100,33,36]
# for x in a:
#     if x%2==0:
#      print(x)

#Print the elements of a list in reverse order.[4,3,5,6,10,7,1]

# list=[4,3,5,6,10,7,1]
# print(list[::-1])

#Remove the duplicate elements from the list by making it a set [1,2,3,1,2,3,6,7,97,5,4,3,4,5,4]

# a=[1,2,3,1,2,3,6,7,97,5,4,3,4,5,4]
# print(set(a))

#Print only the value of a key in a dictionary.(Take any dictionary of your choice)

# a={1:'vinay',2:'python','mobile':1234,'abcd':'hello'}
# print(a.keys())

#Write a function and pass ‘first_name’ as a parameter and print your first name by calling the function.

# def vinay(a):
#     return(a)
# print(vinay('python'))

#Using for loop print all the elements of the given list.[1,2,3,4,5,6,7,”vinay”,”jeevitha”,10]

# for a in[1,2,3,4,5,6,7,'vinay','jeevitha',10]:
#     print(a)

#Write a function which takes input from the user and does an addition of 5 integer values.

# a=int(input('enter a number- '))
# b=int(input('enter a number- '))
# c=int(input('enter a number- '))
# d=int(input('enter a number- '))
# e=int(input('enter a number- '))
# def vinay(a,b,c,d,e):
#     return(a+b+c+d+e)
# print(vinay(a,b,c,d,e))

from pywhatkit import pywhatkit
pywhatkit.sendwhatmsg("+919100891192","hii ra pand",20,13)
