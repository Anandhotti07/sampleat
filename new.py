'''
answer=[]
for person in ["hi","loop","kill"]:
    answer.append(person[0])
print(answer)
p=[]
l= ["hi","loop","kill"]
for i in l:
    p.append(i[0])
print(p)
print(l[0])
---------------------------------------------------------------------------
l=[1,2,3,4,5,6,7,8]
p=[]
for i in l:
    if i%2==0:
        p.append(i)
print(p)
------------------------------------------------------------------------
answer = [num[0] for num in ["hi","by","ji"]]
print(answer) 
answer2 = [num for num in [1,2,3,46,6,8] if num%2 ==0 or num/2==1]
print(answer2) 
----------------------------------------------------------------------
l = [1,2,3,4]
k = [3,4,5,6]
def intersection(l, k):
    return list(set(l) & set(k))
answer=intersection(l,k)
print(answer) 
--------------------------------------------------------------------------
aanswer = [num for num in list(set([1,2,3,4])&set([3,4,5,6]))]
m = [num[::-1] for num in ["Elie","Tim","Matt"]]
answer2 = [m.lower() for m in m]
print(answer2)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
---------------------------------------------------------

answer = [num for num in range(1,101) if num%12==0]
print(answer)   
l= ["a","m","a","z","i","n","g"]
answer = [num for num in l if l not in ["a","e","i","o","u"]]
print(answer)

l=["a", "m", "a", "z", "i", "n", "g"]
answer=[]
for i in l:
    if i != "a" and i != "e" and i != "o" and i != "u" and i != "i":
        answer.append(i)
print(answer)
        
answer = [i for i in ["a", "m", "a", "z", "i", "n", "g"] if i != "a" and i != "e" and i != "o" and i != "u" and i != "i"]
print(answer)

answer = [char for char in "amazing" if char not in "aeiou"] 

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 

----------------------------------------------------------------------------------- 

def split(word):
    return tuple(word)
     
# Driver code
word = 'geeks'
print(split(word))

from random import choice #DON'T CHANGE!
food = choice(["morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")
    ----------------   
while food in bakery_stock.keys():
    print(f"{bakery_stock[food]} left")
    break
else:
    print("We don't make that")
    -------------------------
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("we don't make that")
-----------------------------____________---
if bakery_stock.get(f"{food}") in bakery_stock.keys():
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

while food in bakery_stock:
    print(f"{bakery_stock[food]} left")
    break
else:
    print("We don't make that")
    -----------------------------------------------------------
answer = {i:chr(i) for i in range(65,91)}
print(answer)

a={}
d={}
for i in range(65,91):
    a[i]=chr(i)
    d.update(a)
print(d)
-------------------------------------------

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values=set(values)
print(static_values)
print(type(static_values))

value = (1)
print(value)

l=[]
def generate_evens():
    for i in range(1,49):
        if i%2==0:
            l.append(i)
    print(l)
generate_evens()

def square(a,b):
   print(a*b)
square(2,3) 

-----------------------
def yell(word):
    return "{}!".format(word.upper())
------------
def yell(a):
    return a.upper()+"!"
print(yell("not print"))
-----------
def yell(word):
    return f"{word.upper()}!"

------------------------------------------------------------------After submission of intel laptop----------------------------------------------------------------

def count_sevens(*args):
    return args.count(7)
    nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
    result1=[]
    for i in nums:
        if i==1:
            result1.append(i)
        elif i==4:
            result1.append(i)
        elif i==7:
            result1.append(i)
    return result1
print(count_sevens(*result1))


a = int(input('Enter a number (-1 to quit): '))
a=0
while a != -1:
    a=a+1
    if a > 2:
        print("Hey! man enter -1")
    a = int(input('Enter a number (-1 to quit): ')) 
    

fin = open("data.txt", "rt")
fout = open("out.txt", "wt")
for line in fin:
	fout.write(line.replace('pyton', 'python'))
fin.close()
fout.close()
------------------------------------------------------

fin = open("C:\python\edit.txt", "rt")
fout = open("C:\python\edit1.txt", "wt")
for line in fin:
	fout.write(line.replace('such', 'much'))
fin.close()
fout.close() 

----------------------------------------------------------------------map--------------------------------
lst=[1,2,3]
def minus(i):
        return i-1
decrement_list=list(map(minus,lst))
print(decrement_list)

---------------------------------------------------------------------------------------------

lst=[1,2,3]
decr=list(map(lambda x : x-1,lst))
print(decr)

------------------------------

def decrement_list(l):
    return list(map(lambda n: n-1, l))
print(decrement_list([1,2,3]))

--------------------------------------------------------------filter---------------------------------

def remove_negatives(l):
    return list(filter(lambda x : x>0,l))
print(remove_negatives([1,2,3,-4,5,6]))

-----------------------------

l=[1,2,3,4,5]
remove_negatives = list(filter(lambda x : x > 0,l)
print(remove_negatives)

-----------------------------

l=[1,2,3,4,-6]
d=[x for x in l if x>0]
print(d)
---------------------
def is_all_strings(l):
    return any(type(x)!=int for x in l)
print(is_all_strings([1,2,3,"anan"]))


n = int(input().strip())
if n%2!=0:
    print("weird")
elif n%2==0 and n in range(2,5):
    print("Not Weird")
elif n%2==0 and n in range(6,20):
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")
        

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n in range(2,5):
            print("Not Weird")
        elif n in range(6,20):
            print("Weird")
        elif n > 20:
            print("Not Weird")

b="anand r hotti and he has androind phone his short name is ands"
z="and"
h=0
j=0
k=0 
print(f"lenght of b is :{len(b)}")
for i in range(0,len(b)+1):
    if h <= len(b):
        f=b[i:]
        j=f.find(z)
        h=h+j
        b=f        
    else:
        break
print(f" h is:{h}","\n",f"j is:{j}","\n",f"lenght of f is :{len(f)}")
print(f"lenght of b is :{len(b)}")

    
   


d={}
f=open("C:\python\sample.txt")
for i in f:
    for j in i.split():
        k=j
        d[k]=d.get(k,0)+1
print(d)

file=open("C:\python\sample.txt","a")
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
---------------------------------------------
import csv
data=[]
with open("C:\\python\\file.txt") as f:
    csv_reader = csv.DictReader(f)
    for i in csv_reader:
        data.append(i)

da=data[1].keys()

with open("C:\\python\\new_file.txt","a") as f:  
    header=da
    csv_writer = csv.DictWriter(f, fieldnames=header)
    csv_writer.writeheader()
    for i in data:
        csv_writer.writerow(i)

        
import csv
data=[]
with open("C:\\python\\file.txt") as f:
    csv_reader = csv.DictReader(f)
    for i in csv_reader:
        data.append(i)
for i in data:
    print(i) '''
import csv
with open("C:\\python\\file.txt","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        print(i[0])
    