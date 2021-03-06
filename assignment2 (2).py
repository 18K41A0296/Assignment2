# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u8PY-UzTGxLTYE9MLchRCbNf_4hHA0bc

1. Area of Triangle :
Given the lengths of three sides of a triangle, calculate the area of the
triangle.
"""

# Area of triangle by heron's formula
# let a,b,c are the lengths of triangle
import math
a=int(input("enter a value :"))
b=int(input("enter b value :"))
c=int(input("enter c value :"))
if (a<(b+c)) or (b<(c+a)) or (c<(b+c)) :
 p=int((a+b+c)/2)
 area=math.sqrt(p*(p-a)*(p-b)*(p-c))
 print('Area of triangle is : ',area)
else :
  print('given lengths does not form triangle')

"""2. Take a string from end user and check if the value is palindrome or not"""

# Given string is a palindrome or not
str=input("Enter the string :")
if str==str[::-1] :
  print('Given string is a palindrome')
else:
  print('Given sting is not a palindrome')

"""3. Write a program that reads a year from the user and displays a message
Indicating whether or not it is a leap year.
"""

year=int(input('Enter any year :'))
if ((year%400==0) or ((year%4==0) and (year%100!=0))):
  print('Given year is a leap year')
else:
  print('Given year is not a leap year')

"""4. Space To Hyphen problem
Take a string as input, and replaces spaces “ “ with hyphens “-”, and
returns a string.
"""

st=input("enter any name :")
print(st.replace(' ','-'))

"""5. Unique Sort problem
Take a string as input that accepts a comma separated sequence of words as
input and prints the unique words in sorted form (alphanumerically).
"""

import string
items = input("Input comma separated sequence of words :")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

"""6. Tax Calculator
Ask the user for their monthly salary. Calculate whether they have to pay tax
and if so, how much is that amount .Print the result
"""

s=int(input("enter your salary:"))
t={1:0,2:0.05,3:0.1,4:0.15,5:0.2,6:0.25,7:0.3}
if s<=250000:
  i=1
elif 250001<=s<=500000:
  i=2
elif 500001<=s<=750000:
  i=3
elif 750001<=s<=1000000:
  i=4
elif 1000001<=s<=1250000:
  i=5
elif 1250001<=s<=1500000:
  i=6
elif s>1500000:
  i=7
tax=s*t[i]
print("total tax=",tax)

"""7. Take a list of integers as an argument, and converts it into a single integer
(return the integer).
"""

st=[]
n=int(input('number of elements to be stored in list :'))
for i in range(0,n):
  k=int(input("enter element :"))
  st.append(k)
print('list elements are:',st)
def combine(st):
  l=len(st)
  print('length:',l)
  com=''
  for j in range(0,l):
    com=com+str(st[j])
  return com
r=combine(st)
m=int(r)
print('combination of list numbers is:',m)

"""8. Units of Time
Create a program that reads duration from the user as a number of days,
hours, minutes, and seconds. Compute and display the total number of
seconds represented by this duration.
"""

day=int(input("enter no of days :"))
hours=int(input("enter no of hours"))
min=int(input("enter no of minutes"))
sec=int(input("enter no of seconds"))
day_sec=24*60*60*day
hours_sec=60*60*hours
min_sec=60*min
total_sec=day_sec+hours_sec+min_sec+sec
print('total no of seconds represented by duration is :',total_sec)

"""9. Sort 3 Integers
Given three integers (given through user input), sort the numbers using
|min| and |max| functions.
"""

a=int(input('enter first number : '))
b=int(input('enter second number : '))
c=int(input('enter third number : '))
maximum=max(a,b,c)
minimum=min(a,b,c)
print('the numbers are shorted in order of: ',minimum,a+b+c-(maximum+minimum),maximum)

"""10.Write a program that reads a date from the user and computes its immediate
successor. The date is the format YYYY-MM-DD. So, 2020-04-15 will have the
successor 2020-04-16.
"""

year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

"""11.Compute product of a list of numbers [45 ,3,2,89,72,1,10,7]
Output: 121111200
"""

st=[]
n=int(input('number of elements to be stored in list :'))
for i in range(0,n):
  k=int(input("enter element :"))
  st.append(k)
print('list elements are:',st)
product=1
l=len(st)
for i in range(0,l):
  product=product*st[i]
print('product of list elements is :',product)

"""12.Compute given Num_list = [5, 6,8 ,34,89,1] to get desired output
Output: Out_list=[11,14,42,123,90]
"""

a=[]
n=int(input('number of elements to be stored in list :'))
for i in range(0,n):
  b=int(input("enter element :"))
  a.append(b)
print('list elements are:',a)
l=len(a)
out_list=[]
for i in range(0,l):
  if (i+1)<l:
    c=a[i]+a[i+1]
    out_list.append(c)
print('output answer is :',out_list)

"""13. Compute given Num_tuple = (5, 6,8 ,3,9,1) to get desired output
Output: Out_list = [5, 30, 240, 720, 6480, 6480]
"""

h=(5,6,8,3,9,1)
l=len(h)
out_put=[]
product=1
for i in range(0,l):
    product=product*h[i]
    out_put.append(product)
print('output answer is :',out_put)

"""14. Write a Python code that takes a number and returns a list of its digits. So
for 586392 it should return [5,8,6,3,9,2]
"""

num=int(input("enter the number :"))
s=[]
for y in str(num):
  s.append(int(y))
print(s)

"""15.Write a program that finds the longest palindromic substring of a given
string
"""

class sub(object):
   def lp(self, s):
      p = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         p[i][i] = True
      ml = 1
      t = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            e = i+l
            if l==2:
               if s[i] == s[e-1]:
                  p[i][e-1]=True
                  ml = l
                  t = i
            else:
               if s[i] == s[e-1] and p[i+1][e-2]:
                  p[i][e-1]=True
                  ml = l
                  t = i
      return s[t:t+ml]
st=input("enter string : ")
ob1 = sub()
print(ob1.lp(st))

"""16. Substring Check (Bug Funny)
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is
a substring of A and 0 otherwise.
First two lines of input:
1010110010 10110
1110111011 10011
First two lines of output:
1
0
"""

P=input("Enter binary string:")
ss=input("Enter binary substring:")
if(P.find(ss)==-1):
      print("0")
else:
      print("1")

"""17. POUR1 - Pouring water
Given two vessels, one of which can accommodate a litres of water and the other
- b litres of water, determine the number of steps required to obtain exactly c litres
of water in one of the vessels.
At the beginning both vessels are empty. The following operations are counted as
'steps':
• emptying a vessel,
• filling a vessel,
• pouring water from one vessel to the other, without spilling, until one of
the vessels is either full or empty.
"""

def gcd(a,b):
    if b==0: 
        return a 
    return gcd(b,a%b) 
def countsteps(a,b,c): 
    vol1=b
    vol2=0
    count=1
    while ((vol1 is not c) and (vol2 is not c)): 
        temp=min(vol1,a-vol2) 
        vol2=vol2+temp 
        vol1=vol1-temp 
        count=count+1
        if ((vol2==c)or(vol1==c)): 
            break
        if vol1==0: 
            vol1=b 
            count=count+1
        if vol2==a: 
            vol2=0
            count=count+1
    return count 
def ispossible(a,b,c): 
    if a>b: 
        temp=a 
        a=b 
        b=temp 
    if c>b: 
        return -1
    if (c%(gcd(b,a)) is not 0): 
        return -1
    return(min(countsteps(b,a,c),countsteps(a,b,c)))
test=int(input("Enter no of testcases : "))
for i in range(test):
  a=int(input("Enter capacity of vessel a : "))
  b=int(input("Enter capacity of vessel b : "))
  c=int(input("Enter capacity to be obtained :"))
  print("Minimum number of steps required is : ",ispossible(a,b,c))