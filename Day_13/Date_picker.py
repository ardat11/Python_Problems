#You are creating a date picker for a website and need to output all of the years in a given period.

#Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.

#The output sequence should start with the first input number and end with the second input number, without including it.

#Sample Input
#2005
#2011

#Sample Output
#[2005, 2006, 2007, 2008, 2009, 2010]


first = int(input())

second = int(input())

myrange = range(first, second)

liste = list(myrange)

print(liste)
