from Student import Student

from numpy import *
import os

'''
student1 = Student("ali")
student2 = Student("Omer")

student1.setSalary(100)
student2.setSalary(200)

sList=[student1,student2]

total =student1.calcSalary(sList)
print(total)
a=student1.raisSal(50)
print(a)

s2 = Student('ahmed')
s2.setSalary(20)
print(student1.share(s2))


class Super1():

    count=0
    def __init__(self,name):
        print('hi')
        self.name = name
        Super1.count +=1

    def getName(self):
        return self.name

#s = Super1('nn')
#print(s.getName())
s2 = Super1
print(s2.count)

a =array([  range(i,i+3)  for i in range(10) ])
print(a)

'''

'''
class Animal:
    def __init__(self,name):
        self.name = name

    def fun(self,number):
       self.number = 3*number
       return self.number

class Dog(Animal):
    def fun(self , number):
       myNumber = super(Dog , self).fun(number)
       print(myNumber)
       print ('dog')



x = Dog("ms")
x.fun(3)

file = open('E:\\pFiles\\pythonFile.txt' ,'a')
file.write("jjj")
file.close()
'''
#os.rename('E:\\pFiles\\pythonFile.txt','E:\\pFiles\\newName.txt')
#os.chdir('E:\\pFiles\\pFiles2')
#os.rmdir('E:\\pFiles\\try')

'''
def fun(a):
    print("hello" , a )
    for i in a:
        print (i)

list1 =[1,2,3]
fun(*list1)
print('------------------')






def funn(a):
    for i in a :
        print (i)

funn(9)
'''


'''
class Animal:
    def __init__(self):
        self.x ='food'

class Dog(Animal)  :
    def __init__(self):
        super(Dog,self).__init__()
        self.y ='here'

d = Dog()
print(d.x)

def fun(n):
    sum =0
    count =0
    while True:
        try:
            numbeeer = float(input('enter a number'))
            sum+= numbeeer
            count+=1
        except ValueError :
          print('enter a true number')
        if(count==n):
            break
    avg = sum/n
    return  avg

print(fun(3))

print('******************')

list1 = list(range(2,10))
list1.reverse()
for i in list1:
    print(i)


print("123".isnumeric())
'''

try :
    n = int(input('enter number'))
except ValueError :
    print('error')
else:
 print('hello')